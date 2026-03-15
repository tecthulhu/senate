# STORY-0118: Constituent identity canonicalization

## Phase
2

## Context
Define the canonical project identifier to use in votes to avoid mismatched naming.

## User value
Constituents and maintainers benefit from constituent identity canonicalization.

## Acceptance criteria
- [x] Canonical format is documented (e.g., `org/repo`).
- [x] `MEMBERSHIP.md` entries align with the canonical format.
- [x] Voting instructions reference the canonical format.

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
- `docs/governance/membership_onboarding.md`
- `votes/README.md`
- `MEMBERSHIP.md`
