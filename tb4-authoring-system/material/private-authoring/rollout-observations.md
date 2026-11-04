# Rollout observations

Platform Stage 2 only. Leave every observed field as `SUPPLY` and the status as `NOT VERIFIED` until `stage2.txt` is a pasted receipt.

```
record_status: NOT VERIFIED
model_label: SUPPLY
full_credit_count: SUPPLY
median_assistant_messages: SUPPLY
stage2_verdict: SUPPLY
```

Proposed targets, copied here so they are not mistaken for observations:

```
stage2_ceiling_quote: count_true(full_credit_boolean) ≤ 2 of 8
acceptance_pass_rate_quote: ≤ 0.6 i.e 4/8
stage2_horizon_quote: median(assistant_message_count) > 80
acceptance_turns_quote: more than 35 turns of all passing runs
numeric_pair: BLOCKED
```

`numeric_pair` stays `BLOCKED` while `C-DIFFICULTY` and `C-HORIZON` are unresolved. Do not write `PASS` on a ceiling. A local dry-run count is not `median_assistant_messages`.
