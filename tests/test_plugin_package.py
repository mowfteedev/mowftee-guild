"""Check the distributable payload, without changing any installed host."""
import importlib.util
from pathlib import Path
import shutil
import tempfile
import unittest
import zipfile

ROOT = Path(__file__).resolve().parent.parent
spec = importlib.util.spec_from_file_location('package_plugin', ROOT/'scripts/package_plugin.py')
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)


class PluginPackageTests(unittest.TestCase):
    def test_archive_preserves_skills_and_leaves_out_repo_and_private_files(self):
        with tempfile.TemporaryDirectory(prefix='guild-package-') as temporary:
            base = Path(temporary)
            source = base/'source'
            source.mkdir()
            for name in ('plugin.json', 'LICENSE'):
                shutil.copy2(ROOT/name, source/name)
            shutil.copytree(ROOT/'.agents', source/'.agents')
            shutil.copytree(ROOT/'skills', source/'skills')
            (source/'.git').mkdir()
            (source/'.git/config').write_text('LOCAL REPOSITORY DATA')
            (source/'.env').write_text('LOCAL CONFIGURATION')
            (source/'skills/backend/.env').write_text('LOCAL SKILL SCRATCH FILE')
            (source/'workflows').mkdir()
            (source/'workflows/note.md').write_text('HUMAN REFERENCE')
            (source/'skills/backend/references/__pycache__').mkdir()
            (source/'skills/backend/references/__pycache__/cache.pyc').write_bytes(b'CACHE')
            archive = module.package_plugin(source, base/'output')
            with zipfile.ZipFile(archive) as bundle:
                self.assertIsNone(bundle.testzip())
                names = set(bundle.namelist())
                skills = list((ROOT/'skills').glob('*/SKILL.md'))
                self.assertEqual(len([n for n in names if n.endswith('/SKILL.md')]),len(skills))
                for path in (ROOT/'skills').rglob('*'):
                    if path.is_file() and '__pycache__' not in path.parts:
                        self.assertEqual(bundle.read(path.relative_to(ROOT).as_posix()),path.read_bytes())
                for name in ('plugin.json', 'LICENSE', '.agents/plugins/marketplace.json'):
                    self.assertEqual(bundle.read(name),(ROOT/name).read_bytes())
                self.assertFalse(any('__pycache__' in n or n.endswith('.env') or n.startswith(('.git/','workflows/')) for n in names))

    def test_linked_resource_is_rejected_before_creating_an_archive(self):
        with tempfile.TemporaryDirectory(prefix='guild-package-link-') as temporary:
            base = Path(temporary)
            source = base/'source'
            source.mkdir()
            for name in ('plugin.json', 'LICENSE'):
                shutil.copy2(ROOT/name, source/name)
            shutil.copytree(ROOT/'.agents', source/'.agents')
            skill = source/'skills/example'
            skill.mkdir(parents=True)
            (skill/'SKILL.md').write_text('EXAMPLE SKILL')
            outside = base/'outside'
            outside.mkdir()
            (outside/'local.txt').write_text('DO NOT PACKAGE')
            (skill/'references').symlink_to(outside,target_is_directory=True)
            with self.assertRaises(ValueError):
                module.package_plugin(source, base/'output')
            self.assertFalse((base/'output').exists())


if __name__ == '__main__':
    unittest.main()
