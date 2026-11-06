# Source map

Source PDF: `Thanos _ Guidelines _ Onboarding SOP v3.0.pdf`.
Document title: Thanos | Guidelines | Onboarding SOP v3.0. Opening body title: Terminal Bench 4 (TB 4) — Task Proposal & Submission Guide for Trainers / Annotators.
Producer metadata: Google Docs renderer. 32 pages. Dated in file metadata 2026-11-06.

The previous 26-page `Freelancers _ Thanos _ Guidelines.pdf` is historical only. It is not an active source. Where the two disagree, SOP v3.0 wins. Where SOP v3.0 disagrees with itself, `CONFLICT-REGISTER.md` records both sides.

The PDF says it is one of a three-document set, then contains all three documents in one file:

| Document named on p.1 | Where it actually is |
| --- | --- |
| 1. Proposal & Submission Guide | pp. 1–18, including Stage 3 |
| 2. TB4 — Static Checks Reference | pp. 19–21 |
| 3. TB4 — Rubric Review Reference | pp. 23–25 |

Two further layers are in the same PDF and are not part of that three-document list:

| Layer | Pages | What it governs |
| --- | --- | --- |
| Thanos batch taxonomy | pp. 28–30 | Categories, subcategories, 20% batch cap |
| Acceptance criteria | pp. 31–32 | Acceptance difficulty/horizon wording and the printed pipeline |

Page 22 is empty in the text layer (image). Pages 12, 17, and 18 are mostly screenshots or a short checklist.

Screenshots: pp. 5, 6, 12, 13, 15, 17. Their UI text is not fully in the text layer. Rule IDs in `PLATFORM-RULE-CATALOG.md` mix v3 prose (`TB4.CANARY_*`) with older screenshot labels (`TB3.*`). Severity badges are still `U-SEVERITY-ALIGNMENT`.

## Strata

Use these names in the register. They are extraction labels, not PDF bookmarks.

| Stratum | Pages | How to treat it |
| --- | --- | --- |
| A. Current platform workflow | 1–18 | Proposal, build, Stage 1–3. Opening: no Discord step; no `canary_string` upload field; in-file canary markers required. |
| B. Static checks | 19–21 | Mechanical law, including README headings, exact agent timeout 28800, advisory canary format. |
| C. Rubric | 23–25 | 30 criteria. Close sentence protects 7 reuploads. |
| D. Limits and leftover checklist | 26–27 | Limits table 7 reuploads. Troubleshooting still has Discord, `canary_string`, Proposal Match, Agent Trials, 9 Quality Dimensions, and “You hit 3 versions.” |
| E. Batch taxonomy and acceptance | 28–32 | Procurement on top of the platform. |

## Page index (SOP v3.0)

| Page | Section | Notes |
| --- | --- | --- |
| 1 | Opening; document set; start of TB3 → TB4 change table | No Discord. No `canary_string` at upload. Canary markers required in files (§4.3). Stage 3 accepts the task. Agent internet: public (change table). |
| 2 | Change table continued | README four headings become required. Agent timeout exactly 28800 becomes required. `[task] name = "terminal-bench/<slug>"`. Slug ≤ 3 components. Canary row: warning, not blocker. GPU: schema/capability, not canonical-name list. |
| 3 | Canary severity note; 9-step journey; start of Step 1 | Journey step 4 includes canary markers. Step 9 is Stage 3. |
| 4 | §3.1 six criteria; §3.2 five form fields | Verifiable, well-specified, solvable, difficult, interesting, outcome-verified. |
| 5 | Form screenshot; §3.3 proposal content; start of §3.4 | Under 2000 characters. Two or three paragraphs. |
| 6 | Verdict; §3.5 grant; start of §3.6 | ACTIVE grant freezes text. |
| 7 | Revise; §4 separate verifier; start of example tree | Example: “Canary on line 1.” |
| 8 | Example tree; §4.2 construction; start of §4.3 canary | `content.split()` ≤ 1500. Align with Terminal-Bench 4. Two-line canary with `GUID`. |
| 9 | Rest of canary; §4.4 rules people miss; Oracle/NOP table | Comment syntax by file type. Skip `environment/data/` and binaries. Footer N = `[agent].timeout_sec`. |
| 10 | §4.6 self-test; §5 upload; start of §5.1 gates | I01, G01–G03. G02 still says agent networking is non-public. |
| 11 | G04–G06, P04; severity; §5.2 outcomes | REQUIRED / OPTIONAL / ADVISORY / IF APPLICABLE. |
| 12 | Clean Stage 1 screenshot | Image. |
| 13 | Rejected Stage 1; §5.3 re-upload | One fully green version. Partial credit across versions does not count. |
| 14 | §6 Stage 2 | `count_true(full_credit_boolean) ≤ 4`. `median(assistant_message_count) > 35`. K=8. |
| 15 | Stage 2 screenshot; §6.3 FAIL repair; start of §7 Stage 3 | Do not hide information. Do not pad. Stage 2 PASS does not accept. |
| 16 | Stage 3 attributions and three verdicts | `ACCEPTED` / `REJECTED` / `COULD NOT COMPLETE`. |
| 17 | Stage 3 screenshot | Image. |
| 18 | Pre-upload checklist | Canary in listed text files. Metadata. Oracle 1.0 / NOP 0.0. |
| 19 | Static Checks Reference opening and first checks | Mentions missing canary. First seven named checks. |
| 20 | Remaining named checks; leftover “three reuploads”; metadata hard blocks | Cap 28800s with leftover 6-hour CI sentence. `check-allow-internet`. README headings listed. |
| 21 | README headings; timeout/footer 28800; advisory canary format (no `GUID` word); pre-upload checklist | C-CANARY-FMT against p.8. |
| 22 | (empty text layer) | Image or blank. |
| 23–25 | Rubric groups A–E, 30 criteria | Close: protects 7 reuploads. |
| 26 | Limits table; troubleshooting | Table: 7 reuploads, submissions 1, hourly 2, daily 5, creation 2. Nearby prose: 7. Troubleshooting: leftover 3 versions, `canary_string`, Proposal Match. |
| 27 | File-hash error; final checklist | Discord DMs; canary in every file; `canary_string` at upload; 9 Quality Dimensions. |
| 28–30 | Taxonomy | Official taxonomy of Terminal Bench 3. 20% cap. Deprioritized Science / Operations / Media. Note: rough numbers out of 66. |
| 31 | Acceptance criteria | Pass rate ≤ 0.6 i.e. 4/8. Minimum 35 turns of all passing runs. `TASK_REVIEW_AUTOMATION.md`. |
| 32 | Pipeline close | Hacker–fixer loop. “all four criteria” vs six bullets. |

## Requirement classes relative to the previous PDF

| Class | Meaning | Examples |
| --- | --- | --- |
| Superseded | Previous-PDF rule replaced by SOP v3.0 | No-canary policy; Stage 2 `≤ 2` and median `> 80`; agent timeout cap 18000; Stage 3 as `DEFERRED` with no criteria |
| Newly introduced | Stated in v3.0 and not an active previous-PDF rule | Task README four headings; `[task] name = "terminal-bench/<slug>"`; exact agent timeout 28800; two-line Harbor canary format; Stage 3 verdicts; public agent-network change-table row |
| Unchanged | Same obligation, possibly new page number | Proposal 2000-character cap; separate verifier; Oracle 1.0 / NOP 0.0; 30 rubric criteria; G01–G06 + P04; taxonomy 20% cap |
| Internally contradictory | Two v3.0 statements stand | `C-INTERNET`, leftover `C-REUPLOADS` “3”, `C-CANARY` upload field vs p.1, `C-CANARY-FMT` GUID token, `C-DIFFICULTY`, `C-HORIZON`, `C-TIMEOUT` 6-hour sentence, `C-FOUR-CRITERIA`, `C-MISSING-COLUMNS`, `C-NINE-DIMENSIONS`, `C-LEGACY-CARDS`, `C-ACCOUNT-LIMITS` |
| Practice | Engineering method, not a source rule | Three-block complexity record; wrapping ZIP as default; shebang-then-canary in scripts |

Do not treat a Practice paragraph as closing a contradiction.

Identifier-level lists: `REQUIREMENT-CLASSES.md`. Retired previous-PDF numbers: `HISTORICAL-PREVIOUS-PDF.md` (not an active source).

## Old-PDF → v3.0 page shift (historical)

Use only to read older notes. Do not cite the old PDF as current.

| Old 26-page range | SOP v3.0 range |
| --- | --- |
| 1–2 opening / change table | 1–3 |
| 3–5 proposal | 4–6 |
| 6–8 build | 7–10 |
| 8–11 Stage 1 | 10–13 |
| 12–13 Stage 2 | 14–15 |
| (absent / deferred Stage 3) | 15–17 |
| 13–14 checklist | 18 |
| 15–16 static checks | 19–21 |
| 17–19 rubric | 23–25 |
| 20–21 limits | 26–27 |
| 22–24 taxonomy | 28–30 |
| 25–26 acceptance | 31–32 |

## External documents named but not included

Canonical list: `UNAVAILABLE-SOURCES.md`.

| Name | Where named | Status |
| --- | --- | --- |
| Terms of Use / Clickwrap Agreement | PDF outline, page target `-1` | Not in the PDF body. |
| `TASK_REVIEW_AUTOMATION.md` | p.31 | Not in the PDF. The six bullets under that sentence are the only local specification. |
| “Taxonomies tab” | p.31 | Taxonomy table is pp. 28–30 of this PDF. |
| “github” hyperlink text | pp. 28–29 | No URL in the text layer. |
| Pinned Harbor version | p.10 G02 | Identifier not given. |
| Supported network configuration key | pp. 1–2 | Named, not specified (`U-NET-CONFIG`). |
| Onboarding HR / integrity SOP | Not in this PDF | `U-ADMIN-POLICY`. |

## Task-level vs batch-level vs platform-controlled

| Kind | Who enforces it | Examples |
| --- | --- | --- |
| Task-level | Author, then platform checks on that ZIP | Instruction, verifier, metadata, README, canary markers, Oracle/NOP, one task’s difficulty |
| Batch-level | Whoever delivers the round | No category above 20%. One task per deprioritized subcategory. |
| Account-level | Platform limits table | 7 reuploads per task, hourly 2, daily 5, creation limit, total submissions |
| Platform-controlled | The platform, not the author | I01, G01–G06, P04, Stage 2 eight frozen-policy rollouts, Stage 3 qualitative review, grant suspend/revoke |
