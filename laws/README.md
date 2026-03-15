# Law Index

All active, amended, and repealed laws of the senate.

| Law ID   | Title                        | Status | Enacted    |
|----------|------------------------------|--------|------------|
| LAW-000  | Operating Principles         | active | 2026-03-13 |
| LAW-001  | Planning Rules               | active | 2026-03-13 |
| LAW-002  | Backlog Format               | active | 2026-03-13 |
| LAW-003  | Engineering Standards        | active | 2026-03-13 |
| LAW-004  | Security Standards           | active | 2026-03-13 |
| LAW-005  | Testing Standards            | active | 2026-03-13 |
| LAW-006  | Release Standards            | active | 2026-03-13 |
| LAW-007  | Observability Standards      | active | 2026-03-13 |
| LAW-008  | Review Cadence               | active | 2026-03-13 |
| LAW-009  | AI Workflows                 | active | 2026-03-13 |
| LAW-010  | Continuous Improvement       | active | 2026-03-13 |
| LAW-011  | Blocker Management           | active | 2026-03-13 |
| LAW-012  | Bill Submission Process      | active | 2026-03-13 |

## Versioning

Law versions are tracked via the law file content plus the `sha256` values recorded in `sync/manifest.json`. When a law changes, update the law file, refresh the corresponding manifest `sha256`, and bump the manifest `version` and `last_updated` fields. Amendment records in `laws/amendments/` provide the human-readable change history and references to the approving bill or decision.

## Directory Structure

- `active/` — Currently enforceable laws
- `repealed/` — Laws that have been repealed (kept for historical record)
- `amendments/` — Amendment records tracking changes to existing laws
