"""Decision logging utilities for Praneet-style workflow tracing."""

from __future__ import annotations

import json
from datetime import datetime, timezone
from pathlib import Path
from typing import Dict, List, Optional


def repo_root() -> Path:
    return Path(__file__).resolve().parents[2]


def default_logs_dir() -> Path:
    return repo_root() / "logs"


def _iso_now() -> str:
    return datetime.now(timezone.utc).replace(microsecond=0).isoformat()


def _append_daily_log(logs_dir: Path, record: Dict) -> Path:
    date_part = record["timestamp"][:10]
    time_part = record["timestamp"][11:16]
    daily_path = logs_dir / "daily" / f"{date_part}.md"
    daily_path.parent.mkdir(parents=True, exist_ok=True)

    if not daily_path.exists():
        daily_path.write_text(f"# Daily Decisions: {date_part}\n\n", encoding="utf-8")

    with daily_path.open("a", encoding="utf-8") as handle:
        handle.write(
            f"- {time_part} `{record['skill']}/{record['stage']}`: {record['decision']} "
            f"(confidence {record['confidence']:.2f})\n"
        )
        handle.write(f"  Rationale: {record['rationale']}\n")
        handle.write(
            f"  Flags: irreversible={str(record['irreversible']).lower()}, "
            f"needs_user_input={str(record['needs_user_input']).lower()}\n"
        )
    return daily_path


def _append_milestone_log(logs_dir: Path, record: Dict, milestone: str) -> Path:
    slug = "-".join(milestone.lower().split())
    slug = "".join(ch for ch in slug if ch.isalnum() or ch == "-") or "milestone"
    milestone_path = logs_dir / "milestones" / f"{slug}.md"
    milestone_path.parent.mkdir(parents=True, exist_ok=True)

    if not milestone_path.exists():
        milestone_path.write_text(
            f"# Milestone Decisions: {milestone}\n\n",
            encoding="utf-8",
        )

    with milestone_path.open("a", encoding="utf-8") as handle:
        handle.write(
            f"- {record['timestamp']} `{record['skill']}/{record['stage']}`: "
            f"{record['decision']} (confidence {record['confidence']:.2f})\n"
        )
        handle.write(f"  Rationale: {record['rationale']}\n")
    return milestone_path


def record_decision(
    *,
    skill: str,
    stage: str,
    decision: str,
    rationale: str,
    confidence: float,
    irreversible: bool,
    needs_user_input: bool,
    tags: Optional[List[str]] = None,
    milestone: Optional[str] = None,
    logs_dir: Optional[Path] = None,
) -> Dict[str, Path]:
    root = logs_dir or default_logs_dir()
    root.mkdir(parents=True, exist_ok=True)

    record = {
        "timestamp": _iso_now(),
        "skill": skill,
        "stage": stage,
        "decision": decision,
        "rationale": rationale,
        "confidence": confidence,
        "irreversible": irreversible,
        "needs_user_input": needs_user_input,
        "tags": tags or [],
    }

    stream_path = root / "decision-log.jsonl"
    with stream_path.open("a", encoding="utf-8") as handle:
        handle.write(json.dumps(record, sort_keys=True) + "\n")

    outputs = {
        "stream": stream_path,
        "daily": _append_daily_log(root, record),
    }
    if milestone:
        outputs["milestone"] = _append_milestone_log(root, record, milestone)
    return outputs


def build_playbook(
    *,
    logs_dir: Optional[Path] = None,
    output_path: Optional[Path] = None,
) -> Path:
    root = logs_dir or default_logs_dir()
    stream_path = root / "decision-log.jsonl"
    out = output_path or (repo_root() / "docs" / "praneet-playbook.md")
    out.parent.mkdir(parents=True, exist_ok=True)

    records: List[Dict] = []
    if stream_path.exists():
        with stream_path.open("r", encoding="utf-8") as handle:
            for line in handle:
                line = line.strip()
                if not line:
                    continue
                records.append(json.loads(line))

    by_skill: Dict[str, int] = {}
    by_tag: Dict[str, int] = {}
    for record in records:
        by_skill[record["skill"]] = by_skill.get(record["skill"], 0) + 1
        for tag in record.get("tags", []):
            by_tag[tag] = by_tag.get(tag, 0) + 1

    recent = list(reversed(records[-8:]))
    lines = [
        "# Praneet Playbook",
        "",
        "## Why this exists",
        "This playbook is generated from decision logs and captures how Praneet works with Codex.",
        "",
        "## Decision volume by skill",
    ]
    if by_skill:
        for skill, count in sorted(by_skill.items(), key=lambda item: (-item[1], item[0])):
            lines.append(f"- `{skill}`: {count}")
    else:
        lines.append("- No decisions logged yet.")

    lines.append("")
    lines.append("## Frequent tags")
    if by_tag:
        for tag, count in sorted(by_tag.items(), key=lambda item: (-item[1], item[0]))[:10]:
            lines.append(f"- `{tag}`: {count}")
    else:
        lines.append("- No tags logged yet.")

    lines.append("")
    lines.append("## Recent decisions")
    if recent:
        for record in recent:
            lines.append(
                f"- {record['timestamp']} `{record['skill']}/{record['stage']}`: "
                f"{record['decision']} (confidence {record['confidence']:.2f})"
            )
            lines.append(f"  Rationale: {record['rationale']}")
    else:
        lines.append("- No decisions logged yet.")

    lines.append("")
    lines.append("## Logging locations")
    lines.append("- Daily logs: `logs/daily/`")
    lines.append("- Milestone logs: `logs/milestones/`")
    lines.append("- Structured stream: `logs/decision-log.jsonl`")
    lines.append("")
    lines.append("Generated by `skillpack build-playbook`.")
    out.write_text("\n".join(lines) + "\n", encoding="utf-8")
    return out
