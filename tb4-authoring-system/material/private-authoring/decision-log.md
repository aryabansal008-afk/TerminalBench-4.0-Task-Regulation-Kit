# Decision log

One block per human gate. Do not delete superseded decisions; add a newer block.

```
id:
status: NOT STARTED
choice:
decided_by: SUPPLY
date: SUPPLY
receipt_or_reason:
```

`status` is one of `NOT STARTED`, `IN PROGRESS`, `PASS`, `FAIL`, `BLOCKED`, `NOT VERIFIED`, `NOT APPLICABLE`. An unresolved conflict is not `PASS`. A provisional choice stays `IN PROGRESS`. `decided_by` and `date` stay `SUPPLY` until a person writes them. Do not invent a name.

Category, subcategory, programming language, and the task idea are not gates for the user. They are the authoring agent’s record in `selection.md`.

Gates that need a block before packaging: `C-CANARY`, `C-ACCOUNT-LIMITS`. `U-LANGUAGE-FIELD` records the UI control’s label, or `not shown`, after the agent has already chosen the language.

`C-CANARY` leftover upload-field text stays open. In-file §4.3 markers are required. Do not invent a proposal-specific canary.

`C-REUPLOADS` workflow uses the limits table (7). Leftover “3” sentences are flagged. `C-DIFFICULTY`, `C-HORIZON`, `C-TIMEOUT`, and `C-INTERNET` are not decided by picking the stricter leftover sentence.
