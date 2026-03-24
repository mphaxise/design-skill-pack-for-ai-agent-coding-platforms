import os
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]


class CliIntegrationTests(unittest.TestCase):
    def _run(self, args: list[str]) -> subprocess.CompletedProcess[str]:
        env = os.environ.copy()
        env["PYTHONPATH"] = str(REPO_ROOT / "src")
        return subprocess.run(
            [sys.executable, "-m", "skillpack.cli", *args],
            cwd=REPO_ROOT,
            env=env,
            capture_output=True,
            text=True,
            check=True,
        )

    def test_end_to_end_cli_generates_all_four_skill_outputs(self) -> None:
        check = self._run(["check-contracts"])
        self.assertIn("valid", check.stdout.lower())

        with tempfile.TemporaryDirectory() as tmp:
            out_dir = Path(tmp)
            outputs = {
                "research": out_dir / "research.md",
                "design_qa": out_dir / "design-qa.md",
                "pmf": out_dir / "pmf.md",
                "ux": out_dir / "ux.md",
            }

            self._run(
                [
                    "generate-research-brief",
                    "--topic",
                    "CLI Integration",
                    "--audience",
                    "Design teams",
                    "--out",
                    str(outputs["research"]),
                ]
            )
            self._run(
                [
                    "generate-design-qa",
                    "--feature",
                    "Integration Flow",
                    "--target-user",
                    "Design operators",
                    "--out",
                    str(outputs["design_qa"]),
                ]
            )
            self._run(
                [
                    "generate-pmf-review",
                    "--product",
                    "Skill Pack",
                    "--segment",
                    "UX practitioners",
                    "--out",
                    str(outputs["pmf"]),
                ]
            )
            self._run(
                [
                    "generate-ux-review",
                    "--flow",
                    "Onboarding",
                    "--target-user",
                    "Founders",
                    "--out",
                    str(outputs["ux"]),
                ]
            )

            for path in outputs.values():
                self.assertTrue(path.exists())

            self.assertIn("## Needs Your Judgment", outputs["research"].read_text(encoding="utf-8"))
            self.assertIn("## Needs Your Judgment", outputs["design_qa"].read_text(encoding="utf-8"))
            self.assertIn("## Needs Your Judgment", outputs["pmf"].read_text(encoding="utf-8"))
            self.assertIn("## Needs Your Judgment", outputs["ux"].read_text(encoding="utf-8"))


if __name__ == "__main__":
    unittest.main()
