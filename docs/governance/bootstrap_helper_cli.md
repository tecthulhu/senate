# Bootstrap Helper CLI (Optional)

This helper is an optional convenience for downloading the senate bootstrap artifacts. It does **not** replace the single-line AI bootstrap instruction.

## What It Does

- Verifies `bootstrap/integrity.json` (and optionally the secondary gist).
- Downloads the `.project_management` skeleton and active laws.
- Copies `sync/manifest.json` and `BOOTSTRAP.md` into your destination.

## Usage

```bash
python3 scripts/bootstrap_cli.py --dest /path/to/project
```

### Dry Run

```bash
python3 scripts/bootstrap_cli.py --dest /path/to/project --dry-run
```

### Require Secondary Gist Check

```bash
python3 scripts/bootstrap_cli.py --dest /path/to/project --require-gist
```

## Notes

- The default source is `kescott027/senate` at `main`.
- Use this only as a helper; the AI bootstrap flow remains the authoritative path.
