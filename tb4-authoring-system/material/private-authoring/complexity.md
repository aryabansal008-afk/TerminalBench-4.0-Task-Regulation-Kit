# Complexity record

Private evidence. Not a ZIP member. Do not write that the task is difficult or long-horizon anywhere in this file. Those words belong only to a platform verdict, after a receipt exists.

`record_status` is `NOT STARTED`, `IN PROGRESS`, `PASS`, `FAIL`, `BLOCKED`, `NOT VERIFIED`, or `NOT APPLICABLE`. Construction can be `IN PROGRESS` while local measurements and platform verdicts are `NOT VERIFIED`. Do not set the whole record to `PASS` from the proposed-target quotes.

```
record_status: NOT STARTED
```

## Preconditions

```
objective:
reference_solution:
inputs_complete:
verification:
```

`reference_solution` is `NOT VERIFIED` until Oracle has been run, then the reward token and the date. `inputs_complete` names any input that is still missing, or `yes`. `verification` is `outcome` only when tests grade the artifact and not the route. A missing run is `NOT VERIFIED`, not a pass.

## Construction

```
expertise:
interacting_constraints:
naive_approaches:
shortcut_check:
strengthening:
```

`naive_approaches` is one line each: the approach, the instruction sentence it fails, and the local reward once run (`NOT VERIFIED` until then). `strengthening` stays empty until a measurement or a receipt shows the task is too easy or too short. Name the page 15 move and the instruction sentence added with it.

The author’s private stage dependence, if it helps, stays here as `stages_private`. Do not copy it into `instruction.md`.

## Proposed targets

Quotes only. Not results. Numeric pair is unresolved. See `03-difficulty-and-horizon/DESIGN.md`.

```
difficult_qualitative: years of domain expertise, not volume; a few undergraduate days is too easy (p.3)
solvable_qualitative: an expert who knows the answer can implement it in a few hours (p.3)
stage2_difficulty_ceiling: count_true(full_credit_boolean) ≤ 4 of 8 (p.14) — unresolved against acceptance pass-rate wording
acceptance_pass_rate: ≤ 0.6, written “i.e 4/8” (p.31) — unresolved against Stage 2
stage2_horizon_ceiling: median(assistant_message_count) > 35 (p.14) — unresolved against acceptance minimum
acceptance_turns: more than 35 turns of all passing runs (p.31) — unresolved against Stage 2 median
```

## Local measurements

```
oracle:
nop:
dry_run_model:
dry_run_date:
dry_run_reward:
dry_run_assistant_messages:
```

Leave a field blank until that command has been run. Do not infer a platform median from one local transcript.

## Platform verdicts

```
stage2_full_credit_count:
stage2_median_assistant_messages:
stage2_verdict:
acceptance_numbers_quoted:
```

Leave these blank until the receipt exists. Do not copy the proposed-target ceilings into the observed fields.
