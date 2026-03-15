# Sprint Sync Protocol

## Overview

The sprint-sync protocol ensures constituent projects stay up to date with senate laws and participate in the legislative process. Sync should occur at every sprint start.

## Sync Steps

1. **Fetch manifest**: Agent fetches `sync/manifest.json` from the senate repo (`kescott027/senate`) via the GitHub API.

2. **Compare hashes**: Compare the `sha256` hashes in the manifest against the local `.senate-sync.json` `law_hashes` map in the constituent repo.

3. **Download changed laws**: For any law where the hash differs, download the updated law file from the senate repo.

4. **Check pending bills**: Review the `pending_bills` array in the manifest for any bills that need evaluation or votes from this constituent.

5. **Apply compatible changes**: Update local governance files with laws that do not conflict with local laws.

6. **File FEEDBACK for conflicts**: If a downloaded law conflicts with a local law, file a `FEEDBACK` issue on the senate repo explaining the conflict.

7. **Verify voting readiness**: Use `docs/governance/voting_readiness_checklist.md`. If not ready, remediate before voting.

8. **Vote on open bills**: For any pending bills in the `voting-open` state, evaluate and post a structured vote comment.

9. **Update local sync state**: Update the local `.senate-sync.json` with the new `law_hashes` values and sync timestamp.

## Local .senate-sync.json Format

```json
{
  "last_sync": "2026-03-13T00:00:00Z",
  "senate_repo": "kescott027/senate",
  "law_hashes": {
    "LAW-000": "<hash>",
    "LAW-001": "<hash>"
  },
  "pending_votes": []
}
```

## Conflict Resolution

When a senate law conflicts with a local law:

1. The senate law takes precedence immediately.
2. The constituent must file a `FEEDBACK` issue or a `BILL_AMENDMENT`.
3. The local law must be updated or removed to resolve the conflict.

See `templates/sprint-sync-checklist.md` for a ready-to-use checklist.

## Manifest Update Process (Senate Maintainers)

When a law file changes, update the manifest to keep hashes and versions accurate:

1. Update the law file under `laws/active/` (or move to `repealed/` if applicable).
2. Recompute the law file hash and update the `sha256` field in `sync/manifest.json`.
3. Update `sync/manifest.json` `last_updated` and increment the top-level `version`.
4. Run `python3 scripts/verify_manifest_hashes.py` to confirm all law hashes match.
5. Run `./bootstrap/regenerate-integrity.sh --check-only` and update integrity if required.
