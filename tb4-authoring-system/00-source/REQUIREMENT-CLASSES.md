# Requirement classes (SOP v3.0 vs previous PDF)

Classification of register rows against the previous 26-page freelancer PDF. SOP v3.0 is authoritative. Internal v3.0 contradictions stay open in `CONFLICT-REGISTER.md`. This file does not invent a winner. Numeric cells from the previous PDF are tabulated in `HISTORICAL-PREVIOUS-PDF.md` and are not operational targets.

Each register row still carries: identifier, PDF page/section, applicable condition (requirement text), obligation, validation method (`compliance_check`), guidance file (`explained_in`), related implementation (evidence / tools named in the row), and unresolved contradiction (`contradiction_or_rejection_risk`).

## Explicitly superseded (previous PDF no longer active)

| Previous rule | Active SOP v3.0 replacement | Register / conflict |
| --- | --- | --- |
| No canary comment lines | Two-line Harbor canary in checked text files; missing = warning | `REQ-W-004`, `REQ-W-005`, `C-CANARY` |
| Stage 2 `count_true ≤ 2` | `count_true(full_credit_boolean) ≤ 4` | `REQ-S2-003`, `C-DIFFICULTY` |
| Stage 2 median `> 80` | `median(assistant_message_count) > 35` | `REQ-S2-004`, `C-HORIZON` |
| Agent timeout cap 18000 | `[agent].timeout_sec = 28800` exact | `REQ-SC-check-task-timeout`, `C-TIMEOUT` |
| Discord / canary DM as the decision path | Platform proposal, verdict, grant | `REQ-W-002`, `REQ-W-003`, `C-DISCORD` |
| Re-upload freely | Immutable Version N of N | `REQ-W-012`, `C-REUPLOAD-FREELY` |
| “Agent Trials” as the difficulty card | Stage 2 predicates | `REQ-W-011`, `C-AGENT-TRIALS` |
| QC alone as final review | QC then Super QC | `REQ-W-013`, `C-QC-LAYERS` |
| Stage 3 as `DEFERRED` with no criteria (previous reading) | Stage 3 qualitative acceptance with three verdicts | `REQ-S3-001`, `REQ-S3-002`, `REQ-UI-001` |

## Newly introduced in SOP v3.0

| Requirement | Source | Register |
| --- | --- | --- |
| Task `README.md` four exact headings | p.2 #6; pp. 20–21 | `REQ-SC-check-task-readme` |
| `[task] name = "terminal-bench/<slug>"` and ≤ 3 hyphen tokens | p.2 #10–11 | `REQ-SC-check-publication-name` |
| Exact agent timeout 28800 and footer 28800 | p.2; p.21 | `REQ-SC-check-task-timeout` (value), `REQ-BD-017` |
| Two-line canary (`GUID` then proposal placeholder) | pp. 8–9 | `REQ-W-004` |
| Wrapping ZIP or flat ZIP | p.2 #10; G01 | `REQ-G-004`, `U-ZIP-ROOT` |
| Stage 3 `ACCEPTED` / `REJECTED` / `COULD NOT COMPLETE` | pp. 15–16 | `REQ-S3-002` |
| Change-table public agent network | pp. 1–2 | `C-INTERNET` statement A; do not invent the replacement key |

## Unchanged (same obligation, new page numbers)

Proposal 2000-character cap (`REQ-PR-016`). Separate verifier (`REQ-BD-001`). Oracle 1.0 / NOP 0.0 (`REQ-BD-022`, `REQ-BD-023`). Named static checks other than README/publication/timeout-value (`REQ-SC-check-*` except the newly introduced rows). 30 rubric criteria (`REQ-RB-*`). I01, G01–G06, P04 (`REQ-G-*`, `REQ-PL-*`). Taxonomy 20% cap and deprioritized slices (`REQ-TX-*`, `REQ-SUB-*`). Absolute paths, no LLM headings in the instruction, industrial-not-contest (`REQ-BD-006`–`REQ-BD-011`).

## Internally contradictory inside SOP v3.0

Do not reconcile. Register obligation is `unresolved` where the row is the conflict itself; other rows cite the conflict id.

| Conflict | Register rows that carry it |
| --- | --- |
| `C-INTERNET` | `REQ-SC-check-allow-internet`, `REQ-G-005` |
| `C-REUPLOADS` leftover “3” | `REQ-LM-001`, `REQ-SC-REUPLOAD-SENTENCE` |
| `C-CANARY` leftover upload field / Discord | `REQ-W-004`, `REQ-LM-008` |
| `C-CANARY-FMT` GUID token | `REQ-W-004`, `U-CANARY-FORMAT` |
| `C-DIFFICULTY` / `C-HORIZON` | `REQ-S2-003`, `REQ-S2-004`, `REQ-AC-002`, `REQ-AC-003` |
| `C-TIMEOUT` 6-hour sentence | `REQ-SC-check-task-timeout` |
| `C-FOUR-CRITERIA` | `REQ-AC-012` |
| `C-MISSING-COLUMNS` | `REQ-AC-004` |
| `C-NINE-DIMENSIONS` / `C-LEGACY-CARDS` | `REQ-LM-008`, `REQ-UI-001` |
| `C-ACCOUNT-LIMITS` | `REQ-LM-002`, `REQ-LM-005` |
| `C-TB3-LABEL` | `REQ-G-005`, `REQ-TX-001` |

## Engineering recommendations that are not formal requirements

Obligation `advisory` or `example`. Do not treat them as blocking gates.

- `REQ-W-005` canary severity (warning, not blocker) — still put the markers.
- `REQ-BD-002` more than five files.
- `REQ-BD-004` solution split at ~20 lines.
- `REQ-PR-023` concreteness tip.
- `REQ-PR-034` Client-fit note (observed reviewer practice, not a seventh criterion).
- `REQ-TX-007` release-composition remarks (not quotas).
- `REQ-W-015`, `REQ-G-015`, `REQ-PR-033`, `REQ-UI-002`, `REQ-BD-003` screenshots and example trees.

Platform rows (`REQ-PL-*`, most `REQ-G-*`) are platform-enforced, not author-invented checks.
