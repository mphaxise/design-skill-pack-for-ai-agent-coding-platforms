import unittest
from pathlib import Path
import sys

REPO_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(REPO_ROOT / "src"))

from skillpack.lens import load_lens, validate_lens  # noqa: E402


class LensTests(unittest.TestCase):
    def test_default_lens_is_valid(self) -> None:
        data = load_lens()
        errors = validate_lens(data)
        self.assertEqual([], errors)
        self.assertEqual("Praneet", data["owner"])

    def test_missing_field_fails_validation(self) -> None:
        data = load_lens()
        data.pop("ask_policy")
        errors = validate_lens(data)
        self.assertTrue(any("ask_policy" in err for err in errors))


if __name__ == "__main__":
    unittest.main()
