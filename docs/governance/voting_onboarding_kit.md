# Voting-Ready Onboarding Kit

This kit provides the fastest path for a new constituent to become voting-ready and submit a valid first vote.

## Prerequisites

- Membership approved and listed in `MEMBERSHIP.md`.
- Laws synced into the constituent repo (`laws/active/` present).
- Local `.senate-sync.json` updated after sync.
- Canonical project identity is known (use `org/repo` as listed in `MEMBERSHIP.md`).

Use the readiness checklist before voting: `docs/governance/voting_readiness_checklist.md`.

## Fast-Path Steps

1. Confirm membership entry exists in `MEMBERSHIP.md` and matches your canonical `org/repo`.
2. Run sprint sync per `sync/README.md` and update `.senate-sync.json`.
3. Complete the voting readiness checklist (must be "Ready").
4. Set up vote notifications (see "Notification Path" below).
5. Review the open bill and submit your vote using the LAW-012 format.

## Vote Format Example (LAW-012)

```
**VOTE**
project: org/repo
vote: yea | nay | abstain
reason: <brief justification>
```

## First Vote Walkthrough

1. Find the bill issue labeled `voting-open` in the senate repo.
2. Read the bill summary and proposed changes.
3. Ensure your project identity matches the entry in `MEMBERSHIP.md` (canonical format: `org/repo`).
4. Post a single vote comment using the required format, for example:

```
**VOTE**
project: kescott027/netdata
vote: yea
reason: Supports the proposed governance improvement.
```

5. Verify your vote is counted:
   - Your comment appears on the issue.
   - The final tally or decision record references your `org/repo` entry.

If you need to change a vote before the window closes, post a new comment with the updated vote.

## Notification Path

- Watch the senate repository for issue activity.
- Filter for issues labeled `voting-open`.
- When voting closes, maintainers remove `voting-open` and post a decision record summary.

## Where to Look Next

- Voting lifecycle details: `docs/governance/voting_lifecycle.md`
- Sprint sync checklist: `templates/sprint-sync-checklist.md`
- Vote records and tallies: `votes/README.md`
