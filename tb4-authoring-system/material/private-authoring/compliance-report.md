# Compliance report

Task slug:
ZIP SHA-256:
Grant revision:
Canary decision:

## Gaps

| Requirement ID | Stage | Status | What is missing |
| --- | --- | --- | --- |
| SUPPLY | SUPPLY | NOT VERIFIED | A blank row is `NOT VERIFIED`, not `PASS`. |

## Platform receipts

| Stage | Outcome string | Rule or predicate | Observed value |
| --- | --- | --- | --- |
| Stage 1 |  |  |  |
| Stage 2 difficulty |  | Stage 2 prints `count_true(full_credit_boolean) ≤ 2`. Acceptance prints pass rate ≤ 0.6 “i.e 4/8”. Record both. `C-DIFFICULTY` is unresolved. |  |
| Stage 2 long_horizon |  | Stage 2 prints `median(assistant_message_count) > 80`. Acceptance prints more than 35 turns of all passing runs. Record both. `C-HORIZON` is unresolved. |  |

## Not claimed

- Stage 3, while deferred.
- Acceptance, until maintainer sign-off and the hacker–fixer loop are recorded.
- Batch quotas, unless `batch-slot.md` is attached.
