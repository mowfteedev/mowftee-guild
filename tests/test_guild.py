"""Filesystem/CLI regression tests. Every mutation stays in a temporary root."""
import argparse
import importlib.util
import json
import os
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile
import unittest
from unittest.mock import patch

ROOT = Path(__file__).resolve().parent.parent
spec = importlib.util.spec_from_file_location('guild', ROOT / 'scripts/guild.py')
guild = importlib.util.module_from_spec(spec)
spec.loader.exec_module(guild)

class GuildTests(unittest.TestCase):
    def setUp(self):
        self.temporary = tempfile.TemporaryDirectory(prefix='mowftee-guild-test-')
        self.addCleanup(self.temporary.cleanup)
        self.base = Path(self.temporary.name).resolve()
        self.dest = self.base / 'skills with spaces'
        self.home = self.base / 'home'
        self.home.mkdir()
        self.env = os.environ.copy()
        self.env.update(HOME=str(self.home), PYTHONDONTWRITEBYTECODE='1')

    def cli(self, *args, expected=0, source=ROOT):
        result = subprocess.run([sys.executable, str(source / 'scripts/guild.py'), *map(str,args)],
                                text=True, capture_output=True, env=self.env, cwd=self.base)
        self.assertEqual(result.returncode, expected, result.stdout + result.stderr)
        return result

    def install(self, skills='backend', **kwargs):
        return self.cli('install','--dest',self.dest,'--skills',skills,**kwargs)

    def manifest(self):
        return json.loads((self.dest / guild.CONTROL / 'manifest.json').read_text())

    def copy_source(self):
        source = self.base / 'source'
        shutil.copytree(ROOT, source, ignore=shutil.ignore_patterns('.git','__pycache__','.venv'))
        return source

    def test_validate_and_json_discovery(self):
        self.cli('validate')
        data = json.loads(self.cli('list','--json').stdout)
        self.assertEqual({s['name'] for s in data['skills']}, set(data['profiles']['all']))
        self.assertIn('backend', data['profiles']['core'])

    def test_no_arguments_only_prints_help(self):
        self.assertIn('usage:', self.cli().stdout)
        self.assertEqual(list(self.home.iterdir()), [])

    def test_unknown_duplicate_and_empty_selection_do_not_write(self):
        for names in ('unknown','../backend','backend,backend','backend,'):
            self.cli('install','--dest',self.dest,'--skills',names,expected=1)
            self.assertFalse(self.dest.exists())

    def test_mutually_exclusive_selection(self):
        self.cli('install','--dest',self.dest,'--skills','backend','--profile','core',expected=2)
        self.assertFalse(self.dest.exists())

    def test_unknown_profile_does_not_write(self):
        self.cli('install','--dest',self.dest,'--profile','no-such-profile',expected=1)
        self.assertFalse(self.dest.exists())

    def test_dry_run_creates_no_directories(self):
        self.cli('install','--dest',self.dest,'--profile','all','--dry-run')
        self.assertFalse(self.dest.exists())
        self.assertEqual(list(self.home.iterdir()), [])

    def test_install_all_self_contained_payloads_and_check(self):
        self.cli('install','--dest',self.dest,'--profile','all')
        data = guild.catalog()
        self.assertEqual(set(self.manifest()['skills']), set(data['profiles']['all']))
        for name in self.manifest()['skills']:
            self.assertEqual(guild.inventory(self.dest/name), guild.inventory(ROOT/'skills'/name))
        self.cli('check','--dest',self.dest)

    def test_additive_install_preserves_other_profiles(self):
        self.install('backend')
        self.install('frontend')
        self.assertEqual(set(self.manifest()['skills']), {'backend','frontend'})
        self.cli('check','--dest',self.dest)

    def test_reinstall_unchanged_payload_is_idempotent(self):
        self.install()
        before = guild.inventory(self.dest/'backend')
        self.install()
        self.assertEqual(guild.inventory(self.dest/'backend'), before)
        self.assertFalse((self.dest/guild.CONTROL/'backups').exists())

    def test_unmanaged_collision_preserves_original_and_other_targets(self):
        (self.dest/'frontend').mkdir(parents=True)
        sentinel = self.dest/'frontend/user.txt'
        sentinel.write_text('USER OWNED')
        self.cli('install','--dest',self.dest,'--skills','backend,frontend',expected=1)
        self.assertEqual(sentinel.read_text(), 'USER OWNED')
        self.assertFalse((self.dest/'backend').exists())
        self.assertFalse((self.dest/guild.CONTROL).exists())

    def test_force_backups_unmanaged_payload(self):
        (self.dest/'backend').mkdir(parents=True)
        (self.dest/'backend/user.txt').write_text('USER OWNED')
        self.cli('install','--dest',self.dest,'--skills','backend','--force')
        backups = list((self.dest/guild.CONTROL/'backups').iterdir())
        self.assertEqual(len(backups), 1)
        self.assertEqual((backups[0]/'old/backend/user.txt').read_text(), 'USER OWNED')
        self.assertEqual(json.loads((backups[0]/'manifest.before.json').read_text())['skills'], {})
        self.cli('check','--dest',self.dest)

    def test_modified_files_block_install_and_uninstall(self):
        self.install()
        sentinel = self.dest/'backend/references/runbook.md'
        sentinel.write_text('USER MODIFIED')
        for action in ('install','uninstall'):
            self.cli(action,'--dest',self.dest,'--skills','backend',expected=1)
            self.assertEqual(sentinel.read_text(), 'USER MODIFIED')
        self.assertIn('MODIFIED', self.cli('check','--dest',self.dest,expected=1).stdout)

    def test_added_file_is_detected_as_local_modification(self):
        self.install()
        (self.dest/'backend/notes.txt').write_text('USER ADDED')
        self.cli('uninstall','--dest',self.dest,expected=1)
        self.assertTrue((self.dest/'backend/notes.txt').exists())

    def test_force_uninstall_retains_user_changes_in_backup(self):
        self.install()
        (self.dest/'backend/user.txt').write_text('USER MODIFIED')
        self.cli('uninstall','--dest',self.dest,'--force')
        self.assertFalse((self.dest/'backend').exists())
        backups = list((self.dest/guild.CONTROL/'backups').iterdir())
        self.assertEqual((backups[0]/'old/backend/user.txt').read_text(), 'USER MODIFIED')
        self.assertEqual(self.manifest()['skills'], {})

    def test_uninstall_only_owned_and_selected_skills(self):
        self.install('backend,frontend')
        (self.dest/'unrelated').mkdir()
        (self.dest/'unrelated/keep').write_text('KEEP')
        self.cli('uninstall','--dest',self.dest,'--skills','backend')
        self.assertTrue((self.dest/'frontend/SKILL.md').exists())
        self.assertEqual((self.dest/'unrelated/keep').read_text(), 'KEEP')
        self.assertEqual(set(self.manifest()['skills']), {'frontend'})

    def test_force_cannot_uninstall_unmanaged_skill(self):
        (self.dest/'backend').mkdir(parents=True)
        (self.dest/'backend/keep').write_text('KEEP')
        self.cli('uninstall','--dest',self.dest,'--skills','backend','--force',expected=1)
        self.assertEqual((self.dest/'backend/keep').read_text(), 'KEEP')

    @unittest.skipUnless(hasattr(os, 'mkfifo'), 'FIFO unavailable')
    def test_special_files_block_mutations_without_removing_them(self):
        self.install()
        fifo = self.dest/'backend/user.pipe'
        os.mkfifo(fifo)
        self.cli('uninstall','--dest',self.dest,'--force',expected=1)
        self.assertTrue(fifo.exists())

    def test_empty_uninstall_is_noop(self):
        self.cli('uninstall','--dest',self.dest)
        self.assertFalse(self.dest.exists())

    def test_dry_run_uninstall_changes_nothing(self):
        self.install()
        before = guild.inventory(self.dest)
        self.cli('uninstall','--dest',self.dest,'--dry-run')
        self.assertEqual(guild.inventory(self.dest), before)

    def test_check_detects_missing_installed_file(self):
        self.install()
        (self.dest/'backend/references/runbook.md').unlink()
        self.assertIn('MODIFIED', self.cli('check','--dest',self.dest,expected=1).stdout)

    def test_check_reports_source_update_without_reinstall(self):
        self.install()
        source = self.copy_source()
        with (source/'skills/backend/references/runbook.md').open('a') as handle:
            handle.write('\nSource revision.\n')
        self.assertIn('OUTDATED', self.cli('check','--dest',self.dest,source=source,expected=1).stdout)

    def test_corrupt_manifest_blocks_mutations(self):
        self.install()
        path = self.dest/guild.CONTROL/'manifest.json'
        path.write_text('{')
        self.cli('uninstall','--dest',self.dest,expected=1)
        self.assertTrue((self.dest/'backend/SKILL.md').exists())

    def test_manifest_traversal_cannot_delete_outside_directory(self):
        self.install()
        outside = self.base/'outside'
        outside.mkdir()
        (outside/'keep').write_text('KEEP')
        path = self.dest/guild.CONTROL/'manifest.json'
        data = self.manifest()
        data['skills']['../../outside'] = data['skills']['backend']
        path.write_text(json.dumps(data))
        self.cli('uninstall','--dest',self.dest,'--force',expected=1)
        self.assertEqual((outside/'keep').read_text(), 'KEEP')
        self.assertTrue((self.dest/'backend/SKILL.md').exists())

    def test_manifest_relative_file_traversal_is_rejected(self):
        self.install()
        data = self.manifest()
        data['skills']['backend']['files']['../outside'] = 'a'*64
        (self.dest/guild.CONTROL/'manifest.json').write_text(json.dumps(data))
        self.cli('install','--dest',self.dest,expected=1)
        self.assertTrue((self.dest/'backend/SKILL.md').exists())

    @unittest.skipUnless(hasattr(os,'symlink'), 'symlink unavailable')
    def test_destination_symlink_is_rejected(self):
        outside = self.base/'outside'
        outside.mkdir()
        self.dest.symlink_to(outside, target_is_directory=True)
        self.cli('install','--dest',self.dest,expected=1)
        self.assertEqual(list(outside.iterdir()), [])

    @unittest.skipUnless(hasattr(os,'symlink'), 'symlink unavailable')
    def test_nested_payload_symlink_is_rejected_even_with_force(self):
        self.install()
        outside = self.base/'outside.txt'
        outside.write_text('KEEP')
        (self.dest/'backend/link').symlink_to(outside)
        self.cli('uninstall','--dest',self.dest,'--force',expected=1)
        self.assertEqual(outside.read_text(), 'KEEP')

    @unittest.skipUnless(hasattr(os,'symlink'), 'symlink unavailable')
    def test_control_directory_symlink_is_rejected(self):
        self.dest.mkdir()
        outside = self.base/'outside'
        outside.mkdir()
        (self.dest/guild.CONTROL).symlink_to(outside, target_is_directory=True)
        self.cli('install','--dest',self.dest,expected=1)
        self.assertEqual(list(outside.iterdir()), [])

    @unittest.skipUnless(hasattr(os,'symlink'), 'symlink unavailable')
    def test_dangling_manifest_symlink_is_rejected(self):
        (self.dest/guild.CONTROL).mkdir(parents=True)
        (self.dest/guild.CONTROL/'manifest.json').symlink_to(self.base/'missing.json')
        self.cli('install','--dest',self.dest,expected=1)
        self.assertFalse((self.base/'missing.json').exists())

    def test_stale_lock_blocks_force_install(self):
        self.install()
        (self.dest/guild.CONTROL/'lock').mkdir()
        self.cli('install','--dest',self.dest,'--force',expected=1)
        self.assertTrue((self.dest/guild.CONTROL/'lock').exists())
        self.cli('check','--dest',self.dest)

    def test_interrupted_transaction_blocks_later_mutation(self):
        self.install()
        transaction = self.dest/guild.CONTROL/'transactions/interrupted'
        transaction.mkdir()
        (transaction/'journal.json').write_text('{}')
        self.cli('uninstall','--dest',self.dest,'--force',expected=1)
        self.assertTrue((self.dest/'backend/SKILL.md').exists())
        self.assertTrue(transaction.exists())
        self.assertFalse((self.dest/guild.CONTROL/'lock').exists())

    def test_manifest_write_failure_rolls_back_all_moved_payloads(self):
        self.install()
        user_file = self.dest/'backend/user.txt'
        user_file.write_text('USER CONTENT TO PRESERVE')
        before = guild.inventory(self.dest/'backend')
        old = self.manifest()
        original_manifest = (self.dest/guild.CONTROL/'manifest.json').read_bytes()
        new = json.loads(json.dumps(old))
        for name in ('backend','frontend'):
            new['skills'][name] = {'version':'2.0.0','files':guild.inventory(ROOT/'skills'/name)}
        real_writer = guild.atomic_json
        def fail_at_commit(path, data):
            if path == self.dest/guild.CONTROL/'manifest.json':
                raise OSError('simulated disk failure')
            return real_writer(path, data)
        with patch.object(guild, 'atomic_json', side_effect=fail_at_commit):
            with self.assertRaises(OSError):
                guild.transact(self.dest,['backend','frontend'],old,new,True,True)
        self.assertEqual(guild.inventory(self.dest/'backend'), before)
        self.assertFalse((self.dest/'frontend').exists())
        self.assertEqual((self.dest/guild.CONTROL/'manifest.json').read_bytes(), original_manifest)
        self.assertEqual(list((self.dest/guild.CONTROL/'transactions').iterdir()), [])

    def test_init_is_idempotent_and_does_not_overwrite_existing_memory(self):
        project = self.base/'new project'
        self.cli('init',project,'--name','Dự án kiểm chứng')
        memory = project/'.memory'
        self.assertEqual(len(list(memory.rglob('*.md'))), 10)
        progress = memory/'progress.md'
        progress.write_text('USER PROGRESS')
        self.cli('init',project)
        self.assertEqual(progress.read_text(), 'USER PROGRESS')
        self.assertIn('Dự án kiểm chứng', (memory/'architecture.md').read_text())
        self.assertIn('PROPOSED', (memory/'adr/0001-khoi-tao-du-an.md').read_text())

    def test_init_dry_run_writes_nothing(self):
        project = self.base/'not-created'
        self.cli('init',project,'--dry-run')
        self.assertFalse(project.exists())

    @unittest.skipUnless(hasattr(os,'symlink'), 'symlink unavailable')
    def test_init_preflights_all_paths_before_writing(self):
        project = self.base/'project'
        (project/'.memory').mkdir(parents=True)
        outside = self.base/'outside.txt'
        outside.write_text('KEEP')
        (project/'.memory/requirements.md').symlink_to(outside)
        self.cli('init',project,expected=1)
        self.assertFalse((project/'.memory/architecture.md').exists())
        self.assertEqual(outside.read_text(), 'KEEP')

    def test_host_defaults_use_only_isolated_home(self):
        targets = {'codex':'.agents/skills','antigravity':'.gemini/config/skills',
                   'antigravity-cli':'.gemini/antigravity-cli/skills'}
        for tool, relative in targets.items():
            self.cli('install','--tool',tool,'--skills','backend')
            self.assertTrue((self.home/relative/'backend/SKILL.md').exists())
            self.cli('check','--tool',tool)

    def test_workspace_install_and_explicit_destination_precedence(self):
        workspace = self.base/'workspace'
        self.cli('install','--tool','codex','--scope','workspace','--workspace',workspace,'--skills','backend')
        self.assertTrue((workspace/'.agents/skills/backend/SKILL.md').exists())
        self.cli('install','--scope','workspace','--workspace',workspace,'--dest',self.dest,'--skills','frontend')
        self.assertTrue((self.dest/'frontend/SKILL.md').exists())
        self.assertFalse((workspace/'.agents/skills/frontend').exists())

    def test_source_directory_cannot_be_installation_destination(self):
        self.cli('install','--dest',ROOT/'skills','--skills','backend',expected=1)

    def test_frontmatter_catalog_drift_blocks_installation(self):
        source = self.copy_source()
        path = source/'skills/backend/SKILL.md'
        path.write_text(path.read_text().replace('name: backend','name: unexpected'))
        self.cli('install','--dest',self.dest,'--skills','frontend',source=source,expected=1)
        self.assertFalse(self.dest.exists())

    def test_broken_reference_blocks_installation(self):
        source = self.copy_source()
        (source/'skills/backend/references/runbook.md').unlink()
        self.cli('install','--dest',self.dest,'--skills','frontend',source=source,expected=1)
        self.assertFalse(self.dest.exists())

    def test_bash_launcher_from_another_directory(self):
        result = subprocess.run(['bash',str(ROOT/'setup.sh'),'list','--profile','core'],
                                cwd=self.base,env=self.env,text=True,capture_output=True)
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertIn('backend', result.stdout)
        self.assertEqual(list(self.home.iterdir()), [])

if __name__ == '__main__':
    unittest.main()
