# Continue a task in a new conversation

Use this when a conversation ended and the task already has evidence. The new Grok conversation does not remember the old one. The evidence pack is the memory. Attach `ATTACHMENT-MANIFEST.md`’s core, then the bundle for the stage you are resuming, then the task-specific files below.

Do not re-run ideation because the chat was lost. Do not ask the user for a category, subcategory, language, or task idea. Those are already in `selection.md` if stage 1 finished.

## Entry

You can name the stage from the evidence, without a transcript.

| If these files exist and the later ones do not | Resume at |
| --- | --- |
| Nothing under `evidence/<slug>/` | `START-FRESH.md` stage 1 |
| `selection.md` and `complexity.md`, no `proposal.md` | Stage 2 |
| `proposal.md`, no `proposal-receipt.txt` | The user still needs to submit. Do not invent a receipt. |
| `proposal-receipt.txt` whose grant is not `ACTIVE` | Stage 2 revision, using the final analysis |
| Grant `ACTIVE` in the receipt, no task tree | Stage 4 |
| Task tree, no `oracle.txt`, or Oracle still `NOT VERIFIED` | Stage 5 |
| Local Oracle `1.0`, NOP `0.0`, naive attempts `0.0`, no ZIP | `REVIEW-BEFORE-PACKAGING.md` |
| `sha256.txt` or a Stage 1 receipt | Stop this file. That work is packaging and platform review, not a fresh creation stage. Read `13-packaging/PACKAGE.md` and `14-platform-review/STAGE-1.md` only if the user opened that stage on purpose. |

## What to attach

**Mandatory.** Core from `ATTACHMENT-MANIFEST.md`. `selection.md`. `complexity.md`. `decision-log.md`. The stage bundle for the resume point. This file.

**Conditional.** `proposal.md` and `proposal-count.txt` after stage 2. `proposal-receipt.txt` after submission. `coverage.md` and the task directory after stage 4. `checker-report.txt`, `rubric-review.md`, `oracle.txt`, `nop.txt`, and `dry-run.md` after they exist.

**Reading order.** `AGENTS.md`, `00-source/HOW-TO-READ.md`, this file, the stage section of `START-FRESH.md` for the resume point, then the task-specific files. Do not read a later stage’s procedure in order to “get ahead.”

## What stays intact

- Category, subcategory, and programming language in `selection.md`. Changing category or language after the platform task exists violates `REQ-LM-006`.
- The frozen problem statement in `proposal-receipt.txt` after an `ACTIVE` grant (`REQ-PR-027`).
- Proposed targets, local measurements, and platform verdicts stay in their own blocks of `complexity.md`. Do not move a local number into the platform block.
- Provisional decisions (`C-CANARY`, `C-TIMEOUT`, `C-INTERNET`, `C-REUPLOADS`) stay provisional. Do not close them because a new chat feels like a clean start.
- `batch_context: missing` stays missing until a count file is attached.

## Prompt

```
You are continuing an existing Terminal-Bench 4 task. You have no earlier conversation. The attached evidence is the record. Do not re-select the category, subcategory, programming language, or task idea. Do not ask me to select them.

Read 17-conversation-flow/CONTINUE-TASK.md and determine the resume stage from the files present. Then follow only that stage in START-FRESH.md. If the grant is ACTIVE, the problem statement in proposal-receipt.txt is the scope. If a required evidence file for that stage is missing, name it and stop.

Keep proposed targets, local measurements, and platform verdicts in separate blocks. Do not claim difficulty or long horizon from the prose of the task. Do not package from this file. If the resume point is REVIEW-BEFORE-PACKAGING.md, follow that file. Do not call the task ready while any mandatory check is FAIL, BLOCKED, or NOT VERIFIED.
```

## Failure

If `selection.md` contradicts `proposal.md` or the receipt’s category, stop. Do not silently pick one. The lock and the grant rule decide which file wins: before creation, `selection.md` is the choice; after an `ACTIVE` grant, the frozen problem statement is the scope; category and language on the created platform task cannot be edited.

If evidence was edited by hand and a reward or verdict has no command transcript, treat that field as missing. Do not backfill it.

## Next

The next step is the resume stage’s own next step, in `START-FRESH.md`. Continuation is not a seventh stage.
