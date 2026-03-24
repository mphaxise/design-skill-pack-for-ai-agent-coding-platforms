"""PMF/FMF review generation for the Codex-first skill pack."""

from __future__ import annotations

from pathlib import Path
from typing import Dict, Optional

from .personalization import lens_tokens, slugify


def repo_root() -> Path:
    return Path(__file__).resolve().parents[2]


def template_path() -> Path:
    return repo_root() / "templates" / "pmf_review.md.tmpl"


def default_output_path(product: str) -> Path:
    return repo_root() / "outputs" / f"pmf-review-{slugify(product)}.md"


def generate_pmf_review(
    *,
    product: str,
    segment: str,
    decision: Optional[str] = None,
    lens: Optional[Dict] = None,
) -> str:
    text = template_path().read_text(encoding="utf-8")
    values = lens_tokens(lens)
    values.update(
        {
            "product": product,
            "segment": segment,
            "decision": decision
            or "Decide whether to continue current PMF hypothesis, narrow scope, or reposition.",
            "signal_1": "User interview pain intensity",
            "signal_1_quality": "partial",
            "signal_2": "Activation-to-repeat behavior",
            "signal_2_quality": "assumption",
            "signal_3": "Willingness-to-pay proxy",
            "signal_3_quality": "assumption",
            "risk_1": "Signal quality is too qualitative for shipping-confidence PMF claims",
            "risk_2": "Behavioral evidence is thin across representative users",
            "risk_3": "Positioning may be broad relative to urgent user pain",
            "next_action_1": "Run one fast falsification test on top risk assumption",
            "next_action_2": "Collect one behavioral signal that can change conviction",
            "next_action_3": "Choose continue, narrow, or reposition with explicit rationale",
            "pov_applied_1": "PMF claims are held to a mixed-evidence bar before strong conclusions.",
            "pov_applied_2": "Interview and behavioral evidence are both surfaced when they disagree.",
            "pov_applied_3": "Recommendations prioritize clarity and trust over optimistic fit narratives.",
            "assumption_1": "Current segment framing is directionally correct but not yet behaviorally validated.",
            "assumption_2": "Qualitative pain signals are recent enough to guide exploration decisions.",
            "judgment_1": "Confirm which signal would actually change your PMF conviction now.",
            "judgment_2": "Choose continue, narrow, or reposition before irreversible scope commitments.",
        }
    )
    return text.format(**values)


def write_pmf_review(content: str, output_path: Path) -> Path:
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(content, encoding="utf-8")
    return output_path
