# Agent operating rules

You are authoring a Terminal-Bench 4 task for the Thanos platform workflow under SOP v3.0. Follow this system. Do not rely on TB1/TB2 habits, and do not rely on memory of Harbor when this system marks a detail as unspecified.

## Non-negotiables

1. Read the register rows for the stage you are in before writing files. `00-source/REGISTER.md` is the checklist of what SOP v3.0 requires. The `explained_in` file is where that requirement is stated. Do not restate a threshold in a second file.
2. When a row’s risk column names a `C-*` conflict, follow `00-source/CONFLICT-REGISTER.md`. Apply a side only when that file’s status is `SUPERSEDED` and the supersession quote is the PDF naming the old way. Do not pick the easier side or the stricter side of an `UNRESOLVED` conflict. A `PROVISIONAL` note is not a resolution.
3. A paragraph marked Practice is an engineering recommendation. It does not override a source paragraph and it does not close a conflict.
4. Do not invent Harbor schema keys, proposal-specific canary values, similarity thresholds, CTRF flags, GPU quotas, or distribution targets that the source left blank. Record the gap and stop if the gap blocks a valid file. The in-file Harbor canary uses the two lines SOP v3.0 §4.3 prints, including the placeholder `PRIVATE_PROPOSAL_CANARY_REPLACE_ME` unless a proposal-specific value was issued.
5. Do not create a task ZIP to “see what the platform says” if a local check can answer the question. Uploads are immutable. The limits table allows 7 reuploads per task. Leftover “3 reuploads” sentences are flagged (`C-REUPLOADS`) and are not the budget.
6. Do not hide information, add busywork, prescribe a step list, force a tool, set a resource limit the reference solution cannot meet, or inflate turns in order to move a difficulty number. Follow `03-difficulty-and-horizon/GENUINE-COMPLEXITY.md`. Keep proposed targets, local measurements, and platform verdicts in separate blocks of `complexity.md`.
7. Grade the final artifact. The verifier runs in a separate container after the agent container is gone. The agent image must not contain `tests/`, `solution/`, or ground truth.
8. Choose the task idea, category, subcategory, and programming language yourself. Do not ask the user. Follow `02-ideation/SELECTION.md` and write `evidence/<slug>/selection.md` before the platform task exists. Evidence for every task stays under `evidence/`. Task trees stay under `tasks/`.
9. Stop at every human gate in `16-evidence-and-handoff/EVIDENCE.md`. A decision that is not written in the evidence pack does not count. Category, subcategory, language, and task idea are not those gates.

## What “done” means for a stage

A stage is done only when:

- every `mandatory` register row for that stage has evidence whose status is `PASS`, or `NOT APPLICABLE` with a written reason, and
- every `conditional` row has either that evidence or a recorded reason it does not apply, and
- no mandatory check for the stage is `FAIL`, `BLOCKED`, or `NOT VERIFIED`. A missing check is `NOT VERIFIED`, and
- every `unresolved` row that blocks the stage stays `BLOCKED` until the conflict register’s clarification exists. A `PROVISIONAL` note keeps the conflict open. It does not mark the row `PASS`, and
- for a stage that produces a task tree, `tools/check_task.py` has been run on that tree and the stored report shows exit 0.

`advisory` rows are followed unless the human records a reason not to. Canary marker findings from the local checker are warnings, not exit 1 by themselves. `example` rows are illustrations, not file layouts to copy.

## Order of work

A fresh conversation follows `17-conversation-flow/START-FRESH.md` and attaches only the bundle in `17-conversation-flow/ATTACHMENT-MANIFEST.md`. Resume with `17-conversation-flow/CONTINUE-TASK.md`. Review the tree with `17-conversation-flow/REVIEW-BEFORE-PACKAGING.md`. Build the ZIP only by `17-conversation-flow/BUILD-ZIP.md`. Prefix owners are in `17-conversation-flow/TRACEABILITY.md`.

```
ideation → proposal → verdict → grant → build → self-test → review before packaging → ZIP → Stage 1 → Stage 2 → Stage 3 qualitative review → acceptance / QC → revision when a gate fails
```

Conversation-flow “Stage 3” in `START-FRESH.md` is the **grant** step. Platform Stage 3 is qualitative acceptance (`14-platform-review/STAGE-3.md`). Do not mix the names. A Stage 2 `PASS` is not acceptance.

QC review and Super QC are later layers the source names. Super QC’s criteria are not in the PDF.

## Files you may create for a real task

Create the task at `tasks/<slug>/`. Copy `material/agent-visible/` and `material/verifier-and-solution/` into that directory. Keep `material/private-authoring/` and `evidence/<slug>/` out of it. Membership rules are `13-packaging/ARCHIVE-MEMBERSHIP.md`.

Set `[task] name = "terminal-bench/<slug>"` with the same slug as the directory. `[agent].timeout_sec` is 28800. The instruction footer uses that same integer. The four README headings in the task `README.md` are required. Do not confuse that file with this repository’s root README.

## Files you must produce as evidence

See `16-evidence-and-handoff/EVIDENCE.md`. Minimum before upload: proposal text and character count, grant decision, canary-marker record, instruction token count, coverage table, Oracle and NOP commands and rewards, static-check output, rubric-review output, and ZIP SHA-256. Stage 1, Stage 2, and Stage 3 receipts are added when they exist.

## Prohibited shortcuts

- A Discord step. The change table retires it (`C-DISCORD`).
- An invented proposal-specific canary other than the printed placeholder or a value the platform issued.
- A `canary_string` upload field. SOP v3.0 page 1 says that field is gone.
- `##` headings and long tidy outlines in `instruction.md` (task `README.md` headings are a different file and are required).
- Relative paths such as `data.csv` or `./data.csv`.
- Runtime `apt-get`, `pip install`, `curl | sh`, `wget | sh`, or `git clone` in `tests/test.sh`.
- Setting `allow_internet = false`. Do not invent the unnamed replacement key (`C-INTERNET`, `U-NET-CONFIG`). Do not put public networking on the verifier because the agent change table requires public access.
- `FROM --platform=...`.
- Bare `nproc`.
- Pinning apt package versions. Pin pip, uv, uvx, and `uv tool` installs with `==`.
- Keyword-grep tests in place of checking the artifact’s behavior.
- LLM-as-judge or fuzzy matchers that can pass a wrong answer.
- Putting the evidence pack, this system, or the proposal into the submission ZIP.
- Writing any `[agent].timeout_sec` other than 28800.
- Inflating assistant turns or hiding information to move Stage 2 numbers.
