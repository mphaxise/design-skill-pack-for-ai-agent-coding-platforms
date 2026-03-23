# Implementation Strategy

## Problem statement
The project needs an executable v0 that converts strategy into usable skill artifacts while keeping security and scope tight.

## Target users
- Internal builder (Codex-first workflow owner)
- Early collaborators evaluating the skill pack quality

## Scope (MVP vs later)
### MVP
- Repository skeleton for docs, skills, templates, source, tests
- Role-boundary specs for 4 skills
- First vertical slice: research-brief artifact generation + policy validation
- Personalization layer: machine-readable Praneet Lens + checkpoint asks + decision logs

### Later
- Additional generators/checkers for PMF and UX QA outputs
- Platform adapters
- Richer test suites and golden files

## Risks and assumptions
- Risk: unclear acceptance tests create rework
- Risk: output formats may drift without contract tests
- Assumption: Python stdlib is available in local environments
- Assumption: markdown artifacts are enough for early validation

## Architecture and tech choices
- Python module under `src/skillpack/`
- JSON manifest for skill contracts and boundaries
- Markdown templates and deterministic output writer
- `unittest` + shell checks for CI-friendly validation
- Lens loader + validator + decision-log/playbook generator

## Skill acceptance criteria (critical gap fix)
| Skill | Required output | Handoff boundary | Prohibited behavior |
| --- | --- | --- | --- |
| `/design-qa` | QA findings grouped by severity + concrete repro path | Escalates product-level framing questions to `/pmf-review` | No implementation architecture advice beyond QA impact notes |
| `/pmf-review` | PMF/FMF critique with confidence + evidence gaps | Hands UX interaction-level critique to `/ux-review` | No fabricated market evidence or competitor claims |
| `/ux-review` | UX critique with prioritized fixes and rationale | Hands test/quality validation to `/design-qa` when verification is needed | No code-style-only review without user-impact framing |
| `/research-brief` | Structured brief with objective, hypotheses, methods, and next decisions | Produces inputs for other skills; does not run QA itself | No fake citations, no invented participant insights |

## Security constraints matrix (critical gap fix)
| Constraint | v0 policy |
| --- | --- |
| Data handling | Local files only; no automatic external fetches in v0 |
| Evidence integrity | All uncertain claims must be labeled as assumptions |
| Tooling boundary | Stdlib-only execution path for first slice |
| Output safety | Explicitly block fabricated metrics, citations, and interviews |

## 60-90 minute first milestone
Create repo structure, contract files, and CLI command to generate one research brief from topic + audience inputs.

## End-of-day outcome
MVP vertical slice runs locally with passing tests and documented commands.

## Not in scope
- External API calls
- Multi-tenant auth
- Non-deterministic generation pipelines

## Next 1-3 concrete actions
1. Add skill contract manifest and initial SKILL.md files.
2. Implement CLI generation flow for research briefs.
3. Add tests for manifest loading and output contract.
