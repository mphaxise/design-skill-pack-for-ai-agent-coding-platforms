"""Command-line entrypoint for the design skill pack MVP."""

from __future__ import annotations

import argparse
from pathlib import Path

from .contracts import assert_contracts_valid, load_contracts
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

    brief = subparsers.add_parser(
        "generate-research-brief",
        help="Generate a deterministic markdown research brief.",
    )
    brief.add_argument("--topic", required=True)
    brief.add_argument("--audience", required=True)
    brief.add_argument("--objective", default=None)
    brief.add_argument("--problem-statement", default=None)
    brief.add_argument("--decision", default=None)
    brief.add_argument("--out", type=Path, default=None)

    return parser


def _cmd_check_contracts(path: Path | None) -> int:
    data = load_contracts(path)
    assert_contracts_valid(data)
    print("Contracts valid.")
    return 0


def _cmd_generate_research_brief(args: argparse.Namespace) -> int:
    content = generate_research_brief(
        topic=args.topic,
        audience=args.audience,
        objective=args.objective,
        problem_statement=args.problem_statement,
        decision=args.decision,
    )
    output_path = args.out or default_output_path(args.topic)
    write_research_brief(content, output_path)
    print(f"Research brief written to: {output_path}")
    return 0


def main(argv: list[str] | None = None) -> int:
    parser = _build_parser()
    args = parser.parse_args(argv)

    if args.command == "check-contracts":
        return _cmd_check_contracts(args.path)
    if args.command == "generate-research-brief":
        return _cmd_generate_research_brief(args)

    parser.error(f"Unknown command: {args.command}")
    return 2


if __name__ == "__main__":
    raise SystemExit(main())
