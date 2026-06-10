import importlib.util
import tempfile
import unittest
from pathlib import Path


SCRIPT_PATH = Path(__file__).resolve().parents[1] / "scripts" / "estimate_tokens.py"


def load_module():
    spec = importlib.util.spec_from_file_location("estimate_tokens", SCRIPT_PATH)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


class FakeEncoding:
    def encode(self, text):
        return text.split()


class EstimateTokensTest(unittest.TestCase):
    def test_rolls_file_counts_up_to_each_parent_directory(self):
        module = load_module()

        with tempfile.TemporaryDirectory() as temp_dir:
            root = Path(temp_dir)
            (root / "alpha.txt").write_text("one two", encoding="utf-8")
            nested = root / "docs" / "guides"
            nested.mkdir(parents=True)
            (nested / "intro.md").write_text("three four five", encoding="utf-8")

            result = module.estimate_tokens(root, FakeEncoding())

        self.assertEqual(result.total_tokens, 5)
        self.assertEqual(result.file_count, 2)
        self.assertEqual(result.directory_totals[Path(".")], 5)
        self.assertEqual(result.directory_totals[Path("docs")], 3)
        self.assertEqual(result.directory_totals[Path("docs/guides")], 3)
        self.assertEqual(result.skipped_files, [])

    def test_skips_default_generated_directories(self):
        module = load_module()

        with tempfile.TemporaryDirectory() as temp_dir:
            root = Path(temp_dir)
            (root / "keep.txt").write_text("one", encoding="utf-8")
            git_dir = root / ".git"
            git_dir.mkdir()
            (git_dir / "ignored.txt").write_text("two three four", encoding="utf-8")
            node_modules = root / "node_modules"
            node_modules.mkdir()
            (node_modules / "ignored.js").write_text("five six", encoding="utf-8")

            result = module.estimate_tokens(root, FakeEncoding())

        self.assertEqual(result.total_tokens, 1)
        self.assertEqual(result.file_count, 1)
        self.assertEqual(result.skipped_directories, [Path(".git"), Path("node_modules")])

    def test_skips_binary_like_files(self):
        module = load_module()

        with tempfile.TemporaryDirectory() as temp_dir:
            root = Path(temp_dir)
            (root / "keep.txt").write_text("one two", encoding="utf-8")
            (root / "image.bin").write_bytes(b"abc\x00def")

            result = module.estimate_tokens(root, FakeEncoding())

        self.assertEqual(result.total_tokens, 2)
        self.assertEqual(result.file_count, 1)
        self.assertEqual(result.skipped_files, [(Path("image.bin"), "binary")])

    def test_skips_unreadable_files(self):
        module = load_module()

        with tempfile.TemporaryDirectory() as temp_dir:
            root = Path(temp_dir)
            (root / "keep.txt").write_text("one two", encoding="utf-8")
            (root / "missing-link.txt").symlink_to(root / "does-not-exist.txt")

            result = module.estimate_tokens(root, FakeEncoding())

        self.assertEqual(result.total_tokens, 2)
        self.assertEqual(result.file_count, 1)
        self.assertEqual(result.skipped_files, [(Path("missing-link.txt"), "unreadable")])

    def test_rejects_missing_root(self):
        module = load_module()

        with tempfile.TemporaryDirectory() as temp_dir:
            missing = Path(temp_dir) / "missing"

            with self.assertRaises(FileNotFoundError):
                module.estimate_tokens(missing, FakeEncoding())


if __name__ == "__main__":
    unittest.main()
