# Historical: previous 26-page freelancer PDF

This file is **not an active source**. It exists so superseded numbers can be audited without appearing in operational guidance, templates, or validators as current rules.

Active source: `Thanos _ Guidelines _ Onboarding SOP v3.0.pdf` (32 pages). Where the two disagree, SOP v3.0 wins. Internal SOP v3.0 contradictions stay in `CONFLICT-REGISTER.md`.

Identifier-level class lists: `REQUIREMENT-CLASSES.md`.

## Superseded values (do not apply)

| Topic | Previous PDF (retired) | SOP v3.0 (active) |
| --- | --- | --- |
| Stage 2 difficulty | `count_true(full_credit_boolean) ≤ 2` (at most 2 of 8 full credit) | `≤ 4` of 8 (`REQ-S2-003`). Acceptance-page wording remains a separate unresolved statistic (`C-DIFFICULTY`). |
| Stage 2 horizon | `median(assistant_message_count) > 80` | `> 35` (`REQ-S2-004`). Acceptance minimum over passing runs remains unresolved (`C-HORIZON`). |
| Agent timeout | Cap 18000 seconds | `[agent].timeout_sec = 28800` exactly. Do not copy that integer onto the verifier automatically (`C-TIMEOUT`). |
| Canary | No canary comment lines in files | Two-line Harbor canary in checked text files; missing markers are warnings, not blockers. |
| Canary upload field | `canary_string` at upload / Discord DM | No upload field. Grant links the ZIP (`C-CANARY` leftover text on pp. 26–27 is not an instruction to fill a field). |
| Decision path | Discord bot reaction plus DM | Platform proposal, verdict, grant (`C-DISCORD`). |
| Re-upload | “Re-upload freely” | Immutable Version N of N (`C-REUPLOAD-FREELY`). Budget is the limits table **7**, not leftover “3”. |
| Difficulty card | “Agent Trials” | Stage 2 predicates (`C-AGENT-TRIALS`). |
| Final review | QC alone | QC then Super QC (`C-QC-LAYERS`). Platform Stage 3 is qualitative acceptance with three verdicts, not a deferred empty tab. |

## How this file may be used

- Quote a retired number only to explain why a receipt or an old note is wrong.
- Do not copy a cell from the “Previous PDF” column into `task.toml`, `instruction.md`, a checker default, a test fixture that is expected to pass, or a conversation-flow prompt as the target.

`--canary-policy no-canary` on local tools is CLI compatibility. It does not restore the retired no-canary rule.
