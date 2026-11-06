# Local tools

These scripts approximate the checks SOP v3.0 states in text. They do not run Harbor, Oracle, NOP, or the platform.

| Script | What it does |
| --- | --- |
| `check_proposal.py` | Character count under 2000, two or three paragraphs, no headings, no `REPLACE_ME`, no steering phrases. |
| `check_task.py` | Slug, Harbor canary markers (advisory), task README headings, `[task] name`, metadata, agent timeout 28800, suffix, absolute paths, Docker limits, verifier shape, reward path. |
| `package_task.py` | Runs the task preflight, then writes a ZIP (`--layout wrapped` or `flat`) with a fixed member timestamp and prints SHA-256. Does not upload. |
| `build_register.py` | Rewrites `00-source/REGISTER.md` and `REGISTER.csv` from the generators and `00-source/PLATFORM-RULE-CATALOG.md`. |

`--canary-policy` is accepted for CLI compatibility. It does not restore the retired no-canary rule. Missing or malformed canary markers are warnings (`TB4.CANARY_MISSING` / `TB4.CANARY_FORMAT`), not blocking failures. `--canary-string` is only an optional issued proposal-canary value for the second marker line. It is not an upload field.

`[agent].timeout_sec` must be exactly 28800. `[verifier].timeout_sec` must be a positive integer at most 28800; the exact-28800 rule does not apply to the verifier.

Exit 0 is one preflight. It is not the full static-check table, not G06, and not a readiness claim.

Regenerating the register overwrites hand edits to `00-source/REGISTER.md` and `REGISTER.csv`. Change `build_register.py`, `register_extra.py`, or `00-source/PLATFORM-RULE-CATALOG.md`, then run `build_register.py`. The scripts are authoring tools. They are not members of a submission ZIP.
