"""Load and validate Praneet Lens configuration."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Dict, List, Optional

REQUIRED_LENS_FIELDS = {
    "version",
    "owner",
    "captured_on",
    "optimization_priority",
    "scope_default_when_uncertain",
    "pmf_evidence_policy",
    "conflict_resolution_policy",
    "ux_quality_bar",
    "risk_posture",
    "communication_style",
    "design_expression",
    "ask_policy",
    "non_negotiables",
    "artifact_style",
    "decision_logging_cadence",
}


def repo_root() -> Path:
    return Path(__file__).resolve().parents[2]


def default_lens_path() -> Path:
    return repo_root() / "skills" / "contracts" / "praneet-lens.json"


def load_lens(path: Optional[Path] = None) -> Dict:
    lens_path = path or default_lens_path()
    with lens_path.open("r", encoding="utf-8") as handle:
        return json.load(handle)


def validate_lens(data: Dict) -> List[str]:
    errors: List[str] = []
    missing = sorted(REQUIRED_LENS_FIELDS - set(data.keys()))
    for field in missing:
        errors.append(f"missing '{field}'")

    opt = data.get("optimization_priority")
    if opt is not None and (not isinstance(opt, list) or len(opt) < 1):
        errors.append("'optimization_priority' must be a non-empty list")

    ask = data.get("ask_policy")
    if ask is not None and (not isinstance(ask, list) or len(ask) < 1):
        errors.append("'ask_policy' must be a non-empty list")

    non_negotiables = data.get("non_negotiables")
    if non_negotiables is not None:
        if not isinstance(non_negotiables, list) or len(non_negotiables) < 2:
            errors.append("'non_negotiables' must include at least two items")

    cadence = data.get("decision_logging_cadence")
    allowed_cadence = {
        "daily",
        "milestone",
        "both_daily_and_milestone",
    }
    if cadence is not None and cadence not in allowed_cadence:
        errors.append(
            "'decision_logging_cadence' must be one of: daily, milestone, both_daily_and_milestone"
        )

    return errors


def assert_lens_valid(data: Dict) -> None:
    errors = validate_lens(data)
    if errors:
        message = "Praneet lens validation failed:\n- " + "\n- ".join(errors)
        raise ValueError(message)
