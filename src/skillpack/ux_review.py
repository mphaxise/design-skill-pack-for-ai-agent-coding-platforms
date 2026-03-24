"""UX review generation for the Codex-first skill pack."""

from __future__ import annotations

from pathlib import Path
from typing import Dict, Optional

from .personalization import lens_tokens, slugify


def repo_root() -> Path:
    return Path(__file__).resolve().parents[2]


def template_path() -> Path:
    return repo_root() / "templates" / "ux_review.md.tmpl"


def default_output_path(flow: str) -> Path:
    return repo_root() / "outputs" / f"ux-review-{slugify(flow)}.md"


def generate_ux_review(
    *,
    flow: str,
    target_user: str,
    context: Optional[str] = None,
    lens: Optional[Dict] = None,
) -> str:
    text = template_path().read_text(encoding="utf-8")
    values = lens_tokens(lens)
    values.update(
        {
            "flow": flow,
            "target_user": target_user,
            "context": context or "Primary core flow under current MVP constraints.",
            "issue_1": "Key intention is not explicit enough at first decision point",
            "issue_2": "Recovery path after minor errors is unclear",
            "issue_3": "Secondary actions distract from primary task completion",
            "fix_1": "Make primary task intent explicit in first screen/copy block",
            "fix_2": "Add lightweight guided recovery state after common user error",
            "fix_3": "Demote secondary actions until primary goal is complete",
            "impact_1": "Improves first-time comprehension and reduces hesitation",
            "impact_2": "Reduces abandonment after recoverable mistakes",
            "impact_3": "Increases completion likelihood on core task",
            "next_action_1": "Select speed-first or craft-first fix path",
            "next_action_2": "Implement top 2 UX fixes and re-evaluate",
            "next_action_3": "Validate with one focused walkthrough session",
            "pov_applied_1": "Critique prioritizes user trust and clarity over visual novelty.",
            "pov_applied_2": "Tradeoffs are framed as forced options when uncertainty is high.",
            "pov_applied_3": "Recommendations avoid manipulative UX and vanity outcomes.",
            "assumption_1": "User context and task urgency remain consistent with current segment.",
            "assumption_2": "Current flow constraints allow copy/layout-level changes in this cycle.",
            "judgment_1": "Confirm the non-negotiable user feeling for this flow.",
            "judgment_2": "Approve speed-first vs craft-first recommendation path.",
        }
    )
    return text.format(**values)


def write_ux_review(content: str, output_path: Path) -> Path:
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(content, encoding="utf-8")
    return output_path
