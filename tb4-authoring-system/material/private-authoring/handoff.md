# Handoff

What the next conversation must receive. This is not a reasoning transcript.

```
from_stage: SUPPLY
to_stage: SUPPLY
record_status: NOT STARTED
```

| Attached path | Status |
| --- | --- |
| SUPPLY | NOT STARTED |

Status is `NOT STARTED`, `IN PROGRESS`, `PASS`, `FAIL`, `BLOCKED`, `NOT VERIFIED`, or `NOT APPLICABLE`. `PASS` on a row means the file was attached and the next stage’s entry condition accepts it. It does not mean the task passed a platform gate.

Next checkpoint, copied from `17-conversation-flow/START-FRESH.md` or `17-conversation-flow/BUILD-ZIP.md`:

```
next_checkpoint: SUPPLY
unresolved_ids: SUPPLY
```
