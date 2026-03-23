import tempfile
import unittest
from pathlib import Path
import sys

REPO_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(REPO_ROOT / "src"))

from skillpack.decision_log import build_playbook, record_decision  # noqa: E402


class DecisionLogTests(unittest.TestCase):
    def test_record_decision_writes_stream_daily_and_milestone(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            logs_dir = Path(tmp) / "logs"
            outputs = record_decision(
                skill="/research-brief",
                stage="strategy-gate",
                decision="Choose confidence-first scope",
                rationale="Trust and clarity are top priority",
                confidence=0.84,
                irreversible=True,
                needs_user_input=True,
                tags=["lens", "strategy"],
                milestone="v0-personalization",
                logs_dir=logs_dir,
            )
            self.assertTrue(outputs["stream"].exists())
            self.assertTrue(outputs["daily"].exists())
            self.assertTrue(outputs["milestone"].exists())

    def test_build_playbook_creates_markdown(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            logs_dir = Path(tmp) / "logs"
            out = Path(tmp) / "playbook.md"
            record_decision(
                skill="/pmf-review",
                stage="belief-gate",
                decision="Require mixed evidence before fit claim",
                rationale="Avoid false confidence",
                confidence=0.76,
                irreversible=False,
                needs_user_input=True,
                tags=["pmf", "evidence"],
                logs_dir=logs_dir,
            )
            path = build_playbook(logs_dir=logs_dir, output_path=out)
            self.assertTrue(path.exists())
            text = path.read_text(encoding="utf-8")
            self.assertIn("Decision volume by skill", text)
            self.assertIn("/pmf-review", text)


if __name__ == "__main__":
    unittest.main()
