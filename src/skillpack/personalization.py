"""Shared personalization helpers for lens-aware outputs."""

from __future__ import annotations

from typing import Dict, Optional

from .lens import load_lens


def slugify(value: str) -> str:
    slug = "-".join(value.lower().split())
    slug = "".join(ch for ch in slug if ch.isalnum() or ch == "-")
    return slug or "artifact"


def lens_tokens(lens: Optional[Dict] = None) -> Dict[str, str]:
    active_lens = lens or load_lens()
    optimization_priority = active_lens.get("optimization_priority", [])
    ask_policy = active_lens.get("ask_policy", [])
    non_negotiables = active_lens.get("non_negotiables", [])

    return {
        "lens_primary_optimization": optimization_priority[0]
        if optimization_priority
        else "unknown",
        "lens_scope_default": active_lens.get("scope_default_when_uncertain", "unknown"),
        "lens_evidence_bar": active_lens.get("pmf_evidence_policy", {}).get(
            "shipping_claim_phase",
            "unknown",
        ),
        "lens_risk_posture": active_lens.get("risk_posture", "unknown"),
        "lens_non_negotiable_1": non_negotiables[0]
        if len(non_negotiables) > 0
        else "unknown",
        "lens_non_negotiable_2": non_negotiables[1]
        if len(non_negotiables) > 1
        else "unknown",
        "lens_ask_policy_1": ask_policy[0] if len(ask_policy) > 0 else "unknown",
        "lens_ask_policy_2": ask_policy[1] if len(ask_policy) > 1 else "unknown",
    }
