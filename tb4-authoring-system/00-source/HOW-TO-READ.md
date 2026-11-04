# How to read this system

The PDF is the source. `REGISTER.md` is the canonical list of extracted requirements. `CONFLICT-REGISTER.md` is the only place a conflict is marked superseded, unresolved, or compatible. `UNAVAILABLE-SOURCES.md` lists documents the PDF names and does not contain. Do not fill those from memory.

A later page does not repeal an earlier page. An earlier page does not repeal a later page. Apply a side only when the conflict register quotes the PDF naming that side as the old way.

## Source requirements and engineering practice

| Label | Meaning |
| --- | --- |
| Source | A rule stated in the PDF, including screenshot text that was legible. |
| Practice | A way to carry out a source rule without adding a requirement the PDF does not state. Practice never chooses the easier or the stricter side of an unresolved conflict. |

If a practice paragraph and a source paragraph disagree, follow the source. If two source paragraphs disagree, follow the conflict register.

## Obligation classes

| Class | Meaning | What to do |
| --- | --- | --- |
| `mandatory` | Required for a compliant task, proposal, batch, or account action. | Satisfy it and keep evidence. |
| `conditional` | Required only when the feature is present. The PDF’s phrase is `IF APPLICABLE`. | If present, treat as mandatory. If absent, record why. |
| `advisory` | Recommended, or warning-level. `OPTIONAL / ADVISORY` does not by itself reject the task. | Follow it, or record a reason not to. |
| `example` | A sample task, verdict, hash, or layout. The DFIR tree on pages 6–7 is an example of extra files, not the required file list. | Use the pattern the surrounding prose states. Do not copy its filenames into an unrelated task. |
| `unresolved` | The PDF does not let the author execute the point unambiguously. | Stop for the clarification named in the conflict register or `UNRESOLVED.md`. |
| `platform` | Enforced on an uploaded ZIP or during rollout. A local script cannot mark it passed. | Prevent the failing condition. Evidence is the platform receipt. |

## Scope and stage

Scope is `task`, `batch`, `account`, `platform`, or `process`. Stage is one or more of `proposal`, `grant`, `build`, `self-test`, `package`, `stage1`, `stage2`, `acceptance`, `batch`, `account`. Evidence is collected at the earliest stage where it can be shown.

## Platform severity, page 9

| Platform label | Effect the PDF states |
| --- | --- |
| `REQUIRED` | Rejects the task, or marks Stage 1 incomplete when the failure is platform-side. |
| `OPTIONAL / ADVISORY` | Does not reject. `Stage 1 accepted · 2 warnings` can still be a pass. |
| `IF APPLICABLE` | Evaluated only when the feature is used. Compose rules are the PDF’s example. |

Outcome strings: `Stage 1 rejected — upload a corrected ZIP`; `Stage 1 could not complete — retry`; `Stage 1 accepted` / `PASSED STAGE 1` / `READY_FOR_STAGE2`.

## Where a rule lives

State each source rule in the lifecycle file named by the register’s `explained_in` field. Other files cite the requirement ID. Do not restate a threshold in a second file in order to “help.” If a number must be repeated so a stage can be done without opening the PDF, the repeated sentence must match the lifecycle file, and the lifecycle file must match the PDF quote in the register.
