"""Load and validate skill contract definitions."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Dict, List, Optional

REQUIRED_SKILL_FIELDS = {
    "name",
    "objective",
    "required_output",
    "handoff_to",
    "prohibited",
    "security",
}

REQUIRED_SECURITY_FIELDS = {
    "no_fabrication",
    "external_fetch_allowed",
    "local_write_allowed",
}


def repo_root() -> Path:
    return Path(__file__).resolve().parents[2]


def default_contract_path() -> Path:
    return repo_root() / "skills" / "contracts" / "skill-contracts.json"


def load_contracts(path: Optional[Path] = None) -> Dict:
    contract_path = path or default_contract_path()
    with contract_path.open("r", encoding="utf-8") as handle:
        return json.load(handle)


def validate_contracts(data: Dict) -> List[str]:
    errors: List[str] = []

    if "version" not in data:
        errors.append("missing top-level 'version'")

    skills = data.get("skills")
    if not isinstance(skills, list) or not skills:
        errors.append("'skills' must be a non-empty list")
        return errors

    seen_names = set()
    for idx, skill in enumerate(skills):
        prefix = f"skills[{idx}]"
        if not isinstance(skill, dict):
            errors.append(f"{prefix} must be an object")
            continue

        missing_fields = sorted(REQUIRED_SKILL_FIELDS - set(skill.keys()))
        for field in missing_fields:
            errors.append(f"{prefix} missing '{field}'")

        name = skill.get("name")
        if isinstance(name, str):
            if name in seen_names:
                errors.append(f"duplicate skill name '{name}'")
            seen_names.add(name)

        security = skill.get("security")
        if isinstance(security, dict):
            missing_security = sorted(REQUIRED_SECURITY_FIELDS - set(security.keys()))
            for field in missing_security:
                errors.append(f"{prefix}.security missing '{field}'")
        else:
            errors.append(f"{prefix}.security must be an object")

    return errors


def assert_contracts_valid(data: Dict) -> None:
    errors = validate_contracts(data)
    if errors:
        message = "Contract validation failed:\n- " + "\n- ".join(errors)
        raise ValueError(message)
