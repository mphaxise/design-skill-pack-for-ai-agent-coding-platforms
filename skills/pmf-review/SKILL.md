# /pmf-review

## Objective
Evaluate PMF/FMF signal quality and identify the highest-risk product assumptions.

## Inputs
- Product concept and target segment
- Existing evidence and confidence level
- Key distribution/retention assumptions

## Output contract
- PMF/FMF risk summary
- Evidence quality labels (`strong`, `partial`, `assumption`)
- Next 1-3 validation actions

## Role boundary
- This skill does not perform detailed UX heuristic audits.
- Hands interaction-level critique to `/ux-review`.

## Personal Perspective Checkpoint (Mandatory)
- Ask at strategy gate: "Which signal would actually change your mind?"
- Ask at conflict gate: if interview pain conflicts with behavioral data, present both views and propose one falsification test.
- Ask before irreversible recommendation: "Continue, narrow, or reposition?"

## Security constraints
- No fabricated market stats, competitive intel, or user interview quotes.
- Separate observed evidence from assumptions.
