#!/usr/bin/env python3
"""Build a Harbor task ZIP and print its SHA-256.

Does not upload. Refuses symlinks, missing files, and a failed local preflight.
Default layout is one top-level slug directory. SOP v3.0 also allows a flat ZIP
when every member sits at the archive root with no wrapping directory.
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
    parser.add_argument(
        "--canary-policy",
        choices=("no-canary", "required"),
        default=None,
        help="Obsolete; accepted for CLI compatibility and forwarded to check_task.py",
    )
    parser.add_argument("--canary-string", default=None)
    parser.add_argument(
        "--layout",
        choices=("wrapped", "flat"),
        default="wrapped",
        help="wrapped: one top-level directory named the slug. flat: members at ZIP root.",
    )
    parser.add_argument("--skip-check", action="store_true")
    args = parser.parse_args()
    task = args.task.resolve()
    script = Path(__file__).with_name("check_task.py")
    if not args.skip_check:
        command = [sys.executable, str(script), str(task)]
        if args.canary_policy:
            command.extend(["--canary-policy", args.canary_policy])
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
            if args.layout == "flat":
                arcname = str(relative)
            else:
                arcname = str(Path(task.name) / relative)
            info = zipfile.ZipInfo(arcname)
            info.date_time = (1980, 1, 1, 0, 0, 0)
            info.compress_type = zipfile.ZIP_DEFLATED
            info.external_attr = 0o644 << 16
            archive.writestr(info, path.read_bytes())
    digest = hashlib.sha256(args.out.read_bytes()).hexdigest()
    print(f"wrote {args.out}")
    print(f"sha256 {digest}")
    if args.layout == "flat":
        print("layout flat (no wrapping directory)")
    else:
        print("single top-level directory:", task.name)
    print("not uploaded")
    return 0


if __name__ == "__main__":
    sys.exit(main())
