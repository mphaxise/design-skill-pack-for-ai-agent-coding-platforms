# Product Strategy

## Problem statement
AI coding agents can generate code quickly but often miss UX rigor and product signal quality, causing teams to ship features that are technically correct but user-weak.

## Target users
- Primary: UX researchers/designers embedded in agent-assisted product teams
- Secondary: founders and PMs validating PMF/FMF with limited research bandwidth

## Scope (MVP vs later)
### MVP
- Four roles with explicit boundaries: `/design-qa`, `/pmf-review`, `/ux-review`, `/research-brief`
- Opinionated, compact output formats with next actions
- One production-ready flow proving real value
- Personal operator lens so outputs reflect a specific practitioner method, not generic AI style

### Later
- Cross-platform packs for other agent ecosystems
- Domain presets (B2B SaaS, consumer mobile, marketplace)
- Collaboration/export integrations

## Risks and assumptions
- Risk: too much process overhead could reduce adoption
- Risk: unclear role boundaries may duplicate output
- Assumption: users value artifact quality over breadth for v0
- Assumption: narrow v0 increases trust and speed

## Architecture and tech choices
- Product behavior encoded as skill markdown + templates
- Lightweight local CLI for repeatable artifact generation
- Tests focused on structural correctness and policy enforcement

## Role-boundary acceptance criteria (critical gap fix)
- Each skill must declare: primary objective, required output format, and explicit handoff boundary.
- Any PMF/FMF claims must include evidence quality labels (`strong`, `partial`, `assumption`).
- UX and QA outputs must include at least one user-impact rationale per recommendation.
- Research briefs must include decision target, hypotheses, method choice, and open risks.

## 60-90 minute first milestone
Publish strategy docs and planning-gate reviews with role boundaries and explicit acceptance criteria.

## End-of-day outcome
A working Codex-first v0 with one demonstrable workflow, committed and pushed.

## Not in scope
- Full dashboard or hosted service
- Automated data collection from third-party tools
- Complex orchestration across multiple agents

## Next 1-3 concrete actions
1. Finalize planning gates and acceptance criteria.
2. Implement research-brief first slice with policy checks.
3. Validate with tests and document quickstart.
