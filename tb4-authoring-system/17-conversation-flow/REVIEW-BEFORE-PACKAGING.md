# Review and repair before packaging

Use this after stage 5 and before `tools/package_task.py`. The agent repairs the tree or reports that it is ready. It does not upload. It does not mark Stage 1, Stage 2, or acceptance as passed.

A fresh conversation must attach the core in `ATTACHMENT-MANIFEST.md`, this file, and the task-specific set below. Chat history is not evidence.

## Purpose

Find defects that would spend an immutable version: static-check failures, rubric fails, Oracle not at `1.0`, NOP not at `0.0`, a naive attempt at `1.0`, instruction drift from the frozen proposal, hidden tests, leaked answers, or a ZIP that would contain private evidence.

## Entry

All of these are true:

- `proposal-receipt.txt` shows an `ACTIVE` grant.
- The task directory is `tasks/<slug>/` and contains no `REPLACE_ME`.
- `complexity.md` has local measurements for Oracle, NOP, and each naive approach, or the field says `NOT VERIFIED`.
- Platform-verdict fields are still blank, unless a receipt is actually attached. A blank field is `NOT VERIFIED`.

If Oracle or NOP is `NOT VERIFIED`, this review cannot pass. Return to stage 5 and run the commands. Do not package on a plan to run them later.

## Reading order

1. `AGENTS.md`
2. `00-source/HOW-TO-READ.md`
3. This file
4. `15-revision/REVISION.md`
5. `16-evidence-and-handoff/EVIDENCE.md` readiness list
6. `13-packaging/ARCHIVE-MEMBERSHIP.md`
7. `10-checks-and-coverage/STATIC-CHECKS.md` and `RUBRIC.md`
8. The frozen problem statement, `selection.md`, `decision-log.md`, `coverage.md`, `complexity.md`
9. The task tree, last, so the rules are already in view

## Mandatory and conditional

**Mandatory.** Core, this file, `15-revision/REVISION.md`, `16-evidence-and-handoff/EVIDENCE.md`, `13-packaging/ARCHIVE-MEMBERSHIP.md`, `13-packaging/PACKAGE.md`, `10-checks-and-coverage/STATIC-CHECKS.md`, `10-checks-and-coverage/RUBRIC.md`, `11-validation/VALIDATION.md`, the task tree, and the evidence files named in the entry condition.

**Conditional.** Conflict sections `C-CANARY`, `C-TIMEOUT`, `C-INTERNET`, and `C-REUPLOADS`. `C-REUPLOADS` matters only when a version number is already 4, 5, 6, or 7. `14-platform-review/STAGE-1.md` is not required to decide local readiness. Attach it only if a previous upload receipt is part of the repair.

**Requirement IDs.** `REQ-W-009`, `REQ-W-010`, `REQ-W-012`, `REQ-BD-022`, `REQ-BD-023`, `REQ-BD-024`, `REQ-PR-027`, `REQ-G-001`, `REQ-G-004`, `REQ-LM-003`, `REQ-LM-004`, `REQ-LM-007`, `REQ-RB-01` through `REQ-RB-30` via `RUBRIC.md`, and every `REQ-SC-check-*` row via `STATIC-CHECKS.md`. Paste an individual register block only for a check that is failing.

## What the review writes

`evidence/<slug>/pre-package-review.md`, from `material/private-authoring/pre-package-review.md`. Each check is `PASS`, `FAIL`, `BLOCKED`, `NOT VERIFIED`, or `NOT APPLICABLE`. It does not replace `checker-report.txt` or `rubric-review.md`. Those stay the command and rubric records.

Also update `complexity.md` only to fix a number that was filed in the wrong block. Do not invent a new measurement.

## Checks before anyone packages

- Frozen problem statement and `instruction.md` name the same artifact, inputs, and graded conditions.
- Category and language match `selection.md`. They were recorded before creation.
- `decision-log.md` has provisional blocks for `C-CANARY` and `C-TIMEOUT`. No invented canary string is in the tree.
- `tools/check_task.py --canary-policy <the provisional choice>` was run on this tree. The saved report matches this tree.
- Coverage has no instruction sentence without a test and no test without an instruction sentence.
- Oracle local reward is `1.0`. NOP local reward is `0.0`. Each naive attempt is `0.0`. Partial NOP is not recorded as a platform ruling (`C-REWARD-LITERAL`).
- Rubric fails are fixed, not relabeled.
- The tree contains no `.git`, no symlink, no credential, and no copy of `tests/` or `solution/` under `environment/`.
- Private evidence is not inside the task directory.
- The reviewer did not write “difficult,” “long horizon,” “Stage 2 pass,” or “accepted” from the sound of the task.

## Prompt

```
You are reviewing a Terminal-Bench 4 task before packaging. You have no earlier conversation. The attached tree and evidence are the record.

Follow 17-conversation-flow/REVIEW-BEFORE-PACKAGING.md. Copy material/private-authoring/pre-package-review.md to evidence/<slug>/pre-package-review.md and set each check to PASS, FAIL, BLOCKED, NOT VERIFIED, or NOT APPLICABLE. Repair FAIL rows only when 15-revision/REVISION.md allows the edit without changing the frozen proposal. If a repair would change graded conditions, stop and say a new proposal is required.

Do not invent Harbor output. Do not package, do not upload, and do not fill platform verdicts. Do not ask me for a category or a task idea. Do not add a canary string. Use PASS, FAIL, BLOCKED, NOT VERIFIED, or NOT APPLICABLE. A missing check is NOT VERIFIED. Do not say the tree is ready while any mandatory check is FAIL, BLOCKED, or NOT VERIFIED. If every executable check is PASS and every unresolved conflict is recorded BLOCKED, name BUILD-ZIP.md as the next file and stop.
```

## Failure and the next step

| Finding | Next step |
| --- | --- |
| `NOT VERIFIED` on Oracle, NOP, or the checker | Return to `START-FRESH.md` stage 5. Do not package. |
| Checker or rubric fail | Fix under `15-revision/REVISION.md`, re-run the failed check, and review again. |
| Instruction drifted from the frozen statement | Restore the instruction, or stop for a new proposal if the drift was intentional. |
| Naive attempt scores `1.0` | Strengthen under `03-difficulty-and-horizon/GENUINE-COMPLEXITY.md`. Add the new requirement to the instruction and `coverage.md` together. Re-run Oracle, NOP, and that attempt. |
| Local dry-run is only a handful of turns | Same strengthening path. Do not add busywork or hidden steps. |
| Grant is not `ACTIVE` | Do not package. Return to stage 3. |
| Every executable check is `PASS`, and every unresolved conflict is recorded `BLOCKED` | Follow `BUILD-ZIP.md`. Do not call the tree ready, and do not treat this review as a ZIP, a Stage 1 pass, or acceptance. |

A pass on this review is not `PASSED STAGE 1` and not a Stage 2 `PASS`.
