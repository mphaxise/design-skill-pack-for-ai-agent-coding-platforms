import tempfile
import unittest
from pathlib import Path
import sys

REPO_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(REPO_ROOT / "src"))

from skillpack.pmf_review import (  # noqa: E402
    generate_pmf_review,
    write_pmf_review,
)


class PmfReviewTests(unittest.TestCase):
    def test_generated_pmf_review_has_required_sections(self) -> None:
        content = generate_pmf_review(
            product="Design Skill Pack",
            segment="UX practitioners",
        )
        required_headers = [
            "# PMF/FMF Review:",
            "## Segment",
            "## Decision To Unblock",
            "## Evidence Signals",
            "## PMF/FMF Risks",
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

    def test_write_pmf_review_persists_content(self) -> None:
        content = generate_pmf_review(
            product="Agent UX Toolkit",
            segment="Founders",
        )
        with tempfile.TemporaryDirectory() as tmp:
            out = Path(tmp) / "pmf-review.md"
            write_pmf_review(content, out)
            self.assertTrue(out.exists())
            saved = out.read_text(encoding="utf-8")
        self.assertIn("Agent UX Toolkit", saved)


if __name__ == "__main__":
    unittest.main()
