"""Command-line entrypoint for the design skill pack MVP."""

from __future__ import annotations

import argparse
from pathlib import Path

from .contracts import assert_contracts_valid, load_contracts
from .design_qa import (
    default_output_path as default_design_qa_output_path,
    generate_design_qa,
    write_design_qa,
)
from .decision_log import build_playbook, record_decision
from .lens import assert_lens_valid, load_lens
from .pmf_review import (
    default_output_path as default_pmf_review_output_path,
    generate_pmf_review,
    write_pmf_review,
)
from .research_brief import (
    default_output_path as default_research_brief_output_path,
    generate_research_brief,
    write_research_brief,
)
from .ux_review import (
    default_output_path as default_ux_review_output_path,
    generate_ux_review,
    write_ux_review,
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

    design_qa = subparsers.add_parser(
        "generate-design-qa",
        help="Generate a deterministic markdown design QA report.",
    )
    design_qa.add_argument("--feature", required=True)
    design_qa.add_argument("--target-user", required=True)
    design_qa.add_argument("--qa-scope", default=None)
    design_qa.add_argument("--objective", default=None)
    design_qa.add_argument("--lens-path", type=Path, default=None)
    design_qa.add_argument("--out", type=Path, default=None)

    pmf_review = subparsers.add_parser(
        "generate-pmf-review",
        help="Generate a deterministic markdown PMF/FMF review artifact.",
    )
    pmf_review.add_argument("--product", required=True)
    pmf_review.add_argument("--segment", required=True)
    pmf_review.add_argument("--decision", default=None)
    pmf_review.add_argument("--lens-path", type=Path, default=None)
    pmf_review.add_argument("--out", type=Path, default=None)

    ux_review = subparsers.add_parser(
        "generate-ux-review",
        help="Generate a deterministic markdown UX review artifact.",
    )
    ux_review.add_argument("--flow", required=True)
    ux_review.add_argument("--target-user", required=True)
    ux_review.add_argument("--context", default=None)
    ux_review.add_argument("--lens-path", type=Path, default=None)
    ux_review.add_argument("--out", type=Path, default=None)

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
    output_path = args.out or default_research_brief_output_path(args.topic)
    write_research_brief(content, output_path)
    print(f"Research brief written to: {output_path}")
    return 0


def _cmd_generate_design_qa(args: argparse.Namespace) -> int:
    lens = load_lens(args.lens_path)
    content = generate_design_qa(
        feature=args.feature,
        target_user=args.target_user,
        qa_scope=args.qa_scope,
        objective=args.objective,
        lens=lens,
    )
    output_path = args.out or default_design_qa_output_path(args.feature)
    write_design_qa(content, output_path)
    print(f"Design QA report written to: {output_path}")
    return 0


def _cmd_generate_pmf_review(args: argparse.Namespace) -> int:
    lens = load_lens(args.lens_path)
    content = generate_pmf_review(
        product=args.product,
        segment=args.segment,
        decision=args.decision,
        lens=lens,
    )
    output_path = args.out or default_pmf_review_output_path(args.product)
    write_pmf_review(content, output_path)
    print(f"PMF review written to: {output_path}")
    return 0


def _cmd_generate_ux_review(args: argparse.Namespace) -> int:
    lens = load_lens(args.lens_path)
    content = generate_ux_review(
        flow=args.flow,
        target_user=args.target_user,
        context=args.context,
        lens=lens,
    )
    output_path = args.out or default_ux_review_output_path(args.flow)
    write_ux_review(content, output_path)
    print(f"UX review written to: {output_path}")
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
    if args.command == "generate-design-qa":
        return _cmd_generate_design_qa(args)
    if args.command == "generate-pmf-review":
        return _cmd_generate_pmf_review(args)
    if args.command == "generate-ux-review":
        return _cmd_generate_ux_review(args)
    if args.command == "log-decision":
        return _cmd_log_decision(args)
    if args.command == "build-playbook":
        return _cmd_build_playbook(args)

    parser.error(f"Unknown command: {args.command}")
    return 2


if __name__ == "__main__":
    raise SystemExit(main())
