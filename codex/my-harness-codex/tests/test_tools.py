import importlib.util
import json
import os
from pathlib import Path
import subprocess
import tempfile
import unittest
from unittest.mock import patch

ROOT = Path(__file__).resolve().parents[1]


def module(name, path):
    spec = importlib.util.spec_from_file_location(name, ROOT / path)
    loaded = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(loaded)
    return loaded


compare = module("compare", "skills/desarrollo-pr-pendientes/scripts/compare_refs.py")
tasks = module("tasks", "skills/desarrollo-sprint-informe/scripts/task_commits.py")
specs = module("specs", "skills/desarrollo-ticket-leer/scripts/select_spec.py")
staged = module("staged", "optional/check_staged.py")
installer = module("installer", "scripts/install.py")


class GitCase(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory(prefix="harness-test-")
        self.addCleanup(self.temp.cleanup)
        self.workspace = Path(self.temp.name)
        self.repo = self.workspace / "repo"
        self.repo.mkdir()
        self.git("init", "-q", "-b", "main")
        self.commit("base.txt", "base\n", "base")

    def git(self, *args):
        # Isolate hooks/config/identity from the user's Git configuration.
        env = os.environ.copy()
        for key in list(env):
            if key.startswith("GIT_"):
                env.pop(key)
        env.update(GIT_CONFIG_NOSYSTEM="1", GIT_CONFIG_GLOBAL=os.devnull)
        return subprocess.run(["git", "-c", "core.hooksPath=" + os.devnull,
                               "-c", "user.name=Harness Test", "-c", "user.email=test@example.invalid",
                               "-c", "commit.gpgsign=false", "-C", str(self.repo), *args],
                              check=True, capture_output=True, text=True, env=env).stdout.strip()

    def commit(self, path, text, message):
        (self.repo / path).write_text(text)
        self.git("add", "--", path)
        self.git("commit", "-qm", message)
        return self.git("rev-parse", "HEAD")

    def test_squash_is_equal_at_endpoints(self):
        self.git("checkout", "-qb", "feature")
        self.commit("sample.txt", "feature\n", "ABC-1 change")
        self.git("checkout", "-q", "main")
        self.commit("other.txt", "other\n", "independent")
        self.git("merge", "--squash", "feature")
        self.git("commit", "-qm", "squash")
        self.assertNotEqual(self.git("diff", "--stat", "main...feature", "--", "sample.txt"), "")
        result = compare.compare(self.repo, "main", "feature", ["sample.txt"])
        self.assertTrue(result["same_content"])
        self.assertEqual(result["deployment"], "not_verified")
        self.assertFalse(compare.compare(self.repo, "main", "feature", [])["same_content"])

    def test_different_content_does_not_claim_missing_feature(self):
        self.git("branch", "before")
        self.commit("sample.txt", "new", "ABC-1")
        result = compare.compare(self.repo, "before", "main", ["sample.txt"])
        self.assertEqual(result["interpretation"], "different_content_review_required")

    def test_literal_pathspec_and_unknown_ref(self):
        self.git("branch", "before")
        self.commit("sample1.txt", "new", "change")
        self.assertTrue(compare.compare(self.repo, "before", "main", ["sample[1].txt"])["same_content"])
        with self.assertRaises(subprocess.CalledProcessError):
            compare.compare(self.repo, "missing", "main", [])

    def test_worktrees_and_partial_containment(self):
        first = self.commit("a.txt", "one", "ABC-1 first")
        self.git("branch", "release", first)
        self.commit("a.txt", "two", "ABC-1 second")
        self.commit("b.txt", "unrelated", "ABC-10 another task")
        worktree = self.workspace / "linked"
        self.git("worktree", "add", "-qb", "fix/ABC-1", str(worktree))
        self.assertTrue((worktree / ".git").is_file())
        self.assertIn(worktree.resolve(), tasks.discover(self.workspace))
        record = tasks.scan(worktree, "ABC-1", ["release", "main", "missing"])
        self.assertEqual(len(record["commits"]), 2)
        refs = {r["ref"]: r for r in record["release_refs"]}
        self.assertFalse(refs["release"]["all_matching_commits_contained"])
        self.assertTrue(refs["main"]["all_matching_commits_contained"])
        self.assertIsNone(refs["missing"]["all_matching_commits_contained"])

    def test_literal_ticket_and_no_evidence(self):
        self.commit("a.txt", "one", "BUG.1+ specific")
        self.commit("b.txt", "two", "BUGx1+ unrelated")
        self.assertEqual(len(tasks.scan(self.repo, "BUG.1+", [])["commits"]), 1)
        record = tasks.scan(self.repo, "ABSENT-1", ["main"])
        self.assertEqual(record["status"], "no_references_found")
        self.assertIsNone(record["release_refs"][0]["all_matching_commits_contained"])

    def test_invalid_index_valid_worktree_is_rejected(self):
        path = self.repo / "sample.json"
        path.write_text("{invalid")
        self.git("add", "sample.json")
        path.write_text("{}")
        self.assertEqual(staged.check(self.repo)[0]["status"], "FALLA")

    def test_valid_index_invalid_worktree_is_accepted(self):
        path = self.repo / "sample.json"
        path.write_text("{}")
        self.git("add", "sample.json")
        path.write_text("{invalid")
        self.assertEqual(staged.check(self.repo)[0]["status"], "PASA")

    def test_compiler_errors_and_no_pycache(self):
        path = self.repo / "sample.py"
        path.write_text("return 1\n")
        self.git("add", "sample.py")
        self.assertEqual(staged.check(self.repo)[0]["status"], "FALLA")
        self.assertFalse((self.repo / "__pycache__").exists())

    def test_deleted_file_is_not_checked(self):
        self.commit("old.json", "{}", "add")
        self.git("rm", "old.json")
        self.assertEqual(staged.check(self.repo), [])


class SpecCase(unittest.TestCase):
    def test_exact_id_numeric_version_not_upload_date(self):
        result = specs.select("ABC-1", [
            {"title": "spec-ABC-10-v20.md", "date": 999, "url": "secret"},
            {"title": "spec-ABC-1-v2.md", "date": 900},
            {"title": "spec-ABC-1-v10.md", "date": 100, "url": "secret"},
        ])
        self.assertEqual(result["candidates"][0]["version"], 10)
        self.assertNotIn("secret", json.dumps(result))

    def test_duplicate_highest_is_ambiguous(self):
        result = specs.select("ABC-1", [{"title": "spec-ABC-1-v2.md", "date": d} for d in (1, 2)])
        self.assertEqual(result["status"], "ambiguous")

    def test_literal_ticket_and_not_found(self):
        self.assertEqual(specs.select("A.1", [{"title": "spec-Ax1-v2.md"}])["status"], "not_found")


class InstallerCase(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory(prefix="harness-install-test-")
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name) / "package"
        self.home = Path(self.temp.name) / "home"
        (self.root / "skills/example").mkdir(parents=True)
        (self.root / "skills/example/SKILL.md").write_text("example")
        (self.root / "agents").mkdir()
        (self.root / "agents/example.toml").write_text('name = "example"\n')

    def test_dry_run_has_no_writes(self):
        self.assertEqual(installer.install(self.root, self.home)["action"], "dry_run")
        self.assertFalse(self.home.exists())
        self.assertFalse((self.root / ".local-state").exists())

    def test_idempotent_install_and_uninstall(self):
        self.assertEqual(installer.install(self.root, self.home, True)["new_entries"], 2)
        self.assertEqual(installer.install(self.root, self.home, True)["new_entries"], 0)
        installer.uninstall(self.root, self.home, True)
        self.assertFalse((self.home / ".agents/skills/example").is_symlink())
        self.assertFalse((self.home / ".codex/agents/example.toml").exists())

    def test_collision_aborts_all_changes(self):
        path = self.home / ".codex/agents/example.toml"
        path.parent.mkdir(parents=True)
        path.write_text("existing user content")
        with self.assertRaises(ValueError):
            installer.install(self.root, self.home, True)
        self.assertEqual(path.read_text(), "existing user content")
        self.assertFalse((self.home / ".agents/skills/example").exists())

    def test_modified_entry_preserved_on_uninstall(self):
        installer.install(self.root, self.home, True)
        path = self.home / ".codex/agents/example.toml"
        path.write_text("user edited")
        with self.assertRaises(ValueError):
            installer.uninstall(self.root, self.home, True)
        self.assertEqual(path.read_text(), "user edited")
        self.assertTrue((self.home / ".agents/skills/example").is_symlink())

    def test_io_failure_rolls_back_new_entries(self):
        with patch.object(installer, "create_file", side_effect=OSError("simulated disk error")):
            with self.assertRaises(OSError):
                installer.install(self.root, self.home, True)
        self.assertFalse((self.home / ".agents/skills/example").is_symlink())
        self.assertFalse((self.home / ".codex/agents/example.toml").exists())

    def test_untrusted_manifest_destination_rejected(self):
        installer.install(self.root, self.home, True)
        manifest = installer.state_path(self.root, self.home)
        data = json.loads(manifest.read_text())
        data["entries"][0]["destination"] = str(self.home / "other")
        manifest.write_text(json.dumps(data))
        with self.assertRaises(ValueError):
            installer.uninstall(self.root, self.home, True)


if __name__ == "__main__":
    unittest.main()
