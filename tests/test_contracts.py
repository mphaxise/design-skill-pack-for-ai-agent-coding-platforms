import json
import tempfile
import unittest
from pathlib import Path
import sys

REPO_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(REPO_ROOT / "src"))

from skillpack.contracts import load_contracts, validate_contracts  # noqa: E402


class ContractTests(unittest.TestCase):
    def test_default_contracts_are_valid(self) -> None:
        data = load_contracts()
        errors = validate_contracts(data)
        self.assertEqual([], errors)
        self.assertEqual(4, len(data["skills"]))

    def test_missing_security_field_fails_validation(self) -> None:
        data = load_contracts()
        data["skills"][0]["security"].pop("no_fabrication")
        errors = validate_contracts(data)
        self.assertTrue(any("no_fabrication" in err for err in errors))

    def test_duplicate_name_fails_validation(self) -> None:
        data = load_contracts()
        data["skills"][1]["name"] = data["skills"][0]["name"]
        errors = validate_contracts(data)
        self.assertTrue(any("duplicate skill name" in err for err in errors))


class ContractLoadPathTests(unittest.TestCase):
    def test_load_from_explicit_path(self) -> None:
        sample = {
            "version": "0.0.1",
            "skills": [
                {
                    "name": "/x",
                    "objective": "x",
                    "required_output": [],
                    "handoff_to": [],
                    "prohibited": [],
                    "security": {
                        "no_fabrication": True,
                        "external_fetch_allowed": False,
                        "local_write_allowed": True,
                    },
                }
            ],
        }
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "contracts.json"
            path.write_text(json.dumps(sample), encoding="utf-8")
            loaded = load_contracts(path)
        self.assertEqual(sample, loaded)


if __name__ == "__main__":
    unittest.main()
