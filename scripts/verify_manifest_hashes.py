#!/usr/bin/env python3
import argparse
import hashlib
import json
import sys
from pathlib import Path

ROOT = Path.cwd()


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(8192), b""):
            digest.update(chunk.replace(b"\r", b""))
    return digest.hexdigest()


def load_manifest(path: Path, errors: list):
    try:
        return json.loads(path.read_text())
    except FileNotFoundError:
        errors.append(f"Missing manifest: {path}")
    except json.JSONDecodeError as exc:
        errors.append(f"Invalid JSON in manifest: {path} ({exc})")
    return None


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Verify sync/manifest.json law file hashes",
    )
    parser.add_argument("--root", default=str(ROOT), help="Repository root to verify")
    parser.add_argument("--verbose", action="store_true", help="Print checks as they run")
    args = parser.parse_args()

    root = Path(args.root).resolve()
    errors = []

    manifest_path = root / "sync/manifest.json"
    manifest = load_manifest(manifest_path, errors)
    if not manifest:
        for err in errors:
            print(err)
        return 1

    laws = manifest.get("laws")
    if not isinstance(laws, dict) or not laws:
        print("Manifest has no laws listed")
        return 1

    for law_id, meta in sorted(laws.items()):
        law_file = meta.get("file")
        expected = meta.get("sha256")
        if not law_file:
            errors.append(f"{law_id} missing file path in manifest")
            continue
        if not expected:
            errors.append(f"{law_id} missing sha256 in manifest")
            continue

        law_path = root / law_file
        if not law_path.exists():
            errors.append(f"{law_id} missing file: {law_file}")
            continue

        actual = sha256_file(law_path)
        if actual != expected:
            errors.append(
                f"{law_id} hash mismatch: expected {expected}, got {actual}"
            )
        elif args.verbose:
            print(f"OK: {law_id} {law_file}")

    if errors:
        print("MANIFEST HASH VERIFICATION FAILED")
        for err in errors:
            print(f"- {err}")
        return 1

    print("MANIFEST HASH VERIFICATION PASSED")
    return 0


if __name__ == "__main__":
    sys.exit(main())
