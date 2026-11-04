# Source map

Source PDF: `Freelancers _ Thanos _ Guidelines.pdf`.
Document title inside the PDF: Terminal Bench 4 (TB 4) — Task Proposal & Submission Guide for Trainers / Annotators.
Producer metadata: Google Docs renderer. 26 pages. Outline entries exist only for the acceptance section; the earlier headings are body text, not PDF bookmarks.

The PDF says it is one of a three-document set, then contains all three documents in one file:

| Document named on p.1 | Where it actually is |
| --- | --- |
| 1. Proposal & Submission Guide | pp. 1–14, with limits and a legacy checklist on pp. 20–21 |
| 2. TB4 — Static Checks Reference | pp. 15–16 |
| 3. TB4 — Rubric Review Reference | pp. 17–19 |

Two further layers are in the same PDF and are not part of that three-document list:

| Layer | Pages | What it governs |
| --- | --- | --- |
| Thanos batch taxonomy | pp. 22–24 | Which categories and subcategories this round collects, and the 20% batch cap |
| Acceptance criteria | pp. 25–26 | Client acceptance: difficulty numbers, horizon numbers, and the review pipeline |

Screenshots on pp. 2, 4, 5, 6, 10, 11, and 13 are images. Their UI text is not in the PDF text layer. Rule IDs in `PLATFORM-RULE-CATALOG.md` were read from those screenshots. Severity badges could not be reliably aligned to rows, so severities are not asserted unless the prose or the rule name states them.

## Strata

Use these names in the register. They are extraction labels, not headings in the PDF.

| Stratum | Pages | How to treat it |
| --- | --- | --- |
| A. Current platform workflow | 1–14, plus the UI screenshots | Procedure text and screenshots. Page 1 states there is no Discord step. Canary sentences inside these pages still conflict with each other and with later pages. See the conflict register. Do not treat this stratum label as a repeal. |
| B. Static checks | 15–16 | Mechanical law. The introductory sentence mentions a missing canary; the check table does not contain a canary check. |
| C. Rubric | 17–19 | Quality law for the local LLM review and the platform quality review. |
| D. Limits and the page 20–21 checklist | 20–21 | The limits table prints reupload, submission, and creation cells. The troubleshooting rows and the final checklist still describe Discord, canaries, Proposal Match, Agent Trials, and 9 Quality Dimensions. Those rows are not marked old except where the change table names them. |
| E. Batch taxonomy and acceptance | 22–26 | Procurement requirements on top of the platform. They bind this round even when the platform page does not repeat them. |

## Page index

| Page | Section | Notes |
| --- | --- | --- |
| 1 | Opening, document set, start of “What changed from TB1/TB2 → TB4” | Page 1 asserts no Discord step, no canary, and no `canary_string`. Discord is superseded by the change table. The canary assertion conflicts with later current-chapter text. Gates G01–G06 and publication barrier P04. |
| 2 | Rest of the change table. “The TB4 journey at a glance” steps 1–8. Dashboard screenshot. | Screenshot columns include Blocking reason, S0/S1/S2 style status, `+ NEW PROPOSAL`, `Upload ZIP`. |
| 3 | Step 1 proposal. §3.1 six reviewer criteria. §3.2 five form fields. | Acceptance requires correct, solvable, verifiable, well-specified, and hard for an interesting reason. |
| 4 | Form screenshot. §3.3 proposal content. §3.4 verdicts Accept, Uncertain. | Hard cap: under 2000 characters. Form target: two or three paragraphs. |
| 5 | Reject. §3.5 grant. §3.6 revise. Accepted-proposal screenshot. | Grant freezes proposal text. Status string `Proposal rejected — revise proposal`. |
| 6 | §4 Step 2 structure. Example tree. Rejected-proposal screenshot. | Opening sentence still says “with your canary in hand”. Example comment says “Canary on line 1”. Both conflict with p.1. |
| 7 | Rest of the example tree. §4.2 construction requirements. Start of §4.3. | Word-count method `content.split()` ≤ 1500. Absolute paths. No exam-style tasks. |
| 8 | Rest of §4.3. §4.4 Oracle/NOP. §4.5 self-test. Start of §5 upload. | Separate verifier. Metadata fields. Canary bullet that conflicts with p.1. |
| 9 | §5.1 gates I01, G01–G06, P04. Severity classes. Start of §5.2. | `PASSED STAGE 1` and `READY_FOR_STAGE2`. |
| 10 | Rest of §5.2. Clean Stage 1 screenshot. | Blocking-reason example `G05.ORACLE.REWARD_BELOW_FULL`. Retry examples `G05.HARBOR.UNKNOWN_EXCEPTION`, `G04.PROFILE.ACCELERATOR_UNSUPPORTED`. |
| 11 | Rejected Stage 1 screenshot. §5.3 re-upload. | One version must be entirely green. Partial credit across versions does not count. |
| 12 | §6 Stage 2. Predicates. | `count_true(full_credit_boolean) ≤ 2`. `median(assistant_message_count) > 80`. 8 rollouts. |
| 13 | Stage 2 screenshot. §6.3 how to fix a FAIL. §7 checklist start. | Do not hide information. Do not pad. Screenshot repeats the two predicates and `Anonymous model`, `effort high`, `K=8`, `policy FROZEN`. |
| 14 | Rest of §7 checklist. | Dry-run on a free/open-source agent. |
| 15 | Static Checks Reference, first seven checks. | Intro mentions “a missing canary”; the table does not. |
| 16 | Remaining static checks. | `timeout_sec` cap 18000. Exact instruction suffix. “three reuploads”. |
| 17–19 | Rubric groups A–E, 30 criteria. | “protects your 3 reuploads”. |
| 20 | Limits table. Troubleshooting table. | Table: 7 reuploads, total submissions 1 account-wide, hourly 2, daily 5, task creation 2. Prose under the table says 3 reuploads. Troubleshooting still mentions the canary DM. |
| 21 | Rest of troubleshooting. Final pre-submission checklist. | Canary-in-every-file checklist, which conflicts with page 1. “All 9 Quality Dimensions”. “You hit 3 versions”. |
| 22–24 | Categories to collect. | TB3 taxonomy. 20% category cap. Deprioritized slices. Subcategory catalog. Note: rough numbers out of 66, but no distribution table is printed. |
| 25 | Acceptance criteria. | Pass rate ≤ 0.6 “i.e 4/8”. Turns > 35. `TASK_REVIEW_AUTOMATION.md` is named and is not in this PDF. |
| 26 | Rest of the review pipeline. | Hacker–fixer loop. “all four criteria” does not match the six bullets. |

## External documents named but not included

The canonical list, including what this system refuses to invent, is `UNAVAILABLE-SOURCES.md`. The rows below are the page index only.

| Name | Where named | Status |
| --- | --- | --- |
| Terms of Use / Clickwrap Agreement | PDF outline, page target `-1` | Not in the PDF body. |
| `TASK_REVIEW_AUTOMATION.md` | p.25 | Not in the PDF. The bullets under that sentence are the only local specification. |
| “Taxonomies tab” | p.25 | The taxonomy table is printed on pp. 22–24 of this same PDF. |
| “github” hyperlinks inside taxonomy cells | pp. 22–23 | The visible text is the word `github`. The URL is not in the text layer. Do not invent the target. |
| Pinned Harbor version | p.9 G02 | Required to parse. The version identifier is not given. |

## Task-level vs batch-level vs platform-controlled

| Kind | Who enforces it | Examples |
| --- | --- | --- |
| Task-level | Author, then platform checks on that ZIP | Instruction, verifier, metadata, Oracle/NOP, one task’s difficulty |
| Batch-level | Whoever delivers the round | No category above 20%. One task per deprioritized subcategory. Do not concentrate Software and Science. |
| Account-level | Platform limits table | Reuploads per task, hourly and daily unique versions, task creation limit, total submissions |
| Platform-controlled | The platform, not the author | I01 snapshot, G01–G06, P04, Stage 2’s 8 frozen-policy rollouts, grant suspend/revoke, Stage 3 deferred |
