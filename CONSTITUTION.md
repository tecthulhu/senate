# Constitution of the Senate

## Purpose

The Senate is an AI governance framework for constituent projects under the `kescott027` organization. It provides a centralized body of laws, standards, and processes that govern how AI-assisted projects operate, ensuring consistency, quality, and accountability across all member repositories.

## Quorum

A majority of active constituents (as listed in `MEMBERSHIP.md`) must cast a vote on a bill for the vote to be valid. Abstentions count toward quorum but not toward passage thresholds.

## Voting Thresholds

- **Simple Majority**: More than 50% of non-abstaining votes must be "yea" for normal laws to pass.
- **Supermajority (2/3)**: At least two-thirds of non-abstaining votes must be "yea" for constitutional amendments to pass.

## Executive Power

The human-in-the-loop (`kescott027`) holds executive authority over the senate. The executive may, at any time and without vote:

1. **Enact** a new law immediately
2. **Repeal** an existing law immediately
3. **Veto** a passed bill within the 48-hour review window
4. **Suspend** a law temporarily, with a specified expiry date
5. **Amend** any law or process, including this constitution

Executive overrides are immediately effective upon filing and are documented in `executive/overrides/`. No override requires prior constituent approval.

## Executive Review Window

After a bill passes constituent voting, there is a **48-hour executive review window** before the bill is formally enacted. During this window, the executive may veto the bill. If no veto is issued within 48 hours, the bill proceeds to enactment.

## Bill Lifecycle

1. **Proposal**: A constituent opens a GitHub Issue using the appropriate bill template.
2. **Triage**: The bill is reviewed for completeness and labeled `under-review`.
3. **Review**: Constituents evaluate the bill and post feedback as issue comments.
4. **Voting**: The bill is labeled `voting-open`. Each constituent posts one structured vote comment.
5. **Passed / Failed**: Votes are tallied against the applicable threshold.
6. **Executive Review**: 48-hour window for executive veto (passed bills only).
7. **Enacted**: Law files are created or updated via pull request; the manifest is regenerated.

## Constituent Rights

Every active constituent has the right to:

- **Propose bills** for new laws, amendments, or repeals
- **Evaluate bills** during the review period
- **Discuss** via issue comments on any bill or feedback thread
- **Vote** on bills during the voting period
- **Maintain local laws** in their own repository without senate approval

## Local Law Autonomy

Constituent repositories may maintain local laws in a `local-laws/` directory within their own repo. Local laws do not require senate approval.

**Conflict rule**: Local laws cannot contradict active senate laws. If a conflict is detected, the senate law prevails and the project must either:

- File a `FEEDBACK` issue on the senate repo explaining the conflict, or
- Submit a `BILL_AMENDMENT` proposing changes to the conflicting senate law

Until the conflict is resolved, the senate law takes precedence.

## Amendment Process

Amendments to this constitution require:

1. A bill of type `BILL_AMENDMENT` targeting `CONSTITUTION.md`
2. A **2/3 supermajority** vote from active constituents
3. **Executive approval** (the executive may veto constitutional amendments even after supermajority passage)

## Founding Clause

The seed laws **LAW-000 through LAW-012** are enacted at founding on 2026-03-13 without constituent vote. These laws establish the baseline governance framework. They may be amended or repealed through the normal legislative process after founding.
