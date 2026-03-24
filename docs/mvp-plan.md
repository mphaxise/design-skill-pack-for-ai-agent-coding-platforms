# MVP Plan

## Problem statement
Deliver the smallest useful Codex-first skill pack that proves UX-practitioner value and is safe to extend.

## Target users
- UX/design practitioners running AI coding agents
- PM/founder users needing rapid review artifacts

## Scope
### MVP
- `skills/design-qa/SKILL.md`
- `skills/pmf-review/SKILL.md`
- `skills/ux-review/SKILL.md`
- `skills/research-brief/SKILL.md`
- `src/skillpack` CLI + templates + tests for all four skill output slices
- `skills/contracts/praneet-lens.json` and mandatory personal-perspective checkpoints
- `logs/` decision logging flow with daily + milestone traces

### Later
- PMF and design QA executable workflows
- Benchmark dataset and grading rubrics
- Publishing adapters

## Risks and assumptions
- Risk: first slice does not demonstrate enough practical value
- Risk: policy boundaries are not enforced by checks
- Assumption: clear templates reduce prompt ambiguity

## Architecture and tech choices
- File-based contracts (`skills/contracts/*.json`)
- CLI entrypoint for generation/checks
- Markdown output artifacts with reproducible structure
- Lens-aware output footer contract (`Praneet POV Applied`, `Assumptions`, `Needs Your Judgment`)

## Skill boundary contract (critical gap fix)
| Skill | Primary job | Inputs | Outputs | Out-of-bounds |
| --- | --- | --- | --- | --- |
| `/design-qa` | Validate UX and product quality risks | UX artifact + acceptance criteria | Defect/risk report | Strategy reframing beyond QA scope |
| `/pmf-review` | Evaluate product-market fit signal quality | Product framing + market assumptions | PMF/FMF risk memo | Feature-level UI QA |
| `/ux-review` | Critique user flows and interaction quality | Flow descriptions, screens, or copy | UX review memo with prioritized fixes | PMF claims without evidence |
| `/research-brief` | Produce structured study brief | Problem statement, audience, constraints | Research brief markdown | Running experiments or fabricating data |

## Security guardrails (critical gap fix)
- No fabricated citations, statistics, or participant quotes.
- Unknowns must be explicitly labeled as assumptions.
- v0 implementation uses local deterministic generation only.
- Contracts must fail checks when required guardrail fields are missing.

## 60-90 minute first milestone
Write planning docs, complete CEO/ENG review gates, and scaffold role-boundary files.

## End-of-day outcome
A committed and pushed v0 with one working vertical slice and tests.

## Not in scope
- Browser automation
- Hosted SaaS interface
- Fine-grained permission broker

## Next 1-3 concrete actions
1. Complete planning gates and incorporate critical fixes.
2. Implement research-brief vertical slice.
3. Add tests/checks and push initial branch.
