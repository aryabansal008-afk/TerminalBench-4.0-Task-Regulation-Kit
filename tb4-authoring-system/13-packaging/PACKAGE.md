# Packaging, immutable versions, and checksums

Archive membership is `ARCHIVE-MEMBERSHIP.md`. This file is the upload procedure.

## Before the ZIP exists

**Source.** Self-test first: static checks, rubric review, Oracle pass, NOP fail. `Upload Harbor task ZIP` is inactive until an `ACTIVE` grant exists. Each upload is immutable. Re-uploading the same bytes fails with `File hash already exists`.

**Practice.**

1. Re-run `tools/check_task.py` on the tree you are about to zip. A pass on an older copy does not count. Canary findings are warnings.
2. Run `python3 tools/package_task.py tasks/<slug> --out tasks/<slug>.zip`. Default `--layout wrapped` writes one top-level slug directory. `--layout flat` is allowed by SOP v3.0. `--canary-policy` is obsolete and optional. The script refuses symlinks, uses a fixed ZIP timestamp so identical trees hash the same, and prints a SHA-256. The end-to-end order is `17-conversation-flow/BUILD-ZIP.md`. The ZIP stays beside the tree, not inside it.
3. Store the digest in `evidence/<slug>/sha256.txt`. Do not add that file to the ZIP and hash again.
4. Confirm the upload button is active. Upload once.

## Version budget

**Source.** Each corrected ZIP is Version N of N. Stage 1 re-runs from the start. Only one version with every gate green reaches Stage 2. Partial credit across versions does not count. Hourly limit: 2 unique versions. Daily limit: 5 unique versions.

The limits table in SOP v3.0 is 7 reuploads per task. Leftover “3 reuploads” / “You hit 3 versions” sentences are flagged (`C-REUPLOADS`) and are not the budget. Hourly limit 2 and daily limit 5 still apply. Quote the live counter in the decision log.

`C-REUPLOAD-FREELY` is superseded: “Re-upload freely” is the old way. Do not expect an in-place replacement.
