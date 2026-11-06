# Pre-package review

Copy into `evidence/<slug>/pre-package-review.md`. Each status is `NOT STARTED`, `IN PROGRESS`, `PASS`, `FAIL`, `BLOCKED`, `NOT VERIFIED`, or `NOT APPLICABLE`. A missing row is `NOT VERIFIED`. Do not set the review to `PASS` while any row below is `FAIL`, `BLOCKED`, or `NOT VERIFIED`.

```
review_status: NOT STARTED
```

| Check | Status | Evidence |
| --- | --- | --- |
| Grant is `ACTIVE` and matches the instruction | NOT VERIFIED | `proposal-receipt.txt` |
| Category and language match `selection.md` | NOT VERIFIED | `selection.md` |
| §4.3 canary markers present (warnings allowed) | NOT VERIFIED | `checker-report.txt` |
| `[agent].timeout_sec` is 28800 and footer matches | NOT VERIFIED | `task.toml`, `instruction.md` |
| `[task] name` matches `terminal-bench/<slug>` | NOT VERIFIED | `task.toml` |
| Task README has the four required headings | NOT VERIFIED | `README.md` |
| Checker exit 0 on this tree | NOT VERIFIED | `checker-report.txt` |
| Coverage has no hidden test and no ungraded sentence | NOT VERIFIED | `coverage.md` |
| Oracle transcript reward `1.0` | NOT VERIFIED | `oracle.txt` |
| NOP transcript reward `0.0` | NOT VERIFIED | `nop.txt` |
| Each named naive attempt reward `0.0` | NOT VERIFIED | `complexity.md` local block |
| Rubric rows `PASS` or reasoned `NOT APPLICABLE` | NOT VERIFIED | `rubric-review.md` |
| No private evidence, credential, symlink, or `.git` in the task tree | NOT VERIFIED | directory listing |
| Platform verdicts left blank | NOT VERIFIED | `complexity.md` platform block |

`C-INTERNET` leftover contradictions stay recorded, not resolved. Canary missing/malformed is a warning, not a packaging blocker.
