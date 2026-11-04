# Packaging manifest

Private. Not a member of the ZIP. Fields marked `SUPPLY` are filled from command output or the UI. Do not invent a hash, a version, or an upload result.

```
record_status: NOT STARTED
grant_state: NOT VERIFIED
frozen_statement_match: NOT VERIFIED
timeout_agent: SUPPLY
timeout_verifier: SUPPLY
suffix_n: SUPPLY
category: SUPPLY
subcategory: SUPPLY
canary_policy: SUPPLY
agent_image_contains: SUPPLY
verifier_image_contains: SUPPLY
open_defects: SUPPLY
version: SUPPLY
sha256: SUPPLY
uploaded: NOT STARTED
```

`record_status` is `NOT STARTED`, `IN PROGRESS`, `PASS`, `FAIL`, `BLOCKED`, `NOT VERIFIED`, or `NOT APPLICABLE`. It may be `PASS` only when `17-conversation-flow/BUILD-ZIP.md` steps 1–13 are `PASS` or reasoned `NOT APPLICABLE` and `open_defects` contains no `BLOCKED` or `NOT VERIFIED` id. While an unresolved conflict remains, `record_status` stays `BLOCKED`. `uploaded` stays `NOT STARTED` until the platform shows a generation. Stage 1 and Stage 2 stay `NOT VERIFIED` on this form. A `PASS` here is not acceptance.

## extraction

Paste the stdout of the zipfile listing command in `17-conversation-flow/BUILD-ZIP.md` step 13.

```
extraction_status: NOT VERIFIED
stdout:
```
