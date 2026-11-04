# Human review, QC, and final acceptance

A platform Stage 2 `PASS` is not acceptance. Page 26: a task is accepted only once it clears the acceptance criteria and is merged following the pipeline — not upon submission and not upon passing static checks alone.

`C-FOUR-CRITERIA`: the heading says “all four criteria” and the page prints six bullets. The word “four” is undefined. Execute every bullet that is printed. Do not drop two because the heading says four.

## Printed pipeline

Each task must pass the full automated and human review pipeline defined in `TASK_REVIEW_AUTOMATION.md`. That file is not in the PDF (`U-AUTOMATION`). The printed bullets are the only local text:

1. Static checks — path validation, Dockerfile sanity, canary strings, metadata completeness, test-reference integrity. Canary strings here are `C-CANARY`. The other items match `10-checks-and-coverage/STATIC-CHECKS.md`.
2. Implementation rubric review — automated `harbor check` against the task-implementation rubric. The 30 criteria are in `10-checks-and-coverage/RUBRIC.md`. Arguments to `harbor check` are not given.
3. Docker / Oracle / No-op validation — the environment builds, the oracle passes, the no-op fails.
4. Maintainer review — sign-off once all automated gates are green.
5. Agent and cheat trials — live agent trials plus adversarial cheat trials probing for reward hacking.
6. Hacker–fixer loop — iterative hardening until an adversarial agent can no longer exploit the verifier.

## QC and Super QC

**Source.** The change table says final review is QC review and then Super QC, a second expert layer (`C-QC-LAYERS`, superseded by addition). Super QC’s criteria are not in the PDF (`U-SUPER-QC`). Do not invent the checklist. Do not skip the layer. The evidence pack is what a second reviewer needs in order to re-grade the rubric without hunting.

Stage 3 in the UI is `Qualitative checks` and is marked `DEFERRED`. Do not call a deferred tab a QC pass, and do not equate Stage 3 with Super QC or with the 9 Quality Dimensions (`C-LEGACY-CARDS`, `C-NINE-DIMENSIONS`).

## Numbers that are not settled by Stage 2

The acceptance page states 8 rollouts, pass rate ≤ 0.6 “i.e 4/8”, more than 35 assistant turns on all passing runs, and a timeout limit of 8 hours, on an anonymous model close to GPT-6-Sol-xhigh. Archive those sentences beside the Stage 2 observations. Item 3 on page 25 refers to difficulty columns and turn-count columns the PDF does not print (`C-MISSING-COLUMNS`). Do not self-reject or self-accept on an imagined second column.

## Exit

**Practice.** Maintainer sign-off, cheat-trial notes, and a Stage 2 pass, all pointing at the same SHA-256. QC and Super QC recorded when they happen. The author does not mark the task merged.
