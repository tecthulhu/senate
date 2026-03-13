# Local Laws - Template

Use this template to set up a `local-laws/` directory in your member repository.

## Setup

Create a `local-laws/` directory in the root of your repository and add a `README.md` file (you can copy this template).

## What Are Local Laws?

Local laws are governance rules specific to your project. They live in your member repository and do not require senate approval. Examples include:

- Project-specific coding conventions beyond LAW-003
- Custom review processes for your domain
- Team-specific sprint cadence adjustments
- Technology-specific security requirements beyond LAW-004

## Format

Local laws should follow a consistent format:

```markdown
---
local_law_id: LOCAL-NNN
title: <title>
status: active | suspended | repealed
created: YYYY-MM-DD
last_amended: YYYY-MM-DD | null
---

# LOCAL-NNN: <title>

<law body>
```

## Conflict Rules

Local laws **cannot contradict active senate laws**. If a conflict is detected:

1. The senate law prevails immediately.
2. You must either:
   - File a `FEEDBACK` issue on `kescott027/senate` explaining the conflict, or
   - Submit a `BILL_AMENDMENT` proposing changes to the conflicting senate law.
3. Update or remove the conflicting local law.

## Sync Verification

During each sprint sync (see `sync/README.md` in the senate repo), your agent should verify that local laws do not conflict with any updated senate laws.
