"""Design QA report generation for the Codex-first skill pack."""

from __future__ import annotations

from pathlib import Path
from typing import Dict, Optional

from .personalization import lens_tokens, slugify


def repo_root() -> Path:
    return Path(__file__).resolve().parents[2]


def template_path() -> Path:
    return repo_root() / "templates" / "design_qa.md.tmpl"


def default_output_path(feature: str) -> Path:
    return repo_root() / "outputs" / f"design-qa-{slugify(feature)}.md"


def generate_design_qa(
    *,
    feature: str,
    target_user: str,
    qa_scope: Optional[str] = None,
    objective: Optional[str] = None,
    lens: Optional[Dict] = None,
) -> str:
    text = template_path().read_text(encoding="utf-8")
    values = lens_tokens(lens)
    values.update(
        {
            "feature": feature,
            "target_user": target_user,
            "objective": objective
            or f"Identify high-risk UX quality issues in '{feature}' before release.",
            "qa_scope": qa_scope
            or "Core user flow, error states, and trust-sensitive copy paths.",
            "finding_p0": "No confirmed P0 issues at current evidence depth",
            "finding_p1": "Ambiguous error-state messaging can break user confidence",
            "finding_p2": "Action labels could be clearer for first-time users",
            "finding_p3": "Minor visual hierarchy inconsistency in secondary state",
            "repro_1": "Start primary task as a first-time user and trigger a recoverable error",
            "repro_2": "Return to flow after interruption and verify state clarity",
            "repro_3": "Compare primary and secondary action comprehension",
            "impact_1": "Confusing error messaging can cause abandonment in trust-sensitive tasks",
            "impact_2": "Lower clarity increases support burden and slows user onboarding",
            "next_action_1": "Patch error-state copy and rerun focused QA",
            "next_action_2": "Align action labels with user intent language",
            "next_action_3": "Run one validation pass with target users",
            "pov_applied_1": "Severity prioritization is tied to user trust impact first.",
            "pov_applied_2": "Recommendations avoid vanity improvements without user-value effect.",
            "pov_applied_3": "Known residual risk is explicitly surfaced before ship decisions.",
            "assumption_1": "Current findings are based on deterministic heuristic review, not live usability sessions.",
            "assumption_2": "Target user context remains stable for this release cycle.",
            "judgment_1": "Confirm severity threshold for stop-ship in this release.",
            "judgment_2": "Approve or reject shipping with listed residual risk.",
        }
    )
    return text.format(**values)


def write_design_qa(content: str, output_path: Path) -> Path:
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(content, encoding="utf-8")
    return output_path
