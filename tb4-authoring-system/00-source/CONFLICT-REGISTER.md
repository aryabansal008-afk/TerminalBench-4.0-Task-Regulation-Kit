# Conflict register

Audit of conflicting instructions in `Freelancers _ Thanos _ Guidelines.pdf` (26 pages). This file is the only resolution record. `CONTRADICTIONS.md` points here. The requirements register still quotes both sides; it does not decide them.

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
| C-CANARY | Canary lines and `canary_string` versus “nothing asks for one” | `UNRESOLVED` |
| C-AGENT-TRIALS | “Agent Trials” card versus Stage 2 predicates | `SUPERSEDED` |
| C-REUPLOAD-FREELY | Unlimited re-upload versus immutable versions | `SUPERSEDED` |
| C-QC-LAYERS | QC alone versus QC then Super QC | `SUPERSEDED` |
| C-LEGACY-CARDS | Proposal Match, Cheat Trial, Harbor Analyze versus Stage 0–3 | `UNRESOLVED` |
| C-NINE-DIMENSIONS | “9 Quality Dimensions” versus 30 rubric criteria, Stage 3 deferred | `UNRESOLVED` |
| C-DIFFICULTY | Full credit ≤ 2 of 8 versus pass rate ≤ 0.6 “i.e 4/8” | `UNRESOLVED` |
| C-HORIZON | Median assistant messages > 80 versus passing runs > 35 | `UNRESOLVED` |
| C-MISSING-COLUMNS | “Fail both columns” versus a one-column table | `UNRESOLVED` |
| C-INTERNET | Open internet by default versus non-public agent networking | `UNRESOLVED` |
| C-TIMEOUT | `timeout_sec` cap 18000 versus rollout “timeout limit 8 hrs” | `UNRESOLVED` |
| C-REUPLOADS | 7 reuploads in the table versus 3 in the prose | `UNRESOLVED` |
| C-ACCOUNT-LIMITS | Total submissions 1 versus task creation limit 2 | `UNRESOLVED` |
| C-FOUR-CRITERIA | “All four criteria” versus six pipeline bullets | `UNRESOLVED` |
| C-TB3-LABEL | TB4 contract prose versus TB3 labels in the UI and taxonomy | `UNRESOLVED` |
| C-HEADINGS | “Well-structured” versus a ban on tidy `##` headings | `COMPATIBLE` |
| C-REWARD-LITERAL | Reward `1` / `0`, `1.0` / `0.0`, and “NOP must not score 1.0” | `COMPATIBLE` on the local commands; partial-NOP platform result `UNRESOLVED` |
| C-EXPERT-TIME | Form “expert time” versus `expert_time_estimate_hours` | Form field defined; toml meaning `UNRESOLVED` |

## C-DISCORD

**Status:** `SUPERSEDED`.

**Statement A, retired.** Page 20, troubleshooting table: “Never received the canary DM. DMs from server members are disabled. Enable them in Discord privacy settings, then ask a moderator to re-send.” Page 21 checklist: “Discord DMs from server members enabled; canary received.” Page 1 change table, column “TB1 / TB2 (old way),” row “The decision”: “A bot reaction plus a DM; the recommendation was for a human maintainer.”

**Statement B, the replacement.** Page 1 opening: “There is no Discord step and no canary string anywhere in this workflow.” Page 1 change table, column “TB4 (new way),” same row: “A review run on the platform: a verdict per criterion, an overall verdict, and a written final analysis you can read in full.”

**Supersession evidence.** The change table is explicitly an old-way / new-way table, and the opening sentence states that this workflow has no Discord step. That identifies the DM path as the thing being replaced. It does not depend on page 20 being later than page 1.

**Apply.** Do not wait for a Discord DM, do not enable Discord as a step in this workflow, and do not treat a missing DM as a blocked proposal. The decision is the platform review.

**Not superseded by this row.** The canary words that share the page 1 sentence and the page 21 checklist item are `C-CANARY`. Retiring Discord does not retire those canary instructions.

**Downstream that no longer depend on Discord.** Proposal verdict, grant, and the start of Stage 1.

## C-CANARY

**Status:** `UNRESOLVED`.

**Statement A.** Page 1: “There is no Discord step and no canary string anywhere in this workflow. If you worked on TB4 before the platform, delete that habit: do not add canary comment lines to your files, and do not look for a canary_string field at upload. Nothing issues one and nothing asks for one.” Page 2, journey step 4: “Build the task locally — separate verifier structure, no canary lines.” Page 13, §7 checklist: “No canary lines anywhere. Nothing in your files, nothing to paste at upload.”

**Statement B.** Page 6, §4: “With your idea approved and your canary in hand.” The example tree comment: “Canary on line 1.” Page 8, §4.3: “Canary in every file (Section 4) — do not forget the solution and test files.” Page 15, static-check introduction: checks catch “a missing canary.” Page 21: “Canary present (inside a comment) in EVERY text file: instruction.md, task.toml, environment/Dockerfile, all of solution/ and all of tests/.” And “Canary entered as the canary_string field at upload.” Page 25 pipeline bullet: static checks include “canary strings.” Pages 10–11 screenshots show rule names `TB3.CANARY_MISSING`, `TB3.CANARY_FORMAT`, and `TB3.CANARY_ADVISORY` under the gate labeled `Harbor + TB3`.

**Why this is not supersession.** Page 1 tells someone who worked on TB4 before the platform to delete the habit, and it asserts that nothing asks for a canary. It does not say that §4, the static-check introduction, the page 21 checklist, the page 25 bullet, or the Stage 1 screenshots are withdrawn. Those passages are not in the old-way column of the change table. “Section 4” in this PDF is the current build chapter and does not define a canary format. Page order is not used either way: page 1 and page 13 forbid canaries; pages 6 and 8, still inside the current build chapter, require them.

**Practical consequences.** A file cannot both contain a canary line and contain no canary line. A ZIP with no canary can be rejected by `TB3.CANARY_MISSING` or `TB3.CANARY_FORMAT` if those rules still run. A ZIP with an invented canary contradicts “Nothing issues one.” The acceptance bullet “canary strings” cannot be marked met or unmet from this PDF alone.

**Clarification needed.** Whether the live Stage 1 job still raises `TB3.CANARY_MISSING` or `TB3.CANARY_FORMAT`; if it does, the exact string the platform issues and the files it must appear in. The PDF says nothing issues one, so this system will not mint a string.

**Downstream actions that stay blocked.** Contents of `instruction.md`, `task.toml`, `environment/Dockerfile`, `solution/`, and `tests/` with respect to a canary; any upload field named `canary_string`; marking the page 25 “canary strings” bullet complete; interpreting a Stage 1 failure on those three rule IDs as either a task defect or a stale rule.

**PROVISIONAL.** The skeletons under `material/agent-visible/` and `material/verifier-and-solution/` contain no canary line. That is a file-state necessity, not a resolution. `tools/check_task.py` refuses to package until a human records which statement this upload is following. That record is provisional until a Stage 1 receipt shows whether a `TB3.CANARY_*` rule fired. Do not describe the omission as compliance with statement B, and do not describe a homemade canary as compliance with statement A.

## C-AGENT-TRIALS

**Status:** `SUPERSEDED`.

**Statement A, retired.** Page 2 change table, old-way column, row “Difficulty”: “Agent Trials” as one card. Page 21 troubleshooting: “Agent Trials / Cheat Trial stay blocked. Proposal Match has not passed yet.” And “Harbor Analyze blocked. Agent Trials must complete first.”

**Statement B, the replacement for the difficulty decision.** Page 2, new-way column, same row: “Stage 2 model rollout, entered only after Stage 1 is accepted. Difficulty and long-horizon gates are decided as verdict predicates.” Pages 12–13 name the predicates `difficulty` = `count_true(full_credit_boolean) ≤ 2` and `long_horizon` = `median(assistant_message_count) > 80`.

**Supersession evidence.** The change table puts the quoted phrase “Agent Trials” in the old-way column and Stage 2 verdict predicates in the new-way column. Difficulty is no longer read off an Agent Trials card.

**Apply.** Read difficulty and long horizon from Stage 2. Do not look for an Agent Trials card as that decision.

**Not superseded.** Page 21’s Cheat Trial, Harbor Analyze, and Proposal Match names, and pages 25–26’s “agent & cheat trials” and “hacker–fixer loop,” are not in that old-way cell. They remain `C-LEGACY-CARDS`. The numeric conflict between the Stage 2 predicates and page 25 is `C-DIFFICULTY` and `C-HORIZON`, not this row.

## C-REUPLOAD-FREELY

**Status:** `SUPERSEDED`.

**Statement A, retired.** Page 2 change table, old way, “Fixing issues”: “Re-upload freely.”

**Statement B.** Same row, new way: “Each corrected ZIP becomes a new immutable version (Version N of N) and Stage 1 re-runs against it. Every version is recorded — arrive green.” Page 11: only one version with every gate green reaches Stage 2. Partial credit across versions does not count. Page 21: “File hash already exists” if the identical ZIP is uploaded again.

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

**Statement A.** Page 20–21 troubleshooting uses Proposal Match, Agent Trials, Cheat Trial, and Harbor Analyze as gates that block one another. The Agent Trials difficulty role is separately superseded by `C-AGENT-TRIALS`. The remaining card names are not.

**Statement B.** Pages 9–13 and the screenshots describe Stage 0 Task proposal, Stage 1 Static checks, Stage 2 Model rollout, and Stage 3 Qualitative checks with the badge `DEFERRED`. They do not mention Proposal Match, Cheat Trial, or Harbor Analyze.

**Statement C, still affirmative.** Pages 25–26: the acceptance pipeline includes “Agent & cheat trials — live agent trials plus adversarial cheat trials specifically probing for reward hacking” and “Hacker–fixer loop — iterative hardening until an adversarial agent can no longer exploit the verifier.”

**Why this is not supersession.** The change table retires “Agent Trials” as the difficulty card. It does not mention cheat trials, Harbor Analyze, or Proposal Match, so it does not retire them. Pages 25–26 require cheat trials and the hacker–fixer loop and do not say those are Stage 2.

**Practical consequences.** Blocking on a card the UI does not show stalls the task. Dropping cheat trials or the hacker–fixer loop can fail acceptance even after a Stage 2 `PASS`. Marking Stage 3 passed while it says `DEFERRED` records a result the screenshot does not show.

**Clarification needed.** Whether Proposal Match, Cheat Trial, and Harbor Analyze still exist as platform steps, whether they were renamed to a stage in this UI, or whether cheat trials and the hacker–fixer loop are human review outside Stage 0–3. What Stage 3 contains while it is deferred.

**Downstream actions that stay blocked.** Calling acceptance complete; equating Stage 2 with cheat trials; equating Stage 3 with Super QC or with the 9 Quality Dimensions (`C-NINE-DIMENSIONS`).

**PROVISIONAL.** None. Do the stages the current UI actually presents, and keep the page 25–26 bullets as open obligations. Do not invent buttons for the old card names, and do not check them off because Stage 2 passed.

## C-NINE-DIMENSIONS

**Status:** `UNRESOLVED`.

**Statement A.** Page 21 checklist: “All 9 Quality Dimensions green on the platform.”

**Statement B.** Pages 17–19 print 30 rubric criteria in groups A–E and say to aim for every one to `PASS`. The page does not call those criteria nine dimensions.

**Statement C.** Screenshots on pages 5, 10, 11, and 13 label `Stage 3 • Qualitative checks` as `DEFERRED`. They do not list nine dimensions or thirty criteria.

**Why this is not supersession.** No sentence says the 30 criteria replace the 9 dimensions, or that Stage 3 is either list.

**Practical consequences.** A local pass on the 30 criteria does not establish that nine platform dimensions are green. Inventing nine names would fabricate a review scheme. Waiting on Stage 3 while the badge says `DEFERRED` waits on criteria the PDF does not list.

**Clarification needed.** The names of the nine Quality Dimensions, and whether they are Stage 3, the rubric, or something else.

**Downstream actions that stay blocked.** The page 21 checklist item “All 9 Quality Dimensions green.” Marking Stage 3 passed.

**PROVISIONAL.** Run the printed 30-criterion rubric because that list is in the PDF and the rubric section says to aim for every criterion to pass. Do not write “9 Quality Dimensions: green” in the evidence pack.

## C-DIFFICULTY

**Status:** `UNRESOLVED`.

**Statement A.** Page 12, §6.2, predicate `difficulty`: `count_true(full_credit_boolean) ≤ 2`. “At most 2 of the 8 rollouts may earn full credit. More than that and the task is too easy.” Page 13 screenshot: “Required: ≤2” for “Full-credit rollouts,” population “Anonymous model.”

**Statement B.** Page 25: “Difficulty: Roll out with an anonymous model, timeout limit 8 hrs, 8 rollouts, pass rate ≤ 0.6.” The metrics table: “Pass rate (8 rollouts, timeout limit 8 hrs)” = “≤ 0.6 i.e 4/8”. Note: “Anonymous model - This model is close to GPT-6-Sol-xhigh performance.”

**Statement C.** Page 25 item 3: “Tasks that fail both difficulty columns, fail solvability, or fail both turn-count columns are rejected.” The printed table has one model column. See `C-MISSING-COLUMNS`.

**Why this is not supersession.** Stage 2 does not say it replaces the acceptance pass rate. The acceptance page does not say it replaces Stage 2. They are not worded as the same predicate: one counts full-credit booleans with a ceiling of 2, the other states a pass rate of ≤ 0.6 and glosses it “i.e 4/8”. The PDF does not say these are the same eight rollouts. Meeting the lower ceiling does not, on this text, prove the acceptance sentence is satisfied, and meeting “4/8” does not prove Stage 2 passes. Choosing ≤ 2 because it is stricter, or ≤ 4 because it is easier, would be a choice the PDF does not make.

**Practical consequences.** A result of 3 of 8 full credit fails statement A and is inside the “i.e 4/8” gloss of statement B. A result of 5 of 8 fails both numeric glosses if “≤ 0.6” is read as forbidding 5/8 (0.625), and the “i.e 4/8” gloss also stops at 4. Whether 0.6 and 4/8 are the same cut is itself slightly loose: 4/8 = 0.5. The PDF equates them with “i.e” and does not explain the arithmetic. This register does not replace either string with a calculated substitute.

**Clarification needed.** Whether Stage 2 and the acceptance difficulty line are one measurement or two; which full-credit count fails acceptance; what the second difficulty column is (`C-MISSING-COLUMNS`).

**Downstream actions that stay blocked.** Declaring a difficulty target for a new task; treating a Stage 2 `PASS` as acceptance on difficulty; treating an acceptance pass rate of 3/8 or 4/8 as a Stage 2 pass; writing a single number into `difficulty_explanation` as “the” gate.

**PROVISIONAL.** None. When a receipt exists, archive the observed count next to both written ceilings. Do not relabel that archive as a resolution.

## C-HORIZON

**Status:** `UNRESOLVED`.

**Statement A.** Page 12, predicate `long_horizon`: `median(assistant_message_count) > 80`. “A median of ~48 turns fails this even when difficulty passes.” Page 13 screenshot: “Median assistant turns,” “Required: >80”.

**Statement B.** Page 25: “We require a minimum of 35 turns of all passing runs in the Anonymous model.” Table: “Turns (role=assistant)” = “Anonymous > 35 turns.”

**Why this is not supersession.** The statistics differ. Statement A is a median over the Stage 2 population. Statement B is a minimum over passing runs, and the table does not say “median.” Neither page says it replaces the other. A median above 80 does not establish that every passing run is above 35. A minimum above 35 does not establish a median above 80. Using both cutoffs because their intersection is stricter is a choice the PDF does not make.

**Practical consequences.** A task can fail Stage 2 with a median around 48 while every passing run is above 35. A task can pass Stage 2 on the median and still have a passing run at or below 35 turns. Page 13’s instruction not to pad, and not to hide information, is the repair note for a Stage 2 long-horizon `FAIL`. It is not a ruling that 80 replaces 35.

**Clarification needed.** Which statistic acceptance uses (median of all rollouts, or minimum of passing runs), and whether that test is the Stage 2 predicate.

**Downstream actions that stay blocked.** Setting a turn target before upload; closing the horizon item in acceptance from a Stage 2 median alone; adding or removing work solely to hit the other page’s number.

**PROVISIONAL.** None.

## C-MISSING-COLUMNS

**Status:** `UNRESOLVED`.

**Statement A.** Page 25 item 3 rejects tasks that “fail both difficulty columns” or “fail both turn-count columns.”

**Statement B.** The metrics table on that page has one column, “Latest Frontier Model.”

**Why this is not supersession.** Item 3 is a rejection rule about two columns. The table does not show two columns and does not say the second column was removed. “Fail both” is not the same rule as “fail the only printed cell,” and it is not the same rule as “fail either.”

**Practical consequences.** If “both” is literal, failing one hidden column might not reject the task. If the second column was simply not printed, one failure might reject it. This PDF does not say which.

**Clarification needed.** The missing column headers and cells, or a statement that the rejection rule no longer refers to two columns.

**Downstream actions that stay blocked.** Any acceptance decision that depends on item 3. Do not invent a second model, a second pass rate, or a waiver.

**PROVISIONAL.** None. `C-DIFFICULTY` and `C-HORIZON` are not resolved by ignoring item 3.

## C-INTERNET

**Status:** `UNRESOLVED`.

**Statement A.** Page 16, `check-allow-internet`: `task.toml` does not set `[environment].allow_internet = false`. “tasks run with open internet by default.” The Stage 1 screenshots also show a rule named `HARBOR.DEPRECATED_ALLOW_INTERNET`. The PDF does not define what that rule matches.

**Statement B.** Page 9, G02: “agent networking is non-public, and verifier isolation is declared.” The screenshots show `TB3.AGENT_NETWORK_NONPUBLIC`. The PDF does not define “non-public.”

**Statements that are not this conflict.** Page 16, `check-trial-network-fetch`, forbids `tests/test.sh` from fetching external resources at verify time. Rubric C, “No shortcut via internet”: the answer cannot simply be looked up online or copied from a public source. Rubric B, “Environment is self-contained”: the task does not rely on flaky external resources. Those sentences do not say what value `allow_internet` must have, and they do not define “non-public.”

**Why this is not supersession.** The static check forbids one assignment, `allow_internet = false`. G02 requires networking that is “non-public” and does not mention that key. The PDF never says that leaving the key unset, setting it true, or forbidding public lookup satisfies “non-public.”

**Practical consequences.** Setting `allow_internet = false` fails the stated static check. Leaving it unset, or setting it true, is not shown to satisfy G02. A task that needs outbound network to be solvable can conflict with “non-public” if that phrase means no public egress. A task that is correct only because the answer is on the public web fails the rubric whether or not the key is set.

**Clarification needed.** The configuration that satisfies “agent networking is non-public,” and whether that configuration is the `allow_internet` key. What `HARBOR.DEPRECATED_ALLOW_INTERNET` and `TB3.AGENT_NETWORK_NONPUBLIC` match.

**Downstream actions that stay blocked.** Claiming G02 networking is satisfied; deciding that the agent image may use public egress; responding to a `TB3.AGENT_NETWORK_NONPUBLIC` failure by editing `allow_internet`.

**PROVISIONAL.** Do not set `allow_internet = false` while acting only on `check-allow-internet`. That follows the static check’s own words. It is not a finding that the task is non-public, and it is not a finding that the static check overrides G02. Say so in the decision log if the key is left unset. Do not add host networking, privileged mode, or verifier-time fetches: those are separate prohibitions in G03 and `check-trial-network-fetch`, not a definition of “non-public.”

## C-TIMEOUT

**Status:** `UNRESOLVED`.

**Statement A.** Page 16, `check-task-timeout`: `[agent]` and `[verifier]` `timeout_sec` are capped at `18000s` (5 hours), “leaving headroom under the CI runner's 6-hour job limit.”

**Statement B.** Page 25: “Roll out with an anonymous model, timeout limit 8 hrs, 8 rollouts, pass rate ≤ 0.6.” The metrics table repeats “timeout limit 8 hrs.”

**Why this is not supersession.** Statement A names the fields `timeout_sec`. Statement B names a rollout “timeout limit” and does not mention those fields. Neither sentence says the two clocks are the same, and neither says they are different. Eight hours is 28800 seconds. The PDF does not do that multiplication and does not say to write 28800 into `timeout_sec`. Inferring that the rollout limit is a different field would be an inference, not a statement in the PDF. Inferring that `timeout_sec` must be 28800 would contradict the named cap only if they are the same field, which is the unresolved point.

**Practical consequences.** Writing a `timeout_sec` above 18000 can fail `check-task-timeout` if that check is applied to the field as written. Writing 18000 or less can be shorter than the rollout limit if the rollout limit is that field. The instruction suffix must use the same integer as `[agent].timeout_sec` (`check-instruction-suffix`). That equality is not in conflict. The conflict is which integer is allowed.

**Clarification needed.** Whether “timeout limit 8 hrs” is the platform’s rollout budget, the required value of `[agent].timeout_sec`, or both.

**Downstream actions that stay blocked.** Choosing the integer for `[agent].timeout_sec` and `[verifier].timeout_sec` as if one page had repealed the other; claiming an 8-hour acceptance rollout is satisfied by a 18000-second task timeout; copying 8 hours into the suffix.

**PROVISIONAL.** Any integer placed in `timeout_sec` is a human choice recorded as provisional against this conflict. The suffix `N` matches that integer because the suffix check says so, not because the 8-hour sentence was rejected. Do not describe the choice as the resolved timeout.

## C-REUPLOADS

**Status:** `UNRESOLVED`.

**Statement A.** Page 20, limits table: “Reuploads (new versions) per task” = `7`.

**Statement B.** The paragraph on the same page, under that table: “with only 3 reuploads per task.” Page 16, end of the static checks: “one of your three reuploads.” Page 19, end of the rubric: “your 3 reuploads.” Page 21, troubleshooting: “You hit 3 versions for that task.”

**Why this is not supersession.** The table and the paragraph under it disagree on one page. The paragraph does not say the table is obsolete. The earlier “three” sentences do not say the table is wrong. The later “three” sentence does not win because it is later.

**Practical consequences.** Planning on 7 can be stopped at version 3. Planning on 3 can leave versions unused, or can abandon a task the table would still allow. Telling an author they “have three” or “have seven” states a counter this PDF does not settle.

**Clarification needed.** Which counter the account enforces, and whether “reuploads,” “versions,” and “unique versions” count the same objects. The hourly limit of 2 unique versions and the daily limit of 5 unique versions are separate cells in the same table and are not contradicted by the “three” sentences. Those two cells still apply.

**Downstream actions that stay blocked.** Uploading a 4th, 5th, 6th, or 7th version as if the count were known; stopping at 3 as if the table were void.

**PROVISIONAL.** None on the count. Still do not upload a ZIP that fails a local static check, Oracle, or NOP. That follows “arrive green” and immutable versions (`C-REUPLOAD-FREELY`), which do not choose 3 or 7.

## C-ACCOUNT-LIMITS

**Status:** `UNRESOLVED`.

**Statement A.** Page 20 table: “Total submissions” = `1 (account-wide)`.

**Statement B.** Same table: “Task creation limit” = `2 tasks`.

**Why this is not supersession.** They are adjacent cells. The PDF does not define “submission” or say that it is a different object from a created task.

**Practical consequences.** Creating a second task can violate statement A if a submission is a task. Refusing a second task can violate statement B if the creation limit is the operative cap.

**Clarification needed.** What a submission counts, and whether the creation limit and the submission limit apply to the same action.

**Downstream actions that stay blocked.** Creating the first platform task and creating a second one, until the account UI or the operator states the remaining quota. Quote that statement in the decision log. Do not treat either cell as repealed.

**PROVISIONAL.** None.

## C-FOUR-CRITERIA

**Status:** `UNRESOLVED`.

**Statement A.** Page 26: “A task is considered accepted only once it clears all four criteria and is merged following this pipeline — not upon submission or upon passing static checks alone.”

**Statement B.** Pages 25–26 list six bullets under the pipeline: static checks, implementation rubric review, Docker / Oracle / No-op validation, maintainer review, agent and cheat trials, and the hacker–fixer loop. The acceptance section also has the headings “Taxonomy & Volume,” “Model-Breaking Difficulty and Solvability Gates,” and “Review Pipeline Compliance.”

**Why this is not supersession.** “Four” does not identify which four. The six bullets do not say they are the four. The three headings are not four either.

**What does apply without resolving the count.** The closing clause is not in conflict with the bullets: acceptance is not submission, and it is not static checks alone.

**Clarification needed.** Which four criteria the sentence counts.

**Downstream actions that stay blocked.** Declaring a task accepted. Checking off a private subset of four bullets as “the four.”

**PROVISIONAL.** None. Do not call the task accepted. Do not drop a printed bullet because the word is “four.”

## C-TB3-LABEL

**Status:** `UNRESOLVED`.

**Statement A.** Page 9, G02 title in the prose: “Harbor + TB4 contract.” The document title is Terminal Bench 4.

**Statement B.** Pages 10–11 screenshots label that gate “Harbor + TB3” and prefix rules `TB3.`. Page 22: “We follow the official taxonomy of Terminal Bench 3.” Page 7: difficulty, turn count, category distribution, and instruction style must align with “Terminal-Bench 3/4.”

**Why this is not supersession.** No sentence says the screenshot’s TB3 prefix is a mistake, or that the TB3 taxonomy sentence is leftover. “3/4” names both.

**Practical consequences.** Renaming a live `TB3.*` rule to `TB4.*` in the evidence pack hides the id the UI showed. Ignoring the TB3 taxonomy because the workflow is titled TB4 drops a sentence the PDF states. Treating every TB3 label as the current contract name drops the G02 prose title.

**Clarification needed.** Whether the running gate is the TB4 contract described in prose, the TB3-labeled checker in the screenshot, or both.

**Downstream actions that stay blocked.** Asserting a single product generation for the checker. When a receipt shows `TB3.*`, archive that id as printed.

**PROVISIONAL.** None. Follow the taxonomy table for categories because page 22 says to follow that taxonomy. That is that sentence’s own scope. It does not rename G02.

## C-HEADINGS

**Status:** `COMPATIBLE`.

**Statement A.** Rubric D, “Clear and well-written”: the instruction is unambiguous, well-structured, and free of contradictions. The rubric does not define “well-structured” as markdown headings.

**Statement B.** Page 7, §4.2: a description in tidy markdown structure, with the example `##` headings, together with excessive length, is taken as “pure LLM synthesis without human review” and is non-compliant.

**Why there is no winner to pick.** Statement B forbids a stated shape. Statement A does not require that shape. Reading “well-structured” as “add `##` headings” would create a conflict the PDF does not state.

**Apply both as written.** Do not use tidy `##` headings or excessive length in the task description. Keep the instruction unambiguous and free of contradictions. Do not add headings in order to satisfy “well-structured.”

## C-REWARD-LITERAL

**Status:** `COMPATIBLE` for the local Oracle and NOP commands. The platform result of a partial NOP reward is `UNRESOLVED`.

**Statement A.** Page 8, §4.3: `test.sh` writes the final reward “(1 pass / 0 fail)” to `/logs/verifier/reward.txt`.

**Statement B.** Page 8, §4.4 table: Oracle expected reward `1.0`; NOP expected reward `0.0`.

**Statement C.** Page 9, G05: “Oracle must score 1.0 and exit cleanly; NOP must not score 1.0.” The reward must be found, parseable, unambiguous, and finite. Screenshots list `NOP.FULL_REWARD` and `NOP.PARTIAL_REWARD`. Their severity badges could not be reliably paired with the rows (`U-SEVERITY-ALIGNMENT`).

**Why the local commands are compatible.** Section 4.4 states the expected local result of the two commands it names: Oracle `1.0`, NOP `0.0`. “1 pass / 0 fail” is the same section’s description of the reward file. The PDF does not say these are different required numbers. G05’s “score 1.0” matches the Oracle cell.

**What stays unresolved.** G05 says NOP must not score 1.0. The local table says the expected NOP result is 0.0. A partial NOP reward is between those sentences. The PDF does not say whether `NOP.PARTIAL_REWARD` rejects the task. Choosing 0.0 because it is stricter would decide that platform question. The local table can still be followed for the local command without that decision.

**Apply.** Local `harbor run --path . --agent oracle` is expected to show reward `1.0`. Local `harbor run --path . --agent nop` is expected to show reward `0.0`. That is what §4.4 says those commands should produce. Do not describe 0.0 as a platform rule stronger than G05. If a receipt says the parser wanted a different literal, archive the receipt. Do not invent the literal in advance.

**Downstream that remains open.** Whether a NOP reward other than 1.0 and other than 0.0 fails Stage 1.

## C-EXPERT-TIME

**Status:** the form field is defined. The meaning of `expert_time_estimate_hours` is `UNRESOLVED`.

**Statement A.** Page 3, §3.2, and the page 4 screenshot: Expert time is hours, “what an expert should need to build the task, not what you spent writing the proposal.” The screenshot helper says the estimate is “what an expert should need, not what you spent writing this.”

**Statement B.** Page 3, §3.1, Solvable: implementable “in a few hours by an expert who knows the answer.”

**Statement C.** Pages 8 and 15: `expert_time_estimate_hours` is required metadata. The PDF does not say whether that field is build time, solve time, or another quantity.

**Why A and B are not a conflict.** They name different activities. Build time and solve time can both be true. Copying one number into the other silently would erase that difference.

**Apply.** The proposal form’s Expert time is build time, as statement A defines it. Do not put drafting time there. Do not assume the toml field is the same number.

**Clarification needed.** What `expert_time_estimate_hours` measures.

**Downstream actions that stay blocked.** Filling `expert_time_estimate_hours` as if the form definition had been copied onto it.

**PROVISIONAL.** If a number is written into the toml field before clarification, `difficulty_explanation` must say which quantity the author intends, and the decision log must mark that label provisional. An empty default still fails `check-task-fields`, which requires the field and does not define it.

## What this audit did not consult

No external URL, Harbor repository, platform ticket, or copy of `TASK_REVIEW_AUTOMATION.md` was used. Audit date: 2026-11-03. Authority for every quote above is the PDF only. Unavailable references are in `UNAVAILABLE-SOURCES.md`.
