# Praneet Decision Rules

## Mechanical vs taste decisions
Mechanical decisions can be auto-resolved. Taste/strategy decisions must be asked.

| Skill | Mechanical auto-decisions | Mandatory ask decisions |
| --- | --- | --- |
| `/research-brief` | section ordering, template completion, assumption labeling | decision-to-unblock framing, hypothesis ambition level, irreversible recommendation path |
| `/pmf-review` | evidence labeling format, risk table structure | what signal changes belief, go/no-go framing, escalation of strategic pivot |
| `/ux-review` | issue grouping, severity ordering, readability edits | which user feeling is non-negotiable, tradeoff between craft and speed |
| `/design-qa` | repro formatting, defect taxonomy, policy checks | severity threshold for immediate stop-ship, acceptable known risk before release |

## Ask gates by skill
### `/research-brief`
- Gate 1: "What decision must this brief unblock today?"
- Gate 2: "Should we optimize for confidence now or speed of learning?"

### `/pmf-review`
- Gate 1: "Which signal would actually change your mind?"
- Gate 2: "Do we continue, narrow, or reposition?"

### `/ux-review`
- Gate 1: "Which user feeling is non-negotiable in this flow?"
- Gate 2: "Approve fast fix set or quality-first fix set?"

### `/design-qa`
- Gate 1: "What severity threshold triggers immediate fix-before-ship?"
- Gate 2: "Is current residual risk acceptable for this release?"

## Output footer contract
Every artifact must end with:
1. `Praneet POV Applied`
2. `Assumptions`
3. `Needs Your Judgment`
