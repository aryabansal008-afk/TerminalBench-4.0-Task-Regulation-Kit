# Revision log

Add a block after any edit that happens once `packaging-manifest.md` was `PASS`, and after any failed stage that changes the tree.

```
date: SUPPLY
changed_paths: SUPPLY
invalidated: SUPPLY
recheck_status: NOT VERIFIED
new_sha256: SUPPLY
```

`recheck_status` is `NOT STARTED`, `IN PROGRESS`, `PASS`, `FAIL`, `BLOCKED`, `NOT VERIFIED`, or `NOT APPLICABLE`. Name the evidence files set back to `NOT VERIFIED`, using the table in `17-conversation-flow/BUILD-ZIP.md`. Do not copy the previous hash into `new_sha256`. Leave it `SUPPLY` until `package_task.py` prints a new one.
