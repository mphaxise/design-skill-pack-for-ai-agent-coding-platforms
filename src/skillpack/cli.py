"""Command-line entrypoint for the design skill pack MVP."""

from __future__ import annotations

import argparse
from pathlib import Path

from .contracts import assert_contracts_valid, load_contracts
from .decision_log import build_playbook, record_decision
from .lens import assert_lens_valid, load_lens
from .research_brief import (
    default_output_path,
    generate_research_brief,
    write_research_brief,
)


def _build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(prog="skillpack")
    subparsers = parser.add_subparsers(dest="command", required=True)

    check = subparsers.add_parser(
        "check-contracts",
        help="Validate skill contract definitions.",
    )
    check.add_argument(
        "--path",
        type=Path,
        default=None,
        help="Optional path to contract JSON.",
    )
    check.add_argument(
        "--lens-path",
        type=Path,
        default=None,
        help="Optional path to Praneet lens JSON.",
    )

    brief = subparsers.add_parser(
        "generate-research-brief",
        help="Generate a deterministic markdown research brief.",
    )
    brief.add_argument("--topic", required=True)
    brief.add_argument("--audience", required=True)
    brief.add_argument("--objective", default=None)
    brief.add_argument("--problem-statement", default=None)
    brief.add_argument("--decision", default=None)
    brief.add_argument("--lens-path", type=Path, default=None)
    brief.add_argument("--out", type=Path, default=None)

    log_decision = subparsers.add_parser(
        "log-decision",
        help="Record a decision in daily and milestone logs.",
    )
    log_decision.add_argument("--skill", required=True)
    log_decision.add_argument("--stage", required=True)
    log_decision.add_argument("--decision", required=True)
    log_decision.add_argument("--rationale", required=True)
    log_decision.add_argument("--confidence", type=float, default=0.7)
    log_decision.add_argument("--irreversible", action="store_true")
    log_decision.add_argument("--needs-user-input", action="store_true")
    log_decision.add_argument(
        "--tags",
        default="",
        help="Comma-separated tags.",
    )
    log_decision.add_argument(
        "--milestone",
        default=None,
        help="Optional milestone name for deep log file.",
    )

    playbook = subparsers.add_parser(
        "build-playbook",
        help="Generate playbook markdown from decision logs.",
    )
    playbook.add_argument("--out", type=Path, default=None)

    return parser


def _cmd_check_contracts(path: Path | None, lens_path: Path | None) -> int:
    data = load_contracts(path)
    assert_contracts_valid(data)
    lens = load_lens(lens_path)
    assert_lens_valid(lens)
    print("Contracts and Praneet lens valid.")
    return 0


def _cmd_generate_research_brief(args: argparse.Namespace) -> int:
    lens = load_lens(args.lens_path)
    content = generate_research_brief(
        topic=args.topic,
        audience=args.audience,
        objective=args.objective,
        problem_statement=args.problem_statement,
        decision=args.decision,
        lens=lens,
    )
    output_path = args.out or default_output_path(args.topic)
    write_research_brief(content, output_path)
    print(f"Research brief written to: {output_path}")
    return 0


def _cmd_log_decision(args: argparse.Namespace) -> int:
    raw_tags = [tag.strip() for tag in args.tags.split(",") if tag.strip()]
    paths = record_decision(
        skill=args.skill,
        stage=args.stage,
        decision=args.decision,
        rationale=args.rationale,
        confidence=args.confidence,
        irreversible=args.irreversible,
        needs_user_input=args.needs_user_input,
        tags=raw_tags,
        milestone=args.milestone,
    )
    print(f"Decision written to: {paths['stream']}")
    print(f"Daily log updated: {paths['daily']}")
    if "milestone" in paths:
        print(f"Milestone log updated: {paths['milestone']}")
    return 0


def _cmd_build_playbook(args: argparse.Namespace) -> int:
    path = build_playbook(output_path=args.out)
    print(f"Playbook written to: {path}")
    return 0


def main(argv: list[str] | None = None) -> int:
    parser = _build_parser()
    args = parser.parse_args(argv)

    if args.command == "check-contracts":
        return _cmd_check_contracts(args.path, args.lens_path)
    if args.command == "generate-research-brief":
        return _cmd_generate_research_brief(args)
    if args.command == "log-decision":
        return _cmd_log_decision(args)
    if args.command == "build-playbook":
        return _cmd_build_playbook(args)

    parser.error(f"Unknown command: {args.command}")
    return 2


if __name__ == "__main__":
    raise SystemExit(main())
