# Failure diagnosis, change impact, and revalidation

A failed gate names the next edit. It does not authorize a quiet expansion of the frozen proposal.

## Diagnosis

**Source.** Read the blocking reason, the final analysis, or the Stage 2 header. Examples the PDF itself gives:

| Signal | What the PDF says to do |
| --- | --- |
| `Stage 1 rejected — upload a corrected ZIP` with a rule id | Fix that defect. Upload a new immutable version. Stage 1 re-runs from the start. |
| `Stage 1 could not complete — retry` | Retry. Do not rewrite the task to explain a platform-side failure. |
| Stage 2 `difficulty` FAIL | Add depth: cross-source correlation, consistent state, stricter exactness. Do not hide information. |
| Stage 2 `long_horizon` FAIL | Add real sequential work and boundary conditions. Do not pad. |
| Stage 2 `INDETERMINATE` | Not a difficulty failure. Do not press Stop during an active provider attempt. |
| Proposal `Reject` or `Uncertain` | Revise the proposal. No grant, so no ZIP. |
| `Duplicate detected` or novelty rejection | A semantic change, not a rename. The threshold is unknown. |
| `File hash already exists` | Change the task. Do not re-wrap the same bytes. |
| Oracle below 1.0 | Fix the solution or the verifier, including missing verifier dependencies. |
| NOP at 1.0 | The verifier is weak. Tighten the tests. |

## Change impact

**Source.** The granted proposal text is frozen. A material change is a new task. Category and programming language are locked at creation. Each ZIP is a new version. Partial credit across versions does not count.

**Practice.** Before editing, write a private impact note with three lists:

- Files that will change.
- Graded conditions that will change. If this list is non-empty, diff it against the granted problem statement. Stop and ask for a new proposal if the outcome, the inputs, or the graded conditions move.
- Checks that must be re-run. Use the table below. Do not skip a row because an earlier version already passed it.

| Edit | Re-run |
| --- | --- |
| Instruction wording, paths, or suffix | `check_task.py`, coverage table, rubric group D, Oracle, NOP |
| `timeout_sec` | Suffix equality, both timeout fields, Oracle, NOP |
| Agent Dockerfile or fixtures | Image build, absolute paths, leak check, Oracle, NOP |
| Tests or ground truth | Coverage table, Oracle, NOP, the negative cases in `11-validation/VALIDATION.md` |
| Solution only | Oracle, and a leak check that the instruction did not gain hints |
| Metadata only | `check-task-fields`, rubric E metadata, no new ZIP until the rest of the tree is still the tree you last validated |

A change aimed at one Stage 2 predicate usually moves the other. Re-measure both locally as far as a dry-run can, and archive both platform ceilings again after the next rollout.

## Revalidation before the next upload

**Practice.** The next ZIP is a new version, so the previous green gates do not carry over. The minimum before that upload is: `check_task.py` on the tree being zipped, the coverage table updated, Oracle `1.0`, NOP `0.0`, and the cheat that previously succeeded now scoring `0.0` if a cheat was the reason for the edit. Quote `C-REUPLOADS` if this version number is 4, 5, 6, or 7.
