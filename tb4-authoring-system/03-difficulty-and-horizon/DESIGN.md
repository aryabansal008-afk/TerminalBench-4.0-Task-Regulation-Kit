# Legitimate difficulty and long horizon

SOP v3.0 Stage 2 predicates are the active numeric bars for rollout. Acceptance-page wording is still a different statistic (`C-DIFFICULTY`, `C-HORIZON`). Do not design to one page and call that compliance with the other. Keep proposed targets, local measurements, and platform verdicts in separate blocks.

| Bar | Where | What that page states | Status |
| --- | --- | --- | --- |
| Proposal “Difficult” | p.4 | Years of domain expertise, not volume. An average undergraduate finishing it in a few days is too easy. | Apply. Not part of the numeric conflict. |
| Proposal “Solvable” | p.4 | An expert who already knows the answer can implement it in a few hours. | Apply. |
| Stage 2 `difficulty` | p.14 | `count_true(full_credit_boolean) ≤ 4` on 8 rollouts. More than that and the task is too easy. | Active Stage 2 rule. Unresolved against the acceptance pass-rate sentence. |
| Acceptance pass rate | p.31 | ≤ 0.6, written “i.e 4/8”, 8 rollouts, timeout limit 8 hrs. Anonymous model “is GPT-6-Sol-xhigh performance.” | Unresolved against Stage 2. |
| Stage 2 `long_horizon` | p.14 | `median(assistant_message_count) > 35`. A median around 25 fails even when difficulty passes. | Active Stage 2 rule. Unresolved against the acceptance minimum. |
| Acceptance turns | p.31 | More than 35 turns of all passing runs. Table: Anonymous > 35 turns (TB4 ≈ 75). | Unresolved against Stage 2 median. |

Stage 2 uses one frozen policy. The screenshot records `effort high` and `K=8` as properties of that policy. The author does not set them. Both predicates are computed on the same 8 rollouts. Page 31 item 3 says tasks that fail both difficulty columns or both turn-count columns are rejected. The printed table has one model column (`C-MISSING-COLUMNS`). Do not invent the second column.

## What counts as difficulty

**Source.** Rubric C: hardness from real reasoning or engineering. Not obscure trivia, trick wording, or guess-the-format. Not a trivial one-liner or an obvious lookup. Not a public page the agent can copy. The proposal names the naive approach and why it fails. When difficulty is not met: add depth by more cross-source correlation, more state that must stay consistent, and stricter exactness in the output contract. Do not fix it by hiding information in the instruction.

When the median is too low, the task is hard but short. Add genuine work in sequence. Padding with busywork does not survive Stage 3.

Instruction length is not difficulty. The TB4 reference distribution is average 267 words and maximum 1406, counted in the way `content.split()` counts, with a hard cap of 1500.

## Construction and measurement

How to build the work: `GENUINE-COMPLEXITY.md`.

**Practice.** Keep three records apart in `evidence/<slug>/complexity.md`:

- Proposed targets are the qualitative bars and both written ceilings above. They are quotes. They are not results.
- Local measurements are Oracle, NOP, naive-attempt rewards, and the dry-run’s own model, reward, and assistant-message count. A local failure does not predict a platform fail. A local success in a handful of turns is a signal to strengthen the task. It is not a Stage 2 median.
- Platform verdicts are filled only from a Stage 2 receipt or an acceptance note that quotes numbers. The observed full-credit count and the observed median sit beside both written ceilings. Do not convert one ceiling into the other.

`difficulty_explanation` names the engineering constraint. It does not cite “≤4”, “4/8”, or “>35”, and it does not say a gate has been passed.
