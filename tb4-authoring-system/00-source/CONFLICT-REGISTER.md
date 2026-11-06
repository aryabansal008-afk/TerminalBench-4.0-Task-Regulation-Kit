# Conflict register

Audit of conflicting instructions in `Thanos _ Guidelines _ Onboarding SOP v3.0.pdf` (32 pages). This file is the only resolution record. `CONTRADICTIONS.md` points here. The requirements register still quotes both sides; it does not decide them. Where SOP v3.0 supersedes the previous 26-page freelancer PDF, the v3.0 statement is the active rule.

No source outside the PDF was consulted. Nothing below is a Harbor manual, a live platform response, or a reconstructed `TASK_REVIEW_AUTOMATION.md`. Named documents that are not in the PDF are listed in `UNAVAILABLE-SOURCES.md`, not treated as conflicts and not filled in.

## How a status is assigned

A later page does not override an earlier page. An earlier page does not override a later page. A screenshot does not override prose, and prose does not override a screenshot, unless the document itself identifies one instruction as the old way and the other as its replacement.

| Status | Meaning |
| --- | --- |
| `SUPERSEDED` | The PDF itself names the old instruction and the replacement. The quoted evidence is the supersession. Apply the replacement. |
| `UNRESOLVED` | Both statements stand. The PDF does not say which one wins. Do not pick the easier one or the stricter one. |
| `COMPATIBLE` | The statements can both be followed. A conflict appears only if a word is given a meaning the PDF does not give it. |

`PROVISIONAL` is not a status. It marks a working note under an `UNRESOLVED` conflict. A provisional note does not close the conflict, does not satisfy the other statement, and must be copied into the decision log if anyone acts on it.

## Status index

| ID | Topic | Status |
| --- | --- | --- |
| C-DISCORD | Discord decision path versus platform review | `SUPERSEDED` |
| C-CANARY | In-file Harbor canary markers versus leftover `canary_string` / Discord checklist text | `UNRESOLVED` (in-file markers are required; upload-field and Discord leftovers remain) |
| C-AGENT-TRIALS | “Agent Trials” card versus Stage 2 predicates | `SUPERSEDED` |
| C-REUPLOAD-FREELY | Unlimited re-upload versus immutable versions | `SUPERSEDED` |
| C-QC-LAYERS | QC alone versus QC then Super QC | `SUPERSEDED` |
| C-LEGACY-CARDS | Proposal Match, Cheat Trial, Harbor Analyze versus Stage 0–3 | `UNRESOLVED` |
| C-NINE-DIMENSIONS | “9 Quality Dimensions” versus 30 rubric criteria, Stage 3 deferred | `UNRESOLVED` |
| C-DIFFICULTY | Stage 2 full credit ≤ 4 of 8 versus acceptance pass rate ≤ 0.6 “i.e 4/8” | `UNRESOLVED` |
| C-HORIZON | Stage 2 median assistant messages > 35 versus minimum of all passing runs > 35 | `UNRESOLVED` |
| C-MISSING-COLUMNS | “Fail both columns” versus a one-column table | `UNRESOLVED` |
| C-INTERNET | Public agent network (change table) versus G02 non-public versus `allow_internet` default | `UNRESOLVED` |
| C-TIMEOUT | Exact `[agent].timeout_sec = 28800` versus leftover “6-hour CI headroom” sentence | `UNRESOLVED` (agent value is 28800; the 6-hour sentence and verifier exactness stay open) |
| C-REUPLOADS | Limits table 7 versus leftover prose that still says 3 | `UNRESOLVED` (workflow follows the table value 7; leftover “3” sentences are flagged, not applied) |
| C-ACCOUNT-LIMITS | Total submissions 1 versus task creation limit 2 | `UNRESOLVED` |
| C-FOUR-CRITERIA | “All four criteria” versus six pipeline bullets | `UNRESOLVED` |
| C-TB3-LABEL | TB4 contract prose versus TB3 labels in the UI and taxonomy | `UNRESOLVED` |
| C-HEADINGS | “Well-structured” versus a ban on tidy `##` headings | `COMPATIBLE` |
| C-REWARD-LITERAL | Reward `1` / `0`, `1.0` / `0.0`, and “NOP must not score 1.0” | `COMPATIBLE` on the local commands; partial-NOP platform result `UNRESOLVED` |
| C-EXPERT-TIME | Form “expert time” versus `expert_time_estimate_hours` | Form field defined; toml meaning `UNRESOLVED` |

## C-DISCORD

**Status:** `SUPERSEDED`.

**Statement A, retired.** Page 26, troubleshooting table: “Never received the canary DM. DMs from server members are disabled. Enable them in Discord privacy settings, then ask a moderator to re-send.” Page 27 checklist: “Discord DMs from server members enabled; canary received.” Page 1 change table, column “TB1 / TB2 (old way),” row “The decision”: “A bot reaction plus a DM; the recommendation was for a human maintainer.”

**Statement B, the replacement.** SOP v3.0 page 1: “There is no Discord step: the proposal, the verdict and the grant all live on the platform.” The change table still puts the Discord DM path in the retired workflow.

**Supersession evidence.** The change table is explicitly an old-way / new-way table, and the opening sentence states that this workflow has no Discord step. That identifies the DM path as the thing being replaced. It does not depend on page 26 being later than page 1.

**Apply.** Do not wait for a Discord DM, do not enable Discord as a step in this workflow, and do not treat a missing DM as a blocked proposal. The decision is the platform review.

**Not superseded by this row.** In-file canary markers are `C-CANARY`. Retiring Discord does not retire those markers. It does retire waiting on a canary DM.

**Downstream that no longer depend on Discord.** Proposal verdict, grant, and the start of Stage 1.

## C-CANARY

**Status:** in-file markers are the SOP v3.0 rule. Leftover `canary_string` / Discord checklist text and the GUID-token spelling remain `UNRESOLVED`.

**Active rule, SOP v3.0 pages 1, 3, 8–9, 21.** Canary markers are required in the checked text files, in the two-line Harbor format in §4.3. Missing or malformed markers are Stage 1 **warnings** (`TB4.CANARY_MISSING`, `TB4.CANARY_FORMAT`, `TB4.CANARY_ADVISORY`), not rejections. There is no `canary_string` field at upload; the grant links the ZIP. Use `PRIVATE_PROPOSAL_CANARY_REPLACE_ME` unless a proposal-specific canary was issued. Do not invent a third value. Match comment syntax to the file type. Skip `environment/data/` fixtures and binaries.

**Supersession of the previous PDF.** The 26-page freelancer guide forbade canary comment lines. SOP v3.0 page 1 replaces that: markers “are still required in TB4” and “go inside the task files, exactly as described in Section 4.3.” Journey step 4 now says to include them.

**Leftover contradictions inside SOP v3.0.**

- Page 8 line 1 includes the word `GUID`; page 21 omits it (`C-CANARY-FMT`). Templates and the checker accept both documented forms; skeletons follow §4.3 (with `GUID`).
- Pages 26–27 troubleshooting and checklist still mention a Discord canary DM and a `canary_string` upload field. Page 1 says that field does not exist. Do not wait on Discord. Do not fill an upload field the opening says is gone.

**Apply.** Put the two marker lines in `instruction.md`, `task.toml`, `environment/Dockerfile`, and every text file under `solution/` and `tests/`. `tools/check_task.py` warns when they are missing. Do not treat a warning as a Stage 1 rejection.

## C-AGENT-TRIALS

**Status:** `SUPERSEDED`.

**Statement A, retired.** Page 2 change table, old-way column, row “Difficulty”: “Agent Trials” as one card. Page 27 troubleshooting: “Agent Trials / Cheat Trial stay blocked. Proposal Match has not passed yet.” And “Harbor Analyze blocked. Agent Trials must complete first.”

**Statement B, the replacement for the difficulty decision.** SOP v3.0: Stage 2 model rollout after Stage 1. Pages 14–15 name the predicates `difficulty` = `count_true(full_credit_boolean) ≤ 4` and `long_horizon` = `median(assistant_message_count) > 35`.

**Supersession evidence.** The change table puts the quoted phrase “Agent Trials” in the old-way column and Stage 2 verdict predicates in the new-way column. Difficulty is no longer read off an Agent Trials card.

**Apply.** Read difficulty and long horizon from Stage 2. Do not look for an Agent Trials card as that decision.

**Not superseded.** Page 27’s Cheat Trial, Harbor Analyze, and Proposal Match names, and pages 31–32’s “agent & cheat trials” and “hacker–fixer loop,” are not in that old-way cell. They remain `C-LEGACY-CARDS`. The numeric conflict between the Stage 2 predicates and page 31 is `C-DIFFICULTY` and `C-HORIZON`, not this row.

## C-REUPLOAD-FREELY

**Status:** `SUPERSEDED`.

**Statement A, retired.** Page 2 change table, old way, “Fixing issues”: “Re-upload freely.”

**Statement B.** Same row, new way: “Each corrected ZIP becomes a new immutable version (Version N of N) and Stage 1 re-runs against it. Every version is recorded — arrive green.” Page 13: only one version with every gate green reaches Stage 2. Partial credit across versions does not count. Page 27: “File hash already exists” if the identical ZIP is uploaded again.

**Supersession evidence.** The change table labels free re-upload as the old way and immutable versions as the new way.

**Apply.** Each upload is a new immutable version. Do not expect an in-place replacement. Do not re-upload unchanged bytes.

**Not decided here.** How many versions are allowed is `C-REUPLOADS`.

## C-QC-LAYERS

**Status:** `SUPERSEDED` by addition.

**Statement A, retired as the whole of final review.** Page 2 change table, old way, “Final review”: “QC review.”

**Statement B.** Same row, new way: “QC review and then Super QC (a second, expert layer).”

**Supersession evidence.** The change table states the new final review as QC and then Super QC, not QC alone.

**Apply.** Final review has both layers, in that order. Super QC’s criteria are not in the PDF. That absence is `U-SUPER-QC` in `UNAVAILABLE-SOURCES.md`. It is not a reason to skip the layer or to invent its checklist. Stage 3 is not identified as Super QC (`C-LEGACY-CARDS`).

## C-LEGACY-CARDS

**Status:** `UNRESOLVED`.

**Statement A.** Pages 26–27 troubleshooting uses Proposal Match, Agent Trials, Cheat Trial, and Harbor Analyze as gates that block one another. The Agent Trials difficulty role is separately superseded by `C-AGENT-TRIALS`. The remaining card names are not.

**Statement B.** Pages 10–17 and the screenshots describe Stage 0 Task proposal, Stage 1 Static checks, Stage 2 Model rollout, and Stage 3 Qualitative checks. SOP v3.0 prose on pp. 15–16 gives Stage 3 verdicts (`ACCEPTED` / `REJECTED` / `COULD NOT COMPLETE`). Older screenshot chrome may still show `DEFERRED`. They do not mention Proposal Match, Cheat Trial, or Harbor Analyze.

**Statement C, still affirmative.** Pages 31–32: the acceptance pipeline includes “Agent & cheat trials — live agent trials plus adversarial cheat trials specifically probing for reward hacking” and “Hacker–fixer loop — iterative hardening until an adversarial agent can no longer exploit the verifier.”

**Why this is not supersession.** The change table retires “Agent Trials” as the difficulty card. It does not mention cheat trials, Harbor Analyze, or Proposal Match, so it does not retire them. Pages 31–32 require cheat trials and the hacker–fixer loop and do not say those are Stage 2.

**Practical consequences.** Blocking on a card the UI does not show stalls the task. Dropping cheat trials or the hacker–fixer loop can fail acceptance even after a Stage 2 `PASS`. Marking Stage 3 passed while it says `DEFERRED` records a result the screenshot does not show.

**Clarification needed.** Whether Proposal Match, Cheat Trial, and Harbor Analyze still exist as platform steps, whether they were renamed to a stage in this UI, or whether cheat trials and the hacker–fixer loop are human review outside Stage 0–3. What Stage 3 contains while it is deferred.

**Downstream actions that stay blocked.** Calling acceptance complete; equating Stage 2 with cheat trials; equating Stage 3 with Super QC or with the 9 Quality Dimensions (`C-NINE-DIMENSIONS`).

**PROVISIONAL.** None. Do the stages the current UI actually presents, and keep the page 31–32 bullets as open obligations. Do not invent buttons for the old card names, and do not check them off because Stage 2 passed.

## C-NINE-DIMENSIONS

**Status:** `UNRESOLVED`.

**Statement A.** Page 27 checklist: “All 9 Quality Dimensions green on the platform.”

**Statement B.** Pages 23–25 print 30 rubric criteria in groups A–E and say to aim for every one to `PASS`. The page does not call those criteria nine dimensions.

**Statement C.** Screenshots on pages 5, 12, 13, and 15 may still label `Stage 3 • Qualitative checks` as `DEFERRED`, while pp. 15–16 prose give Stage 3 verdicts. They do not list nine dimensions or thirty criteria.

**Why this is not supersession.** No sentence says the 30 criteria replace the 9 dimensions, or that Stage 3 is either list.

**Practical consequences.** A local pass on the 30 criteria does not establish that nine platform dimensions are green. Inventing nine names would fabricate a review scheme. Waiting on Stage 3 while the badge says `DEFERRED` waits on criteria the PDF does not list.

**Clarification needed.** The names of the nine Quality Dimensions, and whether they are Stage 3, the rubric, or something else.

**Downstream actions that stay blocked.** The page 27 checklist item “All 9 Quality Dimensions green.” Marking Stage 3 passed from that checklist.

**PROVISIONAL.** Run the printed 30-criterion rubric because that list is in the PDF and the rubric section says to aim for every criterion to pass. Do not write “9 Quality Dimensions: green” in the evidence pack.

## C-DIFFICULTY

**Status:** `UNRESOLVED` between Stage 2 and the acceptance page. The previous Stage 2 ceiling of ≤ 2 is **superseded** by SOP v3.0.

**Statement A, active Stage 2 rule.** SOP v3.0 page 14, §6.2: `count_true(full_credit_boolean) ≤ 4`. “At most 4 of the 8 rollouts may earn full credit.”

**Statement B.** SOP v3.0 page 31: pass rate ≤ 0.6, written “i.e 4/8”, 8 rollouts, timeout limit 8 hrs. Note: anonymous model “is GPT-6-Sol-xhigh performance.”

**Statement C.** Page 31 item 3 still rejects tasks that “fail both difficulty columns.” The printed table has one column (`C-MISSING-COLUMNS`).

The previous freelancer PDF’s ≤ 2 Stage 2 predicate is not an active rule.

**Why A and B are not supersession of each other.** Stage 2 counts full-credit booleans with ceiling 4. Acceptance states a pass rate of ≤ 0.6 and glosses it “i.e 4/8”. 4/8 = 0.5, which is not 0.6. The PDF equates them with “i.e” and does not explain the arithmetic.

**Apply.** Design and local checks use the Stage 2 predicate ≤ 4 of 8. Archive any acceptance receipt beside both written strings. Do not write either number into `difficulty_explanation` as a passed gate.

## C-HORIZON

**Status:** `UNRESOLVED` between Stage 2 median and acceptance minimum. The previous Stage 2 median > 80 is **superseded** by SOP v3.0.

**Statement A, active Stage 2 rule.** SOP v3.0 page 14: `median(assistant_message_count) > 35`. A median of about 25 fails even when difficulty passes.

**Statement B.** SOP v3.0 page 31: “a minimum of 35 turns of all passing runs.” Table: “Anonymous > 35 turns (TB4 ≈ 75).”

The previous freelancer PDF’s median > 80 is not an active rule.

**Why A and B are not the same test.** A is a median over the Stage 2 population. B is a minimum over passing runs. A median above 35 does not prove every passing run is above 35.

**Apply.** Stage 2 uses the median > 35 predicate. Do not pad turns. Do not treat a Stage 2 `PASS` as the acceptance minimum.

## C-MISSING-COLUMNS

**Status:** `UNRESOLVED`.

**Statement A.** Page 31 item 3 rejects tasks that “fail both difficulty columns” or “fail both turn-count columns.”

**Statement B.** The metrics table on that page has one column, “Latest Frontier Model.”

**Why this is not supersession.** Item 3 is a rejection rule about two columns. The table does not show two columns and does not say the second column was removed. “Fail both” is not the same rule as “fail the only printed cell,” and it is not the same rule as “fail either.”

**Practical consequences.** If “both” is literal, failing one hidden column might not reject the task. If the second column was simply not printed, one failure might reject it. This PDF does not say which.

**Clarification needed.** The missing column headers and cells, or a statement that the rejection rule no longer refers to two columns.

**Downstream actions that stay blocked.** Any acceptance decision that depends on item 3. Do not invent a second model, a second pass rate, or a waiver.

**PROVISIONAL.** None. `C-DIFFICULTY` and `C-HORIZON` are not resolved by ignoring item 3.

## C-INTERNET

**Status:** `UNRESOLVED`.

**Statement A.** SOP v3.0 pages 1–2 change table: both the agent environment and the agent phase must resolve to **public** network access. Replace the deprecated `allow_internet` field with the “supported network configuration.” That replacement key is not named (`U-NET-CONFIG`).

**Statement B.** Static check `check-allow-internet` (p.20): do not set `[environment].allow_internet = false`. “tasks run with open internet by default.”

**Statement C.** G02 (p.10): “agent networking is non-public, and verifier isolation is declared.”

These three sentences stand inside SOP v3.0. Public agent access is not a license to put public networking on the verifier, to use host networking, or to fetch at verify time (`check-trial-network-fetch`, G03).

**Statements that are not this conflict.** Page 20, `check-trial-network-fetch`, forbids `tests/test.sh` from fetching external resources at verify time. Rubric C, “No shortcut via internet”: the answer cannot simply be looked up online or copied from a public source. Rubric B, “Environment is self-contained”: the task does not rely on flaky external resources. Those sentences do not say what value `allow_internet` must have, and they do not define “non-public.”

**Why this is not supersession.** The static check forbids one assignment, `allow_internet = false`. G02 requires networking that is “non-public” and does not mention that key. The PDF never says that leaving the key unset, setting it true, or forbidding public lookup satisfies “non-public.”

**Practical consequences.** Setting `allow_internet = false` fails the stated static check. Leaving it unset, or setting it true, is not shown to satisfy G02. A task that needs outbound network to be solvable can conflict with “non-public” if that phrase means no public egress. A task that is correct only because the answer is on the public web fails the rubric whether or not the key is set.

**Clarification needed.** The configuration that satisfies “agent networking is non-public,” and whether that configuration is the `allow_internet` key. What `HARBOR.DEPRECATED_ALLOW_INTERNET` and `TB3.AGENT_NETWORK_NONPUBLIC` match.

**Downstream that stay open.** Claiming G02 “non-public” is satisfied; inventing the unnamed replacement for `allow_internet`; treating a `TB3.AGENT_NETWORK_NONPUBLIC` failure as a reason to set `allow_internet = false`.

**PROVISIONAL.** Do not set `allow_internet = false`. Do not invent a replacement key. Do not add public networking to the verifier because the agent change table requires public access. Do not add host networking, privileged mode, or verifier-time fetches.

## C-TIMEOUT

**Status:** the agent value is settled by SOP v3.0. Leftover CI-headroom wording and verifier exactness remain `UNRESOLVED`.

**Active rule.** Change table rows 8–9 and the static-check hard-block list: `[agent].timeout_sec` is exactly `28800`. The instruction footer states 28800 seconds. `check-task-timeout` caps `[agent]` and `[verifier]` at 28800s (8 hours).

**Leftover contradiction.** The same timeout check still says this “leav[es] headroom under the CI runner's 6-hour job limit.” Eight hours is not headroom under six hours. Do not revive the previous 18000-second cap.

**Verifier.** The exact-28800 strict policy is written for the agent timeout and the instruction footer. The verifier field is capped at 28800; SOP v3.0 does not say to copy 28800 onto `[verifier].timeout_sec`. Set the verifier long enough to grade, not as a second copy of the agent budget.

**Apply.** Write 28800 in `[agent].timeout_sec` and in the footer. Do not use 18000.

## C-REUPLOADS

**Status:** `UNRESOLVED`.

**Statement A, table and nearby prose.** SOP v3.0 page 26 limits table: “Reuploads (new versions) per task” = `7`. The paragraph under that table: “with only 7 reuploads per task.” Page 25 rubric close: “protects your 7 reuploads.”

**Statement B, leftover.** Page 20 static-check close: “one of your three reuploads.” Page 26 troubleshooting: “You hit 3 versions for that task.”

**Why this is not silent resolution.** The leftover “3” sentences are still printed. They are flagged. The workflow uses the limits table.

**Operational policy under this system.** SOP v3.0’s limits table and the paragraph immediately under it on page 26 both state **7** reuploads per task. The rubric close on page 25 also says 7. Leftover “three reuploads” / “You hit 3 versions” sentences on pages 20, 26, and 27 are flagged as contradictory leftovers. They are not applied as the budget.

**Still apply without choosing 3.** Hourly limit 2 and daily limit 5. Immutable versions. Do not upload a ZIP that fails local static checks, Oracle, or NOP.

## C-ACCOUNT-LIMITS

**Status:** `UNRESOLVED`.

**Statement A.** Page 26 table: “Total submissions” = `1 (account-wide)`.

**Statement B.** Same table: “Task creation limit” = `2 tasks`.

**Why this is not supersession.** They are adjacent cells. The PDF does not define “submission” or say that it is a different object from a created task.

**Practical consequences.** Creating a second task can violate statement A if a submission is a task. Refusing a second task can violate statement B if the creation limit is the operative cap.

**Clarification needed.** What a submission counts, and whether the creation limit and the submission limit apply to the same action.

**Downstream actions that stay blocked.** Creating the first platform task and creating a second one, until the account UI or the operator states the remaining quota. Quote that statement in the decision log. Do not treat either cell as repealed.

**PROVISIONAL.** None.

## C-FOUR-CRITERIA

**Status:** `UNRESOLVED`.

**Statement A.** Page 32: “A task is considered accepted only once it clears all four criteria and is merged following this pipeline — not upon submission or upon passing static checks alone.”

**Statement B.** Pages 31–32 list six bullets under the pipeline: static checks, implementation rubric review, Docker / Oracle / No-op validation, maintainer review, agent and cheat trials, and the hacker–fixer loop. The acceptance section also has the headings “Taxonomy & Volume,” “Model-Breaking Difficulty and Solvability Gates,” and “Review Pipeline Compliance.”

**Why this is not supersession.** “Four” does not identify which four. The six bullets do not say they are the four. The three headings are not four either.

**What does apply without resolving the count.** The closing clause is not in conflict with the bullets: acceptance is not submission, and it is not static checks alone.

**Clarification needed.** Which four criteria the sentence counts.

**Downstream actions that stay blocked.** Declaring a task accepted. Checking off a private subset of four bullets as “the four.”

**PROVISIONAL.** None. Do not call the task accepted. Do not drop a printed bullet because the word is “four.”

## C-TB3-LABEL

**Status:** `UNRESOLVED`.

**Statement A.** Page 10, G02 title in the prose: “Harbor + TB4 contract.” The document title is Terminal Bench 4.

**Statement B.** Pages 12–13 screenshots label that gate “Harbor + TB3” and prefix rules `TB3.`. Page 28: “We follow the official taxonomy of Terminal Bench 3.” Page 8: difficulty, turn count, category distribution, and instruction style must align with “Terminal-Bench 3/4.”

**Why this is not supersession.** No sentence says the screenshot’s TB3 prefix is a mistake, or that the TB3 taxonomy sentence is leftover. “3/4” names both.

**Practical consequences.** Renaming a live `TB3.*` rule to `TB4.*` in the evidence pack hides the id the UI showed. Ignoring the TB3 taxonomy because the workflow is titled TB4 drops a sentence the PDF states. Treating every TB3 label as the current contract name drops the G02 prose title.

**Clarification needed.** Whether the running gate is the TB4 contract described in prose, the TB3-labeled checker in the screenshot, or both.

**Downstream actions that stay blocked.** Asserting a single product generation for the checker. When a receipt shows `TB3.*`, archive that id as printed.

**PROVISIONAL.** None. Follow the taxonomy table for categories because page 28 says to follow that taxonomy. That is that sentence’s own scope. It does not rename G02.

## C-HEADINGS

**Status:** `COMPATIBLE`.

**Statement A.** Rubric D, “Clear and well-written”: the instruction is unambiguous, well-structured, and free of contradictions. The rubric does not define “well-structured” as markdown headings.

**Statement B.** Page 8, §4.2: a description in tidy markdown structure, with the example `##` headings, together with excessive length, is taken as “pure LLM synthesis without human review” and is non-compliant.

**Why there is no winner to pick.** Statement B forbids a stated shape. Statement A does not require that shape. Reading “well-structured” as “add `##` headings” would create a conflict the PDF does not state.

**Apply both as written.** Do not use tidy `##` headings or excessive length in the task description. Keep the instruction unambiguous and free of contradictions. Do not add headings in order to satisfy “well-structured.”

## C-REWARD-LITERAL

**Status:** `COMPATIBLE` for the local Oracle and NOP commands. The platform result of a partial NOP reward is `UNRESOLVED`.

**Statement A.** Page 9, §4.3: `test.sh` writes the final reward “(1 pass / 0 fail)” to `/logs/verifier/reward.txt`.

**Statement B.** Page 9, §4.4 table: Oracle expected reward `1.0`; NOP expected reward `0.0`.

**Statement C.** Page 11, G05: “Oracle must score 1.0 and exit cleanly; NOP must not score 1.0.” The reward must be found, parseable, unambiguous, and finite. Screenshots list `NOP.FULL_REWARD` and `NOP.PARTIAL_REWARD`. Their severity badges could not be reliably paired with the rows (`U-SEVERITY-ALIGNMENT`).

**Why the local commands are compatible.** Section 4.4 states the expected local result of the two commands it names: Oracle `1.0`, NOP `0.0`. “1 pass / 0 fail” is the same section’s description of the reward file. The PDF does not say these are different required numbers. G05’s “score 1.0” matches the Oracle cell.

**What stays unresolved.** G05 says NOP must not score 1.0. The local table says the expected NOP result is 0.0. A partial NOP reward is between those sentences. The PDF does not say whether `NOP.PARTIAL_REWARD` rejects the task. Choosing 0.0 because it is stricter would decide that platform question. The local table can still be followed for the local command without that decision.

**Apply.** Local `harbor run --path . --agent oracle` is expected to show reward `1.0`. Local `harbor run --path . --agent nop` is expected to show reward `0.0`. That is what §4.4 says those commands should produce. Do not describe 0.0 as a platform rule stronger than G05. If a receipt says the parser wanted a different literal, archive the receipt. Do not invent the literal in advance.

**Downstream that remains open.** Whether a NOP reward other than 1.0 and other than 0.0 fails Stage 1.

## C-EXPERT-TIME

**Status:** the form field is defined. The meaning of `expert_time_estimate_hours` is `UNRESOLVED`.

**Statement A.** Page 4, §3.2, and the page 5 screenshot: Expert time is hours, “what an expert should need to build the task, not what you spent writing the proposal.” The screenshot helper says the estimate is “what an expert should need, not what you spent writing this.”

**Statement B.** Page 4, §3.1, Solvable: implementable “in a few hours by an expert who knows the answer.”

**Statement C.** Pages 9 and 19: `expert_time_estimate_hours` is required metadata. The PDF does not say whether that field is build time, solve time, or another quantity.

**Why A and B are not a conflict.** They name different activities. Build time and solve time can both be true. Copying one number into the other silently would erase that difference.

**Apply.** The proposal form’s Expert time is build time, as statement A defines it. Do not put drafting time there. Do not assume the toml field is the same number.

**Clarification needed.** What `expert_time_estimate_hours` measures.

**Downstream actions that stay blocked.** Filling `expert_time_estimate_hours` as if the form definition had been copied onto it.

**PROVISIONAL.** If a number is written into the toml field before clarification, `difficulty_explanation` must say which quantity the author intends, and the decision log must mark that label provisional. An empty default still fails `check-task-fields`, which requires the field and does not define it.

## What this audit did not consult

No external URL, Harbor repository, platform ticket, or copy of `TASK_REVIEW_AUTOMATION.md` was used. Audit date: 2026-11-03. Authority for every quote above is the PDF only. Unavailable references are in `UNAVAILABLE-SOURCES.md`.
