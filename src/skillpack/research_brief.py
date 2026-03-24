"""Research brief generation for the first MVP slice."""

from __future__ import annotations

from pathlib import Path
from typing import Dict, Optional

from .personalization import lens_tokens, slugify


def repo_root() -> Path:
    return Path(__file__).resolve().parents[2]


def template_path() -> Path:
    return repo_root() / "templates" / "research_brief.md.tmpl"


def default_output_path(topic: str) -> Path:
    return repo_root() / "outputs" / f"research-brief-{slugify(topic)}.md"


def generate_research_brief(
    *,
    topic: str,
    audience: str,
    objective: Optional[str] = None,
    problem_statement: Optional[str] = None,
    decision: Optional[str] = None,
    lens: Optional[Dict] = None,
) -> str:
    text = template_path().read_text(encoding="utf-8")
    values = lens_tokens(lens)
    values.update(
        {
        "topic": topic,
        "objective": objective
        or f"De-risk the key UX and product assumptions around '{topic}'.",
        "audience": audience,
        "problem_statement": problem_statement
        or "The team needs evidence-backed direction before investing in broader implementation.",
        "decision": decision
        or "Decide whether to proceed with MVP scope as-is, narrow scope, or reposition.",
        "hypothesis_1": "Users understand the core value proposition without extra onboarding",
        "hypothesis_2": "The proposed workflow can be completed within one focused session",
        "method_plan": "Run 3-5 structured walkthrough interviews plus one artifact critique session.",
        "risk_1": "Recruiting the right participant profile may take longer than expected",
        "risk_2": "Feedback quality may vary if prompts are too broad",
        "next_action_1": "Confirm participant profile and recruit list",
        "next_action_2": "Draft interview/discussion guide",
        "next_action_3": "Schedule synthesis readout with decision owners",
        "pov_applied_1": "Decision framing prioritizes clarity and user trust before expansion.",
        "pov_applied_2": "Fit claims are explicitly marked as assumptions unless mixed evidence exists.",
        "pov_applied_3": "Options are constrained to a forced two-path decision when scope is uncertain.",
        "assumption_1": "Qualitative signal quality is sufficient for early exploration decisions.",
        "assumption_2": "No irreversible recommendation is finalized without explicit approval.",
        "judgment_1": "Confirm which decision this brief must unblock in this cycle.",
        "judgment_2": "Approve one of the two proposed strategy options before implementation.",
    }
    )
    return text.format(**values)


def write_research_brief(content: str, output_path: Path) -> Path:
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(content, encoding="utf-8")
    return output_path
