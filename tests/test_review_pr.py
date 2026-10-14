"""Behavioral checks of the isolated PR helper using local Git only."""
from pathlib import Path
import subprocess
import os
import shutil
import tempfile
import unittest

SCRIPT = Path(__file__).resolve().parents[1] / 'core/idempiere-pr-review/scripts/review-pr.sh'

class ReviewWorktreeTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory(prefix='review fixtures ')
        self.base = Path(self.temp.name)
        self.upstream = self.base / 'upstream'
        self.work = self.base / 'developer'
        self.destination = self.base / 'review space'
        self.git(self.base, 'init', '-q', '-b', 'master', str(self.upstream))
        self.configure(self.upstream)
        (self.upstream / 'source.txt').write_text('base\n')
        self.git(self.upstream, 'add', 'source.txt')
        self.git(self.upstream, 'commit', '-qm', 'Base fixture')
        self.base_head = self.git(self.upstream, 'rev-parse', 'HEAD').stdout.strip()
        self.git(self.upstream, 'checkout', '-qb', 'ticket')
        (self.upstream / 'source.txt').write_text('PR behavior\n')
        self.git(self.upstream, 'commit', '-qam', 'IDEMPIERE-1234 Fixture change')
        self.pr_head = self.git(self.upstream, 'rev-parse', 'HEAD').stdout.strip()
        self.git(self.upstream, 'update-ref', 'refs/pull/1/head', self.pr_head)
        self.git(self.upstream, 'checkout', '-q', 'master')
        self.git(self.base, 'clone', '-q', str(self.upstream), str(self.work))
        self.configure(self.work)
        self.git(self.work, 'remote', 'add', 'upstream', 'https://github.com/idempiere/idempiere.git')
        # Official configured URL, local fixture transport. No network or account use.
        self.git(self.work, 'config', f'url.{self.upstream}.insteadOf', 'https://github.com/idempiere/idempiere.git')
        # Test-only transport shim: get-url sees the configured URL while fetch
        # uses Git's local insteadOf rewrite. Production validates effective URLs.
        real_git = shutil.which('git')
        self.bin = self.base / 'bin'
        self.bin.mkdir()
        shim = self.bin / 'git'
        shim.write_text('#!/bin/bash\n'
                        'if [[ "${3:-}" = remote && "${4:-}" = get-url ]]; then\n'
                        f'  exec "{real_git}" -C "$2" config --get "remote.$5.url"\n'
                        'fi\n'
                        f'exec "{real_git}" "$@"\n')
        shim.chmod(0o755)
        self.helper_env = dict(os.environ, PATH=str(self.bin) + os.pathsep + os.environ['PATH'])
        self.original_head = self.git(self.work, 'rev-parse', 'HEAD').stdout.strip()

    def tearDown(self):
        self.temp.cleanup()

    def git(self, cwd, *args):
        return subprocess.run(['git', '-C', str(cwd), *args], text=True, capture_output=True, check=True)

    def configure(self, cwd):
        self.git(cwd, 'config', 'user.name', 'Review Fixture')
        self.git(cwd, 'config', 'user.email', 'fixture@example.invalid')
        self.git(cwd, 'config', 'commit.gpgSign', 'false')

    def helper(self, *args, success=True):
        result = subprocess.run(['bash', str(SCRIPT), *map(str, args)], cwd=self.work, text=True, capture_output=True, env=self.helper_env)
        self.assertEqual(result.returncode == 0, success, result.stdout + result.stderr)
        return result

    def prepare(self):
        self.helper('prepare', '1', self.destination)

    def assert_original(self):
        self.assertEqual(self.git(self.work, 'branch', '--show-current').stdout.strip(), 'master')
        self.assertEqual(self.git(self.work, 'rev-parse', 'HEAD').stdout.strip(), self.original_head)

    def test_merge_preserves_dirty_original_and_untracked_work(self):
        (self.work / 'source.txt').write_text('Developer work\n')
        (self.work / 'notes.txt').write_text('Untracked work\n')
        self.prepare()
        self.assert_original()
        self.assertEqual((self.work / 'source.txt').read_text(), 'Developer work\n')
        self.assertEqual((self.work / 'notes.txt').read_text(), 'Untracked work\n')
        self.assertEqual((self.destination / 'source.txt').read_text(), 'PR behavior\n')
        parents = self.git(self.destination, 'show', '-s', '--format=%P', 'HEAD').stdout.split()
        self.assertEqual(parents, [self.base_head, self.pr_head])
        self.helper('cleanup', self.destination)
        self.assertFalse(self.destination.exists())
        self.assert_original()

    def test_existing_destination_is_not_overwritten(self):
        self.destination.mkdir()
        (self.destination / 'valuable.txt').write_text('Keep')
        self.helper('prepare', '1', self.destination, success=False)
        self.assertEqual((self.destination / 'valuable.txt').read_text(), 'Keep')

    def test_wrong_remote_and_secret_url_are_not_printed(self):
        secret_url = 'https://secret-token@example.invalid/private.git'
        self.git(self.work, 'remote', 'set-url', 'upstream', secret_url)
        result = self.helper('prepare', '1', self.destination, success=False)
        self.assertNotIn('secret-token', result.stdout + result.stderr)
        self.assertFalse(self.destination.exists())

    def test_missing_pr_does_not_create_worktree_or_refs(self):
        self.helper('prepare', '9', self.destination, success=False)
        self.assertFalse(self.destination.exists())
        self.assertEqual(self.git(self.work, 'for-each-ref', 'refs/idempiere-review').stdout, '')
        self.assert_original()

    def test_conflict_cleans_only_review_worktree(self):
        (self.upstream / 'source.txt').write_text('Conflicting upstream\n')
        self.git(self.upstream, 'commit', '-qam', 'Upstream change')
        self.helper('prepare', '1', self.destination, success=False)
        self.assertFalse(self.destination.exists())
        self.assert_original()
        self.assertEqual(self.git(self.work, 'for-each-ref', 'refs/idempiere-review').stdout, '')

    def test_cleanup_refuses_untracked_file(self):
        self.prepare()
        (self.destination / 'analysis.txt').write_text('Keep findings')
        self.helper('cleanup', self.destination, success=False)
        self.assertTrue((self.destination / 'analysis.txt').exists())

    def test_cleanup_refuses_ignored_file(self):
        self.prepare()
        gitdir = Path(self.git(self.destination, 'rev-parse', '--absolute-git-dir').stdout.strip())
        common = Path(self.git(self.destination, 'rev-parse', '--path-format=absolute', '--git-common-dir').stdout.strip())
        (common / 'info/exclude').write_text('report.log\n')
        (self.destination / 'report.log').write_text('Preserve local report')
        self.helper('cleanup', self.destination, success=False)
        self.assertTrue((self.destination / 'report.log').exists())

    def test_cleanup_refuses_added_commit(self):
        self.prepare()
        (self.destination / 'fix.txt').write_text('Useful proposed fix')
        self.git(self.destination, 'add', 'fix.txt')
        self.git(self.destination, 'commit', '-qm', 'Local fix')
        self.helper('cleanup', self.destination, success=False)
        self.assertTrue((self.destination / 'fix.txt').exists())

    def test_cleanup_refuses_foreign_worktree(self):
        self.git(self.work, 'worktree', 'add', '-q', '--detach', str(self.destination), 'HEAD')
        self.helper('cleanup', self.destination, success=False)
        self.assertTrue(self.destination.exists())

    def test_already_integrated_pr_has_safe_cleanup(self):
        self.git(self.upstream, 'merge', '--ff-only', 'ticket')
        self.prepare()
        self.helper('cleanup', self.destination)
        self.assertFalse(self.destination.exists())
        self.assert_original()

if __name__ == '__main__':
    unittest.main()
