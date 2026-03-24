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
- Encode a personalized operator lens so outputs reflect a real practitioner method.

## Planned structure
- `docs/`: strategy, planning, and review artifacts
- `skills/`: skill specs and role boundaries
- `src/`: executable helper code for MVP skill workflows
- `tests/`: minimal automated checks
- `logs/`: daily and milestone decision trails

## Quickstart
Validate role contracts:

```bash
make check-contracts
```

Run tests:

```bash
make test
```

Generate a v0 research brief artifact:

```bash
PYTHONPATH=src python3 -m skillpack.cli generate-research-brief \
  --topic "Codex-first Design Skill Pack" \
  --audience "UX practitioners and PMs"
```

The generated file is written under `outputs/`.

Generate the other three skill artifacts:

```bash
PYTHONPATH=src python3 -m skillpack.cli generate-design-qa \
  --feature "Onboarding Flow" \
  --target-user "New users"

PYTHONPATH=src python3 -m skillpack.cli generate-pmf-review \
  --product "Design Skill Pack" \
  --segment "UX practitioners"

PYTHONPATH=src python3 -m skillpack.cli generate-ux-review \
  --flow "Activation Flow" \
  --target-user "Product builders"
```

Log a design/product decision:

```bash
PYTHONPATH=src python3 -m skillpack.cli log-decision \
  --skill /research-brief \
  --stage strategy-gate \
  --decision "Choose confidence-first brief scope" \
  --rationale "Current cycle prioritizes trust and clarity" \
  --confidence 0.82 \
  --needs-user-input \
  --tags lens,strategy \
  --milestone v0-personalization
```

Build the playbook from decision logs:

```bash
PYTHONPATH=src python3 -m skillpack.cli build-playbook
```

## Milestones
- First 60-90 minutes: ship Codex-first v0 scope + role boundary docs + planning-gate reviews.
- End of day: approved implementation brief + first working MVP slice committed and pushed.
