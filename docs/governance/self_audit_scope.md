# Self-Audit Scope and Signals

## Purpose

Define what the system should analyze to detect governance gaps and improvement opportunities, and how those findings map to bill types with explicit safety gates.

## Scope Boundaries

### In Scope

- Governance documentation completeness and consistency.
- Law index, manifest, and template alignment.
- Workflow compliance with existing laws (planning, testing, security, review cadence).
- Backlog hygiene and sprint governance artifacts.
- Voting and proposal workflow completeness.

### Out of Scope

- Direct code changes in constituent repositories.
- Legal or policy interpretation beyond documented laws.
- Automated submission of bills without human approval.
- External data sources not stored in this repository.

## Sources of Truth

- `laws/` (active, amendments, repealed).
- `docs/governance/` (process documentation).
- `project_management_skeleton/` and `.project_management/` (planning and audit trails).
- `sync/manifest.json` and `bootstrap/integrity.json` (hash integrity).
- GitHub issues and pull requests for bills and evidence.

## Signal Catalog

| Signal ID | Signal | Detection method | Default bill type | HITL gate |
| --- | --- | --- | --- | --- |
| SA-001 | Missing governance document required by a law | Law references doc path that does not exist | Amendment | Required |
| SA-002 | Stale law index or manifest mismatch | `laws/README.md` or `sync/manifest.json` out of sync with `laws/active/` | Amendment | Required |
| SA-003 | Conflicting or duplicated law requirements | Two laws prescribe incompatible steps or thresholds | Amendment | Required |
| SA-004 | Missing workflow step mandated by law | Workflow doc lacks required step (e.g., review cadence, veto window) | Amendment | Required |
| SA-005 | Overdue governance artifacts | Sprint logs, phase reports, or audits missing beyond required cadence | Feedback | Required |
| SA-006 | Repeated executive overrides in short window | Overrides exceed defined threshold in `executive/` | Feedback | Required |
| SA-007 | Security or quality gate absent | Required check is missing from CI or policy docs | Amendment | Required |
| SA-008 | Template drift | `project_management_skeleton/` differs from live rules with no explanation | Amendment | Required |
| SA-009 | Broken references | README or governance docs contain dead links or missing anchors | Feedback | Required |
| SA-010 | Unresolved blockers beyond SLA | Blockers remain open past allowed window | Feedback | Required |
| SA-011 | Missing proposal/voting artifacts | `templates/` or `votes/` missing required files | Amendment | Required |
| SA-012 | Evidence gaps for completed stories | Done stories lack PR, test, or doc references | Feedback | Required |

## Bill Mapping Rules

- Amendment: Default for most governance gaps where an existing law or process needs clarification.
- New Law: Use only when no current law covers the gap and the change introduces a new requirement.
- Repeal: Use only when a law is obsolete or conflicts with higher-order governance.
- Feedback: Use for non-binding process improvements or reminders.

## Safety Constraints and HITL Gates

- Human approval is mandatory before creating any bill or issue.
- Any proposal that changes law requirements, security posture, or review cadence must be confirmed by HITL.
- Do not include secrets, tokens, or private repository data in audit output.
- Do not infer or speculate beyond the evidence in the repository.
- When evidence is ambiguous, stop and request clarification rather than proposing a bill.

## Audit Checklist

- [ ] Scan governance docs for missing or inconsistent references.
- [ ] Verify law index and manifest alignment with active law files.
- [ ] Confirm workflows include mandated steps and gates.
- [ ] Check sprint artifacts for completeness (logs, ratings, closeouts).
- [ ] Review executive overrides for unusual frequency.
- [ ] Verify templates match documented processes.
- [ ] Validate links and references in README and governance docs.
