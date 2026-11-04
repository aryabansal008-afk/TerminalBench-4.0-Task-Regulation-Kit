# Legitimate difficulty and long horizon

The PDF states more than one numeric bar. `C-DIFFICULTY` and `C-HORIZON` are unresolved. Do not design to the stricter figure and call that compliance with both pages. There is no provisional numeric target. Archive both written ceilings beside any observed result.

| Bar | Where | What that page states | Status |
| --- | --- | --- | --- |
| Proposal “Difficult” | p.3 | Years of domain expertise, not volume. An average undergraduate finishing it in a few days is too easy. | Apply. Not part of the numeric conflict. |
| Proposal “Solvable” | p.3 | An expert who already knows the answer can implement it in a few hours. | Apply. |
| Stage 2 `difficulty` | p.12 | `count_true(full_credit_boolean) ≤ 2` on 8 rollouts. More than that and the task is too easy. A median around 48 can still fail horizon. | Unresolved against the next row. |
| Acceptance pass rate | p.25 | ≤ 0.6, written “i.e 4/8”, 8 rollouts, timeout limit 8 hrs. Anonymous model “close to GPT-6-Sol-xhigh performance.” | Unresolved against the previous row. |
| Stage 2 `long_horizon` | p.12 | `median(assistant_message_count) > 80`. | Unresolved against the next row. |
| Acceptance turns | p.25 | More than 35 turns of all passing runs. Table: Anonymous > 35 turns, role=assistant. | Unresolved against the previous row. |

Stage 2 uses one frozen policy. The screenshot records `effort high` and `K=8` as properties of that policy. The author does not set them. Both predicates are computed on the same 8 rollouts. The PDF does not say those eight are the acceptance page’s eight. Page 25 item 3 says tasks that fail both difficulty columns or both turn-count columns are rejected. The printed table has one model column (`C-MISSING-COLUMNS`). Do not invent the second column.

## What counts as difficulty

**Source.** Rubric C: hardness from real reasoning or engineering. Not obscure trivia, trick wording, or guess-the-format. Not a trivial one-liner or an obvious lookup. Not a public page the agent can copy. The proposal names the naive approach and why it fails. Page 13, when difficulty is not met: add depth by more cross-source correlation, more state that must stay consistent, and stricter exactness in the output contract. Do not fix it by hiding information in the instruction.

When the median is too low, the task is hard but short. Add genuine work in sequence: more components that must all hold together, and more recovery and boundary conditions the agent has to discover and handle. Padding with busywork does not survive later review.

Instruction length is not difficulty. The TB4 reference distribution is average 267 words and maximum 1406, counted in the way `content.split()` counts, with a hard cap of 1500. Making the instruction longer risks that cap and the LLM-fingerprint rejection.

## Construction and measurement

How to build the work, which substitutes are not difficulty, and how to strengthen without hidden grading criteria: `GENUINE-COMPLEXITY.md`.

**Practice.** Keep three records apart in `evidence/<slug>/complexity.md`:

- Proposed targets are the qualitative bars and both written ceilings above. They are quotes. They are not results.
- Local measurements are Oracle, NOP, naive-attempt rewards, and the dry-run’s own model, reward, and assistant-message count. A local failure does not predict a platform fail. A local success in a handful of turns is a signal to strengthen the task. It is not a Stage 2 median.
- Platform verdicts are filled only from a Stage 2 receipt or an acceptance note that quotes numbers. The observed full-credit count and the observed median sit beside both written ceilings. Do not convert one ceiling into the other.

`difficulty_explanation` names the engineering constraint. It does not cite “≤2”, “4/8”, “>80”, or “>35”, and it does not say a gate has been passed.
