"""Verify revision tracking detects real resource changes without touching skills."""
from pathlib import Path
import runpy
import subprocess
import tempfile
import unittest

SCRIPT = Path(__file__).resolve().parents[1] / 'scripts/catalog_versions.py'

class CatalogRevisionTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory(prefix='catalog revision ')
        self.root = Path(self.temp.name)
        namespace = runpy.run_path(str(SCRIPT))
        self.inventory = namespace['inventory']
        self.inventory.__globals__['ROOT'] = self.root
        for group in ['idempiere-8', 'idempiere-13']:
            folder = self.root / group / 'sample-skill'
            folder.mkdir(parents=True)
            (folder / 'SKILL.md').write_text('---\nname: sample-skill\ndescription: Fixture\n---\nRule\n')

    def tearDown(self):
        self.temp.cleanup()

    def test_same_resources_same_skill_revision_distinct_target_entries(self):
        data = self.inventory()
        self.assertEqual(data['entry_count'], 2)
        self.assertEqual(data['distinct_names'], 1)
        self.assertEqual(data['skills'][0]['content_revision'], data['skills'][1]['content_revision'])
        self.assertNotEqual(data['skills'][0]['target_idempiere'], data['skills'][1]['target_idempiere'])

    def test_added_modified_and_renamed_resource_changes_revision(self):
        original = self.inventory()['skills'][0]['content_revision']
        reference = self.root / 'idempiere-13/sample-skill/reference.md'
        reference.write_text('First resource')
        added = self.inventory()['skills'][0]['content_revision']
        self.assertNotEqual(original, added)
        reference.write_text('Updated resource')
        updated = self.inventory()['skills'][0]['content_revision']
        self.assertNotEqual(added, updated)
        reference.rename(reference.with_name('renamed.md'))
        self.assertNotEqual(updated, self.inventory()['skills'][0]['content_revision'])

    def test_repository_readme_is_not_a_skill_resource(self):
        before = self.inventory()
        (self.root / 'README.md').write_text('Repository documentation')
        self.assertEqual(before, self.inventory())

    def test_check_is_read_only_and_rejects_stale_inventory(self):
        scripts = self.root / 'scripts'
        scripts.mkdir()
        local_script = scripts / 'catalog_versions.py'
        local_script.write_bytes(SCRIPT.read_bytes())
        def invoke(flag):
            return subprocess.run(['python3', str(local_script), flag], capture_output=True, text=True)
        self.assertEqual(invoke('--write').returncode, 0)
        manifest = self.root / 'docs/skill-versions.json'
        recorded = manifest.read_bytes()
        self.assertEqual(invoke('--check').returncode, 0)
        (self.root / 'idempiere-8/sample-skill/SKILL.md').write_text('Changed instructions')
        self.assertNotEqual(invoke('--check').returncode, 0)
        self.assertEqual(recorded, manifest.read_bytes())

if __name__ == '__main__':
    unittest.main()
