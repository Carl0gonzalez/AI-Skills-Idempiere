import importlib.util
from pathlib import Path
import tempfile
import tomllib
import unittest

spec = importlib.util.spec_from_file_location("installer", Path(__file__).resolve().parents[1] / "install.py")
installer = importlib.util.module_from_spec(spec)
spec.loader.exec_module(installer)


class InstallationTests(unittest.TestCase):
    def test_dry_run_install_idempotency_and_uninstall(self):
        with tempfile.TemporaryDirectory() as directory:
            home = Path(directory)
            installer.run(home)
            self.assertEqual(list(home.iterdir()), [])
            installer.run(home, apply=True)
            entries = installer.plan(home)
            for path, source, content in entries:
                self.assertTrue(installer.same(path, source, content))
                if content:
                    data = tomllib.loads(path.read_text())
                    self.assertNotIn("__SKILLS_ROOT__", data["developer_instructions"])
                    self.assertNotIn("model", data)
            before = {path: path.lstat().st_mtime_ns for path, _, _ in entries}
            installer.run(home, apply=True)
            self.assertEqual(before, {path: path.lstat().st_mtime_ns for path, _, _ in entries})
            installer.run(home, apply=True, uninstall=True)
            self.assertTrue(all(not path.exists() and not path.is_symlink() for path, _, _ in entries))

    def test_conflict_is_detected_before_any_creation(self):
        with tempfile.TemporaryDirectory() as directory:
            home = Path(directory)
            collision = home / ".codex/agents/idempiere-reviewer.toml"
            collision.parent.mkdir(parents=True)
            collision.write_text("custom configuration")
            with self.assertRaises(ValueError):
                installer.run(home, apply=True)
            self.assertEqual(collision.read_text(), "custom configuration")
            self.assertFalse((home / ".agents").exists())
            self.assertFalse((collision.parent / "idempiere-designer.toml").exists())

    def test_legacy_duplicate_and_broken_link_are_preserved(self):
        for location in (".codex/skills", ".agents/skills"):
            with self.subTest(location=location), tempfile.TemporaryDirectory() as directory:
                home = Path(directory)
                path = home / location / installer.SKILLS[0]
                path.parent.mkdir(parents=True)
                path.symlink_to(home / "missing")
                with self.assertRaises(ValueError):
                    installer.run(home, apply=True)
                self.assertTrue(path.is_symlink())

    def test_uninstall_preserves_modified_agent_and_other_entries(self):
        with tempfile.TemporaryDirectory() as directory:
            home = Path(directory)
            installer.run(home, apply=True)
            path = home / ".codex/agents/idempiere-reviewer.toml"
            path.write_text("customized")
            with self.assertRaises(ValueError):
                installer.run(home, apply=True, uninstall=True)
            self.assertEqual(path.read_text(), "customized")
            self.assertTrue((home / ".agents/skills" / installer.SKILLS[0]).is_symlink())


if __name__ == "__main__":
    unittest.main()
