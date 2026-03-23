# /research-brief

## Objective
Generate a structured research brief that aligns product questions with concrete research actions.

## Inputs
- Topic
- Target audience
- Product decision to unblock
- Constraints (time/team/resources)

## Output contract
- Objective and decision target
- Hypotheses
- Method plan
- Open risks and next actions

## Role boundary
- This skill creates the brief only; it does not execute studies or fabricate findings.
- Handoffs can feed `/ux-review` and `/pmf-review`.

## Personal Perspective Checkpoint (Mandatory)
- Ask at strategy gate: "What decision must this brief unblock today?"
- Ask at uncertainty gate: present two options and force a choice:
  - Option A: optimize for confidence and narrower scope
  - Option B: optimize for learning speed and broader exploration
- Ask before irreversible recommendation: "Approve the recommendation path before implementation?"

## Security constraints
- No fabricated citations, participant quotes, or metrics.
- Unknowns must be marked as assumptions.
