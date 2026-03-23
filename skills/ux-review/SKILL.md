# /ux-review

## Objective
Provide concise UX critique tied to user outcomes, clarity, and flow quality.

## Inputs
- UX flow description, mock summary, or interaction narrative
- Product intent and target user
- Known constraints (time, platform, complexity)

## Output contract
- Prioritized UX issues
- Recommended fixes with rationale
- Open risks and questions

## Role boundary
- This skill does not claim PMF/FMF outcomes.
- Hands formal verification and regression-style checks to `/design-qa`.

## Personal Perspective Checkpoint (Mandatory)
- Ask at taste gate: "Which user feeling is non-negotiable in this flow?"
- Ask at tradeoff gate: present two options and force a choice:
  - Option A: speed-first fixes with minimum quality bar
  - Option B: craft-first fixes for stronger UX confidence
- Ask before irreversible recommendation: "Approve this priority order for implementation?"

## Security constraints
- No fabricated usability study outcomes.
- Label uncertain claims as assumptions.
