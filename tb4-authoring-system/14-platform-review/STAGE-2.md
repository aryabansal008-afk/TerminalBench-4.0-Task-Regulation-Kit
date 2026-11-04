# Stage 2 predicates

You do not drive Stage 2. You read it. It starts only after Stage 1 is accepted. “Agent Trials” as the difficulty card is the old way (`C-AGENT-TRIALS`). Read difficulty and long horizon from these predicates.

## What the platform runs

- 8 rollouts against the evaluation model, under a frozen policy. Policy key, digest, capacity profile, and retention profile are recorded.
- The UI label is `Anonymous model`, with `effort high` and `K=8` as policy properties, not author settings.
- Flow: `QUEUED → PREPARING → RUNNING → COLLECTING → CLOSING → COMPLETE`.
- It may sit at `Stage 2 running · waiting on provider`.
- Each slot becomes a terminal attempt record. The tab shows `8 of 8 reconciled`, plus graded results, unclosed attempts, and retry attempts.

## Predicates

Both must hold on a Stage 2 pass. The header names the one that failed, for example `Failed on long_horizon`.

| Predicate | Rule as printed on page 12 | Fail means |
| --- | --- | --- |
| `difficulty` | `count_true(full_credit_boolean) ≤ 2` | More than 2 of 8 earned full credit. The task is too easy. |
| `long_horizon` | `median(assistant_message_count) > 80` | The median trajectory is too short. About 48 fails even if difficulty passed. |

Overall verdict: `PASS` or `FAIL`. If the run is blocked, the screenshot shows `INDETERMINATE` and “population incomplete.” An indeterminate run is not a difficulty failure. The example blocker is `RUNNER_EXECUTION_FAILED`, cleared by platform on-call. Do not press `Stop` while a provider attempt is active. The source says the missing trustworthy grade makes the run noncanonical rather than retryable.

A Stage 2 `PASS` is not an acceptance result. The acceptance page states pass rate ≤ 0.6 “i.e 4/8” and more than 35 turns of all passing runs. `C-DIFFICULTY` and `C-HORIZON` do not let either page replace the other. Archive the observed full-credit count and the observed median beside both written ceilings.

## When the verdict is FAIL

Read the ceilings in `03-difficulty-and-horizon/DESIGN.md` and strengthen under `03-difficulty-and-horizon/GENUINE-COMPLEXITY.md`. Then rebuild, re-run local checks, Oracle, NOP, and the naive attempts. Upload a new version only after the revalidation list in `15-revision/REVISION.md`. A change aimed at one predicate usually moves the other. Re-check both. Put the new receipt in the platform-verdict block. Do not hide information. Do not pad. Do not describe the redesign as a passed gate.

Download trajectories when a human is allowed to. They show whether failures are hardness or ambiguity. They are evidence, not ZIP members.
