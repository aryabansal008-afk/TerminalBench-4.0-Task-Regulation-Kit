# Requirement traceability

Source of IDs: `00-source/REGISTER.md`. That file is generated. Do not hand-edit it. Each row’s `explained_in` path is the guidance file. `tools/build_register.py` refuses to write the register if that path is missing.

Read a requirement forward: ID → `explained_in` file → checkpoint below → artifact → evidence field on the register row.

Read it backward: evidence file → artifact → checkpoint → guidance file → the IDs in that prefix. Open the register section for the exact sentence. Do not treat the prefix as a substitute for the row.

Statuses used on evidence: `NOT STARTED`, `IN PROGRESS`, `PASS`, `FAIL`, `BLOCKED`, `NOT VERIFIED`, `NOT APPLICABLE`. A blank evidence file is `NOT STARTED`. A missing transcript is `NOT VERIFIED`, not `PASS`. Rubric statuses are not Harbor results. Local rewards are not platform verdicts.

## Forward map

| IDs | Guidance file that exists | Creation checkpoint | ZIP checkpoint | Artifact or decision | Evidence |
| --- | --- | --- | --- | --- | --- |
| `REQ-W-001`–`REQ-W-006`, `REQ-W-014` | `AGENTS.md`, `00-source/HOW-TO-READ.md`, `00-source/CONFLICT-REGISTER.md`, `00-source/INVENTORY.md` | `START-FRESH.md` stage 1 | `BUILD-ZIP.md` step 14, conflicts stay open | Operating rules and conflict choices | `decision-log.md` |
| `REQ-W-007`, `REQ-W-008` | `04-proposal/PROPOSAL.md` | Stage 2 and stage 3 | Step 1 | Submitted proposal and receipt | `proposal.md`, `proposal-receipt.txt` |
| `REQ-W-009` | `11-validation/VALIDATION.md`, `10-checks-and-coverage/STATIC-CHECKS.md`, `10-checks-and-coverage/RUBRIC.md` | Stage 5 | Steps 7 and 8 | Local self-test | `checker-report.txt`, `rubric-review.md`, `oracle.txt`, `nop.txt` |
| `REQ-W-010`, `REQ-W-012` | `13-packaging/PACKAGE.md`, `14-platform-review/STAGE-1.md` | Not a creation pass | Steps 12 and 14 | Immutable ZIP | `sha256.txt`, `packaging-manifest.md` |
| `REQ-W-011` | `14-platform-review/STAGE-2.md` | Not a creation pass | Step 14, left `NOT VERIFIED` | Stage 2 predicates | `stage2.txt` |
| `REQ-W-013` | `14-platform-review/ACCEPTANCE.md` | Not a creation pass | Step 14, left `NOT VERIFIED` | QC then Super QC | `acceptance.txt` |
| `REQ-W-015` | `14-platform-review/STAGE-1.md` | `NOT APPLICABLE` until a task row exists | Step 14 if a receipt exists | Blocking-reason column | `stage1.txt` |
| `REQ-PR-001`–`REQ-PR-034` | `04-proposal/PROPOSAL.md` | Stages 2 and 3 | Step 1 | Proposal text and grant | `proposal.md`, `proposal-receipt.txt` |
| `REQ-UI-002` | `04-proposal/PROPOSAL.md` | Stage 2 | `NOT APPLICABLE` at zip time | Form prompts already followed | `proposal.md` |
| `REQ-BD-001`–`REQ-BD-021` | `06-harbor-task/LAYOUT.md`, `06-harbor-task/METADATA.md`, `05-instruction/INSTRUCTION.md`, `07-agent-environment/ENVIRONMENT.md`, `08-reference-solution/SOLUTION.md`, `09-verifier/VERIFIER.md` | Stage 4 | Steps 2–6 | Task tree | `coverage.md`, `checker-report.txt` |
| `REQ-BD-026` | `09-verifier/VERIFIER.md` | Stage 4 for the file; stage 5 for the oracle run that executes it | Steps 2, 3, and 7 | `solution/solve.sh` exists, is not copied into the agent image, and is the oracle entry | `solution/solve.sh`, `oracle.txt` |
| `REQ-BD-022`, `REQ-BD-023` | `11-validation/VALIDATION.md` | Stage 5 | Step 7 | Oracle and NOP transcripts | `oracle.txt`, `nop.txt` |
| `REQ-BD-024` | `11-validation/VALIDATION.md` | Stage 5 | Step 8 | Static and rubric reports | `checker-report.txt`, `rubric-review.md` |
| `REQ-BD-025` | `12-local-trials/TRIALS.md` | Stage 5 | Step 14 | Dry-run, local only | `dry-run.md` |
| `REQ-SC-000`, `REQ-SC-check-*`, `REQ-SC-REUPLOAD-SENTENCE` | `10-checks-and-coverage/STATIC-CHECKS.md`, `00-source/CONFLICT-REGISTER.md` for `C-REUPLOADS` and `C-CANARY` | Stage 5 | Steps 8 and 12 | Checker output and reupload note | `checker-report.txt`, `decision-log.md` |
| `REQ-RB-01`–`REQ-RB-30`, `REQ-RB-LOCAL` | `10-checks-and-coverage/RUBRIC.md` | Stage 5 | Step 8 | Rubric justifications | `rubric-review.md` |
| `REQ-G-001`–`REQ-G-015` | `14-platform-review/STAGE-1.md`, `13-packaging/ARCHIVE-MEMBERSHIP.md` | Not a creation pass | Steps 10 and 14 | ZIP shape and, later, the Stage 1 receipt | `packaging-manifest.md`, `stage1.txt` |
| `REQ-S2-001`–`REQ-S2-008` | `14-platform-review/STAGE-2.md`, `03-difficulty-and-horizon/DESIGN.md`, `03-difficulty-and-horizon/GENUINE-COMPLEXITY.md` | Stage 5 may apply `REQ-S2-006` and `REQ-S2-007` only as repair rules | Step 14 | Platform rollout | `stage2.txt`, `complexity.md` platform block |
| `REQ-LM-001`–`REQ-LM-008` | `00-source/CONFLICT-REGISTER.md`, `02-ideation/SELECTION.md`, `13-packaging/PACKAGE.md` | Stage 1 for `REQ-LM-005` and `REQ-LM-006` | Steps 1 and 12 | Category lock, quotas, identical-hash rule | `selection.md`, `decision-log.md` |
| `REQ-TX-001`–`REQ-TX-009` | `01-taxonomy-and-batch/TAXONOMY.md`, `01-taxonomy-and-batch/BATCH.md` | Stage 1 | Step 1, match only | Chosen category | `selection.md`, `applicability.md` |
| `REQ-SUB-*` | `01-taxonomy-and-batch/TAXONOMY.md` | Stage 1, one row | Step 1 | The chosen subcategory row is `PASS` as a fit decision. Every other `REQ-SUB-*` row is `NOT APPLICABLE` | `applicability.md` |
| `REQ-AC-001`–`REQ-AC-013` | `14-platform-review/ACCEPTANCE.md`, `00-source/INVENTORY.md` for `REQ-AC-001` | Not a creation pass | Step 14, `NOT VERIFIED` | Acceptance pipeline | `acceptance.txt` |
| `REQ-UI-001` | `14-platform-review/ACCEPTANCE.md` | `NOT APPLICABLE` until the UI is on screen | Step 14 | Stage tabs, including deferred Stage 3 | `acceptance.txt` |
| `REQ-PL-*` | `00-source/PLATFORM-RULE-CATALOG.md` | `NOT APPLICABLE` until a receipt names the rule | Step 10 for G01 shape only as a local refusal of symlinks and extra roots; every `REQ-PL-*` result stays `NOT VERIFIED` until Stage 1 | Platform rule id | `stage1.txt` |

## Backward map

| Evidence | Comes from | Checkpoint that may set `PASS` | Checkpoint that must not set `PASS` from this file alone |
| --- | --- | --- | --- |
| `selection.md` | Stage 1 decision | Creation stage 1 | ZIP step 14 |
| `complexity.md` proposed targets | Quotes from `DESIGN.md` | Never `PASS`. They are quotes. | Any checkpoint |
| `complexity.md` local measurements | Oracle, NOP, naive attempts, dry-run | Stage 5 and ZIP steps 7 and 9, and only for those commands | Stage 2 and acceptance |
| `complexity.md` platform block | `stage2.txt` or an acceptance quote | ZIP step 14 only after a receipt | Stage 5 |
| `proposal.md` | Stage 2 | Creation stage 2 after `check_proposal.py` | Grant, until a receipt exists |
| `proposal-receipt.txt` | Platform, pasted | Creation stage 3 | A locally written verdict |
| `coverage.md` | Stage 4 and ZIP step 5 | Those checkpoints | Rubric or Oracle |
| `checker-report.txt` | `tools/check_task.py` | Stage 5 and ZIP step 8 | `harbor check`, G06 |
| `rubric-review.md` | Local rubric reading | Stage 5 and ZIP step 8 | Oracle, Stage 1 |
| `oracle.txt`, `nop.txt` | Harbor, pasted | Stage 5 and ZIP step 7 | Stage 2 `difficulty` |
| `dry-run.md` | Local model, pasted | Stage 5 | `REQ-S2-003`, `REQ-S2-004` |
| `cheat-trials.md` | Author attempts | ZIP step 9 | Acceptance bullet 5 until a reviewer runs it |
| `sha256.txt` | `package_task.py` stdout | ZIP step 12 | Upload, Stage 1 |
| `packaging-manifest.md` | ZIP steps 1–14 | ZIP step 14 for local readiness only | Acceptance |
| `stage1.txt` | Platform receipt | After upload, outside this local ready mark | A local checker exit |
| `stage2.txt` | Platform receipt | After Stage 2 | A dry-run count |
| `acceptance.txt` | Maintainer, QC, Super QC | When those events are pasted | Stage 2 `PASS` |
| `applicability.md` | Folder and `REQ-SUB-*` decisions | The stage that records the decision | A folder marked `NOT APPLICABLE` without a reason |
| `revision-log.md` | An edit after a ready mark | The recheck named in `BUILD-ZIP.md` | The previous digest |
