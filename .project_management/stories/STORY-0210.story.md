# STORY-0210: Define self-audit scope and signals

## Phase
3

## Context
Specify what the system should analyze to detect governance gaps and improvement opportunities.

## User value
Constituents and maintainers benefit from define self-audit scope and signals.

## Acceptance criteria
- [x] A checklist or spec enumerates signals (missing docs, stale laws, conflicts, process gaps).
- [x] Each signal maps to a bill type (new law, amendment, repeal, feedback).
- [x] Safety constraints and HITL gates are explicit.

## Non-functional requirements
- Security: No secret leakage; follow LAW-004 for token handling.
- Reliability: Documentation and scripts must be deterministic and repeatable.
- Performance: N/A (documentation/process).

## Implementation notes
Published a self-audit scope doc with signal catalog, bill mapping rules, and HITL gates.

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
- `docs/governance/self_audit_scope.md`
- `README.md` (Quick Links)
