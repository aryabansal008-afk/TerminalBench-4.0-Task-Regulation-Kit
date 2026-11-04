# Agent operating rules

You are authoring a Terminal-Bench 4 task for the Thanos platform workflow. Follow this system. Do not rely on TB1/TB2 habits, and do not rely on memory of Harbor when this system marks a detail as unspecified.

## Non-negotiables

1. Read the register rows for the stage you are in before writing files. `00-source/REGISTER.md` is the checklist of what the PDF requires. The `explained_in` file is where that requirement is stated. Do not restate a threshold in a second file.
2. When a row’s risk column names a `C-*` conflict, follow `00-source/CONFLICT-REGISTER.md`. Apply a side only when that file’s status is `SUPERSEDED` and the supersession quote is the PDF naming the old way. Do not pick the easier side or the stricter side of an `UNRESOLVED` conflict. A `PROVISIONAL` note is not a resolution.
3. A paragraph marked Practice is an engineering recommendation. It does not override a source paragraph and it does not close a conflict.
4. Do not invent Harbor schema keys, canary strings, similarity thresholds, CTRF flags, GPU quotas, or distribution targets that the source left blank. Record the gap and stop if the gap blocks a valid file.
5. Do not create a task ZIP to “see what the platform says” if a local check can answer the question. Uploads are immutable. How many are allowed is `C-REUPLOADS` and is unresolved.
6. Do not hide information, add busywork, prescribe a step list, force a tool, set a resource limit the reference solution cannot meet, or inflate turns in order to move a difficulty number. Follow `03-difficulty-and-horizon/GENUINE-COMPLEXITY.md`. Do not claim difficulty or long horizon because the task sounds complex. Keep proposed targets, local measurements, and platform verdicts in separate blocks of `complexity.md`.
7. Grade the final artifact. The verifier runs in a separate container after the agent container is gone. The agent image must not contain `tests/`, `solution/`, or ground truth.
8. Choose the task idea, category, subcategory, and programming language yourself. Do not ask the user. Follow `02-ideation/SELECTION.md` and write `evidence/<slug>/selection.md` before the platform task exists. Do not copy a taxonomy example into the task, and do not prefer a category the files do not name. Evidence for every task stays under `evidence/`. Task trees stay under `tasks/`.
9. Stop at every human gate in `16-evidence-and-handoff/EVIDENCE.md`. A decision that is not written in the evidence pack does not count. Category, subcategory, language, and task idea are not those gates.

## What “done” means for a stage

A stage is done only when:

- every `mandatory` register row for that stage has evidence whose status is `PASS`, or `NOT APPLICABLE` with a written reason, and
- every `conditional` row has either that evidence or a recorded reason it does not apply, and
- no mandatory check for the stage is `FAIL`, `BLOCKED`, or `NOT VERIFIED`. A missing check is `NOT VERIFIED`, and
- every `unresolved` row that blocks the stage stays `BLOCKED` until the conflict register’s clarification exists. A `PROVISIONAL` note keeps the conflict open. It does not mark the row `PASS`, and
- for a stage that produces a task tree, `tools/check_task.py` has been run on that tree and the stored report shows exit 0.

`advisory` rows are followed unless the human records a reason not to. `example` rows are illustrations, not file layouts to copy.

## Order of work

A fresh conversation follows `17-conversation-flow/START-FRESH.md` and attaches only the bundle in `17-conversation-flow/ATTACHMENT-MANIFEST.md`. Resume with `17-conversation-flow/CONTINUE-TASK.md`. Review the tree with `17-conversation-flow/REVIEW-BEFORE-PACKAGING.md`. Build the ZIP only by `17-conversation-flow/BUILD-ZIP.md`. Prefix owners are in `17-conversation-flow/TRACEABILITY.md`.

```
ideation → proposal → verdict → grant → build → self-test → review before packaging → ZIP → Stage 1 → Stage 2 → acceptance / QC → revision when a gate fails
```

Stage 3 in the platform UI is labeled `Stage 3 • Qualitative checks` and `DEFERRED`. Do not wait on it and do not mark it passed. QC review and Super QC are later layers the source names. Super QC’s criteria are not in the PDF.

## Files you may create for a real task

Create the task at `tasks/<slug>/`. Copy `material/agent-visible/` and `material/verifier-and-solution/` into that directory. Keep `material/private-authoring/` and `evidence/<slug>/` out of it. Membership rules are `13-packaging/ARCHIVE-MEMBERSHIP.md`.

## Files you must produce as evidence

See `16-evidence-and-handoff/EVIDENCE.md`. Minimum before upload: proposal text and character count, grant decision, provisional canary decision, instruction token count, coverage table, Oracle and NOP commands and rewards, static-check output, rubric-review output, and ZIP SHA-256. Stage 1 and Stage 2 receipts are added when they exist.

## Prohibited shortcuts

- A Discord step. The change table retires it (`C-DISCORD`).
- An invented canary string. The PDF says nothing issues one (`C-CANARY`). Omitting a canary is not established as safe.
- `##` headings and long tidy outlines in `instruction.md`.
- Relative paths such as `data.csv` or `./data.csv`.
- Runtime `apt-get`, `pip install`, `curl | sh`, `wget | sh`, or `git clone` in `tests/test.sh`.
- Setting `allow_internet = false` as a guess at “non-public” networking (`C-INTERNET`).
- `FROM --platform=...`.
- Bare `nproc`.
- Pinning apt package versions. Pin pip, uv, uvx, and `uv tool` installs with `==`.
- Keyword-grep tests in place of checking the artifact’s behavior.
- LLM-as-judge or fuzzy matchers that can pass a wrong answer.
- Putting the evidence pack, this system, or the proposal into the submission ZIP.
