import tempfile
import unittest
from pathlib import Path
import sys

REPO_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(REPO_ROOT / "src"))

from skillpack.ux_review import (  # noqa: E402
    generate_ux_review,
    write_ux_review,
)


class UxReviewTests(unittest.TestCase):
    def test_generated_ux_review_has_required_sections(self) -> None:
        content = generate_ux_review(
            flow="Activation Flow",
            target_user="Product builders",
        )
        required_headers = [
            "# UX Review:",
            "## Target User",
            "## Context",
            "## Prioritized Issues",
            "## Recommended Fixes",
            "## User Outcome Rationale",
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

    def test_write_ux_review_persists_content(self) -> None:
        content = generate_ux_review(
            flow="Research Intake Flow",
            target_user="Design leads",
        )
        with tempfile.TemporaryDirectory() as tmp:
            out = Path(tmp) / "ux-review.md"
            write_ux_review(content, out)
            self.assertTrue(out.exists())
            saved = out.read_text(encoding="utf-8")
        self.assertIn("Research Intake Flow", saved)


if __name__ == "__main__":
    unittest.main()
