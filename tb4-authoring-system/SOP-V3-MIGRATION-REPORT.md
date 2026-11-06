# SOP v3.0 migration report

In-place migration of `tb4-authoring-system/` from the 26-page freelancer PDF to `Thanos | Guidelines | Onboarding SOP v3.0` (32 pages). Architecture preserved: 17 lifecycle folders, registers, conflicts, templates, tools. No parallel v3 repo. No live upload. Harbor/Docker/platform execution: **NOT VERIFIED**.

## What is active

| Topic | SOP v3.0 rule in this system |
| --- | --- |
| Source | SOP v3.0 only. Previous PDF numbers: `00-source/HISTORICAL-PREVIOUS-PDF.md`. |
| Stage 2 difficulty | `count_true(full_credit_boolean) ≤ 4` |
| Stage 2 horizon | `median(assistant_message_count) > 35` |
| Agent timeout | `[agent].timeout_sec = 28800` exact; footer matches |
| Verifier timeout | Positive integer ≤ 28800; not auto-copied from the agent |
| Canary | Two-line Harbor markers in checked text files; missing = warning |
| Publication | `[task] name = "terminal-bench/<slug>"`; slug ≤ 3 hyphen tokens |
| Task README | Four exact headings (not the repo root README) |
| ZIP | `package_task.py --layout wrapped` (default) or `flat` |
| Reuploads | Limits table **7**; leftover “3” flagged (`C-REUPLOADS`) |
| Discord / `canary_string` upload | Not used (`C-DISCORD` superseded; leftover field text stays open) |
| Platform Stage 3 | Qualitative acceptance with three verdicts (`STAGE-3.md`) |
| Conversation Stage 3 | Grant checkpoint (`START-FRESH.md`) |

## What stayed unresolved (inside v3.0)

Do not treat these as closed: `C-INTERNET`, `C-CANARY` leftover upload/Discord text and GUID-token spelling, `C-TIMEOUT` 6-hour sentence / verifier exactness, `C-REUPLOADS` leftover “3”, `C-DIFFICULTY`, `C-HORIZON`, `C-MISSING-COLUMNS`, `C-ACCOUNT-LIMITS`, `C-FOUR-CRITERIA`, `C-LEGACY-CARDS`, `C-NINE-DIMENSIONS`, `C-TB3-LABEL`, `C-EXPERT-TIME` (toml meaning), `C-REWARD-LITERAL` (partial NOP). Gaps: `UNRESOLVED.md`, `UNAVAILABLE-SOURCES.md`.

## Tools

`tools/check_task.py`, `check_proposal.py`, `package_task.py` follow the table above. `--canary-policy` is CLI compatibility only. Regression: `python3 tools/test_sop_v3.py` (8 tests). Register: 335 rows, `REGISTER.md` synchronized with `REGISTER.csv`.

## Cursor prompts

Workspace root `prompt.md` is the two-stage Cursor guide (Part A creation, Part B ZIP). It matches this system. It does not claim platform compliance.

## Not verified

Docker image builds, `harbor run` / `harbor check`, live Stage 1–3, QC, Super QC, and upload. Do not invent those results.
