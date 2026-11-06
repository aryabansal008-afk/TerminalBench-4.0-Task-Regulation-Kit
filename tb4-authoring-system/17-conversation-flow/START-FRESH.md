# Start task creation in a fresh conversation

Use this file when no earlier chat exists. A new Grok conversation has no memory of this system. Attach the files in `ATTACHMENT-MANIFEST.md` for the stage you are starting. Paste that stage’s prompt below the attachments.

The agent chooses the task, category, subcategory, and programming language. It does not ask the user for them. It does not copy a taxonomy example into the task.

Do the stages in order. Do not start a stage whose entry condition is unmet. Private evidence goes in `evidence/<slug>/`. The task tree, once it exists, is `tasks/<slug>/`. Neither directory is a submission ZIP. Do not create either one inside `tb4-authoring-system/` or at the workspace root.

A stage does not advance, and this file does not call a task ready, while any check that stage lists as mandatory is `FAIL`, `BLOCKED`, or `NOT VERIFIED`. A missing check is `NOT VERIFIED`. `NOT APPLICABLE` counts only when `applicability.md` records the reason.

| Order | Stage | Prompt in this file | Advance only when |
| --- | --- | --- | --- |
| 1 | Ideation and category selection | Stage 1 | `selection.md` and the construction block of `complexity.md` exist |
| 2 | Proposal preparation | Stage 2 | `proposal.md` is under 2000 characters and `check_proposal.py` passes |
| 3 | Approval and grant | Stage 3 | The pasted receipt says the grant is `ACTIVE`, or the proposal must be revised |
| 4 | Implementation | Stage 4 | The task tree has no `REPLACE_ME` and matches the frozen problem statement |
| 5 | Validation | Stage 5 | `check_task.py` exit is 0, local Oracle is `1.0`, NOP is `0.0`, naive attempts are `0.0`, rubric rows are `PASS` or reasoned `NOT APPLICABLE`, and no mandatory check is `FAIL`, `BLOCKED`, or `NOT VERIFIED` |

Packaging is not this flow. After stage 5, use `REVIEW-BEFORE-PACKAGING.md`.

If the conversation is lost, switch to `CONTINUE-TASK.md` and reattach the evidence. Do not re-decide the category unless `15-revision/REVISION.md` says the change is a new task.

## Stage 1 — Ideation and category selection

**Purpose.** Explore the whole taxonomy, compare candidates, and record one category, subcategory, language, and task. Record how the work is hard without claiming a difficulty or long-horizon result.

**Entry.** No platform task exists. No granted proposal exists.

**Reading order.** `AGENTS.md`, `00-source/HOW-TO-READ.md`, `01-taxonomy-and-batch/TAXONOMY.md`, `01-taxonomy-and-batch/BATCH.md`, `02-ideation/SELECTION.md`, `02-ideation/IDEATION.md`, `03-difficulty-and-horizon/GENUINE-COMPLEXITY.md`, `03-difficulty-and-horizon/DESIGN.md`. Then the blank `material/private-authoring/selection.md` and `material/private-authoring/complexity.md`.

**Mandatory files.** The core bundle in `ATTACHMENT-MANIFEST.md`, plus `TAXONOMY.md`, `BATCH.md`, `SELECTION.md`, `IDEATION.md`, `GENUINE-COMPLEXITY.md`, `DESIGN.md`, and both blank templates.

**Conditional files.** A batch-owner count file, if one exists. If it does not, write `batch_context: missing`. Do not invent fractions. `00-source/CONFLICT-REGISTER.md` sections `C-ACCOUNT-LIMITS` and `C-DIFFICULTY` / `C-HORIZON` if the status index is not enough to quote them.

**Prior outputs.** None. If the user pastes a batch count, treat it as supplied context, not as an instruction to prefer a category.

**Requirement IDs.** `REQ-W-001`, `REQ-TX-001` through `REQ-TX-009`, `REQ-LM-005`, `REQ-LM-006`, `REQ-PR-005`, `REQ-PR-006`, `REQ-PR-007`, `REQ-PR-019`, `REQ-PR-021`. After a subcategory is chosen, the one `REQ-SUB-*` row for that subcategory. Do not attach every subcategory row.

**Checks before advancing.** `selection.md` names a listed subcategory, or a custom one with a sentence on why none fits. `programming_language` is filled. `batch_context` is `missing` or `supplied`. `complexity.md` names the proposal’s naive approach and at least one more, each tied to a requirement that will be stated in the instruction. Proposed-target block is quotes only. Local and platform blocks are empty. The file does not say the task is difficult or long-horizon.

**Outputs.** `evidence/<slug>/selection.md` and `evidence/<slug>/complexity.md`. No task tree yet. No platform submission.

**Failure.** If every candidate fails feasibility or realism, write that in `not_selected` and stop. Do not draft a proposal. If batch counts would break a printed quota, reject that candidate and select another that passes fit, feasibility, and novelty. Do not ask the user to pick.

**Next.** Stage 2 in a new message, or the next conversation via `CONTINUE-TASK.md`.

```
You are starting a Terminal-Bench 4 task in a fresh conversation. You have no earlier chat. The attached files are the whole record.

Read in the order given in tb4-authoring-system/17-conversation-flow/START-FRESH.md stage 1. Follow 02-ideation/SELECTION.md. Choose the task, category, subcategory, and programming language yourself. Do not ask me to choose them. Do not copy a taxonomy example.

Write evidence/<slug>/selection.md and evidence/<slug>/complexity.md outside tb4-authoring-system/. Fill the construction block and the proposed-target quotes. Leave local measurements and platform verdicts empty. Do not claim difficulty or long horizon. Do not create a task tree, a proposal, or a ZIP.

If a requirement ID listed for stage 1 was not attached, stop and name the missing ID. Do not invent it.
```

## Stage 2 — Proposal preparation

**Purpose.** Draft the five-field proposal from `selection.md`, under 2000 characters, in two or three paragraphs, with no headings and no step list.

**Entry.** Stage 1 outputs exist and the checks above passed. No grant exists yet.

**Reading order.** Core, then `04-proposal/PROPOSAL.md`, then `selection.md` and the construction block of `complexity.md`, then `material/private-authoring/proposal.md`.

**Mandatory files.** Core, `04-proposal/PROPOSAL.md`, the filled `selection.md`, the filled construction and proposed-target blocks of `complexity.md`, `material/private-authoring/proposal.md`.

**Conditional files.** `00-source/CONFLICT-REGISTER.md` section `C-EXPERT-TIME` when writing the expert-time field. `tools/check_proposal.py` is run locally; attach `tools/README.md` only if the runner is not already known.

**Prior outputs.** The stage 1 evidence files. The proposal must name the same task as `task_identity`.

**Requirement IDs.** `REQ-W-007`, `REQ-W-008`, `REQ-PR-001` through `REQ-PR-024`, `REQ-PR-032`, `REQ-PR-034`, `REQ-LM-006`.

**Checks before advancing.** `python3 tb4-authoring-system/tools/check_proposal.py evidence/<slug>/proposal.md` exits 0. Character count is under 2000. The six topics in `PROPOSAL.md` are present in prose. Category and subcategory match `selection.md`. Expert time is build time, and `complexity.md` says which quantity that is (`C-EXPERT-TIME`). The proposal does not say a difficulty gate has been passed.

**Outputs.** `evidence/<slug>/proposal.md` with the character count in the first line of `evidence/<slug>/proposal-count.txt`. Also `evidence/<slug>/proposal-form.md`, filled from `material/private-authoring/proposal-form.md`: title, where the task comes from, the larger problem, what solving it is worth, and the root and single-container checkboxes. Each of those three prose fields stays under 2048 bytes. The user submits this text on the platform. The agent does not invent a verdict.

**Failure.** If the checker fails, revise the draft. If the only way to explain the task is a heading outline or a step list, cut scope back to one objective. Do not submit.

**Next.** The user submits the proposal. Stage 3 starts only after the review receipt is pasted.

```
You are preparing the platform proposal. You have no memory beyond the attached files.

Draft the proposal only from the attached selection.md and the construction block of complexity.md. Follow 04-proposal/PROPOSAL.md. Five fields, under 2000 characters, two or three paragraphs, no headings, no step list. Do not change the category, subcategory, or task identity. Do not ask me to pick a new one.

Write evidence/<slug>/proposal.md and evidence/<slug>/proposal-count.txt. Do not submit it, do not build a task tree, and do not claim a grant. Stop if selection.md or complexity.md is missing.
```

## Stage 3 — Approval and grant

This conversation-flow stage is the **grant**. It is not platform Stage 3 qualitative review (`14-platform-review/STAGE-3.md`).

**Purpose.** Read the platform receipt. Proceed only if the grant is `ACTIVE`. Otherwise revise the proposal or stop.

**Entry.** `proposal.md` was submitted. The user pastes the receipt in this message. The agent cannot grant its own proposal.

**Reading order.** Core, `04-proposal/PROPOSAL.md` from the grant section downward, the receipt, then `proposal.md` and `selection.md`.

**Mandatory files.** Core, `04-proposal/PROPOSAL.md`, `evidence/<slug>/proposal.md`, `evidence/<slug>/selection.md`, and the pasted receipt saved as `evidence/<slug>/proposal-receipt.txt`.

**Conditional files.** `00-source/CONFLICT-REGISTER.md` section `C-LEGACY-CARDS` if the receipt uses the names Proposal Match, Agent Trials, Cheat Trial, or Harbor Analyze. Do not go looking for those buttons when the UI shows Stage 0–3.

**Prior outputs.** The submitted markdown. Compare it to the problem statement as reviewed.

**Requirement IDs.** `REQ-W-002`, `REQ-W-003`, `REQ-W-008`, `REQ-PR-024` through `REQ-PR-033`, `REQ-LM-006`.

**Checks before advancing.** The receipt is saved verbatim. If the grant is `ACTIVE`, `decision-log.md` records the revision id and that the frozen text is the problem statement as reviewed. If category on the receipt differs from `selection.md`, stop. Category cannot be repaired later (`REQ-LM-006`). If the UI showed a language control, record its label or `not shown` (`U-LANGUAGE-FIELD`). If the UI showed a quota, record it. If it showed nothing, write `account_quota: not visible`. Do not ask the user which category to switch to.

**Outputs.** `evidence/<slug>/proposal-receipt.txt` and a decision-log block for the grant. No task files.

**Failure.** `Reject` or `Uncertain`: status is `Proposal rejected — revise proposal`. Revise `proposal.md` against the final analysis and return to stage 2. Duplicate or novelty rejection: change the task semantically in `selection.md`, then stage 2. A surface rename is not a fix (`U-DUPLICATE-THRESHOLD`). Suspended or revoked grant: do not build.

**Next.** Stage 4 only when the grant is `ACTIVE` and the frozen problem statement is in the evidence pack.

```
You are at the grant checkpoint. You have no memory beyond the attached files. The receipt I pasted is the platform result. Do not invent a verdict.

Save the receipt as evidence/<slug>/proposal-receipt.txt. Compare the problem statement as reviewed with proposal.md and selection.md.

If the grant is not ACTIVE, do not build. Say which criterion failed and what must change in the proposal. If the grant is ACTIVE, record the revision and the frozen problem statement in decision-log.md. Do not create the Harbor tree in this turn.

Do not ask me to choose a category or a language. If the receipt’s category differs from selection.md, stop and say the lock in REQ-LM-006 prevents a quiet repair.
```

## Stage 4 — Implementation

**Purpose.** Build the Harbor tree for the frozen proposal: instruction, metadata, agent image, reference solution, and separate verifier.

**Entry.** Decision log says the grant is `ACTIVE`. `proposal-receipt.txt` contains the frozen problem statement. Stage 3 passed.

**Reading order.** Core, frozen problem statement, `selection.md`, `05-instruction/INSTRUCTION.md`, `06-harbor-task/LAYOUT.md`, `06-harbor-task/METADATA.md`, `07-agent-environment/ENVIRONMENT.md`, `08-reference-solution/SOLUTION.md`, `09-verifier/VERIFIER.md`, `13-packaging/ARCHIVE-MEMBERSHIP.md`, `material/MATERIAL-CLASSES.md`. Then the skeletons.

**Mandatory files.** Core, the files in that reading order, `material/agent-visible/instruction.md`, `material/agent-visible/task.toml`, `material/agent-visible/README.md`, `material/agent-visible/environment/Dockerfile`, `material/verifier-and-solution/solution/solve.sh`, `material/verifier-and-solution/solution/solve.py`, `material/verifier-and-solution/tests/Dockerfile`, `material/verifier-and-solution/tests/test.sh`, `material/verifier-and-solution/tests/test_outputs.py`.

**Conditional files.** `01-taxonomy-and-batch/TAXONOMY.md` only for the chosen subcategory if GPU training needs the single-H100 rule (`REQ-TX-006`). `00-source/CONFLICT-REGISTER.md` sections `C-CANARY`, `C-TIMEOUT`, and `C-INTERNET`. Do not attach the platform rule catalog unless a live rejection names a rule.

**Prior outputs.** Frozen problem statement, `selection.md`, construction block of `complexity.md`. The instruction’s graded conditions must match the frozen text. A material change is a new task, not a quiet edit.

**Requirement IDs.** `REQ-BD-001` through `REQ-BD-021`, `REQ-BD-026`, `REQ-PR-027`, `REQ-SC-check-task-slug`, `REQ-SC-check-task-fields`, `REQ-SC-check-task-timeout`, `REQ-SC-check-task-readme`, `REQ-SC-check-publication-name`, `REQ-SC-check-instruction-suffix`, `REQ-SC-check-allow-internet`, `REQ-SC-check-separate-verifier`, `REQ-SC-check-dockerfile-references`, `REQ-SC-check-dockerfile-sanity`, `REQ-SC-check-dockerfile-platform`, `REQ-SC-check-pip-pinning`, `REQ-SC-check-nproc`, `REQ-SC-check-task-absolute-path`. `REQ-BD-026` is the oracle entry `solution/solve.sh`. The oracle transcript that shows it ran is stage 5, not this stage.

**Checks before advancing.** No `REPLACE_ME`. Slug is at most three lowercase kebab tokens. `[task] name = "terminal-bench/<slug>"`. Task `README.md` has the four required headings. `artifacts` is top-level. `[verifier] environment_mode = "separate"`. Agent Dockerfile does not copy `tests/` or `solution/`. `[agent].timeout_sec` is 28800 and the suffix matches. `allow_internet` is not set false. §4.3 canary markers are present. Coverage rows exist for every graded sentence.

**Outputs.** `tasks/<slug>/`, assembled from the agent-visible and verifier skeletons. `evidence/<slug>/coverage.md`. Decision-log lines for `C-CANARY`, `C-TIMEOUT`, and `C-INTERNET`, each marked provisional where the conflict is unresolved.

**Failure.** If the frozen statement and the instruction disagree, stop and name the sentence. Do not “fix” the proposal locally. If the reference solution cannot finish inside 28800 seconds, reduce the work. Do not use an impossible timeout as difficulty. Do not change `[agent].timeout_sec` away from 28800.

**Next.** Stage 5. Do not package.

```
You are implementing the granted task. You have no memory beyond the attached files. The frozen problem statement in proposal-receipt.txt is the scope.

Build the task directory at tasks/<slug>/ from the attached skeletons. Follow the implementation files in START-FRESH.md stage 4, in that order. Keep tests and solution out of the agent image. Keep the SOP v3.0 canary placeholder; do not invent a third canary. Do not set allow_internet = false. [agent].timeout_sec is 28800 and the instruction suffix must match.

Write coverage.md in the evidence pack. Do not run packaging. Do not claim Oracle, NOP, difficulty, or long horizon. If the frozen statement is missing, stop.
```

## Stage 5 — Validation

**Purpose.** Run local static checks, the 30-criterion rubric, Oracle, NOP, and the naive attempts. Record measurements separately from proposed targets and from platform verdicts.

**Entry.** Stage 4 tree exists. Grant is still `ACTIVE`. The tree matches the frozen statement.

**Reading order.** Core, `10-checks-and-coverage/STATIC-CHECKS.md`, `10-checks-and-coverage/RUBRIC.md`, `10-checks-and-coverage/COVERAGE.md`, `11-validation/VALIDATION.md`, `12-local-trials/TRIALS.md`, `03-difficulty-and-horizon/GENUINE-COMPLEXITY.md`, then the task tree and `complexity.md`.

**Mandatory files.** Those procedure files, `tools/README.md`, the task tree, `coverage.md`, and `complexity.md`.

**Conditional files.** A local Harbor transcript, if the user has already run Oracle or NOP. The agent does not invent command output. `REQ-RB-01` through `REQ-RB-30` are the rubric; attach `RUBRIC.md` rather than pasting all thirty register rows unless a row is in dispute.

**Prior outputs.** The task tree and the evidence pack through stage 4.

**Requirement IDs.** `REQ-W-009`, `REQ-BD-022`, `REQ-BD-023`, `REQ-BD-024`, `REQ-BD-025`, `REQ-BD-026` for the oracle run of `solution/solve.sh`, `REQ-SC-000`, every `REQ-SC-check-*` row, `REQ-RB-01` through `REQ-RB-30`, `REQ-RB-LOCAL`, `REQ-S2-006` and `REQ-S2-007` only as the repair rules if a naive attempt or dry-run is too easy. They are not a claim that Stage 2 has run.

**Checks before advancing.** `tools/check_task.py` was run and the saved report shows exit 0. A missing report is `NOT VERIFIED`. Rubric rows are `PASS` or `NOT APPLICABLE` with a reason. A `FAIL` is fixed before the stage advances. Oracle reward token is `1.0`. NOP reward token is `0.0`. Each naive attempt named in `complexity.md` is `0.0`. A missing transcript is `NOT VERIFIED`, and the stage does not advance. Those numbers sit in the local-measurement block only. Platform-verdict fields stay blank. A dry-run, if performed, is recorded as local. A handful of local turns is a reason to strengthen the task, not a Stage 2 median.

**Outputs.** `evidence/<slug>/checker-report.txt`, `rubric-review.md`, `oracle.txt`, `nop.txt`, updated `complexity.md` local block, and `dry-run.md` if a dry-run was run. The user runs Harbor. If Harbor was not run, the agent writes `NOT VERIFIED` and does not invent a reward.

**Failure.** Oracle below `1.0`: fix the solution or the verifier, then re-run. NOP at `1.0` or a naive attempt at `1.0`: tighten tests only for a requirement the instruction already states, or add a page 15 constraint to the instruction and the coverage table together. Do not hide a field. Do not pad turns. If the frozen proposal’s graded conditions would change, stop and return to stage 2 as a new task.

**Next.** `REVIEW-BEFORE-PACKAGING.md`. Do not upload.

```
You are validating the task tree I attached. You have no memory beyond these files. Do not invent Harbor output. If oracle.txt or nop.txt is absent, write NOT VERIFIED in the local-measurement block and list the commands I must run. Do not advance while that status remains.

Follow 11-validation/VALIDATION.md, 10-checks-and-coverage/RUBRIC.md, and 03-difficulty-and-horizon/GENUINE-COMPLEXITY.md. Put Oracle, NOP, naive-attempt, and dry-run numbers only in the local-measurement block of complexity.md. Leave platform verdicts blank. Do not say the task passed Stage 2 or acceptance.

Do not package and do not upload. If a naive attempt scores 1.0, strengthen by a page 15 move that is also written into the instruction. Do not add a hidden test.
```

## Folder coverage

Every directory in `tb4-authoring-system/` is listed. A folder is not skipped because its job looks obvious. Conditional and `NOT APPLICABLE` rows are decisions, recorded in `evidence/<slug>/applicability.md`. Owners for every requirement prefix are in `TRACEABILITY.md`.

| Folder | Purpose | Stage | Files | Class | Why, if not mandatory | Evidence |
| --- | --- | --- | --- | --- | --- | --- |
| `tb4-authoring-system/` | Root of the authoring system. Not a task. | 1 | `README.md`, `AGENTS.md` | Mandatory | Later stages reattach `AGENTS.md` as core. | `handoff.md` lists it. |
| `00-source/` | How to read the PDF, the register, conflicts, and gaps. | 1, and any stage whose IDs are pasted | `HOW-TO-READ.md`, `CONFLICT-REGISTER.md`, `UNRESOLVED.md`, `UNAVAILABLE-SOURCES.md`, `REGISTER.md`, `REGISTER.csv`, `INVENTORY.md`, `REQUIREMENT-CLASSES.md`, `HISTORICAL-PREVIOUS-PDF.md`, `CONTRADICTIONS.md`, `PLATFORM-RULE-CATALOG.md` | Mandatory for `HOW-TO-READ.md` and `CONFLICT-REGISTER.md` | `REGISTER.md` is pasted by ID, not attached whole. `INVENTORY.md`, `REQUIREMENT-CLASSES.md`, and `HISTORICAL-PREVIOUS-PDF.md` are `NOT APPLICABLE` during creation unless a class or retired number is disputed. `PLATFORM-RULE-CATALOG.md` is `NOT APPLICABLE` until a receipt names a rule. `CONTRADICTIONS.md` only points at the conflict register. | Pasted IDs in the bundle. Catalog stays `NOT APPLICABLE` in `applicability.md`. |
| `01-taxonomy-and-batch/` | Full category and subcategory list, and batch quotas. | 1 | `TAXONOMY.md`, `BATCH.md` | Mandatory | | `selection.md` `batch_context`. |
| `02-ideation/` | Candidate comparison and the selection rules. | 1 | `IDEATION.md`, `SELECTION.md` | Mandatory | Not re-run at stages 2–5 unless `CONTINUE-TASK.md` finds no `selection.md`. | `selection.md`. |
| `03-difficulty-and-horizon/` | Genuine complexity and the unread ceilings. | 1 and 5 | `GENUINE-COMPLEXITY.md`, `DESIGN.md` | Mandatory | Stage 1 fills construction and quotes. Stage 5 fills local measurements only. | `complexity.md` three blocks. |
| `04-proposal/` | Proposal fields, review, grant. | 2 and 3 | `PROPOSAL.md` | Mandatory | `NOT APPLICABLE` at stage 1 because the proposal is not drafted yet. | `proposal.md`, then `proposal-receipt.txt`. |
| `05-instruction/` | Agent-facing contract. | 4 | `INSTRUCTION.md` | Mandatory | `NOT APPLICABLE` at stages 1–3. No instruction exists yet. | Task `instruction.md`, `coverage.md`. |
| `06-harbor-task/` | Layout and `task.toml`. | 4 | `LAYOUT.md`, `METADATA.md` | Mandatory | `NOT APPLICABLE` before the grant. | Task tree, checker later. |
| `07-agent-environment/` | Agent image, fixtures, pins. | 4 | `ENVIRONMENT.md` | Mandatory | `NOT APPLICABLE` before implementation. | Agent Dockerfile. |
| `08-reference-solution/` | Reference solution and ground truth. | 4 and 5 | `SOLUTION.md` | Mandatory | Oracle result is stage 5 and stays `NOT VERIFIED` until a transcript exists. | `solution/solve.sh`, `oracle.txt`. |
| `09-verifier/` | Separate verifier and rewards. | 4 and 5 | `VERIFIER.md` | Mandatory | NOP result is stage 5. | `tests/`, `nop.txt`. |
| `10-checks-and-coverage/` | Coverage method, static checks, rubric. | 4 for `COVERAGE.md`; 5 for the other two | `COVERAGE.md`, `STATIC-CHECKS.md`, `RUBRIC.md` | Mandatory at those stages | `STATIC-CHECKS.md` and `RUBRIC.md` are `NOT APPLICABLE` at stage 4 except as constraints already in the layout files. They are mandatory at stage 5. | `coverage.md`, `checker-report.txt`, `rubric-review.md`. |
| `11-validation/` | Oracle, NOP, naive attempts. | 5 | `VALIDATION.md` | Mandatory | `NOT APPLICABLE` before the tree exists. | Local block of `complexity.md`. |
| `12-local-trials/` | What a dry-run may prove. | 5 | `TRIALS.md` | Mandatory to read | The file is in the stage 5 reading order so a local count is not treated as Stage 2. Running a dry-run is conditional. If none was run, `dry-run.md` is `NOT APPLICABLE` with that reason. | `applicability.md` and `dry-run.md`. |
| `13-packaging/` | ZIP membership. Upload procedure is the other flow. | 4 | `ARCHIVE-MEMBERSHIP.md`, `PACKAGE.md` | Conditional | `ARCHIVE-MEMBERSHIP.md` is mandatory at stage 4 so the tree can exclude private files. `PACKAGE.md` is `NOT APPLICABLE` until `BUILD-ZIP.md`. | Task directory contains no evidence files. |
| `14-platform-review/` | Stage 1, Stage 2, Stage 3, acceptance. | 5 | `STAGE-1.md`, `STAGE-2.md`, `STAGE-3.md`, `ACCEPTANCE.md` | `NOT APPLICABLE` | No upload has happened. Repair rules `REQ-S2-006` and `REQ-S2-007` are read from `GENUINE-COMPLEXITY.md`, not as a Stage 2 verdict. Platform Stage 3 is not the grant step. | Platform block of `complexity.md` left blank. |
| `15-revision/` | Change impact after a failure or an edit. | Any failure | `REVISION.md` | Conditional | `NOT APPLICABLE` while the stage checks pass and nothing is edited. Mandatory when a stage fails or the frozen scope would change. | `revision-log.md`. |
| `16-evidence-and-handoff/` | Where records go, and the human gates. | Every stage | `EVIDENCE.md` | Mandatory | | The evidence file named by that stage exists or is `NOT STARTED`. |
| `17-conversation-flow/` | This sequence, attachments, resume, review, ZIP, traceability. | The stage being run | `START-FRESH.md`, `ATTACHMENT-MANIFEST.md`, `CONTINUE-TASK.md`, `REVIEW-BEFORE-PACKAGING.md`, `BUILD-ZIP.md`, `TRACEABILITY.md` | Mandatory for `START-FRESH.md` and `ATTACHMENT-MANIFEST.md` | `CONTINUE-TASK.md` is mandatory only when resuming. `REVIEW-BEFORE-PACKAGING.md` and `BUILD-ZIP.md` are `NOT APPLICABLE` until stage 5 has finished. `TRACEABILITY.md` is mandatory when an ID’s owner is unclear. | `handoff.md`. |
| `material/` | Which files the benchmark agent may see. | 4 | `MATERIAL-CLASSES.md` | Mandatory | `NOT APPLICABLE` before implementation. | Task tree assembled from the two skeleton trees. |
| `material/agent-visible/` | Instruction, toml, README, and agent image skeletons. | 4 | `instruction.md`, `task.toml`, `README.md`, `environment/` | Mandatory | Task README headings are required. This is not the authoring-system root README. | Copies live in the task directory, not in this folder. |
| `material/agent-visible/environment/` | Skeleton agent Dockerfile. | 4 | `Dockerfile` | Mandatory | | Task `environment/Dockerfile` does not copy `tests/` or `solution/`. |
| `material/agent-visible/environment/data/` | Placeholder so the fixture directory exists. | 4 | `.gitkeep` | Conditional | `NOT APPLICABLE` if the task has no file inputs and the Dockerfile does not copy `data/`. If it is copied, replace `.gitkeep` with real fixtures. | Instruction paths match files in the task tree. |
| `material/private-authoring/` | Blank records. Not submitted. | 1, then the stage that fills each template | Templates in that folder | Mandatory for `selection.md` and `complexity.md` at stage 1; each other template is mandatory at the stage `EVIDENCE.md` names it | A template not yet reached is `NOT STARTED`, not `PASS`. | Filled copy under `evidence/<slug>/`. |
| `material/verifier-and-solution/` | Solution and test skeletons. | 4 | `solution/`, `tests/` | Mandatory | Must not be copied into `environment/`. | Both directories exist in the task tree. |
| `material/verifier-and-solution/solution/` | Oracle entry skeletons. | 4 | `solve.sh`, `solve.py` | Mandatory | `solve.py` may stay unused only if `solve.sh` does not call it and the logic is short. Record that as `NOT APPLICABLE` for `solve.py`. | Task `solution/solve.sh`. |
| `material/verifier-and-solution/tests/` | Verifier skeletons. | 4 | `Dockerfile`, `test.sh`, `test_outputs.py` | Mandatory | | Task `tests/test.sh` writes the reward file. |
| `tools/` | Local preflight scripts. | 2 and 5 | `check_proposal.py`, `check_task.py`, `package_task.py`, `build_register.py`, `register_extra.py`, `README.md` | Conditional | `check_proposal.py` is mandatory at stage 2. `check_task.py` and `README.md` are mandatory at stage 5. `package_task.py` is `NOT APPLICABLE` until `BUILD-ZIP.md`. The register generators are `NOT APPLICABLE` to a task. | `proposal-count.txt` or checker stdout. Exit is not invented. |

## Traceability

`TRACEABILITY.md` maps every register prefix to a guidance file that exists, a creation checkpoint, a ZIP checkpoint, an artifact, and an evidence file. Stage prompts in this file name the IDs for that stage. An ID with no pasted row and no guidance file in the bundle is `BLOCKED` until it is attached. Do not mark it `PASS`.
