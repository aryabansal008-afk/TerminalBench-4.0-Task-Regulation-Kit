# What to attach or paste

This file tells a person what to give Grok at each stage. It does not add requirements. The rules stay in the files named here. Paths are relative to `tb4-authoring-system/`.

A fresh conversation has no history. Every stage message must carry the core bundle plus that stage’s bundle plus the task-specific outputs listed for that stage. If a file is missing, the agent stops and names it. The agent does not reconstruct a missing file from memory.

## Mandatory core

Attach these on every stage message, including a continuation and a pre-package review.

| Order | Path | Why it is core |
| --- | --- | --- |
| 1 | `AGENTS.md` | Operating rules, including who chooses the category and what must not be claimed about difficulty. |
| 2 | `00-source/HOW-TO-READ.md` | Source versus practice, and the obligation classes. |
| 3 | `00-source/CONFLICT-REGISTER.md` | Which conflicts are superseded and which stay open. |

`00-source/REGISTER.md` is not core. It is large. Paste only the requirement IDs named for the stage. `00-source/PLATFORM-RULE-CATALOG.md` is not core. Attach a catalog row only when a live receipt names that rule.

## Stage bundles

Read the stage’s files in the order below. Mandatory means the stage is invalid without them. Conditional means attach them only in the case stated. Task-specific files are prior outputs, not system files.

### Stage 1 — Ideation and category selection

| | Path |
| --- | --- |
| Mandatory | `01-taxonomy-and-batch/TAXONOMY.md`, `01-taxonomy-and-batch/BATCH.md`, `02-ideation/SELECTION.md`, `02-ideation/IDEATION.md`, `03-difficulty-and-horizon/GENUINE-COMPLEXITY.md`, `03-difficulty-and-horizon/DESIGN.md`, `material/private-authoring/selection.md`, `material/private-authoring/complexity.md` |
| Conditional | A batch count file, if the batch owner has one. Absence is `batch_context: missing`, not zero. |
| Requirement IDs to paste | `REQ-W-001`, `REQ-TX-001` through `REQ-TX-009`, `REQ-LM-005`, `REQ-LM-006`, `REQ-PR-005`, `REQ-PR-006`, `REQ-PR-007`, `REQ-PR-019`, `REQ-PR-021`. After selection, the single `REQ-SUB-*` row that matches the chosen subcategory. |
| Do not attach | The other `REQ-SUB-*` rows, `REGISTER.md` as a whole, any example task. |

### Stage 2 — Proposal preparation

| | Path |
| --- | --- |
| Mandatory | `04-proposal/PROPOSAL.md`, `material/private-authoring/proposal.md` |
| Task-specific | `evidence/<slug>/selection.md`, `evidence/<slug>/complexity.md` |
| Conditional | Conflict section `C-EXPERT-TIME` |
| Requirement IDs to paste | `REQ-W-007`, `REQ-W-008`, `REQ-PR-001` through `REQ-PR-024`, `REQ-PR-032`, `REQ-PR-034`, `REQ-LM-006` |

### Stage 3 — Approval and grant

| | Path |
| --- | --- |
| Mandatory | `04-proposal/PROPOSAL.md` |
| Task-specific | `evidence/<slug>/proposal.md`, `evidence/<slug>/selection.md`, the platform receipt pasted into the message |
| Conditional | Conflict section `C-LEGACY-CARDS` if the receipt uses old card names |
| Requirement IDs to paste | `REQ-W-002`, `REQ-W-003`, `REQ-W-008`, `REQ-PR-024` through `REQ-PR-033`, `REQ-LM-006` |

### Stage 4 — Implementation

| | Path |
| --- | --- |
| Mandatory | `05-instruction/INSTRUCTION.md`, `06-harbor-task/LAYOUT.md`, `06-harbor-task/METADATA.md`, `07-agent-environment/ENVIRONMENT.md`, `08-reference-solution/SOLUTION.md`, `09-verifier/VERIFIER.md`, `10-checks-and-coverage/COVERAGE.md`, `13-packaging/ARCHIVE-MEMBERSHIP.md`, `material/MATERIAL-CLASSES.md`, and the skeletons under `material/agent-visible/` and `material/verifier-and-solution/` |
| Task-specific | `evidence/<slug>/proposal-receipt.txt`, `selection.md`, `complexity.md`, `decision-log.md` |
| Conditional | Conflict sections `C-CANARY`, `C-TIMEOUT`, `C-INTERNET`. `01-taxonomy-and-batch/TAXONOMY.md` if the task is GPU training (`REQ-TX-006`). |
| Requirement IDs to paste | `REQ-BD-001` through `REQ-BD-021`, `REQ-BD-026`, `REQ-PR-027`, and the `REQ-SC-check-*` IDs listed in `START-FRESH.md` stage 4 |

### Stage 5 — Validation

| | Path |
| --- | --- |
| Mandatory | `10-checks-and-coverage/STATIC-CHECKS.md`, `10-checks-and-coverage/RUBRIC.md`, `10-checks-and-coverage/COVERAGE.md`, `11-validation/VALIDATION.md`, `12-local-trials/TRIALS.md`, `03-difficulty-and-horizon/GENUINE-COMPLEXITY.md`, `tools/README.md` |
| Task-specific | The task directory, `coverage.md`, `complexity.md`, `proposal-receipt.txt` |
| Conditional | Existing `oracle.txt`, `nop.txt`, or `dry-run.md` if those commands were already run |
| Requirement IDs to paste | `REQ-W-009`, `REQ-BD-022`, `REQ-BD-023`, `REQ-BD-024`, `REQ-BD-025`, `REQ-BD-026`, `REQ-SC-000`, `REQ-RB-LOCAL`. The thirty criteria are in `RUBRIC.md`. Paste a `REQ-RB-*` row only if that criterion is in dispute. |

### Continuation

Use `CONTINUE-TASK.md`. Core, plus every task-specific file that stage’s bundle lists, plus `decision-log.md` and `complexity.md` even if the stage table also lists them.

### Review before packaging

Use `REVIEW-BEFORE-PACKAGING.md`. Core, plus `15-revision/REVISION.md`, `16-evidence-and-handoff/EVIDENCE.md`, `13-packaging/PACKAGE.md`, `13-packaging/ARCHIVE-MEMBERSHIP.md`, `material/private-authoring/pre-package-review.md`, the task tree, and the whole `evidence/<slug>/` directory except downloaded trajectories. Trajectories are conditional and only needed when the review is about a Stage 2 fail. Stage 2 has not happened yet in the ordinary pre-package review.

## How to split an oversized bundle

Split only when the message will not accept the full bundle. Do not drop a mandatory file or a named requirement ID to make the message fit.

1. Message 1 of N carries the core, in reading order, and the sentence `Bundle part 1 of N. Do not write files yet.`
2. The next parts carry the remaining mandatory stage files, then conditional files that apply, then task-specific files, then the pasted `## REQ-` blocks in the order listed.
3. The last part ends with `Bundle complete. Begin the stage prompt.` Paste the stage prompt only on that last part.
4. If a single file still does not fit, split that file on its own headings and label the parts `File <path> part i of n`. The agent must not apply a heading it has not received.
5. `REGISTER.md` is never attached whole. If the pasted IDs do not fit, send them in listed order across parts. A missing ID in the middle is a dropped requirement. Stop and send it.
6. `00-source/CONFLICT-REGISTER.md`, if it does not fit, splits as the status index first, then each `C-*` section the stage names. Do not send a later page of the register as a substitute for a named conflict.
7. Do not summarize a mandatory file in place of attaching it. A summary can omit a threshold. The agent’s instruction, if the bundle is incomplete, is to reply with the missing path or ID and write nothing else.

Task files and evidence stay out of the system folder. Do not attach `tb4-authoring-system/` as a zip of the whole tree. That upload hides which stage is active and pulls in unrelated platform-rule rows.
