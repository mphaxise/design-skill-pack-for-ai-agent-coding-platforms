import tempfile
import unittest
from pathlib import Path
import sys

REPO_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(REPO_ROOT / "src"))

from skillpack.research_brief import (  # noqa: E402
    generate_research_brief,
    write_research_brief,
)


class ResearchBriefTests(unittest.TestCase):
    def test_generated_brief_has_required_sections(self) -> None:
        content = generate_research_brief(
            topic="Design QA Workflow",
            audience="UX practitioners",
        )
        required_headers = [
            "# Research Brief:",
            "## Objective",
            "## Target Audience",
            "## Problem Statement",
            "## Decision To Unblock",
            "## Hypotheses",
            "## Method Plan",
            "## Evidence Guardrails",
            "## Personal Perspective Checkpoint",
            "## Open Risks",
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

    def test_write_research_brief_persists_content(self) -> None:
        content = generate_research_brief(
            topic="PMF Signal Review",
            audience="Founders",
        )
        with tempfile.TemporaryDirectory() as tmp:
            out = Path(tmp) / "brief.md"
            write_research_brief(content, out)
            self.assertTrue(out.exists())
            saved = out.read_text(encoding="utf-8")
        self.assertIn("PMF Signal Review", saved)


if __name__ == "__main__":
    unittest.main()
