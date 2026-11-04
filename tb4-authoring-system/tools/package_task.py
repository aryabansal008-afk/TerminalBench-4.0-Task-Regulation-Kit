#!/usr/bin/env python3
"""Build a single-root Harbor task ZIP and print its SHA-256.

Does not upload. Refuses symlinks, missing files, and a failed local preflight.
The ZIP's only top-level entry is the task slug directory. That shape is provisional (U-ZIP-ROOT).
"""

from __future__ import annotations

import argparse
import hashlib
import subprocess
import sys
import zipfile
from pathlib import Path


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("task", type=Path)
    parser.add_argument("--out", type=Path, required=True)
    parser.add_argument("--canary-policy", choices=("no-canary", "required"), required=True)
    parser.add_argument("--canary-string", default=None)
    parser.add_argument("--skip-check", action="store_true")
    args = parser.parse_args()
    task = args.task.resolve()
    script = Path(__file__).with_name("check_task.py")
    if not args.skip_check:
        command = [
            sys.executable,
            str(script),
            str(task),
            "--canary-policy",
            args.canary_policy,
        ]
        if args.canary_string:
            command.extend(["--canary-string", args.canary_string])
        completed = subprocess.run(command, check=False)
        if completed.returncode != 0:
            print("package refused: local preflight failed")
            return completed.returncode
    files: list[tuple[Path, Path]] = []
    for path in sorted(task.rglob("*")):
        if path.is_symlink():
            print(f"package refused: symlink {path}")
            return 1
        if not path.is_file():
            continue
        relative = path.relative_to(task)
        if any(part.startswith("..") for part in relative.parts):
            print(f"package refused: path escapes the task root: {relative}")
            return 1
        files.append((path, relative))
    args.out.parent.mkdir(parents=True, exist_ok=True)
    with zipfile.ZipFile(args.out, "w", compression=zipfile.ZIP_DEFLATED) as archive:
        for path, relative in files:
            archive.write(path, arcname=str(Path(task.name) / relative))
    digest = hashlib.sha256(args.out.read_bytes()).hexdigest()
    print(f"wrote {args.out}")
    print(f"sha256 {digest}")
    print("single top-level directory:", task.name)
    print("not uploaded")
    return 0


if __name__ == "__main__":
    sys.exit(main())
