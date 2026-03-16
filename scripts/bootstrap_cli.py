#!/usr/bin/env python3
import argparse
import hashlib
import json
import sys
from pathlib import Path
from urllib.error import URLError, HTTPError
from urllib.request import urlopen


def sha256_normalized(data: bytes) -> str:
    return hashlib.sha256(data.replace(b"\r", b"")).hexdigest()


def fetch(url: str, timeout: int = 20) -> bytes:
    with urlopen(url, timeout=timeout) as resp:
        return resp.read()


def load_integrity(base_url: str) -> tuple[dict, str]:
    integrity_url = f"{base_url}/bootstrap/integrity.json"
    data = fetch(integrity_url)
    integrity = json.loads(data.decode("utf-8"))
    return integrity, sha256_normalized(data)


def verify_gist(integrity: dict, integrity_hash: str, require_gist: bool) -> None:
    gist_url = (
        integrity.get("secondary_verification", {})
        .get("gist_url")
    )
    if not gist_url:
        if require_gist:
            raise RuntimeError("No secondary verification gist URL found")
        print("WARN: No secondary verification gist URL; skipping gist check")
        return

    try:
        gist_data = fetch(gist_url)
        gist = json.loads(gist_data.decode("utf-8"))
    except (URLError, HTTPError, json.JSONDecodeError) as exc:
        if require_gist:
            raise RuntimeError(f"Gist verification failed: {exc}")
        print(f"WARN: Unable to verify gist ({exc}); continuing")
        return

    expected = gist.get("bootstrap/integrity.json")
    if expected != integrity_hash:
        raise RuntimeError(
            "Integrity hash mismatch between gist and integrity.json"
        )


def select_files(integrity: dict) -> list[str]:
    files = integrity.get("files", {})
    selected = []
    for path in files.keys():
        if path.startswith("project_management_skeleton/"):
            selected.append(path)
        elif path.startswith("laws/active/"):
            selected.append(path)
        elif path in {"sync/manifest.json", "BOOTSTRAP.md"}:
            selected.append(path)
    return sorted(selected)


def map_destination(dest_root: Path, path: str) -> Path:
    if path.startswith("project_management_skeleton/"):
        suffix = path.removeprefix("project_management_skeleton/")
        return dest_root / ".project_management" / suffix
    return dest_root / path


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Optional bootstrap helper CLI (downloads skeleton + laws)",
    )
    parser.add_argument("--dest", default=".", help="Destination root directory")
    parser.add_argument("--repo", default="kescott027/senate", help="GitHub repo")
    parser.add_argument("--ref", default="main", help="Git ref (branch or tag)")
    parser.add_argument("--dry-run", action="store_true", help="Print actions only")
    parser.add_argument(
        "--require-gist",
        action="store_true",
        help="Fail if secondary verification gist cannot be checked",
    )
    args = parser.parse_args()

    dest_root = Path(args.dest).resolve()
    base_url = f"https://raw.githubusercontent.com/{args.repo}/{args.ref}"

    try:
        integrity, integrity_hash = load_integrity(base_url)
        verify_gist(integrity, integrity_hash, args.require_gist)
    except Exception as exc:  # noqa: BLE001
        print(f"ERROR: Integrity verification failed: {exc}")
        return 1

    selected = select_files(integrity)
    if not selected:
        print("ERROR: No files selected for download")
        return 1

    errors = []
    for path in selected:
        dest_path = map_destination(dest_root, path)
        if args.dry_run:
            print(f"DRY-RUN: {path} -> {dest_path}")
            continue

        url = f"{base_url}/{path}"
        try:
            data = fetch(url)
        except Exception as exc:  # noqa: BLE001
            errors.append(f"Failed to download {path}: {exc}")
            continue

        expected = integrity.get("files", {}).get(path)
        actual = sha256_normalized(data)
        if expected and actual != expected:
            errors.append(
                f"Hash mismatch for {path}: expected {expected}, got {actual}"
            )
            continue

        dest_path.parent.mkdir(parents=True, exist_ok=True)
        dest_path.write_bytes(data)

    if errors:
        print("BOOTSTRAP CLI FAILED")
        for err in errors:
            print(f"- {err}")
        return 1

    if args.dry_run:
        print("DRY-RUN COMPLETE")
    else:
        print("BOOTSTRAP CLI COMPLETE")
    return 0


if __name__ == "__main__":
    sys.exit(main())
