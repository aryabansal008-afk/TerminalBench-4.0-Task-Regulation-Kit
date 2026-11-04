# Packaging, immutable versions, and checksums

Archive membership is `ARCHIVE-MEMBERSHIP.md`. This file is the upload procedure.

## Before the ZIP exists

**Source.** Self-test first: static checks, rubric review, Oracle pass, NOP fail. `Upload Harbor task ZIP` is inactive until an `ACTIVE` grant exists. Each upload is immutable. Re-uploading the same bytes fails with `File hash already exists`.

**Practice.**

1. Re-run `tools/check_task.py` on the tree you are about to zip. Pass `--canary-policy` with the provisional `C-CANARY` choice. A pass on an older copy does not count.
2. Run `python3 tools/package_task.py tasks/<slug> --out tasks/<slug>.zip --canary-policy <no-canary|required>`. The policy flag is required by `tools/package_task.py`. `required` also needs `--canary-string` from the platform. The script refuses symlinks, writes one top-level slug directory, and prints a SHA-256. The single top-level directory is provisional (`U-ZIP-ROOT`). The end-to-end order is `17-conversation-flow/BUILD-ZIP.md`. The ZIP stays beside the tree, not inside it.
3. Store the digest in `evidence/<slug>/sha256.txt`. Do not add that file to the ZIP and hash again.
4. Confirm the upload button is active. Upload once.

## Version budget

**Source.** Each corrected ZIP is Version N of N. Stage 1 re-runs from the start. Only one version with every gate green reaches Stage 2. Partial credit across versions does not count. Hourly limit: 2 unique versions. Daily limit: 5 unique versions.

`C-REUPLOADS` is unresolved. The limits table says 7 reuploads per task. Prose on pages 16, 19, 20, and 21 says 3. Do not stop at 3 as if the table were void, and do not spend a 4th through 7th version as if the prose were void. Ask before any upload whose number is inside that disputed range, and quote the live counter. The hourly and daily cells are not part of that conflict.

`C-REUPLOAD-FREELY` is superseded: “Re-upload freely” is the old way. Do not expect an in-place replacement.
