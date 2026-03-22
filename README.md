# Design Skill Pack for AI Agent Coding Platforms

A Codex-first, UX-practitioner-centered skill pack that helps AI coding agents perform stronger UX and product review work.

## Why this exists
AI coding agent ecosystems have strong implementation and code-quality skills, but there is still a visible gap in design and product discovery support for:
- UX QA
- PMF/FMF review
- UX review
- Research brief generation

This repository starts with a Codex-first v0 and is designed to be portable to other agent platforms.

## v0 goals
- Define clear role boundaries for `/design-qa`, `/pmf-review`, `/ux-review`, and `/research-brief`.
- Establish security constraints for each skill.
- Implement one vertical MVP slice end-to-end so the pack is usable immediately.

## Planned structure
- `docs/`: strategy, planning, and review artifacts
- `skills/`: skill specs and role boundaries
- `src/`: executable helper code for MVP skill workflows
- `tests/`: minimal automated checks

## Milestones
- First 60-90 minutes: ship Codex-first v0 scope + role boundary docs + planning-gate reviews.
- End of day: approved implementation brief + first working MVP slice committed and pushed.
