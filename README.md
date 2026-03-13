# Senate

The Senate is a governance framework for AI-assisted projects under the `kescott027` organization. It provides a centralized body of laws, standards, and processes that ensure consistency, quality, security, and accountability across all constituent repositories.

## How It Works

Laws govern how constituent projects operate. The legislative lifecycle is:

1. A constituent **proposes a bill** via GitHub Issue
2. The bill is **triaged** and enters a **review period**
3. Constituents **vote** on the bill
4. Passed bills enter a **48-hour executive review** window
5. If not vetoed, the law is **enacted** and added to the codebase

The executive (`kescott027`) can also enact, repeal, veto, suspend, or amend any law at any time without vote.

## Quick Links

- [Constitution](CONSTITUTION.md) -- Foundational governance rules, voting thresholds, and executive powers
- [Law Index](laws/README.md) -- All active, amended, and repealed laws
- [Membership](MEMBERSHIP.md) -- Active constituent projects
- [Sync Protocol](sync/README.md) -- How constituent projects stay in sync with senate laws
- [Executive Overrides](executive/README.md) -- How executive override power works

## Proposing a Bill

To propose a new law, amendment, or repeal, open a GitHub Issue using the appropriate template:

- [New Law](../../issues/new?template=BILL_NEW_LAW.yml) -- Propose a new LAW-NNN
- [Amendment](../../issues/new?template=BILL_AMENDMENT.yml) -- Propose changes to an existing law
- [Repeal](../../issues/new?template=BILL_REPEAL.yml) -- Propose removing an existing law
- [Feedback](../../issues/new?template=FEEDBACK.yml) -- Provide feedback on laws or process

## Syncing

Constituent projects sync with the senate at each sprint start. See [sync/README.md](sync/README.md) for the full protocol and [templates/sprint-sync-checklist.md](templates/sprint-sync-checklist.md) for a ready-to-use checklist.

## Seed Laws

The senate was founded with 13 seed laws (LAW-000 through LAW-012) covering:

| Law | Topic |
|-----|-------|
| LAW-000 | Operating Principles |
| LAW-001 | Planning Rules |
| LAW-002 | Backlog Format |
| LAW-003 | Engineering Standards |
| LAW-004 | Security Standards |
| LAW-005 | Testing Standards |
| LAW-006 | Release Standards |
| LAW-007 | Observability Standards |
| LAW-008 | Review Cadence |
| LAW-009 | AI Workflows |
| LAW-010 | Continuous Improvement |
| LAW-011 | Blocker Management |
| LAW-012 | Bill Submission Process |

## Repository Structure

```
senate/
  CONSTITUTION.md          # Foundational governance document
  MEMBERSHIP.md            # Active constituent register
  README.md                # This file
  laws/
    README.md              # Law index
    active/                # Currently enforceable laws
    repealed/              # Repealed laws (historical record)
    amendments/            # Amendment records
  executive/
    README.md              # Executive override documentation
    overrides/             # Executive override records
  votes/
    README.md              # Voting process documentation
  sync/
    README.md              # Sprint sync protocol
    manifest.json          # Current law manifest with hashes
  templates/               # Templates for constituent projects
  .github/
    ISSUE_TEMPLATE/        # Bill, feedback, and override templates
    workflows/             # GitHub Actions (to be added)
```
