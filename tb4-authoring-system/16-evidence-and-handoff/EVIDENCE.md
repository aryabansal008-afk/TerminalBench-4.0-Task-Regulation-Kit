# Evidence, handoffs, and submission readiness

Private evidence is not a ZIP member. All evidence packs live in one store, `evidence/`, with one directory per task at `evidence/<slug>/`. All task trees live in one store, `tasks/`, at `tasks/<slug>/`. A finished ZIP sits beside that tree as `tasks/<slug>.zip` and is not a member of the tree. Both stores are siblings of `tb4-authoring-system/`, not inside it. The ZIP and the evidence pack refer to the same SHA-256.

A new conversation does not inherit this pack. `17-conversation-flow/START-FRESH.md` is the creation sequence. `17-conversation-flow/ATTACHMENT-MANIFEST.md` is what to attach. `17-conversation-flow/CONTINUE-TASK.md` resumes from the files below. `17-conversation-flow/REVIEW-BEFORE-PACKAGING.md` is the gate before a ZIP. `17-conversation-flow/BUILD-ZIP.md` is the ZIP procedure. `17-conversation-flow/TRACEABILITY.md` names the owner of each requirement prefix. Blank records start in `material/private-authoring/`.

## Records

| Artifact | Shows |
| --- | --- |
| `selection.md` | Category, subcategory, language, task identity, and the short rationale. Start from `material/private-authoring/selection.md`. Written before the platform task exists. Not a reasoning transcript. |
| `decision-log.md` | Every remaining human gate. Start from `material/private-authoring/decision-log.md`. |
| `proposal.md` | Exact submitted markdown and character count. No headings in this file. |
| `proposal-form.md` | Answers for every proposal form: title, the markdown pointer, where the task comes from, the larger problem, what solving it is worth, and the root and single-container checkboxes. Start from `material/private-authoring/proposal-form.md`. |
| `proposal-record.md` | Status of the proposal check and the grant. Not the text submitted on the form. |
| `proposal-receipt.txt` | Revision, review run, generation, verdicts, final analysis, problem statement as reviewed, grant state. |
| `batch-slot.md` | Category, subcategory, and the batch fraction. |
| `coverage.md` | Instruction condition, path, test, negative, ground-truth derivation. |
| `checker-report.txt` | `tools/check_task.py` stdout for the tree that was zipped. |
| `rubric-review.md` | 30 criteria, each PASS or FAIL, with a justification. |
| `oracle.txt` | Command, exit, reward token. |
| `nop.txt` | Command, exit, reward token. |
| `complexity.md` | Preconditions, naive approaches, and three separated blocks: proposed targets, local measurements, platform verdicts. Start from `material/private-authoring/complexity.md`. |
| `dry-run.md` | Model, date, reward, and assistant-message count of the local run. Those numbers are local measurements, not a platform verdict. |
| `cheat-trials.md` | Each adversarial attempt and the verifier result. |
| `sha256.txt` | Digest of the ZIP that was uploaded. |
| `stage1.txt` | Outcome string, blocking rule, warnings, elapsed. |
| `stage2.txt` | Platform verdict only: both observed predicates, the verdict string, population, policy digest. The written ceilings stay in the proposed-target block of `complexity.md` and are not rewritten as observations. |
| `acceptance.txt` | Maintainer, QC, Super QC, as they happen. |
| `applicability.md` | Folder and subcategory decisions that are conditional or `NOT APPLICABLE`, each with a reason. |
| `requirement-coverage.md` | Register IDs for this task, with a status. A missing row is not `PASS`. |
| `review-findings.md` | Findings before packaging. Distinct from a Harbor transcript. |
| `pre-package-review.md` | One status per review check. Start from `material/private-authoring/pre-package-review.md`. |
| `validation-results.md` | Command name, status, and pasted output. |
| `rollout-observations.md` | Stage 2 numbers only after a receipt. Otherwise `NOT VERIFIED`. |
| `packaging-manifest.md` | ZIP inventory, hash, version, and local-ready status. |
| `revision-log.md` | Edits after a ready mark, and which evidence was invalidated. |
| `handoff.md` | Stage, files attached, and the next checkpoint. |
| `task-specification.md` | Private spec. Not `instruction.md` and not a ZIP member. |

A register row is unmet if the artifact named on that row is missing. Do not backfill a reward or a verdict from memory.

## Human gates

The authoring agent stops and records a decision before continuing. A decision names the ID, the choice, the date, and who decided. Copy it into the task’s `decision-log.md`.

| Gate | When | What to record |
| --- | --- | --- |
| `C-CANARY` | Before the first ZIP | Which PDF statement this upload is following. Mark it `PROVISIONAL`. Do not invent a canary string. The conflict stays open until a Stage 1 receipt shows whether a `TB3.CANARY_*` rule fired. |
| `C-ACCOUNT-LIMITS` | Before creating a platform task, and again before a second one | The quota the live UI shows, or `not visible`. The table says total submissions 1 and task creation limit 2. Neither cell is repealed. Do not ask the user to pick a category or a task because the quota is unresolved. |
| `U-LANGUAGE-FIELD` | When the creation form is on screen | The label of the language control, or `not shown`. The language itself was already chosen in `selection.md`. Do not ask the user which language to use. |
| `C-REUPLOADS` | Before a version numbered 4, 5, 6, or 7 | The live counter. Do not record “the prose wins” or “the table wins.” |
| Material proposal change | After an `ACTIVE` grant | New task, not a quiet edit, if inputs, outcome, or graded conditions move. |
| `C-INTERNET` | Before claiming G02 networking is satisfied, and again if `TB3.AGENT_NETWORK_NONPUBLIC` fires | The receipt text. Do not set `allow_internet = false` to mean “non-public.” |
| `U-SCHEMA` | When Harbor rejects an unknown or missing key | The key name from the rejection. |
| `C-TIMEOUT` | When an integer is written to `timeout_sec` | That the integer is provisional. The suffix matches it. 18000 is not recorded as the resolved timeout, and 8 hours is not copied in as if the cap were repealed. |
| Stage 2 `Stop` | Any time someone wants to press Stop | Do not press it while a provider attempt is active. |

`C-DIFFICULTY` and `C-HORIZON` do not have a numeric choice to record. Record both ceilings and the observed values.

## Platform journey

**Source.** The page 2 journey is eight steps: (1) proposal with title, category, subcategory, expert time, and markdown; (2) Proposal Review Bot plus duplicate and novelty checks; (3) `ACTIVE` grant only if accepted and not a duplicate, text frozen; (4) build locally with a separate verifier, and the journey text says “no canary lines”; (5) self-test static checks, rubric, Oracle pass, NOP fail; (6) upload one ZIP, `G01–G06` and `P04` as one job; (7) re-upload until the status reads `PASSED STAGE 1`; (8) Stage 2 rollouts on a frozen policy decide `PASS` or `FAIL`. The whole workflow lives on the platform. There is no Discord step.

Step 4’s “no canary lines” is one side of `C-CANARY`. It is not a closed rule. Evidence still has to appear in this order. A later artifact does not predate the grant it depends on.

## Handoff between authoring stages

The authoring agent may receive only the stage it is in, plus the register rows for that stage, plus the conflict register when a row names a `C-*` id. It does not receive permission to open the next stage.

| From | To | The handoff must include |
| --- | --- | --- |
| Ideation | Proposal | `selection.md` and the construction block of `complexity.md`, including at least two naive approaches tied to stated requirements. Proposed targets are quotes. Local and platform blocks are empty. No task-tree files yet. |
| Proposal | Build | Grant state `ACTIVE`, the frozen problem statement, character count. |
| Build | Self-test | Task tree assembled from `material/agent-visible/` and `material/verifier-and-solution/`. Private notes stay outside it. |
| Self-test | Package | Checker report, 30 rubric rows, Oracle `1.0`, NOP `0.0`, coverage table, provisional canary record. |
| Package | Stage 1 | SHA-256, version number, confirmation the grant is `ACTIVE`. |
| Stage 1 | Stage 2 | `PASSED STAGE 1` or `READY_FOR_STAGE2` for that digest. |
| Stage 2 | Acceptance | Observed full-credit count, observed median, both written ceilings, same digest. |
| Any failure | Revision | The blocking id or header, the impact note, then the revalidation list. |

## Readiness

Readiness is a claim with a named list of mandatory checks. The claim stays `BLOCKED` or `NOT VERIFIED` while any check on that list is `FAIL`, `BLOCKED`, or `NOT VERIFIED`. A missing check is `NOT VERIFIED`. `NOT APPLICABLE` is allowed only with a written reason. A rubric row is not an execution result. A local reward is not a platform verdict. This system does not mark a task accepted.

The upload claim uses the list below. Each line is mandatory for that claim.

- The grant is `ACTIVE` and the instruction’s graded conditions still match the frozen problem statement. A missing receipt is `NOT VERIFIED`.
- `selection.md` exists and was written before the platform task. Category and programming language in the created task match it.
- `C-CANARY` and `C-ACCOUNT-LIMITS` have decision-log blocks. The canary block is `BLOCKED` and marked provisional. It is not `PASS`. `U-LANGUAGE-FIELD` records the control label, or `not shown`.
- `tools/check_task.py` exit on this tree is 0. A missing report is `NOT VERIFIED`.
- The coverage table has no ungraded instruction condition and no hidden test.
- Local Oracle reward is `1.0` and local NOP reward is `0.0`, each from a pasted transcript.
- The 30 rubric criteria are `PASS` or reasoned `NOT APPLICABLE`. A `FAIL` is fixed, not relabeled.
- The ZIP excludes everything in the exclude list of `13-packaging/ARCHIVE-MEMBERSHIP.md`, and step 13 of `17-conversation-flow/BUILD-ZIP.md` has a pasted listing whose hash matches the packager.
- The version number is not 4, 5, 6, or 7 unless the live reupload counter is quoted. Inside that range with no quoted counter, `C-REUPLOADS` stays `BLOCKED`.

Unresolved conflicts that the claim depends on, including `C-CANARY`, `C-TIMEOUT`, `C-INTERNET`, `C-REUPLOADS`, `U-ZIP-ROOT`, `U-CTRF-FLAG`, and `U-HARBOR-PIN`, stay `BLOCKED`. While any of them is `BLOCKED`, the upload claim is `BLOCKED`. Executable checks that passed keep their own `PASS`. They do not promote the claim.

The acceptance claim stays `NOT VERIFIED` until Stage 1 and Stage 2 receipts exist for that same digest and each of the six printed acceptance bullets is `PASS` or an explicit unresolved ID still marked `BLOCKED`. A `BLOCKED` bullet keeps the acceptance claim `BLOCKED`. The author does not mark the task merged. QC and Super QC are recorded when they happen. Stage 3 stays unread while it says `DEFERRED`.
