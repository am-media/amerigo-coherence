"""Deterministic scope guard tests. Run: python -m unittest discover -s tests."""
import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "tools"))
from guard import check


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

    def test_empty_scope_denied(self):
        self.assertTrue(check({**CONTRACT, "allowed_paths": []}, []))


if __name__ == "__main__":
    unittest.main()
