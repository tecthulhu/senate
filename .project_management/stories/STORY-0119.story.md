# STORY-0119: Voting notification path

## Phase
2

## Context
Document how constituents learn that a vote is open and when it closes.

## User value
Constituents and maintainers benefit from voting notification path.

## Acceptance criteria
- [x] Notification mechanism documented (labels, GitHub watch settings, mention policy).
- [x] Timeline expectations are explicit.
- [x] Linked from onboarding kit and voting guide.

## Non-functional requirements
- Security: No secret leakage; follow LAW-004 for token handling.
- Reliability: Documentation and scripts must be deterministic and repeatable.
- Performance: N/A (documentation/process).

## Implementation notes
See BOOTSTRAP_SENATE.md for detailed context and acceptance criteria.

## Test plan
- Unit: N/A (docs/process)
- Integration: Manual verification of referenced files/steps
- E2E: If applicable, run end-to-end bootstrap smoke checklist

## Observability
- Logs: N/A (documentation)
- Metrics: N/A
- Traces: N/A

## Rollback plan
Revert the changes to restore prior governance documentation.

## Risks / edge cases
- Low

## Definition of Done checklist
- [x] AC met
- [x] Tests added + passing (N/A — docs)
- [x] Lint/format/type checks pass (N/A — docs)
- [x] Security checks pass (N/A — docs)
- [x] Docs updated

## Evidence
- `docs/governance/voting_lifecycle.md`
- `docs/governance/voting_onboarding_kit.md`
