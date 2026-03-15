# STORY-0115: Constituent onboarding kit (voting-ready)

## Phase
2

## Context
Provide a minimal, fast-path onboarding kit so a new constituent can vote quickly.

## User value
Constituents and maintainers benefit from constituent onboarding kit (voting-ready).

## Acceptance criteria
- [x] Kit includes: onboarding steps, sync checklist, vote format example, and “first vote” walkthrough.
- [x] Kit is linked from README and/or `MEMBERSHIP.md`.
- [x] Kit explicitly states prerequisites for voting.

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
- Medium

## Definition of Done checklist
- [x] AC met
- [x] Tests added + passing (N/A — docs)
- [x] Lint/format/type checks pass (N/A — docs)
- [x] Security checks pass (N/A — docs)
- [x] Docs updated

## Evidence
- `docs/governance/voting_onboarding_kit.md`
- `README.md`
- `MEMBERSHIP.md`
