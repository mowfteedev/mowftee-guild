"""Exercise copy/remove only inside a temporary HOME; no host installation."""
from pathlib import Path
import os
import shutil
import subprocess
import tempfile
import unittest

ROOT = Path(__file__).resolve().parent.parent
MARKER = '.mowftee-guild'

class SetupTests(unittest.TestCase):
    def setUp(self):
        self.temporary = tempfile.TemporaryDirectory(prefix='guild-setup-')
        self.addCleanup(self.temporary.cleanup)
        self.base = Path(self.temporary.name).resolve()
        self.home = self.base/'home with spaces'
        self.home.mkdir()
        self.env = dict(os.environ, HOME=str(self.home))
        self.dest = self.home/'.agents/skills'

    def run_setup(self, *args, expected=0, source=ROOT):
        result = subprocess.run(['bash', str(source/'setup.sh'), *args],
                                cwd=self.base, env=self.env, capture_output=True,
                                text=True, timeout=30)
        self.assertEqual(result.returncode, expected, result.stdout+result.stderr)
        return result

    def test_help_and_invalid_arguments_do_not_install(self):
        self.run_setup()
        self.run_setup('--help')
        self.run_setup('unknown', expected=2)
        self.run_setup('install','unknown-host', expected=2)
        self.run_setup('install','codex','extra', expected=2)
        self.assertEqual(list(self.home.iterdir()), [])

    def test_install_copies_the_markdown_for_each_host(self):
        targets = {'codex':'.agents/skills', 'antigravity':'.gemini/config/skills',
                   'antigravity-cli':'.gemini/antigravity-cli/skills'}
        names = {p.name for p in (ROOT/'skills').iterdir() if (p/'SKILL.md').is_file()}
        for host, relative in targets.items():
            self.run_setup('install',host)
            dest = self.home/relative
            self.assertEqual({p.name for p in dest.iterdir()}, names)
            for name in names:
                self.assertEqual((dest/name/'SKILL.md').read_bytes(),
                                 (ROOT/'skills'/name/'SKILL.md').read_bytes())
                self.assertTrue((dest/name/'references/runbook.md').is_file())
                self.assertTrue((dest/name/MARKER).is_file())
                self.assertEqual((dest/name/'LICENSE.txt').read_bytes(),
                                 (ROOT/'LICENSE').read_bytes())

    def test_missing_source_license_does_not_replace_installed_skills(self):
        self.run_setup('install','codex')
        installed = self.dest/'backend/SKILL.md'
        installed.write_text('KEEP INSTALLED COPY')
        source = self.base/'incomplete repo'
        source.mkdir()
        shutil.copy2(ROOT/'setup.sh',source/'setup.sh')
        (source/'skills/backend').mkdir(parents=True)
        (source/'skills/backend/SKILL.md').write_text('NEW COPY')
        self.run_setup('install','codex',source=source,expected=1)
        self.assertEqual(installed.read_text(), 'KEEP INSTALLED COPY')
        self.run_setup('uninstall','codex',source=source)
        self.assertEqual(list(self.dest.iterdir()), [])

    def test_skill_specific_license_is_preserved(self):
        source = self.base/'repo with a specific notice'
        source.mkdir()
        for name in ('setup.sh', 'LICENSE'):
            shutil.copy2(ROOT/name,source/name)
        skill = source/'skills/example'
        skill.mkdir(parents=True)
        (skill/'SKILL.md').write_text('EXAMPLE SKILL')
        (skill/'LICENSE.txt').write_text('SPECIFIC NOTICE TO PRESERVE')
        self.run_setup('install','codex',source=source)
        self.assertEqual((self.dest/'example/LICENSE.txt').read_text(),
                         'SPECIFIC NOTICE TO PRESERVE')

    def test_reinstall_refreshes_own_copies_and_preserves_foreign_files(self):
        self.run_setup('install','codex')
        foreign = self.dest/'another-skill'
        foreign.mkdir()
        (foreign/'keep.txt').write_text('KEEP')
        (self.dest/'backend/old-note.txt').write_text('STALE INSTALLED COPY')
        (self.dest/'backend/SKILL.md').write_text('OLD INSTALLED COPY')
        self.run_setup('install','codex')
        self.assertEqual((self.dest/'backend/SKILL.md').read_bytes(),
                         (ROOT/'skills/backend/SKILL.md').read_bytes())
        self.assertFalse((self.dest/'backend/old-note.txt').exists())
        self.assertEqual((foreign/'keep.txt').read_text(), 'KEEP')

    def test_uninstall_removes_own_copies_including_retired_skills(self):
        self.run_setup('install','codex')
        foreign = self.dest/'another-skill'
        foreign.mkdir()
        (foreign/'keep.txt').write_text('KEEP')
        retired = self.dest/'retired-role'
        retired.mkdir()
        (retired/MARKER).touch()
        (retired/'SKILL.md').write_text('OLD SKILL')
        self.run_setup('uninstall','codex')
        self.assertEqual(list(self.dest.iterdir()), [foreign])
        self.assertEqual((foreign/'keep.txt').read_text(), 'KEEP')
        self.assertTrue((ROOT/'skills/backend/SKILL.md').is_file())
        self.run_setup('uninstall','codex')

    def test_name_collision_is_preserved_before_copying_other_skills(self):
        existing = self.dest/'frontend'
        existing.mkdir(parents=True)
        (existing/'keep.txt').write_text('USER SKILL')
        self.run_setup('install','codex',expected=1)
        self.assertEqual((existing/'keep.txt').read_text(), 'USER SKILL')
        self.assertFalse((self.dest/'backend').exists())

    @unittest.skipUnless(hasattr(os, 'symlink'), 'symlink unavailable')
    def test_symlink_target_is_not_overwritten_or_removed(self):
        self.dest.mkdir(parents=True)
        outside = self.base/'outside'
        outside.mkdir()
        (outside/'keep.txt').write_text('KEEP')
        (self.dest/'frontend').symlink_to(outside,target_is_directory=True)
        self.run_setup('install','codex',expected=1)
        self.run_setup('uninstall','codex')
        self.assertEqual((outside/'keep.txt').read_text(), 'KEEP')
        self.assertTrue((self.dest/'frontend').is_symlink())

    @unittest.skipUnless(hasattr(os, 'symlink'), 'symlink unavailable')
    def test_symlink_inside_an_owned_copy_does_not_modify_external_file(self):
        self.run_setup('install','codex')
        outside = self.base/'outside.txt'
        outside.write_text('KEEP')
        path = self.dest/'backend/SKILL.md'
        path.unlink()
        path.symlink_to(outside)
        self.run_setup('install','codex')
        self.assertEqual(outside.read_text(), 'KEEP')
        self.assertFalse(path.is_symlink())

    def test_source_repository_is_not_replaced_or_removed(self):
        source = self.dest/'backend'
        shutil.copytree(ROOT,source,ignore=shutil.ignore_patterns('.git','__pycache__'))
        (source/MARKER).touch()
        for action in ('install','uninstall'):
            self.run_setup(action,'codex',source=source,expected=1)
            self.assertTrue((source/'setup.sh').is_file())
            self.assertTrue((source/'README.md').is_file())
        self.assertFalse((self.dest/'frontend').exists())

    def test_uninstall_without_installing_does_not_create_directories(self):
        self.run_setup('uninstall','codex')
        self.assertFalse(self.dest.exists())

if __name__ == '__main__':
    unittest.main()
