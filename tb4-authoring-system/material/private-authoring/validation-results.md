# Validation results

One block per command. Paste stdout. Do not write a result the command did not print.

```
command: SUPPLY
status: NOT VERIFIED
exit: SUPPLY
```

```
stdout:
```

`status` is `NOT STARTED`, `IN PROGRESS`, `PASS`, `FAIL`, `BLOCKED`, `NOT VERIFIED`, or `NOT APPLICABLE`.

`harbor run` and `harbor check` stay `NOT VERIFIED` until a transcript is pasted. They are not installed by this system. `tools/check_task.py` and `tools/check_proposal.py` are the local commands. Their exit is `PASS` only when the saved stdout shows that exit. A rubric review is recorded in `rubric-review.md`, not as a substitute for this file.
