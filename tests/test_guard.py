"""Deterministic scope guard tests. Run: python -m unittest discover -s tests."""
import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "tools"))
from guard import check, changed_paths
import subprocess
import tempfile


CONTRACT = {
    "goal": "Make the existing button blue",
    "acceptance": ["Button displays blue"],
    "allowed_paths": ["src/components/Button.tsx", "tests/"],
    "protected_paths": [".coherence/task.json"],
}


class GuardTests(unittest.TestCase):
    def test_allowed_file(self):
        self.assertEqual(check(CONTRACT, ["src/components/Button.tsx"]), [])

    def test_allowed_directory(self):
        self.assertEqual(check(CONTRACT, ["tests/button.test.ts"]), [])

    def test_new_architecture_out_of_scope(self):
        self.assertTrue(check(CONTRACT, ["src/theme/ThemeProvider.tsx"]))

    def test_contract_modification_rejected(self):
        self.assertTrue(check(CONTRACT, [".coherence/task.json"]))

    def test_missing_acceptance_rejected(self):
        self.assertTrue(check({**CONTRACT, "acceptance": []}, []))

    def test_deleted_file_outside_scope_rejected(self):
        self.assertTrue(check(CONTRACT, ['src/legacy/unused.py']))

    def test_git_diff_includes_deletions(self):
        with tempfile.TemporaryDirectory() as tmp:
            def git(*args):
                return subprocess.check_output(['git', '-C', tmp, *args], text=True).strip()
            git('init', '-q')
            git('config', 'user.email', 'test@example.com')
            git('config', 'user.name', 'Test')
            file = Path(tmp) / 'obsolete.py'
            file.write_text('print(1)')
            git('add', '.')
            git('commit', '-qm', 'baseline')
            baseline = git('rev-parse', 'HEAD')
            file.unlink()
            git('add', '-u')
            git('commit', '-qm', 'remove')
            old_cwd = __import__('os').getcwd()
            try:
                __import__('os').chdir(tmp)
                self.assertIn('obsolete.py', changed_paths(baseline))
            finally:
                __import__('os').chdir(old_cwd)

    def test_empty_scope_denied(self):
        self.assertTrue(check({**CONTRACT, "allowed_paths": []}, []))


if __name__ == "__main__":
    unittest.main()
