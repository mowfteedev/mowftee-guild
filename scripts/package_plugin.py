#!/usr/bin/env python3
"""Build a skill-only ZIP with the Python standard library. No installation."""
import json
from pathlib import Path
import re
import zipfile

ROOT = Path(__file__).resolve().parent.parent


def package_plugin(source, destination):
    source, destination = Path(source), Path(destination)
    manifest = json.loads((source/'plugin.json').read_text())
    for key in ('name', 'version'):
        if not re.fullmatch(r'[a-zA-Z0-9_.-]+', manifest[key]):
            raise ValueError(f'Invalid {key} for an archive filename')
    files = [source/'plugin.json', source/'LICENSE',
             source/'.agents/plugins/marketplace.json']
    skills = sorted((source/'skills').glob('*/SKILL.md'))
    if not skills:
        raise ValueError('No skills found')
    for skill in skills:
        files.append(skill)
        for folder in ('references', 'scripts', 'assets', 'agents'):
            resources = skill.parent/folder
            if resources.is_symlink():
                raise ValueError(f'Symlink resource directory: {resources}')
            if resources.is_dir():
                for entry in sorted(resources.rglob('*')):
                    if entry.is_symlink():
                        raise ValueError(f'Symlink resource: {entry}')
                    if entry.is_file() and '__pycache__' not in entry.parts:
                        files.append(entry)
        files.extend(p for p in sorted(skill.parent.glob('LICENSE*')) if p.is_file())
    for path in files:
        if path.is_symlink() or not path.is_file():
            raise ValueError(f'Expected a regular file: {path}')
        if not path.resolve().is_relative_to(source.resolve()):
            raise ValueError(f'File outside plugin source: {path}')
    destination.mkdir(parents=True, exist_ok=True)
    output = destination/f"{manifest['name']}-{manifest['version']}.zip"
    with zipfile.ZipFile(output, 'w', zipfile.ZIP_DEFLATED) as bundle:
        for path in files:
            bundle.write(path, path.relative_to(source).as_posix())
    return output


if __name__ == '__main__':
    print(package_plugin(ROOT, ROOT/'dist'))
