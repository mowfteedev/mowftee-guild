#!/usr/bin/env python3
"""Manage local skills with the Python standard library; never execute payloads."""
import argparse
from contextlib import contextmanager
from datetime import datetime, timezone
import hashlib
import json
import os
from pathlib import Path
import re
import shutil
import sys
import tempfile
from urllib.parse import unquote, urlsplit
import uuid

ROOT = Path(__file__).resolve().parent.parent
CONTROL = '.mowftee-guild'
NAME = re.compile(r'[a-z0-9]+(?:-[a-z0-9]+)*\Z')

class GuildError(Exception):
    """An actionable validation, ownership or input error."""

def read_json(path):
    try:
        return json.loads(path.read_text(encoding='utf-8'))
    except (ValueError, OSError) as exc:
        raise GuildError(f'Cannot read JSON {path}: {exc}') from exc

def valid_name(name):
    return isinstance(name, str) and len(name) <= 64 and NAME.fullmatch(name)

def catalog():
    data = read_json(ROOT / 'catalog.json')
    if not isinstance(data, dict) or data.get('schema_version') != 1:
        raise GuildError('Unsupported catalog schema.')
    if not isinstance(data.get('skills'), list) or not isinstance(data.get('profiles'), dict):
        raise GuildError('Catalog needs skills and profiles.')
    names = [s.get('name') for s in data['skills'] if isinstance(s, dict)]
    if len(names) != len(data['skills']) or not all(valid_name(n) for n in names):
        raise GuildError('Invalid skill name in catalog.')
    if not names or len(names) != len(set(names)):
        raise GuildError('Catalog is empty or has duplicate skills.')
    for profile, members in data['profiles'].items():
        if not valid_name(profile) or not isinstance(members, list) or not members:
            raise GuildError(f'Invalid profile: {profile}')
        if any(not isinstance(n, str) or n not in names for n in members):
            raise GuildError(f'Unknown skill in profile: {profile}')
        if len(members) != len(set(members)):
            raise GuildError(f'Duplicate skill in profile: {profile}')
    if set(data['profiles'].get('all', [])) != set(names):
        raise GuildError('The all profile must cover every skill exactly.')
    if (ROOT / 'VERSION').read_text().strip() != data.get('version'):
        raise GuildError('VERSION and catalog disagree.')
    return data

def frontmatter(path):
    """Parse only this repo's flat YAML subset: JSON-quoted strings/identifiers.

    Unsupported YAML fails rather than being interpreted heuristically.
    """
    match = re.match(r'\A---\n(.*?)\n---\n', path.read_text(encoding='utf-8'), re.S)
    if not match:
        raise GuildError(f'Malformed frontmatter: {path}')
    fields = {}
    for line in match[1].splitlines():
        pair = re.fullmatch(r'(name|description|license): (.+)', line)
        if not pair or pair[1] in fields:
            raise GuildError(f'Unsupported/duplicate frontmatter field: {path}')
        raw = pair[2]
        value = json.loads(raw) if raw.startswith('"') else raw
        if not isinstance(value, str) or (not raw.startswith('"') and not re.fullmatch(r'[A-Za-z0-9-]+', raw)):
            raise GuildError(f'Use JSON-quoted strings or identifiers: {path}')
        fields[pair[1]] = value
    if set(fields) != {'name', 'description', 'license'}:
        raise GuildError(f'Missing frontmatter fields: {path}')
    return fields

def inventory(root):
    if root.is_symlink() or not root.is_dir():
        raise GuildError(f'Expected a real directory, not a symlink: {root}')
    result = {}
    for path in sorted(root.rglob('*')):
        if path.is_symlink():
            raise GuildError(f'Symlink payloads are not managed: {path}')
        if path.is_file():
            result[path.relative_to(root).as_posix()] = hashlib.sha256(path.read_bytes()).hexdigest()
        elif not path.is_dir():
            raise GuildError(f'Special files are not managed: {path}')
    return result

def markdown_links(path):
    fence = None
    for line in path.read_text(encoding='utf-8').splitlines():
        marker = re.match(r'^\s*(`{3,}|~{3,})', line)
        if marker:
            if fence is None:
                fence = marker[1][0]
            elif fence == marker[1][0]:
                fence = None
            continue
        if not fence:
            for target in re.findall(r'\[[^\]]*\]\(([^\s)]+)\)', line):
                if not urlsplit(target).scheme and not target.startswith('#'):
                    yield unquote(target.split('#')[0])

def validate():
    data = catalog()
    names = {s['name'] for s in data['skills']}
    actual = {p.name for p in (ROOT / 'skills').iterdir() if p.is_dir()}
    if names != actual:
        raise GuildError(f'Catalog/directory mismatch: {sorted(names ^ actual)}')
    for skill in data['skills']:
        root = ROOT / 'skills' / skill['name']
        inventory(root)
        fields = frontmatter(root / 'SKILL.md')
        if fields['name'] != skill['name'] or fields['description'] != skill['description']:
            raise GuildError(f'Catalog/frontmatter mismatch: {skill["name"]}')
        if not 1 <= len(fields['description']) <= 1024 or fields['license'] != 'MIT':
            raise GuildError(f'Invalid description/license: {skill["name"]}')
        if len((root / 'SKILL.md').read_text().splitlines()) > 160:
            raise GuildError(f'Move conditional details to references: {skill["name"]}')
        if (root / 'LICENSE.txt').read_bytes() != (ROOT / 'LICENSE').read_bytes():
            raise GuildError(f'License drift: {skill["name"]}')
        ui = (root / 'agents/openai.yaml').read_text(encoding='utf-8').splitlines()
        if len(ui) != 4 or ui[0] != 'interface:':
            raise GuildError(f'Invalid UI metadata: {skill["name"]}')
        values = {}
        for line in ui[1:]:
            pair = re.fullmatch(r'  (display_name|short_description|default_prompt): (".*")', line)
            if not pair or pair[1] in values:
                raise GuildError(f'Invalid UI field: {skill["name"]}')
            values[pair[1]] = json.loads(pair[2])
        if set(values) != {'display_name','short_description','default_prompt'}:
            raise GuildError(f'Incomplete UI metadata: {skill["name"]}')
        if not 25 <= len(values['short_description']) <= 64:
            raise GuildError(f'UI description length: {skill["name"]}')
        if '$' + skill['name'] not in values['default_prompt']:
            raise GuildError(f'UI prompt must name its skill: {skill["name"]}')
        for doc in root.rglob('*.md'):
            for target in markdown_links(doc):
                resolved = (doc.parent / target).resolve()
                if root.resolve() not in resolved.parents or not resolved.exists():
                    raise GuildError(f'Non-self-contained link: {doc}: {target}')
    docs = [ROOT / name for name in ('README.md','CONTRIBUTING.md','CHANGELOG.md')]
    for folder in ('docs','workflows','evals'):
        docs.extend((ROOT / folder).rglob('*.md'))
    for doc in docs:
        for target in markdown_links(doc):
            resolved = (doc.parent / target).resolve()
            if ROOT not in resolved.parents or not resolved.exists():
                raise GuildError(f'Broken/outside link: {doc}: {target}')
    cases = read_json(ROOT / 'evals/scenarios.json')
    ids = set()
    for case in cases:
        if case['id'] in ids or case['primary_skill'] not in names:
            raise GuildError(f'Invalid evaluation case: {case["id"]}')
        ids.add(case['id'])
        if not case['request'] or not case['expected_observations'] or not case['fail_if']:
            raise GuildError(f'Incomplete evaluation case: {case["id"]}')
    if {c['primary_skill'] for c in cases} != names:
        raise GuildError('Evaluation definitions must cover all skills.')
    return data

def selected(args, data, default=None):
    known = [s['name'] for s in data['skills']]
    if args.skills is not None:
        names = [n.strip() for n in args.skills.split(',')]
        if not names or len(names) != len(set(names)) or any(n not in known for n in names):
            raise GuildError('Unknown, empty or duplicate --skills entry; use list.')
        return names
    if args.profile is not None:
        if args.profile not in data['profiles']:
            raise GuildError(f'Unknown profile: {args.profile}')
        return data['profiles'][args.profile]
    return default if default is not None else data['profiles']['core']

def reject_symlink_parts(path):
    for parent in (path, *path.parents):
        if parent.is_symlink():
            raise GuildError(f'Refusing a symlink in the destination path: {parent}')

def destination(args):
    if args.dest:
        path = Path(args.dest).expanduser()
    elif args.scope == 'workspace':
        path = Path(args.workspace).expanduser() / '.agents/skills'
    else:
        suffix = {'codex':'.agents/skills', 'antigravity':'.gemini/config/skills',
                  'antigravity-cli':'.gemini/antigravity-cli/skills'}[args.tool]
        path = Path.home() / suffix
    path = Path(os.path.abspath(path))
    reject_symlink_parts(path)
    if path == Path(path.anchor) or path == Path.home() or path == ROOT or ROOT in path.parents:
        raise GuildError(f'Refusing an unsafe destination: {path}')
    if path.exists() and not path.is_dir():
        raise GuildError(f'Destination is not a directory: {path}')
    return path

def load_manifest(dest):
    store = dest / CONTROL
    reject_symlink_parts(store)
    path = store / 'manifest.json'
    if path.is_symlink():
        raise GuildError(f'Manifest must not be a symlink: {path}')
    if not path.exists():
        return {'owner':'mowftee-guild', 'schema_version':1, 'skills':{}}
    data = read_json(path)
    if (not isinstance(data, dict) or data.get('schema_version') != 1
            or data.get('owner') != 'mowftee-guild' or not isinstance(data.get('skills'), dict)):
        raise GuildError('Unsupported or corrupt ownership manifest.')
    for name, record in data['skills'].items():
        if not valid_name(name) or not isinstance(record, dict) or not isinstance(record.get('files'), dict):
            raise GuildError('Invalid ownership entry; no payloads were changed.')
        for relative, digest in record['files'].items():
            if (not isinstance(relative, str) or not relative or '\\' in relative
                    or Path(relative).is_absolute() or '..' in Path(relative).parts
                    or not isinstance(digest, str) or not re.fullmatch('[a-f0-9]{64}', digest)):
                raise GuildError('Unsafe ownership path or hash; no payloads were changed.')
    return data

def atomic_json(path, data):
    fd, temporary = tempfile.mkstemp(prefix='.manifest-', dir=str(path.parent))
    try:
        with os.fdopen(fd, 'w', encoding='utf-8') as handle:
            json.dump(data, handle, ensure_ascii=False, indent=2)
            handle.write('\n')
        os.replace(temporary, path)
    finally:
        if os.path.exists(temporary):
            os.unlink(temporary)

@contextmanager
def lock(dest):
    store = dest / CONTROL
    dest.mkdir(parents=True, exist_ok=True)
    store.mkdir(exist_ok=True)
    reject_symlink_parts(store)
    directory = store / 'lock'
    try:
        directory.mkdir()
    except FileExistsError as exc:
        raise GuildError(f'Active operation or stale lock: {directory}. See docs/installation.md.') from exc
    try:
        for name in ('transactions','backups'):
            reject_symlink_parts(store / name)
        transactions = store / 'transactions'
        if transactions.exists() and any(transactions.iterdir()):
            raise GuildError(f'Inspect interrupted transaction: {transactions}. See docs/installation.md.')
        yield
    finally:
        directory.rmdir()

def preflight(dest, names, owned, force, uninstall=False):
    for name in names:
        path = dest / name
        if uninstall and name not in owned:
            raise GuildError(f'Refusing to uninstall an unowned skill: {name}')
        if path.is_symlink():
            raise GuildError(f'Refusing a symlink skill directory: {path}')
        if path.exists():
            files = inventory(path)
            if name not in owned and not force:
                raise GuildError(f'Unmanaged skill {name}; --force backs it up before replacement.')
            if name in owned and files != owned[name]['files'] and not force:
                raise GuildError(f'Locally modified skill {name}; --force backs it up before changing it.')

def transact(dest, names, old, new, install, force):
    """Restore moved directories on ordinary errors; not power-loss atomicity."""
    store = dest / CONTROL
    transaction = store / 'transactions' / uuid.uuid4().hex
    transaction.mkdir(parents=True)
    (transaction / 'old').mkdir()
    (transaction / 'new').mkdir()
    moved, installed = [], []
    try:
        atomic_json(transaction / 'manifest.before.json', old)
        atomic_json(transaction / 'journal.json', {'operation':'install' if install else 'uninstall','skills':names})
        if install:
            for name in names:
                shutil.copytree(ROOT / 'skills' / name, transaction / 'new' / name)
                if inventory(transaction / 'new' / name) != new['skills'][name]['files']:
                    raise GuildError(f'Source changed during staging: {name}')
        for name in names:
            preflight(dest, [name], old['skills'], force, uninstall=not install)
            target = dest / name
            if target.exists():
                os.replace(target, transaction / 'old' / name)
                moved.append(name)
            if install:
                os.replace(transaction / 'new' / name, target)
                installed.append(name)
        atomic_json(store / 'manifest.json', new)
    except Exception:
        for name in reversed(installed):
            shutil.rmtree(dest / name)
        for name in reversed(moved):
            os.replace(transaction / 'old' / name, dest / name)
        shutil.rmtree(transaction)
        raise
    if force and moved:
        backups = store / 'backups'
        backups.mkdir(exist_ok=True)
        backup = backups / transaction.name
        os.replace(transaction, backup)
        print(f'Backup: {backup}')
    else:
        shutil.rmtree(transaction)

def lifecycle(args, data):
    dest = destination(args)
    old = load_manifest(dest)
    uninstall = args.command == 'uninstall'
    names = selected(args, data, sorted(old['skills']) if uninstall else None)
    if uninstall and not names:
        print(f'No owned skills to uninstall: {dest}')
        return 0
    preflight(dest, names, old['skills'], args.force, uninstall)
    if args.dry_run:
        print(f'DRY-RUN {args.command}: {dest}')
        for name in names:
            print(f'  {name}')
        return 0
    with lock(dest):
        old = load_manifest(dest)
        preflight(dest, names, old['skills'], args.force, uninstall)
        new = json.loads(json.dumps(old))
        new['version'] = data['version']
        new['updated_at_utc'] = datetime.now(timezone.utc).isoformat()
        for name in names:
            if uninstall:
                new['skills'].pop(name)
            else:
                new['skills'][name] = {'version':data['version'], 'files':inventory(ROOT / 'skills' / name)}
        transact(dest, names, old, new, not uninstall, args.force)
    print(f'{args.command}: {len(names)} skills at {dest}')
    return 0

def check(args, data):
    dest = destination(args)
    manifest = load_manifest(dest)
    names = selected(args, data, sorted(manifest['skills']) or None)
    known = {s['name'] for s in data['skills']}
    failed = False
    print(f'Destination: {dest}')
    for name in names:
        path = dest / name
        if not path.exists() and not path.is_symlink():
            status = 'MISSING'
        elif name not in manifest['skills']:
            status = 'UNMANAGED'
        elif inventory(path) != manifest['skills'][name]['files']:
            status = 'MODIFIED'
        elif name not in known:
            status = 'UNAVAILABLE'
        elif inventory(ROOT / 'skills' / name) != manifest['skills'][name]['files']:
            status = 'OUTDATED'
        else:
            status = 'OK'
        print(f'{name:25} {status}')
        failed = failed or status != 'OK'
    return 1 if failed else 0

def init_memory(args):
    target = Path(os.path.abspath(Path(args.path).expanduser()))
    memory = target / '.memory'
    templates = ROOT / 'templates/memory'
    mapping = {
        'architecture.md':'architecture.md', 'progress.md':'progress.md',
        'adr-template.md':'adr/0001-khoi-tao-du-an.md',
        'gate-checklist-template.md':'gate-checklist.md',
        'test-evidence-template.md':'test-evidence.md',
        'requirements-template.md':'requirements.md',
        'handoff-template.md':'handoff.md', 'risk-register-template.md':'risk-register.md',
        'release-template.md':'release.md', 'incident-template.md':'incident.md',
    }
    reject_symlink_parts(memory)
    values = {'{{PROJECT_NAME}}':args.name or target.name,
              '{{DATE_UTC}}':datetime.now(timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ'),
              '{{ADR_ID}}':'0001', '{{ADR_TITLE}}':'Khởi tạo dự án'}
    plans = []
    for source, relative in mapping.items():
        dest = memory / relative
        reject_symlink_parts(dest)
        if dest.exists():
            if not dest.is_file():
                raise GuildError(f'Memory path is not a file: {dest}')
            print(f'KEEP {dest}')
            continue
        text = (templates / source).read_text(encoding='utf-8')
        for key, value in values.items():
            text = text.replace(key, value)
        plans.append((dest, text))
    for path, text in plans:
        print(f'{"DRY-RUN" if args.dry_run else "CREATE"} {path}')
        if not args.dry_run:
            path.parent.mkdir(parents=True, exist_ok=True)
            with path.open('x', encoding='utf-8') as handle:
                handle.write(text)
    return 0

def selection_options(parser):
    group = parser.add_mutually_exclusive_group()
    group.add_argument('--profile', help='Named profile; install default: core')
    group.add_argument('--skills', help='Exact comma-separated skill names')

def target_options(parser):
    parser.add_argument('--tool', choices=['antigravity','antigravity-cli','codex'], default='antigravity')
    parser.add_argument('--scope', choices=['global','workspace'], default='global')
    parser.add_argument('--workspace', default='.', help='Root for --scope workspace')
    parser.add_argument('--dest', help='Explicit destination overriding tool/scope locations')

def main(argv=None):
    parser = argparse.ArgumentParser(description='mowftee-guild: skills, profiles, source validation and project memory.')
    sub = parser.add_subparsers(dest='command')
    for command in ('install','uninstall'):
        p = sub.add_parser(command)
        selection_options(p)
        target_options(p)
        p.add_argument('--dry-run', action='store_true', help='Plan without writing files')
        p.add_argument('--force', action='store_true', help='Back up existing payloads before replacement/removal')
    p = sub.add_parser('check', aliases=['status'])
    selection_options(p)
    target_options(p)
    p = sub.add_parser('list')
    selection_options(p)
    p.add_argument('--json', action='store_true')
    sub.add_parser('validate', help='Validate source catalog, skills, links and evaluation definitions')
    p = sub.add_parser('init')
    p.add_argument('path', nargs='?', default='.')
    p.add_argument('--name')
    p.add_argument('--dry-run', action='store_true')
    args = parser.parse_args(argv)
    if args.command is None:
        parser.print_help()
        return 0
    try:
        data = validate()
        if args.command == 'validate':
            print(f'Source validation OK: {len(data["skills"])} skills, {len(data["profiles"])} profiles.')
            print('Static validation does not prove AI behavior or runtime host compatibility.')
            return 0
        if args.command == 'list':
            names = selected(args, data, [s['name'] for s in data['skills']])
            skills = [s for s in data['skills'] if s['name'] in names]
            if args.json:
                print(json.dumps({'version':data['version'],'skills':skills,'profiles':data['profiles']},ensure_ascii=False,indent=2))
            else:
                for skill in skills:
                    print(f'{skill["name"]:25} {skill["title"]}')
                print('Profiles: ' + ', '.join(data['profiles']))
            return 0
        if args.command == 'init':
            return init_memory(args)
        if args.command in ('check','status'):
            return check(args, data)
        return lifecycle(args, data)
    except (GuildError, OSError, ValueError, KeyError, TypeError) as exc:
        print(f'ERROR: {exc}', file=sys.stderr)
        return 1

if __name__ == '__main__':
    if sys.version_info < (3, 9):
        print('Python 3.9 or later is required.', file=sys.stderr)
        raise SystemExit(2)
    raise SystemExit(main())
