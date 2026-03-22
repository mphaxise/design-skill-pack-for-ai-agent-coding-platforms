# Idea Strategy

## Problem statement
UX and product practitioners using AI coding agents lack reusable, trusted workflows for design QA, PMF/FMF stress tests, UX reviews, and research-brief generation.

## Source context
- Title: Design Skill Pack for AI Agent Coding Platforms
- Source: Manual backlog (from PraneetIdeas docs/build-ideas.md, captured 2026-03-22)
- Rank/Priority: 9 / 6
- Idea link: https://github.com/mphaxise/design-skill-pack-for-ai-agent-coding-platforms
- Rationale seed: visible gap for UX-practitioner-centered skills across AI coding agent ecosystems.

## Target users
- UX practitioners and researchers collaborating with coding agents
- Product builders needing fast PMF/FMF critique loops
- AI-agent power users who want repeatable design-focused prompts and constraints

## Scope
### MVP
- Codex-first skill pack definitions for `/design-qa`, `/pmf-review`, `/ux-review`, `/research-brief`
- Security + guardrail policy for each role
- One implemented vertical slice with minimal tests

### Later
- Adapters for additional AI coding agent platforms
- Expanded templates and artifact formats (journey maps, heuristic scorecards, interview synthesis)
- Optional analytics and benchmark datasets

## Risks and assumptions
- Risk: skill overlap/confusion between UX review and design QA
- Risk: weak constraints could cause hallucinated or unsafe recommendations
- Assumption: Codex users prefer short, execution-ready outputs over long frameworks
- Assumption: one strong vertical slice is enough to validate utility

## Architecture and tech choices
- Markdown-first skill definitions under `skills/`
- Python 3 stdlib-only helper tooling for portability
- `unittest` for low-friction checks
- File-based templates and generated outputs for transparency

## 60-90 minute first milestone
Define and scope a Codex-first v0 of the design skill pack, including initial SKILL.md structure and role boundaries for `/design-qa`, `/pmf-review`, `/ux-review`, and `/research-brief`.

## End-of-day outcome
Codex-first implementation brief approved, with v0 skill boundaries, security constraints, and next implementation steps documented.

## Not in scope
- Multi-platform runtime integrations in v0
- LLM fine-tuning or custom model hosting
- Full UI product for operating skills

## Next 1-3 concrete actions
1. Run CEO and ENG planning reviews in required modes and record decisions.
2. Convert approved plan into repository scaffolding + first vertical MVP slice.
3. Add minimal tests and publish initial private repo.
