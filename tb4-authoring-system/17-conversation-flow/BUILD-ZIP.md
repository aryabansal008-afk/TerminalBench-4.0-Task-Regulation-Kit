# Build the submission ZIP

Turn a completed task tree into one Harbor ZIP. This file does not accept the task and does not call the archive ready to upload. The archive claim and a platform verdict are different records.

Do this only after `REVIEW-BEFORE-PACKAGING.md` has no `FAIL` and no `NOT VERIFIED` on an executable check this flow repeats. A missing check stays `NOT VERIFIED`. It is not `PASS`. Unresolved conflicts stay `BLOCKED` and keep the archive claim `BLOCKED`. A rubric line is not an Oracle result. An Oracle line is not Stage 1, Stage 2, or acceptance.

Paths below are relative to `tb4-authoring-system/` unless they begin with `evidence/` or `tasks/`. The task directory is `tasks/<slug>/`. Its evidence is `evidence/<slug>/`. Write the ZIP to `tasks/<slug>.zip`. The ZIP is not a member of the evidence pack, and the evidence pack is not a member of the ZIP.

Any edit after `record_status` is `PASS` invalidates the affected evidence. The rule is at the end of this file. Do not set `record_status` to `PASS` again until the rechecks listed there are `PASS` or an explicit `NOT APPLICABLE`, and no relevant mandatory check is `FAIL`, `BLOCKED`, or `NOT VERIFIED`.

## Commands this repo actually runs

| Command | What it does | What it does not do |
| --- | --- | --- |
| `python3 tools/check_proposal.py evidence/<slug>/proposal.md` | Character count, paragraph count, headings, `REPLACE_ME`, steering phrases | Does not judge the six review criteria or the grant |
| `python3 tools/check_task.py tasks/<slug> --canary-policy no-canary` or `--canary-policy required --canary-string <issued>` | Local preflight. Exits 2 if the policy flag is omitted | Does not resolve `C-CANARY`. Does not run Harbor |
| `python3 tools/package_task.py tasks/<slug> --out tasks/<slug>.zip --canary-policy <same>` | Refuses symlinks, runs the preflight unless `--skip-check` is passed, writes one top-level directory named the task folder, prints SHA-256, prints `not uploaded` | Does not upload. The single top-level directory is provisional (`U-ZIP-ROOT`). The ZIP file stays beside the tree |

Do not pass `--skip-check` for an archive that will be marked ready.

`<slug>` and the canary choice are placeholders. The task tree is `tasks/<slug>`. The archive is `tasks/<slug>.zip`. `no-canary` is not a closed reading of the PDF. `required` needs a string the platform issued. This system does not supply one.

## Tooling named by the PDF and not in this repo

Leave the result `NOT VERIFIED` until the user pastes a transcript. Do not invent a reward, a rubric score, or a Harbor exit code.

| Name in the PDF | Gap |
| --- | --- |
| `harbor run --path . --agent oracle` and `--agent nop` | Not installed here. Expected local tokens are `1.0` and `0.0` only after a real run (`11-validation/VALIDATION.md`). |
| `harbor check` | Arguments are not in the PDF (`U-HARBOR-PIN`). |
| pytest CTRF flag and report path | `U-CTRF-FLAG`. |
| Pinned Harbor version | `U-HARBOR-PIN`. |
| Platform button `Upload Harbor task ZIP` | A UI control. No local command uploads. |

## Step 1 — Grant and frozen scope

**Guidance.** `04-proposal/PROPOSAL.md`, `02-ideation/SELECTION.md`, `00-source/CONFLICT-REGISTER.md` (`C-ACCOUNT-LIMITS` only to record the quota, not to change category).

**Inputs.** `evidence/<slug>/proposal-receipt.txt`, `proposal.md`, `selection.md`, `decision-log.md`.

**Evidence.** `packaging-manifest.md` fields `grant_state` and `frozen_statement_match`.

**Pass.** The receipt text says the grant is `ACTIVE`, and the instruction’s artifact, inputs, and graded conditions are the same statements as the problem statement as reviewed. Category and programming language match `selection.md`.

**Fail.** Grant is absent, not `ACTIVE`, or the tree implements a different task.

**Remediation.** Do not zip. Return to `START-FRESH.md` stage 3, or stage 2 if the proposal must be revised. A material scope change is a new task (`15-revision/REVISION.md`).

## Step 2 — Task layout

**Guidance.** `06-harbor-task/LAYOUT.md`.

**Inputs.** The task directory.

**Evidence.** Manifest inventory of paths.

**Pass.** The directory name is at most three lowercase kebab tokens. Present: `instruction.md`, `task.toml`, `environment/Dockerfile`, `solution/solve.sh`, `tests/Dockerfile`, `tests/test.sh`. `solution/solve.py` is present when `solve.sh` launches it.

**Fail.** A missing required path, a second task root, or `REPLACE_ME` still in a file.

**Remediation.** Copy the missing skeleton from `material/agent-visible/` or `material/verifier-and-solution/` and fill it. Re-run step 8’s checker afterward.

## Step 3 — What is inside which image

**Guidance.** `material/MATERIAL-CLASSES.md`, `13-packaging/ARCHIVE-MEMBERSHIP.md`, `07-agent-environment/ENVIRONMENT.md`, `08-reference-solution/SOLUTION.md`, `09-verifier/VERIFIER.md`.

**Inputs.** `environment/Dockerfile`, `tests/Dockerfile`, fixture paths named by the instruction.

**Evidence.** Manifest sections `agent_image_contains` and `verifier_image_contains`.

**Pass.** Inputs the instruction names are copied by the agent Dockerfile. `tests/` and `solution/` are in the task directory so the ZIP contains them, and the agent Dockerfile does not copy them. Ground truth used only by the grader is only in the verifier image.

**Fail.** Tests, solution, or expected answers are copied into the agent image, or a graded input is missing from both images.

**Remediation.** Move the file to the image that may see it. This is a task-tree edit. It invalidates Oracle, NOP, the checker, and any previous digest.

## Step 4 — Metadata and configuration

**Guidance.** `06-harbor-task/METADATA.md`.

**Inputs.** `task.toml`, `instruction.md` suffix, `selection.md`.

**Evidence.** Manifest fields `timeout_agent`, `timeout_verifier`, `suffix_n`, `category`, `subcategory`.

**Pass.** Required metadata fields are non-empty and not `REPLACE_ME`. `category` matches `selection.md`. `[verifier] environment_mode = "separate"`. Top-level `artifacts` is before any `[table]` header. Suffix integer equals `[agent].timeout_sec`. The integer is still provisional (`C-TIMEOUT`). `allow_internet` is not `false` (`C-INTERNET` stays unresolved). GPU types, if any, are from the canonical list. Training GPUs are a single `H100`.

**Fail.** A mismatch between suffix and timeout, a locked category that differs from `selection.md`, or an empty required field.

**Remediation.** Edit `task.toml` or the suffix so they match. Do not treat 18000 or 8 hours as the resolved timeout.

## Step 5 — Instruction, solution, and verifier

**Guidance.** `05-instruction/INSTRUCTION.md`, `10-checks-and-coverage/COVERAGE.md`.

**Inputs.** `instruction.md`, `solution/`, `tests/`, `evidence/<slug>/coverage.md`.

**Evidence.** Updated `coverage.md`. Every row has a status.

**Pass.** Each graded sentence has a test. Each test has a sentence. Output paths used by both solution and tests are in the instruction or `task.toml`. No `##` headings, no step list, no relative paths.

**Fail.** Hidden grading, or an instruction promise with no test.

**Remediation.** Add the sentence and the test together, or delete the extra test. If the frozen proposal’s conditions would change, stop and open a new proposal.

## Step 6 — Dependencies and build

**Guidance.** `07-agent-environment/ENVIRONMENT.md`, `09-verifier/VERIFIER.md`.

**Inputs.** Both Dockerfiles and `tests/test.sh`.

**Evidence.** Checker report after the next `check_task.py` run. There is no local Docker build in this repo. Image build success is `NOT VERIFIED` until Harbor or another build transcript is pasted (`REQ-BD` does not add a `docker build` command).

**Pass.** Apt is unpinned, `apt-get update` precedes install, the lists are removed. pip, uv, uvx, and `uv tool` pins use `==`, or an allowed exception in `ENVIRONMENT.md`. No `FROM --platform=`. No bare `nproc`. `test.sh` does not apt-get, pip install, curl, wget, or git clone. `uv venv` is used, or system-wide Python is documented.

**Fail.** Any of those checker failures.

**Remediation.** Fix the Dockerfile or `test.sh`. Re-run `check_task.py`. A pasted Harbor build failure is fixed the same way and is not a platform retry unless the receipt says `Stage 1 could not complete — retry`.

## Step 7 — Oracle and NOP

**Guidance.** `11-validation/VALIDATION.md`.

**Inputs.** Transcripts the user supplies. This flow does not run Harbor.

**Evidence.** `evidence/<slug>/oracle.txt`, `nop.txt`, and the local-measurement block of `complexity.md`.

**Pass.** Oracle transcript shows reward `1.0`. NOP transcript shows reward `0.0`. Both commands are the ones in `VALIDATION.md`.

**Fail.** Any other reward, a missing file, or a reward written from memory.

**Remediation.** Fix solution or tests per `VALIDATION.md`. Re-run the real command. Set the old transcript status to `NOT VERIFIED` until the new transcript is pasted.

`C-REWARD-LITERAL`: local NOP `0.0` follows the local table. It does not decide `NOP.PARTIAL_REWARD`.

## Step 8 — Static checks and rubric

**Guidance.** `10-checks-and-coverage/STATIC-CHECKS.md`, `10-checks-and-coverage/RUBRIC.md`, `tools/README.md`.

**Inputs.** The task tree about to be zipped.

**Evidence.** `checker-report.txt` from this tree. `rubric-review.md` with one status per criterion `REQ-RB-01` through `REQ-RB-30`.

**Command.**

```
python3 tools/check_task.py tasks/<slug> --canary-policy <no-canary|required>
```

**Pass.** The checker exit is 0 and the report is stored. Each rubric criterion is `PASS` or `NOT APPLICABLE` with a reason. `NOT VERIFIED` is not a pass.

**Fail.** Checker non-zero, or any rubric `FAIL`.

**Remediation.** Fix the named check. A rubric `PASS` does not fill Oracle. An Oracle `1.0` does not fill the rubric.

The checker is not G06 and not `harbor check`.

## Step 9 — Adversarial checks and open defects

**Guidance.** `11-validation/VALIDATION.md`, `03-difficulty-and-horizon/GENUINE-COMPLEXITY.md`, `00-source/UNRESOLVED.md`.

**Inputs.** `complexity.md` naive-attempt rewards, `cheat-trials.md` if any attempts were run.

**Evidence.** Manifest field `open_defects`.

**Pass.** Each named naive attempt has a pasted reward of `0.0`. Known unresolved IDs that affect the ZIP (`C-CANARY`, `C-TIMEOUT`, `C-INTERNET`, `C-REUPLOADS`, `U-ZIP-ROOT`, `U-CTRF-FLAG`, `U-HARBOR-PIN`) are listed as `BLOCKED` or as a provisional choice. None is marked `PASS`.

**Fail.** A naive attempt at `1.0`, a blank reward marked as passed, or an unresolved conflict marked `PASS`.

**Remediation.** Strengthen under `GENUINE-COMPLEXITY.md` without a hidden test. Leave unresolved IDs open.

## Step 10 — Archive safety and candidate root

**Guidance.** `14-platform-review/STAGE-1.md` (G01), `13-packaging/ARCHIVE-MEMBERSHIP.md`.

**Inputs.** The task directory before zipping.

**Evidence.** Manifest statement of symlink check and top-level shape.

**Pass.** `package_task.py` does not refuse the tree. It writes one top-level directory equal to the task folder name. That shape is recorded as provisional (`U-ZIP-ROOT`), not as the PDF’s required shape.

**Fail.** Symlink, path escape, or preflight failure. The script then writes no usable ready mark.

**Remediation.** Remove the symlink or the extra root. If a later Stage 1 receipt rejects the shape, follow the receipt. Do not invent a second layout in advance.

## Step 11 — Exclusions

**Guidance.** `13-packaging/ARCHIVE-MEMBERSHIP.md`.

**Inputs.** A listing of the task directory.

**Evidence.** Manifest exclusion list, each item `PASS` if absent from the tree.

**Must be absent.** `tb4-authoring-system/`, `evidence/<slug>/`, `.git`, `__pycache__`, `*.pyc`, editor swap files, `.DS_Store`, credential files, a copy of `tests/` or `solution/` under `environment/`, `sha256.txt`, proposal, decision log, and any canary string this system invented.

**Fail.** Any of those paths are inside `tasks/<slug>`.

**Remediation.** Move them out. Re-run from step 8. The previous digest is invalid.

## Step 12 — Inventory, checksum, version

**Guidance.** `13-packaging/PACKAGE.md`, `00-source/CONFLICT-REGISTER.md` section `C-REUPLOADS`.

**Inputs.** A tree that passed steps 1–11.

**Command.**

```
python3 tools/package_task.py tasks/<slug> --out tasks/<slug>.zip --canary-policy <no-canary|required>
```

**Evidence.** The script’s stdout pasted into `sha256.txt` and the member list from the extraction check in step 13. Version field is the next integer the user supplies from the platform, or `SUPPLY` if the UI has not shown it. Hourly limit 2 and daily limit 5 are recorded as source limits. The 3-versus-7 reupload count stays `BLOCKED` (`C-REUPLOADS`). Do not choose 3 or 7.

**Pass.** Stdout contains `sha256` and `not uploaded`, and step 13’s listing matches the task files plus the single top-level directory.

**Fail.** Preflight failure, or a digest copied from an older ZIP.

**Remediation.** Fix the preflight and run the command again. Do not reuse the old digest.

## Step 13 — Validate the packaged bytes

**Guidance.** The packager uses `zipfile` in `tools/package_task.py`. Use the same library to list members. This listing is not a Harbor run.

**Command.**

```
python3 -c "import hashlib,sys,zipfile; p=sys.argv[1]; print(hashlib.sha256(open(p,'rb').read()).hexdigest()); z=zipfile.ZipFile(p); print('\n'.join(z.namelist()))" <file>.zip
```

**Evidence.** Paste that stdout under the manifest heading `extraction`.

**Pass.** The hash equals the packager’s printed hash. Every name starts with `<slug>/`. No name is absolute, contains `..`, or is a symlink member. The set of names equals the task files under that one directory. No evidence-pack name appears.

**Fail.** Hash mismatch, a second top-level directory, or an excluded name.

**Remediation.** Discard that ZIP. Return to the failed step. Do not upload it.

## Step 14 — Local readiness is not acceptance

**Guidance.** `16-evidence-and-handoff/EVIDENCE.md`, `14-platform-review/STAGE-1.md`, `14-platform-review/STAGE-2.md`, `14-platform-review/ACCEPTANCE.md`.

**Archive claim.** `packaging-manifest.md` `record_status` may be `PASS` only when every step from 1 through 13 is `PASS` or `NOT APPLICABLE` with a written reason, and none of those steps is `FAIL`, `BLOCKED`, or `NOT VERIFIED`. A missing step is `NOT VERIFIED`.

**Open defects.** `C-CANARY`, `C-TIMEOUT`, `C-INTERNET`, `C-REUPLOADS`, `U-ZIP-ROOT`, `U-CTRF-FLAG`, and `U-HARBOR-PIN` stay `BLOCKED` until the conflict register or a receipt closes them. While any of those IDs is `BLOCKED`, `record_status` stays `BLOCKED`. A step that only records the defect can still be `PASS`. That step `PASS` does not raise the archive claim.

**Platform claim.** Stage 1 `PASSED STAGE 1`, Stage 2 `PASS`, QC, Super QC, and the six acceptance bullets stay `NOT VERIFIED` until a receipt is pasted into `stage1.txt`, `stage2.txt`, or `acceptance.txt`. Proposed targets in `complexity.md` are not observations. Local rewards are not platform verdicts. This file does not call the task ready to upload and does not call it accepted.

**Remediation.** Upload is a separate human action on an `ACTIVE` grant. One upload creates Version N of N and re-runs Stage 1. Identical bytes fail with `File hash already exists`.

## After `record_status` is `PASS`, any task-tree edit

Set `packaging-manifest.md` `record_status` to `NOT VERIFIED`. Set `sha256.txt` to `NOT VERIFIED`. Do not point a `PASS` at the old file.

| What changed | Also set back to `NOT VERIFIED` | Recheck before `record_status` may be `PASS` again |
| --- | --- | --- |
| `instruction.md`, tests, solution, fixtures, or either Dockerfile | `coverage.md` rows that changed, `oracle.txt`, `nop.txt`, naive-attempt lines, `checker-report.txt`, `rubric-review.md` if the contract or behavior changed | Steps 3–9, then 8, then 12–13 |
| `task.toml` only | `checker-report.txt` | Steps 4, 8, 12–13 |
| Evidence text outside the task directory | Nothing inside the ZIP, if the task bytes are unchanged | Record the note. Do not recompute a digest for a file you did not rebuild. If you rebuild anyway, the new digest replaces the old one. |

A status word edited to `PASS` without the command output for that step is not a pass.

## Folder coverage

Every directory in this system is listed. `NOT APPLICABLE` is a decision, not an omission.

| Folder | Purpose | ZIP step | Files | Class | Why, if not mandatory | Evidence |
| --- | --- | --- | --- | --- | --- | --- |
| `tb4-authoring-system/` | System root. Not part of the ZIP. | 11 | `README.md`, `AGENTS.md` | Mandatory | The root must stay outside the task directory. | Exclusion line in the manifest. |
| `00-source/` | Register, conflicts, gaps, page inventory, platform rule names. | 1, 9, 14 | `HOW-TO-READ.md`, `CONFLICT-REGISTER.md`, `UNRESOLVED.md`, `UNAVAILABLE-SOURCES.md`, `REGISTER.md`, `REGISTER.csv`, `INVENTORY.md`, `CONTRADICTIONS.md`, `PLATFORM-RULE-CATALOG.md` | Mandatory for the three reading files named in the steps; catalog is conditional | The catalog is opened only when a receipt names a rule. The whole register is not attached; the prefix map in `TRACEABILITY.md` names the rows. | `open_defects` and the pasted IDs for any failed step. |
| `01-taxonomy-and-batch/` | Category, subcategory, batch quotas. | 1 | `TAXONOMY.md`, `BATCH.md` | Conditional | Re-read only if `task.toml` category or subcategory is being checked against `selection.md`. Batch counts are not recomputed at zip time. | `selection.md` match line. `BATCH.md` is `NOT APPLICABLE` when `batch_context` is `missing` and no new batch claim is made. |
| `02-ideation/` | How the task was chosen. | 1 | `SELECTION.md`, `IDEATION.md` | Conditional | The choice already exists. Re-read `SELECTION.md` only to confirm the lock. Do not run ideation again. | `selection.md` present and unchanged. |
| `03-difficulty-and-horizon/` | What complexity is, and the three measurement blocks. | 9, 14 | `GENUINE-COMPLEXITY.md`, `DESIGN.md` | Mandatory | A local reward must not be written into the platform block while packing. | `complexity.md` blocks still separate. |
| `04-proposal/` | Proposal and grant rules. | 1 | `PROPOSAL.md` | Mandatory | | `grant_state` and frozen-scope line. |
| `05-instruction/` | Agent-facing contract. | 5 | `INSTRUCTION.md` | Mandatory | | `coverage.md`. |
| `06-harbor-task/` | Layout and metadata. | 2, 4 | `LAYOUT.md`, `METADATA.md` | Mandatory | | Manifest inventory and timeout fields. |
| `07-agent-environment/` | Agent image and dependencies. | 3, 6 | `ENVIRONMENT.md` | Mandatory | | Checker report. |
| `08-reference-solution/` | Oracle solution and ground truth. | 3, 7 | `SOLUTION.md` | Mandatory | | `oracle.txt` or `NOT VERIFIED`. |
| `09-verifier/` | Separate verifier and reward file. | 3, 6, 7 | `VERIFIER.md` | Mandatory | | `nop.txt` or `NOT VERIFIED`. |
| `10-checks-and-coverage/` | Static checks, rubric, coverage method. | 5, 8 | `STATIC-CHECKS.md`, `RUBRIC.md`, `COVERAGE.md` | Mandatory | | `checker-report.txt`, `rubric-review.md`, `coverage.md`. |
| `11-validation/` | Oracle, NOP, naive attempts, cheating. | 7, 9 | `VALIDATION.md` | Mandatory | | Local-measurement block. |
| `12-local-trials/` | Dry-run limits. | 14 | `TRIALS.md` | Conditional | Required if `dry-run.md` exists or a dry-run is claimed. `NOT APPLICABLE` if no dry-run is claimed and the field says so. | `dry-run.md` status, not a Stage 2 median. |
| `13-packaging/` | Membership, versions, checksums. | 10–13 | `ARCHIVE-MEMBERSHIP.md`, `PACKAGE.md` | Mandatory | | Manifest and `sha256.txt`. |
| `14-platform-review/` | Stage 1, Stage 2, acceptance. | 10, 14 | `STAGE-1.md`, `STAGE-2.md`, `ACCEPTANCE.md` | Conditional | `STAGE-1.md` is mandatory for the G01 description in step 10. `STAGE-2.md` and `ACCEPTANCE.md` are mandatory only so their results stay `NOT VERIFIED`. They are not run here. | Platform fields blank or receipt-backed. |
| `15-revision/` | What a later edit must recheck. | Invalidation section | `REVISION.md` | Conditional | `NOT APPLICABLE` if the tree does not change after the ready mark. Mandatory as soon as it does. | `revision-log.md`. |
| `16-evidence-and-handoff/` | Evidence destinations and readiness. | 14 | `EVIDENCE.md` | Mandatory | | Evidence files named in that file exist or are `NOT VERIFIED`. |
| `17-conversation-flow/` | Conversation and ZIP procedure. | All steps | `BUILD-ZIP.md`, `TRACEABILITY.md`, `REVIEW-BEFORE-PACKAGING.md`, `START-FRESH.md`, `ATTACHMENT-MANIFEST.md`, `CONTINUE-TASK.md` | Mandatory for this file and `TRACEABILITY.md`; the creation-flow files are conditional | Creation-flow files are re-read only when this ZIP work resumes a creation stage. | `handoff.md` names the step. |
| `material/` | Class rules for what may enter an image. | 3, 11 | `MATERIAL-CLASSES.md` | Mandatory | | Exclusion and image-contents lines. |
| `material/agent-visible/` | Skeletons for instruction, toml, environment. | 2 | `instruction.md`, `task.toml`, `environment/` | Conditional | Used only to replace a missing task file. `NOT APPLICABLE` when the task tree is already complete. | Inventory has no `REPLACE_ME`. |
| `material/agent-visible/environment/` | Skeleton agent Dockerfile. | 2 | `Dockerfile` | Conditional | Same reason as the parent. | Agent Dockerfile exists in the task tree. |
| `material/agent-visible/environment/data/` | Empty fixture placeholder. | 3 | `.gitkeep` | Conditional | `NOT APPLICABLE` when the task’s real fixtures are already in the task tree. Do not ship `.gitkeep` as data unless the instruction names no file inputs and the Dockerfile does not copy an empty mount as a fixture the agent must read. | Instruction paths exist in the task’s `environment/`. |
| `material/private-authoring/` | Evidence templates. Not in the ZIP. | 12 | The templates listed in `material/private-authoring/` | Mandatory as the source of blank records; the filled copies live in `evidence/<slug>/` | The folder itself must not be zipped. | Manifest exclusion. |
| `material/verifier-and-solution/` | Skeletons for solution and tests. | 2 | `solution/`, `tests/` | Conditional | Used only to replace a missing verifier-side file. | Task `solution/` and `tests/` exist and are not inside `environment/`. |
| `material/verifier-and-solution/solution/` | Skeleton `solve.sh` and `solve.py`. | 2 | `solve.sh`, `solve.py` | Conditional | Same reason. | Task `solution/solve.sh` exists. |
| `material/verifier-and-solution/tests/` | Skeleton verifier image and tests. | 2 | `Dockerfile`, `test.sh`, `test_outputs.py` | Conditional | Same reason. | Task `tests/test.sh` writes `/logs/verifier/reward.txt`. |
| `tools/` | Local checker, packager, register generator. | 8, 12, 13 | `check_task.py`, `package_task.py`, `README.md` | Mandatory | `check_proposal.py` is conditional: run it if `proposal.md` changed. `build_register.py` and `register_extra.py` are `NOT APPLICABLE`; they regenerate the system register, not the ZIP. | Checker stdout and packager stdout. |

## Traceability

Every register prefix has an owner in `TRACEABILITY.md`. The ZIP checkpoint for each prefix is the forward map in that file. A prefix is not dropped because this flow does not execute the platform.
