# Stage 3 qualitative checks

Platform Stage 3 is the acceptance review. It is not the conversation-flow “Stage 3” in `17-conversation-flow/START-FRESH.md`, which is the grant step.

SOP v3.0 pp. 15–17: Stage 2 measures; Stage 3 decides. A Stage 2 `PASS` does not accept the task. It only qualifies the ZIP for this review.

## Handoff from Stage 2

Stage 3 reads the evidence Stage 2 already kept. It does not run new attempts. The eight retained rollouts are the whole record. There is nothing the author can trigger.

Archive `stage2.txt` before treating Stage 3 as in progress. The reviewer works from that same SHA-256.

## What the reviewer does

All eight selected attempts are reviewed one by one. Each attempt gets a written finding, an attribution, and an outcome.

| Attribution | Effect |
| --- | --- |
| Genuine model failure | Supports acceptance. The model failed a valid task on its own. |
| Genuine success | Supports acceptance. The model solved the task legitimately. |
| Task defect | Rejects this version when material. A material defect requires a corrected package. |
| Platform defect | Incomplete. The platform recovers the evaluation; no ZIP change. |
| Unresolved | Incomplete. The review names the missing evidence or check. |

Acceptance needs all eight selected outcomes established with no material task defect. “Established” means genuine model failure or genuine success. Unresolved or platform attributions leave the review incomplete rather than failed.

## Verdicts

| Verdict | Meaning | Who acts |
| --- | --- | --- |
| `ACCEPTED` | All 8 outcomes established, no material task defect. | No task-author action. |
| `REJECTED` | Material task defect. This version is rejected. | Author revises using the recorded repair guidance and uploads a new ZIP. That ZIP starts at Stage 1 again. |
| `COULD NOT COMPLETE` | The review could not establish every selected attempt. Not a rejection and not an acceptance. | Review owner. An incomplete review does not require a replacement ZIP. |

The tab states three counts: outcomes established, attempts with task-defect findings, and unresolved.

## Reading a result

- Selected attempts: eight markers — established, invalid (task defect), or unresolved.
- Required changes: on `REJECTED`, the recorded repair guidance. Fix exactly that.
- Attempt review: per-attempt finding, attribution, and outcome. Read findings even on an accepted task.
- Review record: task status, decision, task attribution, limitations, final acceptance, and evaluation ID.

Put the pasted receipt in `evidence/<slug>/acceptance.txt` and the per-attempt notes in `evidence/<slug>/review-findings.md`. A Stage 2 `PASS` must not be copied into those files as an acceptance.

QC and Super QC remain later layers the change table names. Super QC’s criteria are not in the PDF (`U-SUPER-QC`). Stage 3 is not Super QC.

`C-FOUR-CRITERIA`, `C-NINE-DIMENSIONS`, and `C-LEGACY-CARDS` still apply to leftover checklist text. Do not mark the task merged. Do not invent nine dimension names.
