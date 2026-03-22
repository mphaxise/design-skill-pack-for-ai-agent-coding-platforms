# CEO Plan Review

## 1. Mode
Selected mode: `HOLD SCOPE`.

Reason: the product direction is already selected (Codex-first v0 design skill pack), and the highest-value move is to tighten execution quality without expanding surface area.

Assumption: success for this session means a usable v0 that proves one vertical workflow and defines safe role boundaries for the four skills.

## 2. Problem Framing
### Problem statement
AI coding agent workflows are code-strong but UX-practice-weak; teams lack reusable design-oriented skills for QA, PMF/FMF stress tests, UX review, and research-brief generation.

### Target users
- UX practitioners and researchers collaborating with coding agents
- PMs/founders validating product direction under time constraints
- Agent power users needing compact, repeatable review artifacts

### If we do nothing
The workflow remains ad hoc, advice quality varies by prompt author, and design/product decisions keep getting delayed or shipped with weak user evidence.

### Framing check
Current framing is directionally right. The direct path is to prove one vertical slice and lock boundaries, not to broaden platforms yet.

## 3. What Already Exists
- Idea context, rationale, first milestone, and end-of-day target are captured in source backlog artifacts.
- Initial strategy docs are present (`idea-strategy`, `product-strategy`, `implementation-strategy`, `mvp-plan`).
- Clear v0 role list already exists: `/design-qa`, `/pmf-review`, `/ux-review`, `/research-brief`.

Duplication risk: low, but role overlap between `/design-qa` and `/ux-review` can create duplicated outputs without explicit role contracts.

## 4. Recommended Plan
### MVP scope vs later
- MVP: define role contracts + security constraints + implement one runnable research-brief slice with minimal tests.
- Later: platform adapters, richer templates, and expanded evaluators.

### Architecture and tech choices
- Markdown skill specs with explicit boundaries.
- Local Python stdlib CLI for deterministic generation and checks.
- Contract file (JSON) to enforce role boundaries and guardrails.

### 60-90 minute first milestone
Finalize planning docs plus review gates, then scaffold role contracts and a working research-brief command.

### End-of-day outcome
Codex-first implementation brief approved and executed with one committed vertical slice and documented constraints.

### Critical gaps to close before coding
1. No explicit acceptance criteria table mapping each skill to required outputs, prohibited actions, and handoff boundary.
2. Security constraints are mentioned but not yet concretely tied to data handling and allowed local operations.

### Proposed flow
```text
strategy docs -> role/security contracts -> research-brief MVP command -> tests -> push
```

## 5. Risks And Failure Modes
RISK | WHY IT MATTERS | MITIGATION
-----|----------------|-----------
Role ambiguity (`design-qa` vs `ux-review`) | Users get duplicate or contradictory outputs | Add role-contract table with strict inputs/outputs
Over-scoping v0 | Delays proof of value | Keep one vertical slice only
Weak guardrails | Unsafe recommendations or fake evidence | Enforce explicit no-fabrication and source-marking constraints

## 6. Not In Scope
- Multi-platform runtime adapters: defer until Codex-first value is proven.
- Hosted service/UI: defer to post-v0 validation.
- Automated external data ingestion: defer to avoid security and reliability scope creep.

## 7. Next Actions
1. Patch planning docs with skill-level acceptance criteria and security constraints matrix.
2. Scaffold the four skills and shared contract manifest.
3. Implement and test the research-brief vertical slice.
