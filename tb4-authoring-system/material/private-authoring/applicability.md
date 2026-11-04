# Applicability decisions

One row per folder or requirement that is not mandatory for the current stage. A missing row is not `NOT APPLICABLE`.

```
stage: SUPPLY
```

| Item | Status | Reason | Evidence |
| --- | --- | --- | --- |
| `REQ-SUB-*` rows other than the chosen subcategory | NOT APPLICABLE | Only the chosen subcategory row applies. Name it. | `selection.md` |
| Folder or ID | NOT STARTED | Why it is conditional or not applicable. | File that will show the decision |

Status is `NOT STARTED`, `IN PROGRESS`, `PASS`, `FAIL`, `BLOCKED`, `NOT VERIFIED`, or `NOT APPLICABLE`. Use `NOT APPLICABLE` only with a reason. Use `BLOCKED` when an unresolved conflict stops the step. Do not use `PASS` for a folder that was not opened.
