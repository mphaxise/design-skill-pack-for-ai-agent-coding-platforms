# /design-qa

## Objective
Identify UX and product quality issues with severity and reproducible evidence.

## Inputs
- Feature flow or screen summary
- Acceptance criteria
- Known user pain points (if available)

## Output contract
- Severity-ranked findings (`P0`-`P3`)
- Reproduction path for each issue
- User impact statement for each finding

## Role boundary
- This skill does not perform PMF/FMF positioning analysis.
- Escalates strategic fit concerns to `/pmf-review`.

## Security constraints
- No fabricated user data, metrics, or citations.
- Explicitly label unknowns as assumptions.
