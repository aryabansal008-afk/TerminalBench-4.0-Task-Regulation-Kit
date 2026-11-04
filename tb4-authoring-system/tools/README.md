# Local tools

These scripts approximate the checks the PDF states in text. They do not run Harbor, Oracle, NOP, or the platform.

| Script | What it does |
| --- | --- |
| `check_proposal.py` | Character count under 2000, two or three paragraphs, no headings, no `REPLACE_ME`, no steering phrases. |
| `check_task.py` | Slug, canary policy, metadata, timeouts, suffix, absolute paths, Docker limits, verifier shape, reward path. Requires `--canary-policy no-canary` or `--canary-policy required`. |
| `package_task.py` | Runs the task preflight, then writes one top-level directory into a ZIP and prints SHA-256. Does not upload. |
| `build_register.py` | Rewrites `00-source/REGISTER.md` and `REGISTER.csv` from the generators and `00-source/PLATFORM-RULE-CATALOG.md`. |

`check_task.py` exits 2 if `--canary-policy` is omitted. Passing `no-canary` or `required` records a provisional choice. It does not resolve `C-CANARY`. `required` needs `--canary-string` from the platform. The script will not invent one. Exit 0 is one preflight. It is not the full static-check table, not G06, and not a readiness claim.

Regenerating the register overwrites hand edits to `00-source/REGISTER.md` and `REGISTER.csv`. Change `build_register.py`, `register_extra.py`, or `00-source/PLATFORM-RULE-CATALOG.md`, then run `build_register.py`. The scripts are authoring tools. They are not members of a submission ZIP.
