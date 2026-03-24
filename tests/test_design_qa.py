import tempfile
import unittest
from pathlib import Path
import sys

REPO_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(REPO_ROOT / "src"))

from skillpack.design_qa import (  # noqa: E402
    generate_design_qa,
    write_design_qa,
)


class DesignQaTests(unittest.TestCase):
    def test_generated_design_qa_has_required_sections(self) -> None:
        content = generate_design_qa(
            feature="Onboarding Flow",
            target_user="New users",
        )
        required_headers = [
            "# Design QA Report:",
            "## Objective",
            "## Target User",
            "## QA Scope",
            "## Findings (Severity Ranked)",
            "## Reproduction Notes",
            "## User Impact",
            "## Personal Perspective Checkpoint",
            "## Next Actions",
            "## Checklist",
            "## Memo",
            "## Scorecard",
            "## Praneet POV Applied",
            "## Assumptions",
            "## Needs Your Judgment",
        ]
        for header in required_headers:
            self.assertIn(header, content)

    def test_write_design_qa_persists_content(self) -> None:
        content = generate_design_qa(
            feature="Checkout Flow",
            target_user="Returning users",
        )
        with tempfile.TemporaryDirectory() as tmp:
            out = Path(tmp) / "design-qa.md"
            write_design_qa(content, out)
            self.assertTrue(out.exists())
            saved = out.read_text(encoding="utf-8")
        self.assertIn("Checkout Flow", saved)


if __name__ == "__main__":
    unittest.main()
