import tempfile
import unittest
from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "tools"))
from retrofit import inventory


class RetrofitTests(unittest.TestCase):
    def test_report_is_read_only_and_descriptive(self):
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            (root / "app.py").write_text("# TODO revisit\nprint('ok')\n")
            (root / "package.json").write_text("{}")
            result = inventory(root, ["app.py", "package.json"])
            self.assertEqual(result["tracked_files"], 2)
            self.assertEqual(result["dependency_manifests"], ["package.json"])
            self.assertEqual(len(result["maintenance_markers"]), 1)
            self.assertEqual((root / "app.py").read_text(), "# TODO revisit\nprint('ok')\n")

    def test_skips_generated_and_symlink(self):
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            (root / "node_modules").mkdir()
            (root / "node_modules" / "lib.js").write_text("TODO")
            (root / "main.py").write_text("pass")
            (root / "link.py").symlink_to(root / "main.py")
            result = inventory(root, ["node_modules/lib.js", "main.py", "link.py"])
            self.assertEqual(result["tracked_files"], 1)


if __name__ == "__main__":
    unittest.main()
