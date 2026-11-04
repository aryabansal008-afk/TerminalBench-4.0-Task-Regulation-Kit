# Requirements register

Extracted from `Freelancers _ Thanos _ Guidelines.pdf` (26 pages).
Each row is one requirement. Platform rule IDs come from the Stage 1 screenshots and are catalogued, not guessed.
Obligation classes are defined in `00-source/HOW-TO-READ.md`. Conflicts are decided only in `00-source/CONFLICT-REGISTER.md`.

Count: 331.

| Obligation | Rows |
| --- | --- |
| mandatory | 138 |
| conditional | 41 |
| advisory | 10 |
| platform | 123 |
| unresolved | 14 |
| example | 5 |

Regenerate with `python3 tools/build_register.py`.

## REQ-W-001
- obligation: mandatory
- scope: task
- stages: all
- source: p.1 opening
- section: Opening
- explained_in: 09-verifier/VERIFIER.md
- compliance_check: Rubric groups A–E and Oracle 1.0 / NOP 0.0.
- evidence: oracle.txt; nop.txt; rubric-review.md
- contradiction_or_rejection_risk: A lenient verifier or a leaked solution fails G05 or rubric A/C.
- requirement: A TB4 task is a hard, self-contained terminal task with a clean solution and a strict verifier.

## REQ-W-002
- obligation: mandatory
- scope: process
- stages: proposal,package
- source: p.1 opening
- section: Opening
- explained_in: 16-evidence-and-handoff/EVIDENCE.md
- compliance_check: No Discord step is used. The evidence pack contains platform receipts rather than chat logs.
- evidence: proposal-receipt.txt; stage1.txt
- contradiction_or_rejection_risk: Following the legacy Discord path on pp. 20–21 misses the grant and blocks upload.
- requirement: The whole workflow lives on one platform: submit the proposal there, read the verdict there, and upload the ZIP only against a grant.

## REQ-W-003
- obligation: mandatory
- scope: process
- stages: all
- source: p.1 opening
- section: Opening
- explained_in: 00-source/CONFLICT-REGISTER.md
- compliance_check: The decision log does not depend on a Discord DM.
- evidence: decision-log.md
- contradiction_or_rejection_risk: C-DISCORD. The troubleshooting table still tells the author to enable Discord DMs. That path is superseded.
- requirement: There is no Discord step in this workflow.

## REQ-W-004
- obligation: unresolved
- scope: task
- stages: build,package
- source: p.1 opening; p.2 step 4; p.13 §7
- section: Opening / journey / checklist
- explained_in: 00-source/CONFLICT-REGISTER.md
- compliance_check: A provisional C-CANARY decision is in the decision log. No canary string was invented. The conflict stays open until a Stage 1 receipt shows whether a TB3.CANARY_* rule fired.
- evidence: decision-log.md; checker-report.txt
- contradiction_or_rejection_risk: C-CANARY. The opposite instruction is REQ-W-005. The Stage 1 UI still shows TB3.CANARY_MISSING, TB3.CANARY_FORMAT, and TB3.CANARY_ADVISORY.
- requirement: Do not add canary comment lines to files, and do not look for a canary_string field at upload. Nothing issues one and nothing asks for one. Journey step 4: no canary lines. Checklist: no canary lines anywhere.

## REQ-W-005
- obligation: unresolved
- scope: task
- stages: build,package
- source: p.6 §4; p.8 §4.3; p.15 intro; p.21 checklist; p.25 pipeline
- section: Build / static intro / legacy checklist / acceptance
- explained_in: 00-source/CONFLICT-REGISTER.md
- compliance_check: Do not invent a canary. A provisional decision is recorded. This row stays open until a Stage 1 receipt shows whether TB3.CANARY_MISSING or TB3.CANARY_FORMAT fired. Section 4 of this PDF does not define a canary format.
- evidence: decision-log.md; stage1.txt
- contradiction_or_rejection_risk: C-CANARY. U-CANARY-FORMAT. Adding a homemade canary violates REQ-W-004. Omitting one may fail the UI rules if they are still enforced.
- requirement: Conflicting instruction: build 'with your canary in hand'; example tree comment 'Canary on line 1'; 'Canary in every file (Section 4)'; static-check intro says checks catch a missing canary; legacy checklist requires a canary comment in every text file (instruction.md, task.toml, environment/Dockerfile, all of solution/ and tests/) and the canary_string field at upload; acceptance static checks include canary strings.

## REQ-W-006
- obligation: mandatory
- scope: process
- stages: all
- source: p.1 §0
- section: The TB4 document set
- explained_in: 00-source/INVENTORY.md
- compliance_check: The author uses both companion sections, not only the narrative guide.
- evidence: rubric-review.md; checker-report.txt
- contradiction_or_rejection_risk: Skipping the rubric because static checks passed is explicitly the wrong split: static checks do not judge quality.
- requirement: Keep the three-document set: this proposal guide, the Static Checks Reference, and the Rubric Review Reference. In this PDF they are pages 1–14, 15–16, and 17–19.

## REQ-W-007
- obligation: mandatory
- scope: process
- stages: proposal
- source: p.1 change table
- section: What changed
- explained_in: 04-proposal/PROPOSAL.md
- compliance_check: The receipt shows revision 1 or a later revision, not a locally invented approval.
- evidence: proposal-receipt.txt
- contradiction_or_rejection_risk: Building before submission repeats the retired TB1/TB2 habit the table forbids.
- requirement: Start by clicking New proposal and submitting it. Submitting writes revision 1 and dispatches its review in one step.

## REQ-W-008
- obligation: mandatory
- scope: process
- stages: proposal
- source: p.1 change table
- section: The decision
- explained_in: 04-proposal/PROPOSAL.md
- compliance_check: The evidence pack contains all three, not a bot reaction or a DM.
- evidence: proposal-receipt.txt
- contradiction_or_rejection_risk: C-DISCORD.
- requirement: The decision is a review run on the platform: a verdict per criterion, an overall verdict, and a written final analysis the author can read in full.

## REQ-W-009
- obligation: mandatory
- scope: process
- stages: self-test
- source: p.1–2 change table
- section: Self-testing
- explained_in: 11-validation/VALIDATION.md
- compliance_check: Both reports exist and predate the ZIP SHA-256.
- evidence: checker-report.txt; rubric-review.md; sha256.txt
- contradiction_or_rejection_risk: Uploading to discover mechanical failures spends a scarce version. C-REUPLOADS.
- requirement: Before uploading, the author runs the static checks AND the rubric review. The rubric review may be run with free / open-source LLMs.

## REQ-W-010
- obligation: mandatory
- scope: task
- stages: package,stage1
- source: p.2 change table
- section: Submission
- explained_in: 14-platform-review/STAGE-1.md
- compliance_check: One ZIP SHA-256 is bound to one grant revision. Stage 1 starts without a separate trigger.
- evidence: sha256.txt; stage1.txt
- contradiction_or_rejection_risk: Uploading without a grant is impossible (button inactive) and uploading a second different task against the same grant is not what this sentence allows.
- requirement: Upload one immutable Harbor task ZIP against the grant. It enters Stage 1 automatically.

## REQ-W-011
- obligation: mandatory
- scope: platform
- stages: stage2
- source: p.2 change table
- section: Difficulty
- explained_in: 14-platform-review/STAGE-2.md
- compliance_check: Stage 2 evidence shows the two predicates. Stage 2 was not entered on a ZIP that failed Stage 1.
- evidence: stage1.txt; stage2.txt
- contradiction_or_rejection_risk: C-AGENT-TRIALS is superseded. C-LEGACY-CARDS remains open for cheat trials. Treating a local dry-run as the difficulty gate does not satisfy Stage 2.
- requirement: Difficulty is Stage 2 model rollout, entered only after Stage 1 is accepted. Difficulty and long-horizon gates are decided as verdict predicates, not as one 'Agent Trials' card.

## REQ-W-012
- obligation: mandatory
- scope: task
- stages: package,stage1
- source: p.2 change table
- section: Fixing issues
- explained_in: 14-platform-review/STAGE-1.md
- compliance_check: The version label and the full Stage 1 result are archived for every upload. Local checks passed before each upload.
- evidence: stage1.txt; checker-report.txt
- contradiction_or_rejection_risk: C-REUPLOADS. A red upload is permanently recorded even if a later version passes.
- requirement: Each corrected ZIP becomes a new immutable version (Version N of N) and Stage 1 re-runs against it. Every version is recorded. Arrive green.

## REQ-W-013
- obligation: mandatory
- scope: process
- stages: acceptance
- source: p.2 change table
- section: Final review
- explained_in: 14-platform-review/ACCEPTANCE.md
- compliance_check: acceptance.txt names QC and Super QC separately when they occur. Neither is marked done early.
- evidence: acceptance.txt
- contradiction_or_rejection_risk: U-SUPER-QC. C-LEGACY-CARDS. Stage 3 being deferred is not Super QC.
- requirement: Final review is QC review and then Super QC, a second expert layer.

## REQ-W-014
- obligation: mandatory
- scope: process
- stages: all
- source: p.2 §2
- section: The TB4 journey at a glance
- explained_in: 16-evidence-and-handoff/EVIDENCE.md
- compliance_check: Evidence appears in that order. A later artifact does not predate the grant it depends on.
- evidence: decision-log.md; proposal-receipt.txt; stage1.txt; stage2.txt
- contradiction_or_rejection_risk: Skipping step 5 spends a version. C-CANARY applies to step 4.
- requirement: Follow the eight-step order: (1) proposal with title, category, subcategory, expert time, and markdown; (2) Proposal Review Bot plus duplicate and novelty checks; (3) ACTIVE grant only if accepted and not a duplicate, text frozen; (4) build locally with separate verifier and no canary lines; (5) self-test static checks, rubric, Oracle pass, NOP fail; (6) upload ZIP, G01–G06 and P04 as one job; (7) re-upload until the status reads PASSED STAGE 1; (8) Stage 2 rollouts on a frozen policy decide PASS or FAIL.

## REQ-W-015
- obligation: example
- scope: platform
- stages: stage1
- source: p.2–3 screenshot and caption
- section: Task list
- explained_in: 14-platform-review/STAGE-1.md
- compliance_check: When a task is stopped, the archived blocking reason is the rule id from that column, not a paraphrase.
- evidence: stage1.txt
- contradiction_or_rejection_risk: Fixing a guessed rule instead of the named rule wastes a version.
- requirement: The task list is one row per task. S0 / S1 / S2 marks show how far the task has travelled. The Blocking reason column names the exact rule that stopped a task.

## REQ-PR-001
- obligation: mandatory
- scope: process
- stages: proposal
- source: p.3 §3
- section: Step 1
- explained_in: 04-proposal/PROPOSAL.md
- compliance_check: No Harbor tree is built before the proposal is submitted.
- evidence: proposal-receipt.txt
- contradiction_or_rejection_risk: A polished task whose proposal is later rejected cannot be uploaded.
- requirement: TB4 begins on the platform, not in the editor. Click New proposal, fill the form, and submit. The gate is cheap on purpose so unverifiable, too-easy, or not-worth-building tasks are stopped early.

## REQ-PR-002
- obligation: mandatory
- scope: task
- stages: proposal
- source: p.3 §3.1
- section: What the reviewer grades
- explained_in: 04-proposal/PROPOSAL.md
- compliance_check: The receipt shows a verdict per criterion and one overall verdict. Overall Accept is not claimed if a criterion is Reject.
- evidence: proposal-receipt.txt
- contradiction_or_rejection_risk: An Uncertain on a single criterion is not an acceptance. The p.6 example shows Well-specified REJECT blocking the grant.
- requirement: Every criterion is judged separately, then once overall. A proposal is accepted only if it is correct, solvable, verifiable, well-specified, and hard for an interesting reason.

## REQ-PR-003
- obligation: mandatory
- scope: task
- stages: proposal
- source: p.3 §3.1
- section: Verifiable
- explained_in: 04-proposal/PROPOSAL.md
- compliance_check: The proposal states a programmatic check. The later tests are deterministic and not an LLM judge.
- evidence: proposal.md; tests/
- contradiction_or_rejection_risk: Subjective or aesthetic grading is an outright reject.
- requirement: Verifiable means a program separates correct from incorrect, and any other reasonable verifier would agree. Subjective grading is rejected outright.

## REQ-PR-004
- obligation: mandatory
- scope: task
- stages: proposal,build
- source: p.3 §3.1
- section: Well-specified
- explained_in: 04-proposal/PROPOSAL.md
- compliance_check: A second reading of the proposal and of instruction.md produces the same graded fields the tests assert.
- evidence: proposal.md; instruction.md; tests/
- contradiction_or_rejection_risk: The problem-statement restatement is the platform's second reader. Mismatch means not well-specified.
- requirement: Everything the verifier checks is stated. Two readers should independently write verifiers that agree.

## REQ-PR-005
- obligation: mandatory
- scope: task
- stages: proposal,build
- source: p.3 §3.1
- section: Solvable
- explained_in: 03-difficulty-and-horizon/DESIGN.md
- compliance_check: The reference solution exists and Oracle scores 1.0. The proposal argues existence before the grant.
- evidence: proposal.md; oracle.txt
- contradiction_or_rejection_risk: C-EXPERT-TIME. This few-hours figure is solve time, not the form's build-time expert estimate.
- requirement: Give a solution or a convincing argument one exists. It is implementable in a few hours by an expert who knows the answer.

## REQ-PR-006
- obligation: mandatory
- scope: task
- stages: proposal,stage2
- source: p.3 §3.1
- section: Difficult
- explained_in: 03-difficulty-and-horizon/DESIGN.md
- compliance_check: difficulty_explanation names the expertise. A few-days undergraduate shape is redesigned before proposal.
- evidence: proposal.md; task.toml
- contradiction_or_rejection_risk: Busywork volume does not satisfy this row and fails the later horizon guidance against padding.
- requirement: Difficulty is years of domain expertise, not volume of work. Anything an average undergraduate could finish in a few days is too easy.

## REQ-PR-007
- obligation: mandatory
- scope: task
- stages: proposal
- source: p.3 §3.1
- section: Interesting
- explained_in: 03-difficulty-and-horizon/DESIGN.md
- compliance_check: The proposal names who does the work and why. Obscurity is not the difficulty claim.
- evidence: proposal.md
- contradiction_or_rejection_risk: A contrived puzzle fails Interesting and later fails rubric Real-world relevance.
- requirement: Someone could be paid to do this, or a real group wants it solved. Obscure for its own sake does not count.

## REQ-PR-008
- obligation: mandatory
- scope: task
- stages: proposal,build
- source: p.3 §3.1
- section: Outcome-verified
- explained_in: 05-instruction/INSTRUCTION.md
- compliance_check: The proposal and instruction.md do not list the steps or the required tool chain. Tests grade the artifact.
- evidence: proposal.md; instruction.md; tests/
- contradiction_or_rejection_risk: The form says enumerating steps reads as overspecification and costs this criterion.
- requirement: Grade the final state, not the route taken. No prescribed tools and no enumerated step lists.

## REQ-PR-009
- obligation: mandatory
- scope: task
- stages: proposal
- source: p.3 §3.2; p.4 screenshot
- section: Submission form
- explained_in: 04-proposal/PROPOSAL.md
- compliance_check: The submitted receipt shows all five populated.
- evidence: proposal-receipt.txt
- contradiction_or_rejection_risk: An empty field is a form failure before the criteria are even graded.
- requirement: The form has five fields and all five matter: TITLE, CATEGORY, SUBCATEGORY, EXPERT TIME, PROPOSAL MARKDOWN.

## REQ-PR-010
- obligation: mandatory
- scope: task
- stages: proposal
- source: p.3 §3.2; p.4 screenshot
- section: Title
- explained_in: 04-proposal/PROPOSAL.md
- compliance_check: The title and the proposal body name one task.
- evidence: proposal.md
- contradiction_or_rejection_risk: The p.6 reject example failed task identity: title and category were a fixed-point DSP filter while the body was Rust ledger recovery.
- requirement: Title is a specific, descriptive task name. Placeholder: 'What the task asks for, in one line.' The title must describe the same task as the body.

## REQ-PR-011
- obligation: mandatory
- scope: task
- stages: proposal,build
- source: p.3 §3.2
- section: Category
- explained_in: 01-taxonomy-and-batch/TAXONOMY.md
- compliance_check: The value is exactly one of those seven strings in the form and in task.toml.
- evidence: proposal-receipt.txt; task.toml
- contradiction_or_rejection_risk: TB3.CATEGORY_INVALID. Category is locked at creation (REQ-LM-006).
- requirement: Category is one of Science, Software, ML, Operations, Security, Hardware, Media.

## REQ-PR-012
- obligation: mandatory
- scope: task
- stages: proposal,build
- source: p.3 §3.2
- section: Subcategory
- explained_in: 01-taxonomy-and-batch/TAXONOMY.md
- compliance_check: Subcategory is on the receipt and in task.toml. A custom value has a written reason that no listed subcategory fit.
- evidence: proposal-receipt.txt; task.toml; decision-log.md
- contradiction_or_rejection_risk: TB3.SUBCATEGORY_INVALID. U-SUBCATEGORY-KEY for the TOML key spelling.
- requirement: Choose the closest listed subcategory. If none fits, enter a broad, reusable one. Custom values remain valid. Category and subcategory are stored on every revision and the reviewer reads both.

## REQ-PR-013
- obligation: mandatory
- scope: task
- stages: proposal
- source: p.3 §3.2; p.4 screenshot
- section: Expert time
- explained_in: 04-proposal/PROPOSAL.md
- compliance_check: The form value is a build-time estimate. difficulty_explanation states that this is distinct from solve time.
- evidence: proposal-receipt.txt; task.toml
- contradiction_or_rejection_risk: C-EXPERT-TIME.
- requirement: Expert time is in hours. It is what an expert should need to build the task, not what was spent writing the proposal. Screenshot helper: 'The estimate is what an expert should need, not what you spent writing this.'

## REQ-PR-014
- obligation: mandatory
- scope: process
- stages: proposal
- source: p.3 §3.2; p.4 screenshot
- section: Proposal markdown
- explained_in: 04-proposal/PROPOSAL.md
- compliance_check: The archived markdown matches the preview that was submitted. No local edit is described as a change to that revision.
- evidence: proposal.md; proposal-receipt.txt
- contradiction_or_rejection_risk: Editing the proposal in place is impossible; a silent local drift fails the later match to the frozen text.
- requirement: Use the Write / Preview toggle and check the preview before submitting. Submitting writes the first immutable revision and dispatches its review in one step. There is nothing else to do afterwards but wait.

## REQ-PR-015
- obligation: mandatory
- scope: task
- stages: proposal
- source: p.4 screenshot
- section: Form instruction
- explained_in: 04-proposal/PROPOSAL.md
- compliance_check: tools/check_proposal.py reports 2 or 3 paragraphs and no headings. The first paragraph states the goal and the graded output.
- evidence: checker-report.txt; proposal.md
- contradiction_or_rejection_risk: A heading outline can also trip the LLM-fingerprint rule on p.7.
- requirement: Two or three paragraphs is the target. State the goal up front, then everything the verifier will check — nothing left to guessing. Do not enumerate the steps the agent must follow; that reads as overspecification and costs the outcome-verified criterion.

## REQ-PR-016
- obligation: mandatory
- scope: task
- stages: proposal
- source: p.4 §3.3
- section: Length
- explained_in: tools/check_proposal.py
- compliance_check: tools/check_proposal.py character count is strictly less than 2000.
- evidence: checker-report.txt
- contradiction_or_rejection_risk: Over 2000 is a hard miss even if the content is otherwise strong.
- requirement: Keep the proposal under 2000 characters.

## REQ-PR-017
- obligation: mandatory
- scope: task
- stages: proposal
- source: p.4 §3.3
- section: Summary and objective
- explained_in: 04-proposal/PROPOSAL.md
- compliance_check: The proposal contains an absolute output path and a type.
- evidence: proposal.md
- contradiction_or_rejection_risk: A missing path makes the later instruction and the verifier disagree.
- requirement: Describe the core scenario in plain language and the exact deliverable: the precise output file path and type the agent must produce (example shape /app/report.json).

## REQ-PR-018
- obligation: mandatory
- scope: task
- stages: proposal
- source: p.4 §3.3
- section: Environment and inputs
- explained_in: 07-agent-environment/ENVIRONMENT.md
- compliance_check: The proposal's inputs match environment/Dockerfile.
- evidence: proposal.md; environment/Dockerfile
- contradiction_or_rejection_risk: An input named only in the proposal and missing from the image fails 'Solvable from instruction alone' later.
- requirement: Describe what the agent starts with (binaries, a repo, datasets, log files, an API) and any helper tools or pinned engines pre-installed in the container.

## REQ-PR-019
- obligation: mandatory
- scope: task
- stages: proposal
- source: p.4 §3.3
- section: Why it is hard
- explained_in: 03-difficulty-and-horizon/GENUINE-COMPLEXITY.md
- compliance_check: The proposal names the naive approach and the mechanical reason it fails. complexity.md names that approach and at least one more, each tied to an instruction sentence. Neither file says the task has passed a difficulty gate.
- evidence: complexity.md; proposal.md
- contradiction_or_rejection_risk: Vague 'it is hard' tends to score Uncertain or get rejected. Sounding complex is not a measurement.
- requirement: Describe the anti-AI trap: the naive approach an LLM tries first, and exactly why that lazy approach fails. Spell out the real source of difficulty. Source examples: cross-source correlation, adversarial noise, cascading errors.

## REQ-PR-020
- obligation: mandatory
- scope: task
- stages: proposal,build
- source: p.4 §3.3
- section: Verification and grading
- explained_in: 09-verifier/VERIFIER.md
- compliance_check: The proposal's check count and method match tests/. No LLM judge is used.
- evidence: proposal.md; tests/
- contradiction_or_rejection_risk: A single exact-value check on a public constant does not stop hardcoding.
- requirement: State how correctness is checked deterministically (no LLM judges), how many checks, and how the agent is stopped from hardcoding the answer. Source examples: fresh/frozen fixtures, exact-value checks.

## REQ-PR-021
- obligation: mandatory
- scope: task
- stages: proposal
- source: p.4 §3.3
- section: Real-world relevance and feasibility
- explained_in: 03-difficulty-and-horizon/DESIGN.md
- compliance_check: The proposal names the worker and the build-versus-existing status.
- evidence: proposal.md
- contradiction_or_rejection_risk: A demo or toy fails this row and the p.7 industrial-scenario rule.
- requirement: State who actually does this work and why it matters, and whether the data and environment already exist or must be built.

## REQ-PR-022
- obligation: mandatory
- scope: task
- stages: proposal
- source: p.4 §3.3
- section: Why it is distinct
- explained_in: 04-proposal/PROPOSAL.md
- compliance_check: The sentence names a concrete difference, not a synonym.
- evidence: proposal.md
- contradiction_or_rejection_risk: Surface-level changes are not enough when novelty fails. U-DUPLICATE-THRESHOLD.
- requirement: Include a sentence on how the task differs from existing TB tasks and from obvious public problems. This is input to the novelty and duplicate gates.

## REQ-PR-023
- obligation: advisory
- scope: task
- stages: proposal
- source: p.4 §3.3 tip
- section: Tip
- explained_in: 04-proposal/PROPOSAL.md
- compliance_check: Those three items are specific nouns and paths, not adjectives.
- evidence: proposal.md
- contradiction_or_rejection_risk: Uncertain returns the task to 'Proposal rejected — revise proposal'.
- requirement: The more concretely the deliverable, the inputs, and the difficulty are described, the more reliably the bot can judge the proposal. Vague proposals tend to score Uncertain or get rejected.

## REQ-PR-024
- obligation: mandatory
- scope: process
- stages: proposal
- source: p.4–5 §3.4
- section: Verdict
- explained_in: 04-proposal/PROPOSAL.md
- compliance_check: The archived verdict uses those values.
- evidence: proposal-receipt.txt
- contradiction_or_rejection_risk: Do not treat a missing verdict as Accept.
- requirement: The review returns a verdict per criterion and one overall verdict. The visible values are Accept, Uncertain, and Reject.

## REQ-PR-025
- obligation: mandatory
- scope: process
- stages: proposal
- source: p.5 §3.4
- section: Final analysis and problem statement
- explained_in: 04-proposal/PROPOSAL.md
- compliance_check: The evidence pack notes the comparison. A mismatch triggers a revision.
- evidence: proposal-receipt.txt; decision-log.md
- contradiction_or_rejection_risk: Building the author's private intent instead of the restatement diverges from the granted text.
- requirement: Read the Final analysis and the Problem statement, as reviewed, which is the reviewer's restatement. If it does not match what was meant, the proposal is not yet well-specified, whatever the verdict says.

## REQ-PR-026
- obligation: mandatory
- scope: process
- stages: grant,package
- source: p.5 §3.5; p.5 screenshot
- section: Grant
- explained_in: 14-platform-review/STAGE-1.md
- compliance_check: The receipt says GRANT ACTIVE before packaging. The ZIP is tied to that revision.
- evidence: proposal-receipt.txt; sha256.txt
- contradiction_or_rejection_risk: Upload Harbor task ZIP stays inactive until an ACTIVE grant exists.
- requirement: When a proposal is accepted, an ACTIVE grant is recorded for that revision. The grant is the permission to upload. One immutable task ZIP version may be uploaded against it, and its checks begin at Stage 1. Screenshot: 'An ACTIVE grant is recorded for this revision; one immutable task ZIP version may be uploaded. Its checks begin at Stage 1.'

## REQ-PR-027
- obligation: mandatory
- scope: task
- stages: grant,build
- source: p.5 §3.5
- section: Frozen proposal
- explained_in: 04-proposal/PROPOSAL.md
- compliance_check: The built instruction still implements the frozen text. A material change is a new proposal, not an edit.
- evidence: proposal.md; decision-log.md
- contradiction_or_rejection_risk: Legacy 'Proposal Match FAILED' includes divergence from the approved proposal even aside from canaries.
- requirement: The proposal text is frozen at the grant. The revision that was granted is the one the task is judged against. To change the proposal materially, create a new task.

## REQ-PR-028
- obligation: platform
- scope: process
- stages: grant
- source: p.5 §3.5
- section: Suspend or revoke
- explained_in: 04-proposal/PROPOSAL.md
- compliance_check: If the grant is not ACTIVE, no ZIP is uploaded. The reason is archived if shown.
- evidence: proposal-receipt.txt
- contradiction_or_rejection_risk: Uploading after revocation fails closed.
- requirement: An administrator can suspend or revoke a grant. Either closes Stage 1 upload and is recorded with their reason.

## REQ-PR-029
- obligation: mandatory
- scope: process
- stages: proposal
- source: p.5 §3.6; p.6 screenshot
- section: Revise
- explained_in: 04-proposal/PROPOSAL.md
- compliance_check: The new revision number is higher. The failed criterion is answered in the new text.
- evidence: proposal-receipt.txt
- contradiction_or_rejection_risk: Resubmitting the same text does not address the criterion.
- requirement: If the proposal is rejected or uncertain, the status becomes 'Proposal rejected — revise proposal'. Read the final analysis, address the specific criterion that failed, and submit a revised proposal. Revisions are numbered and immutable. Nothing already submitted is edited in place. Screenshot: 'No grant was issued, so Stage 1 remains closed until a revised proposal is accepted.'

## REQ-PR-030
- obligation: mandatory
- scope: account
- stages: proposal
- source: p.6 screenshot
- section: Ownership
- explained_in: 04-proposal/PROPOSAL.md
- compliance_check: The owning expert submits the revision. An admin edit is not assumed.
- evidence: proposal-receipt.txt
- contradiction_or_rejection_risk: Waiting for an administrator to rewrite the proposal leaves Stage 1 closed.
- requirement: Only the expert who owns the task can submit a revision. Administrators can inspect the task but cannot revise it for the owner.

## REQ-PR-031
- obligation: unresolved
- scope: platform
- stages: proposal
- source: p.20 troubleshooting
- section: Duplicate
- explained_in: 00-source/UNRESOLVED.md
- compliance_check: A duplicate block is answered with a substantive change. No similarity score is invented.
- evidence: proposal-receipt.txt
- contradiction_or_rejection_risk: U-DUPLICATE-THRESHOLD.
- requirement: A proposal can be blocked (red) despite a good rubric verdict when a duplicate is detected because similarity is above threshold. The idea already exists and must be reworked into something genuinely distinct. The numeric threshold is not stated.

## REQ-PR-032
- obligation: mandatory
- scope: task
- stages: proposal
- source: p.20 troubleshooting
- section: Novelty
- explained_in: 04-proposal/PROPOSAL.md
- compliance_check: The distinctness sentence and the actual mechanism both change before resubmission.
- evidence: proposal.md
- contradiction_or_rejection_risk: Renaming files or swapping a dataset synonym will be rejected again.
- requirement: A proposal rejected for novelty is semantically the same as an existing task. Surface-level changes are not enough.

## REQ-PR-033
- obligation: example
- scope: task
- stages: proposal
- source: p.5–6 screenshots
- section: Review receipt fields
- explained_in: 00-source/UNRESOLVED.md
- compliance_check: Archive whatever the receipt shows. Do not add images to chase an undefined ratio.
- evidence: proposal-receipt.txt
- contradiction_or_rejection_risk: U-IMAGES-RCA.
- requirement: Observed receipt fields include REVISION, REVIEW RUN, GENERATION, and IMAGES R / C / A. The printed examples show 0 / 0 / 0. The letters are not defined.

## REQ-PR-034
- obligation: advisory
- scope: task
- stages: proposal
- source: p.5–6 screenshots
- section: Client-fit note
- explained_in: 04-proposal/PROPOSAL.md
- compliance_check: The proposal would survive that note. The heading 'Client-fit' is not added to the proposal.
- evidence: proposal.md
- contradiction_or_rejection_risk: This is observed reviewer practice, not a seventh named criterion. Interesting and the p.7 industrial rule still apply.
- requirement: Review examples include a Client-fit note: supported industrial purpose, not a toy, contest problem, or mathematical exercise, with inputs and deliverables that match the purpose.

## REQ-BD-001
- obligation: mandatory
- scope: task
- stages: build
- source: p.6 §4
- section: Separate verifier
- explained_in: 06-harbor-task/LAYOUT.md
- compliance_check: environment/Dockerfile does not copy tests/ or solution/. Ground truth is only in the verifier image. environment_mode is separate.
- evidence: environment/Dockerfile; tests/Dockerfile; task.toml
- contradiction_or_rejection_risk: Ground truth in the agent image fails Answer not leaked and the isolation claim.
- requirement: Tests live in their own container that runs after the agent's container is torn down, so the agent can never read or tamper with tests, solution, or ground-truth data.

## REQ-BD-002
- obligation: advisory
- scope: task
- stages: build
- source: p.6 §4.1
- section: More than five files
- explained_in: 06-harbor-task/LAYOUT.md
- compliance_check: The tree has the fixtures and verifier files the task actually needs, not empty extras.
- evidence: task tree
- contradiction_or_rejection_risk: Padding the tree with unused files does not create difficulty and can trip archive-size rules.
- requirement: A real TB4 task usually has more than a handful of files: input fixtures, a multi-file solution, and a real verifier image. That is expected and encouraged.

## REQ-BD-003
- obligation: example
- scope: task
- stages: build
- source: pp. 6–7 §4.1
- section: Example tree
- explained_in: 06-harbor-task/LAYOUT.md
- compliance_check: New tasks copy the pattern, not the DFIR filenames, unless the task is that task.
- evidence: task tree
- contradiction_or_rejection_risk: Shipping access.log and reconstruction_spec.md in an unrelated task fails the frozen-proposal match.
- requirement: The DFIR layout (instruction.md, task.toml, environment/Dockerfile, environment/data/..., solution/solve.sh, solution/solve.py, tests/Dockerfile, tests/test.sh, tests/test_outputs.py) shows the kinds of extra files. It is one task's layout, not the universal file list.

## REQ-BD-004
- obligation: advisory
- scope: task
- stages: build
- source: p.7 §4.1
- section: Solution split
- explained_in: 09-verifier/VERIFIER.md
- compliance_check: If the reference logic exceeds about 20 lines, it is not all inline in solve.sh.
- evidence: solution/solve.sh; solution/solve.py
- contradiction_or_rejection_risk: A short solve.sh-only solution is allowed. The oracle entry point the guide names is still solve.sh.
- requirement: The preferred pattern for anything longer than about 20 lines is solve.sh as a thin launcher that runs python3 /solution/solve.py, with the reference logic in solve.py.

## REQ-BD-005
- obligation: mandatory
- scope: task
- stages: build
- source: p.7 §4.1
- section: Agent fixtures
- explained_in: 07-agent-environment/ENVIRONMENT.md
- compliance_check: Every input the instruction names is copied by the agent Dockerfile and is not only on the host.
- evidence: environment/Dockerfile; instruction.md
- contradiction_or_rejection_risk: A missing COPY fails G04 or leaves the agent without the promised input.
- requirement: Input data lives under environment/data/ in the example and is copied into the agent image by environment/Dockerfile.

## REQ-BD-006
- obligation: mandatory
- scope: task
- stages: build
- source: p.7 §4.2
- section: No AI fingerprints
- explained_in: 05-instruction/INSTRUCTION.md
- compliance_check: instruction.md has no markdown headings and is not padded. A human has read it.
- evidence: instruction.md; decision-log.md
- contradiction_or_rejection_risk: C-HEADINGS. Rubric 'well-structured' does not authorize ## headings.
- requirement: Task descriptions must carry no obvious traces of LLM synthesis and must pass human review. A description written in tidy markdown structure (example ## Headings) and excessive length is taken as pure LLM synthesis without human review and judged non-compliant.

## REQ-BD-007
- obligation: mandatory
- scope: task
- stages: build
- source: p.7 §4.2
- section: Instruction length
- explained_in: 05-instruction/INSTRUCTION.md
- compliance_check: tools/check_task.py counts content.split() on the whole instruction file at or under 1500. The draft aims near 267 unless the schema truly needs more.
- evidence: checker-report.txt
- contradiction_or_rejection_risk: The PDF does not say whether the suffix is excluded. Counting the whole file is the conservative reading.
- requirement: The instruction must be concise: word count via content.split() must not exceed 1500. For reference, TB4 averages 267 words, with a maximum of 1406.

## REQ-BD-008
- obligation: mandatory
- scope: task
- stages: build
- source: p.7 §4.2
- section: No steering
- explained_in: 05-instruction/INSTRUCTION.md
- compliance_check: Those phrases and close variants are absent.
- evidence: instruction.md; checker-report.txt
- contradiction_or_rejection_risk: Role prompting is also called out in the p.5 review example as something the final instruction must not add.
- requirement: The instruction contains no leading or suggestive phrasing. Source examples: 'please think step by step,' and 'you are an expert in xxx'.

## REQ-BD-009
- obligation: mandatory
- scope: task
- stages: build
- source: p.7 §4.2; p.8 §4.3
- section: Absolute paths
- explained_in: 05-instruction/INSTRUCTION.md
- compliance_check: check-task-absolute-path and the local checker find no relative path tokens in instruction.md.
- evidence: checker-report.txt
- contradiction_or_rejection_risk: ZIP member absolute paths are a different rule (ZIP.ABSOLUTE_PATH) and are also forbidden.
- requirement: Where paths appear they must be absolute, for example /app/solve.py or /app/data.csv. Relative paths such as ./data.csv or data.csv are prohibited.

## REQ-BD-010
- obligation: mandatory
- scope: task
- stages: proposal,build
- source: p.7 §4.2
- section: Industrial scenario
- explained_in: 03-difficulty-and-horizon/DESIGN.md
- compliance_check: The scenario is a real engineering job. Contest and olympiad premises are rejected before proposal.
- evidence: proposal.md
- contradiction_or_rejection_risk: Software/Algorithms and Science/Math still have to obey this prohibition.
- requirement: Tasks must carry real-world significance and a genuine engineering context. Demos, toy projects, and competitive-programming problems (examples LeetCode and math olympiad problems) are strictly prohibited.

## REQ-BD-011
- obligation: mandatory
- scope: task
- stages: proposal
- source: p.7 §4.2
- section: Not exam-style
- explained_in: 03-difficulty-and-horizon/DESIGN.md
- compliance_check: The difficulty explanation is a real failure mode or engineering constraint, not a constructed riddle.
- evidence: proposal.md; task.toml
- contradiction_or_rejection_risk: Hiding the schema to manufacture hardness is both this row and the Stage 2 fix guidance.
- requirement: All quiz- and contest-style problems — any task built from the premise of inventing a hard problem to test the model — fall outside the scope of this procurement.

## REQ-BD-012
- obligation: mandatory
- scope: batch
- stages: batch,build
- source: p.7 §4.2
- section: Align with TB3/TB4
- explained_in: 01-taxonomy-and-batch/TAXONOMY.md
- compliance_check: The task uses this taxonomy, the instruction rules, and the Stage 2 numeric targets.
- evidence: batch-slot.md; stage2.txt
- contradiction_or_rejection_risk: C-TB3-LABEL. The UI says TB3 in places. The taxonomy page says the official taxonomy of Terminal Bench 3.
- requirement: Difficulty, turn count, category distribution, and instruction style must all align with Terminal-Bench 3/4.

## REQ-BD-013
- obligation: mandatory
- scope: task
- stages: build
- source: p.7 §4.3
- section: Separate verifier declaration
- explained_in: 06-harbor-task/METADATA.md
- compliance_check: check-separate-verifier. In TOML, artifacts is written before any [table] header so it stays top-level.
- evidence: task.toml; tests/Dockerfile; checker-report.txt
- contradiction_or_rejection_risk: A key placed after [verifier] is not top-level and fails the check.
- requirement: Set [verifier] environment_mode = "separate". Declare artifacts = [...] at the top level. The source's example is artifacts = ["/app/"]. tests/Dockerfile copies into /tests and pre-creates artifact directories with RUN mkdir -p.

## REQ-BD-014
- obligation: mandatory
- scope: task
- stages: build
- source: p.7 §4.3
- section: No runtime installs
- explained_in: 07-agent-environment/ENVIRONMENT.md
- compliance_check: tests/test.sh contains none of those install forms. The image build contains the pins.
- evidence: tests/test.sh; tests/Dockerfile
- contradiction_or_rejection_risk: check-trial-network-fetch and TRIAL.PUBLIC_FETCH. This is a stated reward-hacking surface.
- requirement: Bake every dependency (uv, pytest plugins, scoring libs, oracle binaries, ground-truth data) into tests/Dockerfile. apt-get install, pip install, and curl | sh at verify time are flaky and not allowed.

## REQ-BD-015
- obligation: mandatory
- scope: task
- stages: build
- source: p.7 §4.3
- section: Clean agent image
- explained_in: 07-agent-environment/ENVIRONMENT.md
- compliance_check: check-dockerfile-references, extended to the whole tests/ and solution/ trees as the prose requires.
- evidence: environment/Dockerfile
- contradiction_or_rejection_risk: A test-only package in the agent image is a leak and a fingerprint of the grader.
- requirement: environment/Dockerfile must not copy tests/ or solution/, and must not contain test-only dependencies.

## REQ-BD-016
- obligation: mandatory
- scope: task
- stages: build
- source: p.7 §4.3
- section: Pins and nproc
- explained_in: 07-agent-environment/ENVIRONMENT.md
- compliance_check: check-pip-pinning, check-dockerfile-sanity, and check-nproc.
- evidence: checker-report.txt
- contradiction_or_rejection_risk: Bare nproc returns the host CPU count inside a container and causes over-parallel OOM or timeouts.
- requirement: pip/uv installs need ==<version> pins. Do not pin apt packages. Do not call bare nproc.

## REQ-BD-017
- obligation: mandatory
- scope: task
- stages: build
- source: p.7 §4.3; p.16 check-instruction-suffix
- section: Instruction suffix
- explained_in: 05-instruction/INSTRUCTION.md
- compliance_check: The last paragraph equals that sentence for the integer timeout, and the file ends with exactly one newline.
- evidence: instruction.md; checker-report.txt
- contradiction_or_rejection_risk: A mismatched N fails check-instruction-suffix. C-TIMEOUT if someone writes 28800 to chase the 8-hour rollout phrase.
- requirement: instruction.md ends with the exact line 'You have N seconds to complete this task. Do not cheat by using online solutions or hints specific to this task.', where N equals [agent].timeout_sec. The static check adds: as its own paragraph, with a single trailing newline. The quotation marks in the PDF delimit the line; they are not part of it.

## REQ-BD-018
- obligation: mandatory
- scope: task
- stages: build
- source: p.7 §4.3
- section: Behavior tests
- explained_in: 09-verifier/VERIFIER.md
- compliance_check: Tests run or parse the artifact. They do not grep the agent's source for keywords.
- evidence: tests/
- contradiction_or_rejection_risk: A keyword test can be passed without the engineering outcome. Rubric A requires outcome-based grading.
- requirement: Tests verify behaviour, not strings: execute the agent's output and check it. Avoid grep-for-keywords tests — they are gameable.

## REQ-BD-019
- obligation: mandatory
- scope: task
- stages: build,self-test
- source: p.8 §4.3
- section: CTRF and reward
- explained_in: 09-verifier/VERIFIER.md
- compliance_check: The command is recorded. The reward file is written on both pass and fail. See REQ-BD-020 for the 1.0 / 0.0 literal.
- evidence: tests/test.sh; oracle.txt; nop.txt
- contradiction_or_rejection_risk: U-CTRF-FLAG. The PDF does not name the pytest flag or the CTRF report path.
- requirement: test.sh runs pytest with CTRF output and writes the final reward (1 pass / 0 fail) to /logs/verifier/reward.txt.

## REQ-BD-020
- obligation: unresolved
- scope: task
- stages: self-test,stage1
- source: p.8 §4.3–4.4; p.9 G05
- section: Reward literal
- explained_in: 00-source/CONFLICT-REGISTER.md
- compliance_check: Local Oracle reward is 1.0 and local NOP reward is 0.0 because section 4.4 states those expected results. That does not decide whether a partial NOP reward fails G05. See C-REWARD-LITERAL.
- evidence: oracle.txt; nop.txt
- contradiction_or_rejection_risk: C-REWARD-LITERAL. C-NOP-STRICTNESS. If a live parser rejects 1.0, switch to the literal the receipt requires.
- requirement: The CTRF bullet says reward 1 pass / 0 fail. The Oracle table says reward 1.0 and 0.0. G05 says Oracle must score 1.0 and exit cleanly, and NOP must not score 1.0. The reward must be found, parseable, unambiguous, and finite.

## REQ-BD-021
- obligation: mandatory
- scope: task
- stages: build
- source: p.8 §4.3; p.15 check-task-fields
- section: Metadata
- explained_in: 06-harbor-task/METADATA.md
- compliance_check: check-task-fields. None of those values is empty or a placeholder.
- evidence: task.toml; checker-report.txt
- contradiction_or_rejection_risk: G02 also requires subcategory, which this list omits. See REQ-PR-012.
- requirement: Fill in author_name, author_email, difficulty_explanation, solution_explanation, verification_explanation, category, tags, and expert_time_estimate_hours. Empty defaults fail checks.

## REQ-BD-022
- obligation: mandatory
- scope: task
- stages: self-test
- source: p.8 §4.4
- section: Oracle
- explained_in: 11-validation/VALIDATION.md
- compliance_check: The command output and reward token are archived before upload.
- evidence: oracle.txt
- contradiction_or_rejection_risk: G05.ORACLE.REWARD_BELOW_FULL and ORACLE.NONZERO_EXIT are the platform forms of this failure.
- requirement: Run `harbor run --path . --agent oracle`. Expected result: 100% pass, reward 1.0. If it fails, the solution or the verifier is broken (bad test.sh logic or a missing dependency in the verifier image).

## REQ-BD-023
- obligation: mandatory
- scope: task
- stages: self-test
- source: p.8 §4.4
- section: NOP
- explained_in: 11-validation/VALIDATION.md
- compliance_check: The command output shows failure and reward 0.0.
- evidence: nop.txt
- contradiction_or_rejection_risk: NOP.FULL_REWARD is the platform rejection. A partial NOP reward is not an acceptable local result.
- requirement: Run `harbor run --path . --agent nop`. Expected result: 100% fail, reward 0.0. If NOP passes, the verifier is weak and the tests must be tightened.

## REQ-BD-024
- obligation: mandatory
- scope: process
- stages: self-test
- source: p.8 §4.5
- section: Local static and rubric
- explained_in: 11-validation/VALIDATION.md
- compliance_check: Both reports are clean on the tree that is zipped.
- evidence: checker-report.txt; static-checks.txt; rubric-review.md
- contradiction_or_rejection_risk: A local pass is not a platform pass. A local fail that is uploaded anyway spends a version.
- requirement: Run static checks locally with no API keys, and run the rubric locally with a free or open-source LLM (the source names smaller Llama- or Kimi-class models as enough to catch obvious gaps). Fix every failure before uploading.

## REQ-BD-025
- obligation: mandatory
- scope: task
- stages: self-test
- source: p.8 §4.5; p.14 checklist
- section: Dry run
- explained_in: 03-difficulty-and-horizon/DESIGN.md
- compliance_check: dry-run.md records the model and those three judgments.
- evidence: dry-run.md
- contradiction_or_rejection_risk: An open model solving the task in a handful of turns is evidence the frontier gate will find it short or easy. An open-model failure is not proof the frontier model will fail.
- requirement: Dry-run the task on free / open-source agents before spending platform trials, to confirm it is solvable, the instruction is clear, and it is not trivially easy, and that it takes a long trajectory.

## REQ-SC-000
- obligation: mandatory
- scope: process
- stages: self-test
- source: p.15 opening
- section: Static checks reference
- explained_in: 10-checks-and-coverage/STATIC-CHECKS.md
- compliance_check: The static report is separate from the rubric report.
- evidence: static-checks.txt; rubric-review.md
- contradiction_or_rejection_risk: The intro sentence mentions a missing canary; the check table does not include one. Follow the table plus C-CANARY.
- requirement: Static checks are fast, deterministic, and need no API keys and no LLM. They do not judge whether the task is good or hard. Run them locally before every upload.

## REQ-SC-check-dockerfile-references
- obligation: mandatory
- scope: task
- stages: build,self-test,stage1
- source: p.15
- section: check-dockerfile-references
- explained_in: 10-checks-and-coverage/STATIC-CHECKS.md
- compliance_check: Local preflight plus the platform static runner. The local script approximates check-dockerfile-references.
- evidence: checker-report.txt; static-checks.txt
- contradiction_or_rejection_risk: None beyond a failed upload.
- requirement: The agent Dockerfile does not copy solution/solve.sh, tests/test.sh, or tests/test_*.py into the image. The agent must never see the tests or solution.

## REQ-SC-check-dockerfile-sanity
- obligation: mandatory
- scope: task
- stages: build,self-test,stage1
- source: p.15
- section: check-dockerfile-sanity
- explained_in: 10-checks-and-coverage/STATIC-CHECKS.md
- compliance_check: Local preflight plus the platform static runner. The local script approximates check-dockerfile-sanity.
- evidence: checker-report.txt; static-checks.txt
- contradiction_or_rejection_risk: None beyond a failed upload.
- requirement: Apt packages are NOT pinned to versions. apt install is preceded by apt-get update and followed by rm -rf /var/lib/apt/lists/* cleanup.

## REQ-SC-check-dockerfile-platform
- obligation: mandatory
- scope: task
- stages: build,self-test,stage1
- source: p.15
- section: check-dockerfile-platform
- explained_in: 10-checks-and-coverage/STATIC-CHECKS.md
- compliance_check: Local preflight plus the platform static runner. The local script approximates check-dockerfile-platform.
- evidence: checker-report.txt; static-checks.txt
- contradiction_or_rejection_risk: None beyond a failed upload.
- requirement: No Dockerfile hardcodes a CPU architecture via FROM --platform=..., so the task runs on x86-64 or arm64 without slow emulation.

## REQ-SC-check-task-absolute-path
- obligation: mandatory
- scope: task
- stages: build,self-test,stage1
- source: p.15
- section: check-task-absolute-path
- explained_in: 10-checks-and-coverage/STATIC-CHECKS.md
- compliance_check: Local preflight plus the platform static runner. The local script approximates check-task-absolute-path.
- evidence: checker-report.txt; static-checks.txt
- contradiction_or_rejection_risk: None beyond a failed upload.
- requirement: Instructions use absolute paths (example /app/data.csv), never relative ones (data.csv).

## REQ-SC-check-test-file-references
- obligation: mandatory
- scope: task
- stages: build,self-test,stage1
- source: p.15
- section: check-test-file-references
- explained_in: 10-checks-and-coverage/STATIC-CHECKS.md
- compliance_check: Local preflight plus the platform static runner. The local script approximates check-test-file-references.
- evidence: checker-report.txt; static-checks.txt
- contradiction_or_rejection_risk: None beyond a failed upload.
- requirement: Every output file referenced by both the tests and the solution is documented in instruction.md or task.toml.

## REQ-SC-check-test-sh-sanity
- obligation: mandatory
- scope: task
- stages: build,self-test,stage1
- source: p.15
- section: check-test-sh-sanity
- explained_in: 10-checks-and-coverage/STATIC-CHECKS.md
- compliance_check: Local preflight plus the platform static runner. The local script approximates check-test-sh-sanity.
- evidence: checker-report.txt; static-checks.txt
- contradiction_or_rejection_risk: None beyond a failed upload.
- requirement: test.sh isolates Python using uv venv, or task.toml / instruction.md explicitly documents system-wide Python usage.

## REQ-SC-check-task-fields
- obligation: mandatory
- scope: task
- stages: build,self-test,stage1
- source: p.15
- section: check-task-fields
- explained_in: 10-checks-and-coverage/STATIC-CHECKS.md
- compliance_check: Local preflight plus the platform static runner. The local script approximates check-task-fields.
- evidence: checker-report.txt; static-checks.txt
- contradiction_or_rejection_risk: None beyond a failed upload.
- requirement: All required task.toml metadata is present: author_name, author_email, difficulty_explanation, solution_explanation, verification_explanation, category, tags, expert_time_estimate_hours.

## REQ-SC-check-task-timeout
- obligation: mandatory
- scope: task
- stages: build,self-test,stage1
- source: p.16
- section: check-task-timeout
- explained_in: 10-checks-and-coverage/STATIC-CHECKS.md
- compliance_check: Local preflight plus the platform static runner. The local script approximates check-task-timeout.
- evidence: checker-report.txt; static-checks.txt
- contradiction_or_rejection_risk: C-TIMEOUT. The acceptance page says an 8-hour rollout limit, which is 28800s and would fail this cap if copied into timeout_sec.
- requirement: [agent] and [verifier] timeout_sec are capped at 18000s (5 hours), leaving headroom under the CI runner's 6-hour job limit.

## REQ-SC-check-instruction-suffix
- obligation: mandatory
- scope: task
- stages: build,self-test,stage1
- source: p.16
- section: check-instruction-suffix
- explained_in: 10-checks-and-coverage/STATIC-CHECKS.md
- compliance_check: Local preflight plus the platform static runner. The local script approximates check-instruction-suffix.
- evidence: checker-report.txt; static-checks.txt
- contradiction_or_rejection_risk: C-REWARD-LITERAL does not apply. A wrong N fails the check.
- requirement: instruction.md ends with the exact timeout / anti-cheat line, N equal to [agent].timeout_sec, as its own paragraph with a single trailing newline.

## REQ-SC-check-gpu-types
- obligation: conditional
- scope: task
- stages: build,self-test,stage1
- source: p.16
- section: check-gpu-types
- explained_in: 10-checks-and-coverage/STATIC-CHECKS.md
- compliance_check: Local preflight plus the platform static runner. The local script approximates check-gpu-types.
- evidence: checker-report.txt; static-checks.txt
- contradiction_or_rejection_risk: None beyond a failed upload.
- requirement: Any gpu_types values are canonical Modal GPU strings: T4, L4, A10, L40S, A100-40GB, A100-80GB, H100, H200, B200, or any.

## REQ-SC-check-task-slug
- obligation: mandatory
- scope: task
- stages: build,self-test,stage1
- source: p.16
- section: check-task-slug
- explained_in: 10-checks-and-coverage/STATIC-CHECKS.md
- compliance_check: Local preflight plus the platform static runner. The local script approximates check-task-slug.
- evidence: checker-report.txt; static-checks.txt
- contradiction_or_rejection_risk: None beyond a failed upload.
- requirement: The task folder name is at most 3 hyphen-separated tokens, lowercase kebab-case.

## REQ-SC-check-allow-internet
- obligation: mandatory
- scope: task
- stages: build,self-test,stage1
- source: p.16
- section: check-allow-internet
- explained_in: 10-checks-and-coverage/STATIC-CHECKS.md
- compliance_check: Local preflight plus the platform static runner. The local script approximates check-allow-internet.
- evidence: checker-report.txt; static-checks.txt
- contradiction_or_rejection_risk: C-INTERNET. G02 also says agent networking is non-public.
- requirement: task.toml does not set [environment].allow_internet = false. Tasks run with open internet by default.

## REQ-SC-check-separate-verifier
- obligation: mandatory
- scope: task
- stages: build,self-test,stage1
- source: p.16
- section: check-separate-verifier
- explained_in: 10-checks-and-coverage/STATIC-CHECKS.md
- compliance_check: Local preflight plus the platform static runner. The local script approximates check-separate-verifier.
- evidence: checker-report.txt; static-checks.txt
- contradiction_or_rejection_risk: None beyond a failed upload.
- requirement: The task is fully configured for separate verifier mode: environment_mode = "separate", artifacts declared at top level, tests/Dockerfile exists and COPYs into /tests, and artifact parent directories are pre-created with RUN mkdir -p.

## REQ-SC-check-trial-network-fetch
- obligation: mandatory
- scope: task
- stages: build,self-test,stage1
- source: p.16
- section: check-trial-network-fetch
- explained_in: 10-checks-and-coverage/STATIC-CHECKS.md
- compliance_check: Local preflight plus the platform static runner. The local script approximates check-trial-network-fetch.
- evidence: checker-report.txt; static-checks.txt
- contradiction_or_rejection_risk: None beyond a failed upload.
- requirement: tests/test.sh does not fetch external resources at verify time (no curl|sh / wget|sh installers, no external curl/wget, no git clone of external URLs). This is a known reward-hacking surface.

## REQ-SC-check-pip-pinning
- obligation: mandatory
- scope: task
- stages: build,self-test,stage1
- source: p.16
- section: check-pip-pinning
- explained_in: 10-checks-and-coverage/STATIC-CHECKS.md
- compliance_check: Local preflight plus the platform static runner. The local script approximates check-pip-pinning.
- evidence: checker-report.txt; static-checks.txt
- contradiction_or_rejection_risk: None beyond a failed upload.
- requirement: Every pip / uv pip / uvx / uv tool install pins an explicit ==<version>. Manifest (-r requirements.txt), local (-e . or .), pip self-upgrade, and VCS URLs with an @ref are allowed.

## REQ-SC-check-nproc
- obligation: mandatory
- scope: task
- stages: build,self-test,stage1
- source: p.16
- section: check-nproc
- explained_in: 10-checks-and-coverage/STATIC-CHECKS.md
- compliance_check: Local preflight plus the platform static runner. The local script approximates check-nproc.
- evidence: checker-report.txt; static-checks.txt
- contradiction_or_rejection_risk: None beyond a failed upload.
- requirement: No bare nproc. It returns the host CPU count inside a container, causing over-parallel OOM/timeouts. Use [environment].cpus or a fixed value instead.

## REQ-SC-check-ai-prompt-sanitization
- obligation: mandatory
- scope: task
- stages: build,self-test,stage1
- source: p.16
- section: check-ai-prompt-sanitization
- explained_in: 10-checks-and-coverage/STATIC-CHECKS.md
- compliance_check: Local preflight plus the platform static runner. The local script approximates check-ai-prompt-sanitization.
- evidence: checker-report.txt; static-checks.txt
- contradiction_or_rejection_risk: None beyond a failed upload.
- requirement: AI prompts do not leak the task solution or hidden data to the model.

## REQ-BD-026
- obligation: mandatory
- scope: task
- stages: build,self-test
- source: pp. 6–7 example; p.15 check-dockerfile-references
- section: Oracle entry point
- explained_in: 09-verifier/VERIFIER.md
- compliance_check: solution/solve.sh exists, is not copied into the agent image, and is what the local oracle run executes.
- evidence: solution/solve.sh; oracle.txt
- contradiction_or_rejection_risk: A solution that lives only in the agent image is visible to the agent and is not an oracle.
- requirement: The oracle entry point is solution/solve.sh. The static check names that path specifically when it forbids copying it into the agent image. The preferred body of a long solution is solution/solve.py, launched by solve.sh with python3 /solution/solve.py.

## REQ-SC-REUPLOAD-SENTENCE
- obligation: unresolved
- scope: account
- stages: package
- source: p.16 closing
- section: Static checks close
- explained_in: 00-source/CONFLICT-REGISTER.md
- compliance_check: Do not rely on this sentence or on the table value 7. Follow C-REUPLOADS.
- evidence: decision-log.md
- contradiction_or_rejection_risk: C-REUPLOADS. The limits table says 7.
- requirement: Fixing a static-check failure after upload costs one of your three reuploads.

## REQ-RB-01
- obligation: mandatory
- scope: task
- stages: self-test,acceptance
- source: pp. 17–19
- section: Group A — Deterministic verification
- explained_in: 10-checks-and-coverage/RUBRIC.md
- compliance_check: Local rubric review records PASS with a justification tied to a file. Platform quality review, when it runs, agrees.
- evidence: rubric-review.md
- contradiction_or_rejection_risk: A FAIL uploaded anyway spends a version.
- requirement: Verification is fully deterministic — no LLM-as-judge, no fuzzy matching that could pass wrong answers or fail right ones.

## REQ-RB-02
- obligation: mandatory
- scope: task
- stages: self-test,acceptance
- source: pp. 17–19
- section: Group A — Outcome-based grading
- explained_in: 10-checks-and-coverage/RUBRIC.md
- compliance_check: Local rubric review records PASS with a justification tied to a file. Platform quality review, when it runs, agrees.
- evidence: rubric-review.md
- contradiction_or_rejection_risk: A FAIL uploaded anyway spends a version.
- requirement: Tests check the agent's final output / artifact, not the specific steps or method used to get there.

## REQ-RB-03
- obligation: mandatory
- scope: task
- stages: self-test,acceptance
- source: pp. 17–19
- section: Group A — Frozen ground truth
- explained_in: 10-checks-and-coverage/RUBRIC.md
- compliance_check: Local rubric review records PASS with a justification tied to a file. Platform quality review, when it runs, agrees.
- evidence: rubric-review.md
- contradiction_or_rejection_risk: A FAIL uploaded anyway spends a version.
- requirement: Expected values come from frozen, in-image fixtures so results are reproducible and not time/network dependent.

## REQ-RB-04
- obligation: mandatory
- scope: task
- stages: self-test,acceptance
- source: pp. 17–19
- section: Group A — Complete coverage
- explained_in: 10-checks-and-coverage/RUBRIC.md
- compliance_check: Local rubric review records PASS with a justification tied to a file. Platform quality review, when it runs, agrees.
- evidence: rubric-review.md
- contradiction_or_rejection_risk: A FAIL uploaded anyway spends a version.
- requirement: Tests cover the full required output (all fields, edge cases), not just a happy-path subset.

## REQ-RB-05
- obligation: mandatory
- scope: task
- stages: self-test,acceptance
- source: pp. 17–19
- section: Group A — Correct expected values
- explained_in: 10-checks-and-coverage/RUBRIC.md
- compliance_check: Local rubric review records PASS with a justification tied to a file. Platform quality review, when it runs, agrees.
- evidence: rubric-review.md
- contradiction_or_rejection_risk: A FAIL uploaded anyway spends a version.
- requirement: The expected answers the tests assert are themselves correct (independently derived / verified).

## REQ-RB-06
- obligation: mandatory
- scope: task
- stages: self-test,acceptance
- source: pp. 17–19
- section: Group A — Strict failure on no-op
- explained_in: 10-checks-and-coverage/RUBRIC.md
- compliance_check: Local rubric review records PASS with a justification tied to a file. Platform quality review, when it runs, agrees.
- evidence: rubric-review.md
- contradiction_or_rejection_risk: A FAIL uploaded anyway spends a version.
- requirement: A do-nothing or partial attempt fails — the verifier is not lenient.

## REQ-RB-07
- obligation: mandatory
- scope: task
- stages: self-test,acceptance
- source: pp. 17–19
- section: Group B — Reference solution exists
- explained_in: 10-checks-and-coverage/RUBRIC.md
- compliance_check: Local rubric review records PASS with a justification tied to a file. Platform quality review, when it runs, agrees.
- evidence: rubric-review.md
- contradiction_or_rejection_risk: A FAIL uploaded anyway spends a version.
- requirement: A correct reference solution is provided and passes all tests (Oracle = 1.0).

## REQ-RB-08
- obligation: mandatory
- scope: task
- stages: self-test,acceptance
- source: pp. 17–19
- section: Group B — Solvable from instruction alone
- explained_in: 10-checks-and-coverage/RUBRIC.md
- compliance_check: Local rubric review records PASS with a justification tied to a file. Platform quality review, when it runs, agrees.
- evidence: rubric-review.md
- contradiction_or_rejection_risk: A FAIL uploaded anyway spends a version.
- requirement: Everything needed to solve the task is in the instruction and environment — no external/hidden knowledge or missing inputs.

## REQ-RB-09
- obligation: mandatory
- scope: task
- stages: self-test,acceptance
- source: pp. 17–19
- section: Group B — Environment is self-contained
- explained_in: 10-checks-and-coverage/RUBRIC.md
- compliance_check: Local rubric review records PASS with a justification tied to a file. Platform quality review, when it runs, agrees.
- evidence: rubric-review.md
- contradiction_or_rejection_risk: A FAIL uploaded anyway spends a version.
- requirement: All required tools, data, and dependencies are present in the container; the task does not rely on flaky external resources.

## REQ-RB-10
- obligation: mandatory
- scope: task
- stages: self-test,acceptance
- source: pp. 17–19
- section: Group B — Achievable in the time budget
- explained_in: 10-checks-and-coverage/RUBRIC.md
- compliance_check: Local rubric review records PASS with a justification tied to a file. Platform quality review, when it runs, agrees.
- evidence: rubric-review.md
- contradiction_or_rejection_risk: A FAIL uploaded anyway spends a version.
- requirement: A capable agent can plausibly finish within [agent].timeout_sec.

## REQ-RB-11
- obligation: mandatory
- scope: task
- stages: self-test,acceptance
- source: pp. 17–19
- section: Group B — No ambiguity in the goal
- explained_in: 10-checks-and-coverage/RUBRIC.md
- compliance_check: Local rubric review records PASS with a justification tied to a file. Platform quality review, when it runs, agrees.
- evidence: rubric-review.md
- contradiction_or_rejection_risk: A FAIL uploaded anyway spends a version.
- requirement: The success condition is unambiguous — there is one clearly correct interpretation of done.

## REQ-RB-12
- obligation: mandatory
- scope: task
- stages: self-test,acceptance
- source: pp. 17–19
- section: Group B — Output schema fully specified
- explained_in: 10-checks-and-coverage/RUBRIC.md
- compliance_check: Local rubric review records PASS with a justification tied to a file. Platform quality review, when it runs, agrees.
- evidence: rubric-review.md
- contradiction_or_rejection_risk: A FAIL uploaded anyway spends a version.
- requirement: The exact output path, format, schema, ordering, and formatting are spelled out so a correct attempt is not failed on a guessable detail.

## REQ-RB-13
- obligation: mandatory
- scope: task
- stages: self-test,acceptance
- source: pp. 17–19
- section: Group C — Genuinely difficult
- explained_in: 10-checks-and-coverage/RUBRIC.md
- compliance_check: Local rubric review records PASS with a justification tied to a file. Platform quality review, when it runs, agrees.
- evidence: rubric-review.md
- contradiction_or_rejection_risk: A FAIL uploaded anyway spends a version.
- requirement: The task is hard for a strong agent — not solvable by a trivial one-liner or obvious lookup.

## REQ-RB-14
- obligation: mandatory
- scope: task
- stages: self-test,acceptance
- source: pp. 17–19
- section: Group C — Non-trivial (NOP fails)
- explained_in: 10-checks-and-coverage/RUBRIC.md
- compliance_check: Local rubric review records PASS with a justification tied to a file. Platform quality review, when it runs, agrees.
- evidence: rubric-review.md
- contradiction_or_rejection_risk: A FAIL uploaded anyway spends a version.
- requirement: Doing nothing, or an obvious naive approach, does not pass.

## REQ-RB-15
- obligation: mandatory
- scope: task
- stages: self-test,acceptance
- source: pp. 17–19
- section: Group C — Difficulty is legitimate
- explained_in: 10-checks-and-coverage/RUBRIC.md
- compliance_check: Local rubric review records PASS with a justification tied to a file. Platform quality review, when it runs, agrees.
- evidence: rubric-review.md
- contradiction_or_rejection_risk: A FAIL uploaded anyway spends a version.
- requirement: Hardness comes from real reasoning/engineering, not from obscure trivia, trick wording, or guess-the-format.

## REQ-RB-16
- obligation: mandatory
- scope: task
- stages: self-test,acceptance
- source: pp. 17–19
- section: Group C — Resistant to reward hacking
- explained_in: 10-checks-and-coverage/RUBRIC.md
- compliance_check: Local rubric review records PASS with a justification tied to a file. Platform quality review, when it runs, agrees.
- evidence: rubric-review.md
- contradiction_or_rejection_risk: A FAIL uploaded anyway spends a version.
- requirement: The agent cannot game the verifier (hardcoding expected values, writing to reward files, reading hidden tests/solution).

## REQ-RB-17
- obligation: mandatory
- scope: task
- stages: self-test,acceptance
- source: pp. 17–19
- section: Group C — Answer not leaked
- explained_in: 10-checks-and-coverage/RUBRIC.md
- compliance_check: Local rubric review records PASS with a justification tied to a file. Platform quality review, when it runs, agrees.
- evidence: rubric-review.md
- contradiction_or_rejection_risk: A FAIL uploaded anyway spends a version.
- requirement: The instruction, environment, and data do not reveal the expected answer or the test internals.

## REQ-RB-18
- obligation: mandatory
- scope: task
- stages: self-test,acceptance
- source: pp. 17–19
- section: Group C — No shortcut via internet
- explained_in: 10-checks-and-coverage/RUBRIC.md
- compliance_check: Local rubric review records PASS with a justification tied to a file. Platform quality review, when it runs, agrees.
- evidence: rubric-review.md
- contradiction_or_rejection_risk: C-INTERNET. Open internet by default does not make a public answer acceptable.
- requirement: The answer cannot simply be looked up online or copied from a public source.

## REQ-RB-19
- obligation: mandatory
- scope: task
- stages: self-test,acceptance
- source: pp. 17–19
- section: Group D — Clear and well-written
- explained_in: 10-checks-and-coverage/RUBRIC.md
- compliance_check: Local rubric review records PASS with a justification tied to a file. Platform quality review, when it runs, agrees.
- evidence: rubric-review.md
- contradiction_or_rejection_risk: C-HEADINGS. Well-structured does not mean ## headings.
- requirement: The instruction is unambiguous, well-structured, and free of contradictions.

## REQ-RB-20
- obligation: mandatory
- scope: task
- stages: self-test,acceptance
- source: pp. 17–19
- section: Group D — No hidden hints or leakage
- explained_in: 10-checks-and-coverage/RUBRIC.md
- compliance_check: Local rubric review records PASS with a justification tied to a file. Platform quality review, when it runs, agrees.
- evidence: rubric-review.md
- contradiction_or_rejection_risk: A FAIL uploaded anyway spends a version.
- requirement: The instruction does not hint at the solution method or leak verifier details.

## REQ-RB-21
- obligation: mandatory
- scope: task
- stages: self-test,acceptance
- source: pp. 17–19
- section: Group D — Absolute paths and concrete I/O
- explained_in: 10-checks-and-coverage/RUBRIC.md
- compliance_check: Local rubric review records PASS with a justification tied to a file. Platform quality review, when it runs, agrees.
- evidence: rubric-review.md
- contradiction_or_rejection_risk: A FAIL uploaded anyway spends a version.
- requirement: All file paths are absolute and every required input/output is named explicitly.

## REQ-RB-22
- obligation: mandatory
- scope: task
- stages: self-test,acceptance
- source: pp. 17–19
- section: Group D — Required suffix present
- explained_in: 10-checks-and-coverage/RUBRIC.md
- compliance_check: Local rubric review records PASS with a justification tied to a file. Platform quality review, when it runs, agrees.
- evidence: rubric-review.md
- contradiction_or_rejection_risk: A FAIL uploaded anyway spends a version.
- requirement: The instruction ends with the exact timeout / anti-cheat line matching the agent timeout.

## REQ-RB-23
- obligation: mandatory
- scope: task
- stages: self-test,acceptance
- source: pp. 17–19
- section: Group D — Self-consistent with tests
- explained_in: 10-checks-and-coverage/RUBRIC.md
- compliance_check: Local rubric review records PASS with a justification tied to a file. Platform quality review, when it runs, agrees.
- evidence: rubric-review.md
- contradiction_or_rejection_risk: A FAIL uploaded anyway spends a version.
- requirement: What the instruction asks for is exactly what the tests check — no drift between statement and grading.

## REQ-RB-24
- obligation: mandatory
- scope: task
- stages: self-test,acceptance
- source: pp. 17–19
- section: Group D — Appropriately scoped
- explained_in: 10-checks-and-coverage/RUBRIC.md
- compliance_check: Local rubric review records PASS with a justification tied to a file. Platform quality review, when it runs, agrees.
- evidence: rubric-review.md
- contradiction_or_rejection_risk: A FAIL uploaded anyway spends a version.
- requirement: The task is a focused, single objective — not a sprawling bundle of unrelated sub-tasks.

## REQ-RB-25
- obligation: mandatory
- scope: task
- stages: self-test,acceptance
- source: pp. 17–19
- section: Group E — Separate verifier configured
- explained_in: 10-checks-and-coverage/RUBRIC.md
- compliance_check: Local rubric review records PASS with a justification tied to a file. Platform quality review, when it runs, agrees.
- evidence: rubric-review.md
- contradiction_or_rejection_risk: A FAIL uploaded anyway spends a version.
- requirement: Tests run in their own container after the agent; the agent image is clean (no tests/solution).

## REQ-RB-26
- obligation: mandatory
- scope: task
- stages: self-test,acceptance
- source: pp. 17–19
- section: Group E — Dependencies pinned and baked
- explained_in: 10-checks-and-coverage/RUBRIC.md
- compliance_check: Local rubric review records PASS with a justification tied to a file. Platform quality review, when it runs, agrees.
- evidence: rubric-review.md
- contradiction_or_rejection_risk: A FAIL uploaded anyway spends a version.
- requirement: All deps are version-pinned and pre-installed in the right image; no runtime installs at verify time.

## REQ-RB-27
- obligation: mandatory
- scope: task
- stages: self-test,acceptance
- source: pp. 17–19
- section: Group E — Sensible resources
- explained_in: 10-checks-and-coverage/RUBRIC.md
- compliance_check: Local rubric review records PASS with a justification tied to a file. Platform quality review, when it runs, agrees.
- evidence: rubric-review.md
- contradiction_or_rejection_risk: A FAIL uploaded anyway spends a version.
- requirement: CPU / memory / storage / timeouts are appropriate — not wastefully large, not too tight to solve.

## REQ-RB-28
- obligation: mandatory
- scope: task
- stages: self-test,acceptance
- source: pp. 17–19
- section: Group E — Reproducible build
- explained_in: 10-checks-and-coverage/RUBRIC.md
- compliance_check: Local rubric review records PASS with a justification tied to a file. Platform quality review, when it runs, agrees.
- evidence: rubric-review.md
- contradiction_or_rejection_risk: A FAIL uploaded anyway spends a version.
- requirement: The images build cleanly and deterministically on a fresh machine.

## REQ-RB-29
- obligation: mandatory
- scope: task
- stages: self-test,acceptance
- source: pp. 17–19
- section: Group E — Real-world relevance
- explained_in: 10-checks-and-coverage/RUBRIC.md
- compliance_check: Local rubric review records PASS with a justification tied to a file. Platform quality review, when it runs, agrees.
- evidence: rubric-review.md
- contradiction_or_rejection_risk: A FAIL uploaded anyway spends a version.
- requirement: The task reflects a realistic, valuable scenario someone would actually do — not a contrived puzzle.

## REQ-RB-30
- obligation: mandatory
- scope: task
- stages: self-test,acceptance
- source: pp. 17–19
- section: Group E — Correct and complete metadata
- explained_in: 10-checks-and-coverage/RUBRIC.md
- compliance_check: Local rubric review records PASS with a justification tied to a file. Platform quality review, when it runs, agrees.
- evidence: rubric-review.md
- contradiction_or_rejection_risk: A FAIL uploaded anyway spends a version.
- requirement: task.toml metadata (difficulty, solution, verification explanations, category, tags, time estimate) is filled in and accurate.

## REQ-RB-LOCAL
- obligation: mandatory
- scope: process
- stages: self-test
- source: p.19 closing
- section: How to use the rubric locally
- explained_in: 10-checks-and-coverage/RUBRIC.md
- compliance_check: The rubric report has no unexplained FAIL and predates the ZIP.
- evidence: rubric-review.md
- contradiction_or_rejection_risk: C-REUPLOADS. C-NINE-DIMENSIONS. There are 30 criteria here, not 9 named dimensions.
- requirement: Run the rubric review with a free / open-source LLM before uploading. Read each FAIL with its justification, fix the underlying issue, and re-run. The page says arriving already passing protects your 3 reuploads.

## REQ-G-001
- obligation: platform
- scope: platform
- stages: package,stage1
- source: p.8 §5; p.5 screenshot
- section: Upload
- explained_in: 14-platform-review/STAGE-1.md
- compliance_check: The archived SHA-256 matches the uploaded bytes. Stage 1 starts on that generation.
- evidence: sha256.txt; stage1.txt
- contradiction_or_rejection_risk: File hash already exists if the same bytes are uploaded again.
- requirement: Upload Harbor task ZIP is inactive until an ACTIVE grant exists. The ZIP is immutable once uploaded: the platform binds its SHA-256 and an upload generation, and Stage 1 begins automatically.

## REQ-G-002
- obligation: platform
- scope: platform
- stages: stage1
- source: p.8 §5
- section: Stage 1 job
- explained_in: 00-source/PLATFORM-RULE-CATALOG.md
- compliance_check: The event log shows that order. The author does not mark individual gates passed.
- evidence: stage1.txt
- contradiction_or_rejection_risk: NOT_REACHED on a later gate means an earlier gate stopped the job.
- requirement: Stage 1 is a sequenced job, not cards triggered one by one. It runs I01 (upload snapshot), gates G01 through G06, and then P04 (the publication barrier). A typical clean run finishes in well under a minute, most of it in G04 through G06.

## REQ-G-003
- obligation: platform
- scope: platform
- stages: stage1
- source: p.9 §5.1
- section: I01
- explained_in: 00-source/PLATFORM-RULE-CATALOG.md
- compliance_check: The receipt shows the bound hash.
- evidence: stage1.txt
- contradiction_or_rejection_risk: SNAPSHOT.UNREADABLE or SNAPSHOT.MUTATING means the archive was not a stable snapshot.
- requirement: I01 Upload snapshot binds the immutable upload generation and SHA-256 snapshot of the ZIP before anything reads it.

## REQ-G-004
- obligation: platform
- scope: task
- stages: package,stage1
- source: p.9 §5.1
- section: G01
- explained_in: 14-platform-review/STAGE-1.md
- compliance_check: The ZIP has one top-level directory, no symlinks, no absolute member names, and is not encrypted.
- evidence: sha256.txt; stage1.txt
- contradiction_or_rejection_risk: U-ZIP-ROOT. The exact top-level shape is unspecified beyond a single candidate root. The packager's single top-level directory is provisional.
- requirement: G01 Archive safety: exact ZIP inventory, safe extract, and a single candidate root. It catches path traversal, absolute paths, symlinks, encrypted members, CRC mismatches, archive bombs, and multiple or zero task roots.

## REQ-G-005
- obligation: platform
- scope: task
- stages: stage1
- source: p.9 §5.1
- section: G02
- explained_in: 00-source/PLATFORM-RULE-CATALOG.md
- compliance_check: The layout matches the required tree and task.toml. The Harbor version is recorded when known.
- evidence: stage1.txt; task.toml
- contradiction_or_rejection_risk: C-TB3-LABEL. U-HARBOR-PIN. C-INTERNET. The screenshot labels this gate Harbor + TB3.
- requirement: G02 Harbor + TB4 contract: Harbor layout parses under the pinned Harbor version; required paths are present and readable; TB4 metadata is valid (category, subcategory, required fields); agent networking is non-public; verifier isolation is declared.

## REQ-G-006
- obligation: platform
- scope: task
- stages: stage1
- source: p.9 §5.1
- section: G03
- explained_in: 07-agent-environment/ENVIRONMENT.md
- compliance_check: No secrets, no privileged or host-network compose, no verifier fetch, no tests copied into the agent image.
- evidence: stage1.txt
- contradiction_or_rejection_risk: Compose rules are IF APPLICABLE.
- requirement: G03 Static execution safety: no hidden runtime, credentials, or network reach-out. It covers credential scanning, Compose dependency and provenance scanning, host binds, privileged containers, host networking, devices, packaged-file mutation, Dockerfile references, and verifier fetch patterns.

## REQ-G-007
- obligation: platform
- scope: task
- stages: stage1
- source: p.9 §5.1
- section: G04
- explained_in: 07-agent-environment/ENVIRONMENT.md
- compliance_check: A local image build succeeds from a clean context. The declared accelerator exists in the allowed profile.
- evidence: stage1.txt
- contradiction_or_rejection_risk: G04.PROFILE.ACCELERATOR_UNSUPPORTED is the prose's example of a retry, not an automatic rewrite.
- requirement: G04 Environment readiness: Harbor can build and start the declared image and Compose environment and reach bound agent-setup evidence. Unsupported profiles, accelerators, prebuilt images, and timeout envelopes fail here.

## REQ-G-008
- obligation: platform
- scope: task
- stages: stage1
- source: p.9 §5.1
- section: G05
- explained_in: 09-verifier/VERIFIER.md
- compliance_check: Local Oracle shows reward 1.0 and local NOP shows reward 0.0, which is what section 4.4 requires of those commands. Whether a partial NOP reward fails Stage 1 is C-REWARD-LITERAL and is unresolved.
- evidence: oracle.txt; nop.txt; stage1.txt
- contradiction_or_rejection_risk: The prose's defect example is G05.ORACLE.REWARD_BELOW_FULL. G05.HARBOR.UNKNOWN_EXCEPTION is a retry example.
- requirement: G05 Verifier controls: Oracle and NOP run as one Harbor job. Oracle must score 1.0 and exit cleanly. NOP must not score 1.0. The reward must be found, parseable, unambiguous, and finite. This is where most real task defects surface.

## REQ-G-009
- obligation: platform
- scope: task
- stages: stage1
- source: p.9 §5.1
- section: G06
- explained_in: 10-checks-and-coverage/STATIC-CHECKS.md
- compliance_check: The static-check table is clean. G06 is not marked passed from the local script alone.
- evidence: static-checks.txt; stage1.txt
- contradiction_or_rejection_risk: The screenshots do not show a separate G06 rule list beyond PACKAGE.* rules under G02.
- requirement: G06 Package quality: static package quality covering instruction, tests, mapping, and related criteria.

## REQ-G-010
- obligation: platform
- scope: platform
- stages: stage1
- source: p.9 §5.1
- section: P04
- explained_in: 00-source/PLATFORM-RULE-CATALOG.md
- compliance_check: P04 is read only after G01–G06. NOT_REACHED is traced to the earlier gate.
- evidence: stage1.txt
- contradiction_or_rejection_risk: A hash-closure or publication failure is platform-side unless the log says the ZIP changed.
- requirement: P04 Final publication barrier binds this ZIP, its receipt, and its artifacts. It sanitises output, closes hashes, persists the result, and publishes the admission — or stops.

## REQ-G-011
- obligation: mandatory
- scope: platform
- stages: stage1
- source: p.9 §5.1
- section: Severity model
- explained_in: 00-source/HOW-TO-READ.md
- compliance_check: A warning is archived and not treated as PASSED failing. A REQUIRED id is fixed or retried according to the outcome class.
- evidence: stage1.txt
- contradiction_or_rejection_risk: U-SEVERITY-ALIGNMENT. Do not invent a per-rule severity the screenshot does not reliably show.
- requirement: REQUIRED rejects the task, or for platform-side rules marks Stage 1 incomplete. OPTIONAL / ADVISORY does not reject; a run can read 'Stage 1 accepted · 2 warnings' and still be fine. IF APPLICABLE is evaluated only when the task uses the feature. Compose-specific rules are the source's example.

## REQ-G-012
- obligation: platform
- scope: platform
- stages: stage1
- source: p.9–10 §5.2
- section: Outcomes
- explained_in: 14-platform-review/STAGE-1.md
- compliance_check: The archived outcome is one of those three strings, plus the blocking rule when present.
- evidence: stage1.txt
- contradiction_or_rejection_risk: The platform fails closed rather than inventing a task defect, so 'could not complete' is never a verdict on the work.
- requirement: Stage 1 ends in exactly one of: 'Stage 1 accepted / PASSED STAGE 1 (READY_FOR_STAGE2)' when all gates passed; 'Stage 1 rejected — upload a corrected ZIP' when a REQUIRED rule found a defect; 'Stage 1 could not complete — retry' when the platform will not attribute the failure to the task.

## REQ-G-013
- obligation: platform
- scope: platform
- stages: stage1
- source: p.10 §5.2
- section: Named examples
- explained_in: 14-platform-review/STAGE-1.md
- compliance_check: Those ids are classified with the prose, not rewritten by habit.
- evidence: stage1.txt
- contradiction_or_rejection_risk: Rewriting a task because of UNKNOWN_EXCEPTION spends a version on a non-defect.
- requirement: Blocking-reason example for a task defect: G05.ORACLE.REWARD_BELOW_FULL. Retry examples: G05.HARBOR.UNKNOWN_EXCEPTION and G04.PROFILE.ACCELERATOR_UNSUPPORTED, also Harbor anomaly, unclassified exception, OOM or eviction, cancellation, unsupported accelerator profile.

## REQ-G-014
- obligation: mandatory
- scope: process
- stages: stage1
- source: p.11 §5.3
- section: Re-upload
- explained_in: 14-platform-review/STAGE-1.md
- compliance_check: The passing Stage 1 receipt is for one SHA-256, and the local Oracle/NOP for that tree predate it.
- evidence: stage1.txt; oracle.txt; nop.txt
- contradiction_or_rejection_risk: C-REUPLOADS.
- requirement: Open the failing gate and read the rule. Use the durable event log for phase order. Fix locally, re-run local static checks and Oracle/NOP, then upload a corrected ZIP. Only one thing reaches Stage 2: every gate green on a single version. Partial credit across versions does not count.

## REQ-G-015
- obligation: example
- scope: platform
- stages: stage1
- source: p.10 screenshot
- section: Clean Stage 1 illustration
- explained_in: 00-source/PLATFORM-RULE-CATALOG.md
- compliance_check: These numbers are an illustration of one run, not quotas.
- evidence: stage1.txt
- contradiction_or_rejection_risk: Do not pad the task until a local counter reads 94.
- requirement: The clean screenshot shows READY_FOR_STAGE2, 6 gates passed, 94 rules passed, 2 warnings, 5 artifacts bound, elapsed 1:12, and Stage 3 Qualitative checks DEFERRED.

## REQ-S2-001
- obligation: platform
- scope: platform
- stages: stage2
- source: p.12 §6
- section: Stage 2 flow
- explained_in: 14-platform-review/STAGE-2.md
- compliance_check: The author does not mark Stage 2 passed while the status is waiting or indeterminate.
- evidence: stage2.txt
- contradiction_or_rejection_risk: Forcing Stop during an active provider attempt makes the run noncanonical rather than retryable.
- requirement: Stage 2 moves QUEUED → PREPARING → RUNNING → COLLECTING → CLOSING → COMPLETE and can sit at 'Stage 2 running · waiting on provider'. The author does not drive it.

## REQ-S2-002
- obligation: platform
- scope: platform
- stages: stage2
- source: p.12 §6.1; p.13 screenshot
- section: Eight rollouts
- explained_in: 14-platform-review/STAGE-2.md
- compliance_check: The receipt shows 8 of 8 reconciled on the frozen policy. The author does not set effort or K.
- evidence: stage2.txt
- contradiction_or_rejection_risk: U-POLICY-DIGEST. The sample hash in the screenshot is not a task field.
- requirement: Stage 2 runs 8 rollouts under a frozen policy. Policy key and digest, capacity profile, and retention profile are recorded. The UI shows 1 MODEL • 8 ROLLOUTS REQUIRED, Anonymous model, messages, effort high, K=8, policy FROZEN.

## REQ-S2-003
- obligation: mandatory
- scope: task
- stages: stage2
- source: p.12 §6.2; p.13 screenshot
- section: difficulty predicate
- explained_in: 03-difficulty-and-horizon/DESIGN.md
- compliance_check: The observed value on the passing run is ≤ 2.
- evidence: stage2.txt
- contradiction_or_rejection_risk: C-DIFFICULTY is unresolved. Do not treat ≤2 as the acceptance pass rate, and do not treat 4/8 as a Stage 2 pass.
- requirement: Predicate difficulty: count_true(full_credit_boolean) ≤ 2. At most 2 of the 8 rollouts may earn full credit. More than that and the task is too easy. UI: Required: ≤2.

## REQ-S2-004
- obligation: mandatory
- scope: task
- stages: stage2
- source: p.12 §6.2; p.13 screenshot
- section: long_horizon predicate
- explained_in: 03-difficulty-and-horizon/DESIGN.md
- compliance_check: The observed median on the passing run is greater than 80.
- evidence: stage2.txt
- contradiction_or_rejection_risk: C-HORIZON is unresolved. The acceptance page states a different statistic: more than 35 turns of all passing runs. Do not treat the median rule as that test.
- requirement: Predicate long_horizon: median(assistant_message_count) > 80. A median of about 48 turns fails this even when difficulty passes. UI label: Median assistant turns, Required: >80.

## REQ-S2-005
- obligation: mandatory
- scope: task
- stages: stage2
- source: p.12 §6.2
- section: Both predicates
- explained_in: 14-platform-review/STAGE-2.md
- compliance_check: A PASS receipt has both predicates true. A FAIL receipt names which one.
- evidence: stage2.txt
- contradiction_or_rejection_risk: Fixing one predicate usually moves the other. Re-check both before resubmitting.
- requirement: Every predicate must hold. The overall verdict is PASS or FAIL, and the header names the predicate that sank it (example: Failed on long_horizon).

## REQ-S2-006
- obligation: mandatory
- scope: task
- stages: stage2
- source: p.13 §6.3
- section: Too easy
- explained_in: 03-difficulty-and-horizon/GENUINE-COMPLEXITY.md
- compliance_check: complexity.md names the page 13 move and the instruction sentence added with it. The coverage table gained a row for that sentence. No test asserts an unstated condition.
- evidence: complexity.md; instruction.md
- contradiction_or_rejection_risk: Hidden information fails Well-specified and Solvable from instruction alone. A task that sounds hard is not this row.
- requirement: If too many rollouts earn full credit, add depth: more cross-source correlation, more state that must stay consistent, stricter exactness in the output contract. Do not fix it by hiding information in the instruction.

## REQ-S2-007
- obligation: mandatory
- scope: task
- stages: stage2
- source: p.13 §6.3
- section: Too short
- explained_in: 03-difficulty-and-horizon/GENUINE-COMPLEXITY.md
- compliance_check: complexity.md names the new component or boundary condition and the instruction sentence that states it. The local-measurement block is re-run. The platform-verdict block is not filled from that rerun.
- evidence: complexity.md
- contradiction_or_rejection_risk: Busywork is a later-review failure even if a local transcript gets longer. Artificial turn inflation is not long horizon.
- requirement: If the median turn count is too low, add genuine sequential work: more components that must all hold together, and more recovery and boundary conditions the agent has to discover and handle. Padding with busywork does not survive the later review and will read as busywork.

## REQ-S2-008
- obligation: platform
- scope: platform
- stages: stage2
- source: p.13 screenshot
- section: Indeterminate
- explained_in: 14-platform-review/STAGE-2.md
- compliance_check: Indeterminate is not recorded as a difficulty FAIL and the task is not rewritten for it.
- evidence: stage2.txt
- contradiction_or_rejection_risk: Pressing Stop while a provider attempt is active makes the run noncanonical rather than retryable.
- requirement: A blocked rollout shows INDETERMINATE, population incomplete, and in the example RUNNER_EXECUTION_FAILED with 'Blocked with 0 of 8 rollouts reconciled. No predicate can move until the blocker clears.' Platform on-call unblocks it.

## REQ-LM-001
- obligation: unresolved
- scope: account
- stages: package
- source: p.20 limits table
- section: Reuploads
- explained_in: 00-source/CONFLICT-REGISTER.md
- compliance_check: Both 7 and 3 are recorded. C-REUPLOADS is unresolved. Do not upload a 4th through 7th version, and do not stop at 3, unless the live counter is quoted in the decision log.
- evidence: decision-log.md
- contradiction_or_rejection_risk: C-REUPLOADS. Prose in four places says 3.
- requirement: The limits table sets Reuploads (new versions) per task to 7.

## REQ-LM-002
- obligation: unresolved
- scope: account
- stages: proposal
- source: p.20 limits table
- section: Total submissions
- explained_in: 00-source/CONFLICT-REGISTER.md
- compliance_check: Human gate before creating a task. The term submission is not defined.
- evidence: decision-log.md
- contradiction_or_rejection_risk: C-ACCOUNT-LIMITS is unresolved. The same table also says task creation limit 2. Do not treat either cell as the account quota.
- requirement: Total submissions is 1 (account-wide).

## REQ-LM-003
- obligation: mandatory
- scope: account
- stages: package
- source: p.20 limits table
- section: Hourly evaluation limit
- explained_in: 14-platform-review/STAGE-1.md
- compliance_check: No third distinct ZIP is uploaded in the same hour.
- evidence: stage1.txt
- contradiction_or_rejection_risk: A unique version is a content change, not a re-click. Identical bytes fail with File hash already exists.
- requirement: Hourly evaluation limit: 2 unique versions.

## REQ-LM-004
- obligation: mandatory
- scope: account
- stages: package
- source: p.20 limits table
- section: Daily evaluation limit
- explained_in: 14-platform-review/STAGE-1.md
- compliance_check: The day's uploads stay at or under 5 unique versions.
- evidence: stage1.txt
- contradiction_or_rejection_risk: Five mechanical failures exhaust the day.
- requirement: Daily evaluation limit: 5 unique versions.

## REQ-LM-005
- obligation: unresolved
- scope: account
- stages: proposal
- source: p.20 limits table
- section: Task creation limit
- explained_in: 00-source/CONFLICT-REGISTER.md
- compliance_check: Before a second platform task, record the live quota if the UI shows it. Do not ask the user to choose a category or a task idea.
- evidence: decision-log.md
- contradiction_or_rejection_risk: C-ACCOUNT-LIMITS is unresolved. The same table also says total submissions 1 (account-wide).
- requirement: Task creation limit: 2 tasks.

## REQ-LM-006
- obligation: mandatory
- scope: task
- stages: proposal
- source: p.20
- section: Locked at creation
- explained_in: 02-ideation/SELECTION.md
- compliance_check: selection.md records category and programming language before the platform task exists. The agent chooses them and does not ask the user. U-LANGUAGE-FIELD: the proposal form's five fields do not include a language field, so the UI control's label is recorded when it appears, or as not shown.
- evidence: selection.md; proposal-receipt.txt
- contradiction_or_rejection_risk: A wrong category cannot be repaired by a later ZIP.
- requirement: Once a task is created you cannot change its category or programming language. Choose carefully.

## REQ-LM-007
- obligation: mandatory
- scope: process
- stages: package
- source: p.21
- section: Identical ZIP
- explained_in: 14-platform-review/STAGE-1.md
- compliance_check: A new upload has a new SHA-256 and a real content change.
- evidence: sha256.txt
- contradiction_or_rejection_risk: Touching a comment only to change the hash, without fixing the defect, fails again and spends a version.
- requirement: The error 'File hash already exists' means the identical ZIP was uploaded again. Make a real change first.

## REQ-LM-008
- obligation: unresolved
- scope: process
- stages: all
- source: pp. 20–21 troubleshooting and checklist
- section: Legacy pipeline names
- explained_in: 00-source/CONFLICT-REGISTER.md
- compliance_check: Do not execute the legacy cards as if the change table retired them. C-LEGACY-CARDS is unresolved. C-CANARY, C-NINE-DIMENSIONS, and C-REUPLOADS stay open. Keep the acceptance obligations that are reprinted on pp. 25–26.
- evidence: decision-log.md
- contradiction_or_rejection_risk: Following this checklist literally contradicts pp. 1–14.
- requirement: The troubleshooting table and final checklist still require a canary DM, canary_string, Proposal Match, Agent Trials, Cheat Trial, Harbor Analyze, and 'All 9 Quality Dimensions green'. They also say 'You hit 3 versions for that task.'

## REQ-TX-001
- obligation: mandatory
- scope: batch
- stages: batch
- source: p.22
- section: Taxonomy source
- explained_in: 01-taxonomy-and-batch/TAXONOMY.md
- compliance_check: Every delivered task uses a category and subcategory from the printed table, or a justified custom subcategory.
- evidence: batch-slot.md
- contradiction_or_rejection_risk: U-TAGS. U-GITHUB. The github hyperlink targets are not in the PDF.
- requirement: Follow the official taxonomy of Terminal Bench 3. Delivered tasks must broadly cover the categories and tags used across TB4.

## REQ-TX-002
- obligation: mandatory
- scope: batch
- stages: batch
- source: p.22
- section: 20% cap
- explained_in: 01-taxonomy-and-batch/BATCH.md
- compliance_check: The batch count by category stays at or under 20% of delivered tasks.
- evidence: batch-slot.md
- contradiction_or_rejection_risk: A one-task delivery cannot satisfy the cap by itself; the slot is still recorded.
- requirement: No single category may exceed 20% of the delivered batch.

## REQ-TX-003
- obligation: mandatory
- scope: batch
- stages: batch
- source: p.22
- section: Deprioritized slices
- explained_in: 01-taxonomy-and-batch/TAXONOMY.md
- compliance_check: The batch plan has one slot per subcategory in those three categories and does not fill the batch with them.
- evidence: batch-slot.md
- contradiction_or_rejection_risk: Science has 7 subcategories, Operations 6, Media 2. That is 15 slots, not a license to add more in those categories.
- requirement: Science, Operations, and Media are deprioritized and included as thin presence slices: 1 task each subcategory. They must not displace the Software / ML / Security / Hardware focus.

## REQ-TX-004
- obligation: mandatory
- scope: batch
- stages: batch
- source: p.22
- section: Do not concentrate
- explained_in: 01-taxonomy-and-batch/BATCH.md
- compliance_check: The plan shows non-zero room for Hardware, Security, and ML, and does not make Software plus Science the bulk.
- evidence: batch-slot.md
- contradiction_or_rejection_risk: Equal footing is subject to the cap and to the one-each rule for deprioritized subcategories.
- requirement: Do not concentrate the batch in Software and Science. Operations, Hardware, Security, Media, and ML tags are in scope on equal footing, subject to the 20% cap.

## REQ-TX-005
- obligation: unresolved
- scope: batch
- stages: batch
- source: p.24 note
- section: 66 tasks
- explained_in: 00-source/UNRESOLVED.md
- compliance_check: No numeric target out of 66 is invented or enforced.
- evidence: batch-slot.md
- contradiction_or_rejection_risk: U-66.
- requirement: The note says the distributions are just rough numbers out of 66 total tasks. No distribution table is printed.

## REQ-TX-006
- obligation: mandatory
- scope: task
- stages: build
- source: p.23 Training
- section: Single H100
- explained_in: 01-taxonomy-and-batch/TAXONOMY.md
- compliance_check: gpu_types for a training task is a single H100, which is in the canonical list.
- evidence: task.toml
- contradiction_or_rejection_risk: Requesting a second GPU or a non-canonical name fails check-gpu-types or the hardware limit.
- requirement: GPU training tasks are bounded by the hardware limit: GPU tasks get a single H100.

## REQ-TX-007
- obligation: advisory
- scope: task
- stages: proposal
- source: pp. 22–24
- section: Release-composition remarks
- explained_in: 01-taxonomy-and-batch/TAXONOMY.md
- compliance_check: Those phrases are not turned into submission quotas.
- evidence: batch-slot.md
- contradiction_or_rejection_risk: The printed quotas are only the 20% cap and one task per deprioritized subcategory.
- requirement: Remarks such as 'largest single subcategory', 'largest ML subcategory', 'smallest ML bucket', and RTL as 'a single-task slice' describe the official release, not a freelancer quota.

## REQ-TX-008
- obligation: mandatory
- scope: task
- stages: proposal
- source: pp. 22–24
- section: Subcategory catalog
- explained_in: 01-taxonomy-and-batch/TAXONOMY.md
- compliance_check: The subcategory string matches one of these unless a custom value was justified.
- evidence: task.toml; 01-taxonomy-and-batch/TAXONOMY.md
- contradiction_or_rejection_risk: The p.2 screenshot chips are examples. Cryptography is under Security in the table, even if a screenshot chip places a sample elsewhere.
- requirement: Use the printed subcategory for the chosen category: Software — Systems, Algorithms, Frontend, Data engineering, Databases; ML — Inference, Evaluation, Training, Kernels; Security — Cryptography, Forensics, AppSec; Hardware — CAD, RTL; Science — Biology, Chemistry, Physics, Earth, Robotics, Math, Linguistics; Operations — Finance, Logistics, Supply chain, Claims, Compliance, Marketing; Media — Music, Design. The full scope sentences live in the taxonomy guidance.

## REQ-SUB-SOF-systems
- obligation: conditional
- scope: task
- stages: proposal,batch
- source: p.22
- section: Software / Systems
- explained_in: 01-taxonomy-and-batch/TAXONOMY.md
- compliance_check: If this subcategory is selected, the task fits this description.
- evidence: proposal.md; batch-slot.md
- contradiction_or_rejection_risk: Release-composition adjectives (largest, smallest, single-task slice) are not quotas. The one-task rule applies only to Science, Operations, and Media.
- requirement: Low-level and infrastructure work: storage engines, concurrency, crash recovery, schedulers, sysadmin-grade debugging. Source example: fix write-ahead-log recovery so a storage engine survives crash-and-replay with correct ordering semantics. Described as the largest single subcategory in the official release, which is not a quota.

## REQ-SUB-SOF-algorithms
- obligation: conditional
- scope: task
- stages: proposal,batch
- source: p.22
- section: Software / Algorithms
- explained_in: 01-taxonomy-and-batch/TAXONOMY.md
- compliance_check: If this subcategory is selected, the task fits this description.
- evidence: proposal.md; batch-slot.md
- contradiction_or_rejection_risk: Release-composition adjectives (largest, smallest, single-task slice) are not quotas. The one-task rule applies only to Science, Operations, and Media.
- requirement: Correctness- and complexity-driven problems whose difficulty is in the logic, not the environment. Includes performance work. The source says speed and efficiency are first-class and correctness alone is not enough. Contest and LeetCode premises remain prohibited.

## REQ-SUB-SOF-frontend
- obligation: conditional
- scope: task
- stages: proposal,batch
- source: p.22
- section: Software / Frontend
- explained_in: 01-taxonomy-and-batch/TAXONOMY.md
- compliance_check: If this subcategory is selected, the task fits this description.
- evidence: proposal.md; batch-slot.md
- contradiction_or_rejection_risk: Release-composition adjectives (largest, smallest, single-task slice) are not quotas. The one-task rule applies only to Science, Operations, and Media.
- requirement: Browser-facing application work: UI state, validation, client/server contracts. Source example: a broken React/TypeScript lead-intake app whose submission pipeline must stay consistent across validation, ledger reconciliation, and CRM export.

## REQ-SUB-SOF-data-engineering
- obligation: conditional
- scope: task
- stages: proposal,batch
- source: p.22
- section: Software / Data engineering
- explained_in: 01-taxonomy-and-batch/TAXONOMY.md
- compliance_check: If this subcategory is selected, the task fits this description.
- evidence: proposal.md; batch-slot.md
- contradiction_or_rejection_risk: Release-composition adjectives (largest, smallest, single-task slice) are not quotas. The one-task rule applies only to Science, Operations, and Media.
- requirement: Streaming and batch pipelines. Source example: debugging five interacting failures in a stream-processing engine's session-window GC, merge, and watermark logic, each guarded by a misleading comment.

## REQ-SUB-SOF-databases
- obligation: conditional
- scope: task
- stages: proposal,batch
- source: p.22
- section: Software / Databases
- explained_in: 01-taxonomy-and-batch/TAXONOMY.md
- compliance_check: If this subcategory is selected, the task fits this description.
- evidence: proposal.md; batch-slot.md
- contradiction_or_rejection_risk: Release-composition adjectives (largest, smallest, single-task slice) are not quotas. The one-task rule applies only to Science, Operations, and Media.
- requirement: Query engines, schema and migration work, transactional semantics, performance tuning. The source says these often run multi-container because databases are one of the richer environments agents must explore. Multi-container is descriptive, not mandatory for every database task.

## REQ-SUB-ML-inference
- obligation: conditional
- scope: task
- stages: proposal,batch
- source: p.22
- section: ML / Inference
- explained_in: 01-taxonomy-and-batch/TAXONOMY.md
- compliance_check: If this subcategory is selected, the task fits this description.
- evidence: proposal.md; batch-slot.md
- contradiction_or_rejection_risk: Release-composition adjectives (largest, smallest, single-task slice) are not quotas. The one-task rule applies only to Science, Operations, and Media.
- requirement: Serving-side work: latency, throughput, batching, deployment config. Framed as LLM inference optimization. Described as the largest ML subcategory in the official release, which is not a quota.

## REQ-SUB-ML-evaluation
- obligation: conditional
- scope: task
- stages: proposal,batch
- source: p.22
- section: ML / Evaluation
- explained_in: 01-taxonomy-and-batch/TAXONOMY.md
- compliance_check: If this subcategory is selected, the task fits this description.
- evidence: proposal.md; batch-slot.md
- contradiction_or_rejection_risk: Release-composition adjectives (largest, smallest, single-task slice) are not quotas. The one-task rule applies only to Science, Operations, and Media.
- requirement: Building and repairing measurement machinery: metrics, statistical tests, monitoring. Source example: repairing a drift monitor whose statistical tests and alerting layer break in ways that mimic real production noise.

## REQ-SUB-ML-training
- obligation: conditional
- scope: task
- stages: proposal,batch
- source: p.22
- section: ML / Training
- explained_in: 01-taxonomy-and-batch/TAXONOMY.md
- compliance_check: If this subcategory is selected, the task fits this description.
- evidence: proposal.md; batch-slot.md
- contradiction_or_rejection_risk: Release-composition adjectives (largest, smallest, single-task slice) are not quotas. The one-task rule applies only to Science, Operations, and Media.
- requirement: Post-training and optimization loops: SFT and RL of small language models. GPU tasks get a single H100. See also REQ-TX-006.

## REQ-SUB-ML-kernels
- obligation: conditional
- scope: task
- stages: proposal,batch
- source: p.23
- section: ML / Kernels
- explained_in: 01-taxonomy-and-batch/TAXONOMY.md
- compliance_check: If this subcategory is selected, the task fits this description.
- evidence: proposal.md; batch-slot.md
- contradiction_or_rejection_risk: Release-composition adjectives (largest, smallest, single-task slice) are not quotas. The one-task rule applies only to Science, Operations, and Media.
- requirement: GPU programming: writing and optimizing CUDA or Triton kernels, enabled by GPU resource containers. Described as the smallest ML bucket in the official release, which is not a quota.

## REQ-SUB-SEC-cryptography
- obligation: conditional
- scope: task
- stages: proposal,batch
- source: p.23
- section: Security / Cryptography
- explained_in: 01-taxonomy-and-batch/TAXONOMY.md
- compliance_check: If this subcategory is selected, the task fits this description.
- evidence: proposal.md; batch-slot.md
- contradiction_or_rejection_risk: Release-composition adjectives (largest, smallest, single-task slice) are not quotas. The one-task rule applies only to Science, Operations, and Media.
- requirement: Breaking or correctly implementing cryptographic constructions: weak primitives, protocol flaws, key recovery. The source's verification note is that you recovered the plaintext or you did not.

## REQ-SUB-SEC-forensics
- obligation: conditional
- scope: task
- stages: proposal,batch
- source: p.23
- section: Security / Forensics
- explained_in: 01-taxonomy-and-batch/TAXONOMY.md
- compliance_check: If this subcategory is selected, the task fits this description.
- evidence: proposal.md; batch-slot.md
- contradiction_or_rejection_risk: Release-composition adjectives (largest, smallest, single-task slice) are not quotas. The one-task rule applies only to Science, Operations, and Media.
- requirement: Reconstructing events from artifacts: packet captures, logs, disk images, memory dumps. Evidence-chaining over long horizons. The source prefers iterative tasks solved through trial and error, not read-and-solve.

## REQ-SUB-SEC-appsec
- obligation: conditional
- scope: task
- stages: proposal,batch
- source: p.23
- section: Security / AppSec
- explained_in: 01-taxonomy-and-batch/TAXONOMY.md
- compliance_check: If this subcategory is selected, the task fits this description.
- evidence: proposal.md; batch-slot.md
- contradiction_or_rejection_risk: Release-composition adjectives (largest, smallest, single-task slice) are not quotas. The one-task rule applies only to Science, Operations, and Media.
- requirement: Application-layer vulnerability discovery and remediation: injection, auth flaws, unsafe deserialization, dependency risk. Described as the smallest security bucket and the closest in shape to ordinary software engineering. Graded output is a repaired behavior or a verified finding, not a procedure for attacking a real system.

## REQ-SUB-HAR-cad
- obligation: conditional
- scope: task
- stages: proposal,batch
- source: p.23
- section: Hardware / CAD
- explained_in: 01-taxonomy-and-batch/TAXONOMY.md
- compliance_check: If this subcategory is selected, the task fits this description.
- evidence: proposal.md; batch-slot.md
- contradiction_or_rejection_risk: Release-composition adjectives (largest, smallest, single-task slice) are not quotas. The one-task rule applies only to Science, Operations, and Media.
- requirement: Programmatic mechanical and geometric modelling: parametric solids, tolerances, exported artifacts checked against geometric ground truth. Described as the larger of the two hardware buckets in the official release.

## REQ-SUB-HAR-rtl
- obligation: conditional
- scope: task
- stages: proposal,batch
- source: p.23
- section: Hardware / RTL
- explained_in: 01-taxonomy-and-batch/TAXONOMY.md
- compliance_check: If this subcategory is selected, the task fits this description.
- evidence: proposal.md; batch-slot.md
- contradiction_or_rejection_risk: Release-composition adjectives (largest, smallest, single-task slice) are not quotas. The one-task rule applies only to Science, Operations, and Media.
- requirement: Register-transfer-level digital design: Verilog/VHDL, testbenches, simulation, synthesis-aware correctness. Described as a single-task slice of the official release, which is a description of that release, not a freelancer quota.

## REQ-SUB-SCI-biology
- obligation: conditional
- scope: task
- stages: proposal,batch
- source: p.23
- section: Science / Biology
- explained_in: 01-taxonomy-and-batch/TAXONOMY.md
- compliance_check: If this subcategory is selected, the task fits this description. This deprioritized subcategory is used at most once in the batch.
- evidence: proposal.md; batch-slot.md
- contradiction_or_rejection_risk: Release-composition adjectives (largest, smallest, single-task slice) are not quotas. The one-task rule applies only to Science, Operations, and Media.
- requirement: Genomics, proteomics, structural/computational biology, bioinformatics. Deprioritized: one task for this subcategory this round. Computational only.

## REQ-SUB-SCI-chemistry
- obligation: conditional
- scope: task
- stages: proposal,batch
- source: p.23
- section: Science / Chemistry
- explained_in: 01-taxonomy-and-batch/TAXONOMY.md
- compliance_check: If this subcategory is selected, the task fits this description. This deprioritized subcategory is used at most once in the batch.
- evidence: proposal.md; batch-slot.md
- contradiction_or_rejection_risk: Release-composition adjectives (largest, smallest, single-task slice) are not quotas. The one-task rule applies only to Science, Operations, and Media.
- requirement: Molecular structure, spectra, crystallography, reaction/property analysis. Deprioritized: one task for this subcategory this round. Computational analysis, not a production procedure.

## REQ-SUB-SCI-physics
- obligation: conditional
- scope: task
- stages: proposal,batch
- source: p.23
- section: Science / Physics
- explained_in: 01-taxonomy-and-batch/TAXONOMY.md
- compliance_check: If this subcategory is selected, the task fits this description. This deprioritized subcategory is used at most once in the batch.
- evidence: proposal.md; batch-slot.md
- contradiction_or_rejection_risk: Release-composition adjectives (largest, smallest, single-task slice) are not quotas. The one-task rule applies only to Science, Operations, and Media.
- requirement: Simulation and numerical modeling of physical systems, including electromagnetic/FDTD device simulation and inverse design. Deprioritized: one task for this subcategory this round.

## REQ-SUB-SCI-earth
- obligation: conditional
- scope: task
- stages: proposal,batch
- source: p.23
- section: Science / Earth
- explained_in: 01-taxonomy-and-batch/TAXONOMY.md
- compliance_check: If this subcategory is selected, the task fits this description. This deprioritized subcategory is used at most once in the batch.
- evidence: proposal.md; batch-slot.md
- contradiction_or_rejection_risk: Release-composition adjectives (largest, smallest, single-task slice) are not quotas. The one-task rule applies only to Science, Operations, and Media.
- requirement: Earth, climate, hydrology, and environmental modeling. Deprioritized: one task for this subcategory this round.

## REQ-SUB-SCI-robotics
- obligation: conditional
- scope: task
- stages: proposal,batch
- source: p.23
- section: Science / Robotics
- explained_in: 01-taxonomy-and-batch/TAXONOMY.md
- compliance_check: If this subcategory is selected, the task fits this description. This deprioritized subcategory is used at most once in the batch.
- evidence: proposal.md; batch-slot.md
- contradiction_or_rejection_risk: Release-composition adjectives (largest, smallest, single-task slice) are not quotas. The one-task rule applies only to Science, Operations, and Media.
- requirement: Dynamics, trajectory optimization, control. Deprioritized: one task for this subcategory this round.

## REQ-SUB-SCI-math
- obligation: conditional
- scope: task
- stages: proposal,batch
- source: p.23
- section: Science / Math
- explained_in: 01-taxonomy-and-batch/TAXONOMY.md
- compliance_check: If this subcategory is selected, the task fits this description. This deprioritized subcategory is used at most once in the batch.
- evidence: proposal.md; batch-slot.md
- contradiction_or_rejection_risk: Release-composition adjectives (largest, smallest, single-task slice) are not quotas. The one-task rule applies only to Science, Operations, and Media.
- requirement: Formalized mathematics and theorem proving (Coq/Lean/Isabelle), formal verification. Deprioritized: one task for this subcategory this round. Olympiad and contest problems remain prohibited.

## REQ-SUB-SCI-linguistics
- obligation: conditional
- scope: task
- stages: proposal,batch
- source: p.23
- section: Science / Linguistics
- explained_in: 01-taxonomy-and-batch/TAXONOMY.md
- compliance_check: If this subcategory is selected, the task fits this description. This deprioritized subcategory is used at most once in the batch.
- evidence: proposal.md; batch-slot.md
- contradiction_or_rejection_risk: Release-composition adjectives (largest, smallest, single-task slice) are not quotas. The one-task rule applies only to Science, Operations, and Media.
- requirement: Computational and historical linguistics. Deprioritized: one task for this subcategory this round.

## REQ-SUB-OPE-finance
- obligation: conditional
- scope: task
- stages: proposal,batch
- source: p.23
- section: Operations / Finance
- explained_in: 01-taxonomy-and-batch/TAXONOMY.md
- compliance_check: If this subcategory is selected, the task fits this description. This deprioritized subcategory is used at most once in the batch.
- evidence: proposal.md; batch-slot.md
- contradiction_or_rejection_risk: Release-composition adjectives (largest, smallest, single-task slice) are not quotas. The one-task rule applies only to Science, Operations, and Media.
- requirement: Quantitative finance, risk, regulatory capital. Deprioritized: one task for this subcategory this round.

## REQ-SUB-OPE-logistics
- obligation: conditional
- scope: task
- stages: proposal,batch
- source: p.23
- section: Operations / Logistics
- explained_in: 01-taxonomy-and-batch/TAXONOMY.md
- compliance_check: If this subcategory is selected, the task fits this description. This deprioritized subcategory is used at most once in the batch.
- evidence: proposal.md; batch-slot.md
- contradiction_or_rejection_risk: Release-composition adjectives (largest, smallest, single-task slice) are not quotas. The one-task rule applies only to Science, Operations, and Media.
- requirement: Dispatch, routing, fleet/flight planning, transportation. Deprioritized: one task for this subcategory this round.

## REQ-SUB-OPE-supply-chain
- obligation: conditional
- scope: task
- stages: proposal,batch
- source: p.23
- section: Operations / Supply chain
- explained_in: 01-taxonomy-and-batch/TAXONOMY.md
- compliance_check: If this subcategory is selected, the task fits this description. This deprioritized subcategory is used at most once in the batch.
- evidence: proposal.md; batch-slot.md
- contradiction_or_rejection_risk: Release-composition adjectives (largest, smallest, single-task slice) are not quotas. The one-task rule applies only to Science, Operations, and Media.
- requirement: Procurement, production planning, manufacturing, ERP. Deprioritized: one task for this subcategory this round.

## REQ-SUB-OPE-claims
- obligation: conditional
- scope: task
- stages: proposal,batch
- source: p.24
- section: Operations / Claims
- explained_in: 01-taxonomy-and-batch/TAXONOMY.md
- compliance_check: If this subcategory is selected, the task fits this description. This deprioritized subcategory is used at most once in the batch.
- evidence: proposal.md; batch-slot.md
- contradiction_or_rejection_risk: Release-composition adjectives (largest, smallest, single-task slice) are not quotas. The one-task rule applies only to Science, Operations, and Media.
- requirement: Insurance/utility claims, billing rules, adjudication. Deprioritized: one task for this subcategory this round.

## REQ-SUB-OPE-compliance
- obligation: conditional
- scope: task
- stages: proposal,batch
- source: p.24
- section: Operations / Compliance
- explained_in: 01-taxonomy-and-batch/TAXONOMY.md
- compliance_check: If this subcategory is selected, the task fits this description. This deprioritized subcategory is used at most once in the batch.
- evidence: proposal.md; batch-slot.md
- contradiction_or_rejection_risk: Release-composition adjectives (largest, smallest, single-task slice) are not quotas. The one-task rule applies only to Science, Operations, and Media.
- requirement: Regulatory reporting and compliance workflows. Deprioritized: one task for this subcategory this round.

## REQ-SUB-OPE-marketing
- obligation: conditional
- scope: task
- stages: proposal,batch
- source: p.24
- section: Operations / Marketing
- explained_in: 01-taxonomy-and-batch/TAXONOMY.md
- compliance_check: If this subcategory is selected, the task fits this description. This deprioritized subcategory is used at most once in the batch.
- evidence: proposal.md; batch-slot.md
- contradiction_or_rejection_risk: Release-composition adjectives (largest, smallest, single-task slice) are not quotas. The one-task rule applies only to Science, Operations, and Media.
- requirement: Ads, CTR, marketing analytics. Deprioritized: one task for this subcategory this round.

## REQ-SUB-MED-music
- obligation: conditional
- scope: task
- stages: proposal,batch
- source: p.24
- section: Media / Music
- explained_in: 01-taxonomy-and-batch/TAXONOMY.md
- compliance_check: If this subcategory is selected, the task fits this description. This deprioritized subcategory is used at most once in the batch.
- evidence: proposal.md; batch-slot.md
- contradiction_or_rejection_risk: Release-composition adjectives (largest, smallest, single-task slice) are not quotas. The one-task rule applies only to Science, Operations, and Media.
- requirement: Music theory, audio transcription and processing. Deprioritized: one task for this subcategory this round.

## REQ-SUB-MED-design
- obligation: conditional
- scope: task
- stages: proposal,batch
- source: p.24
- section: Media / Design
- explained_in: 01-taxonomy-and-batch/TAXONOMY.md
- compliance_check: If this subcategory is selected, the task fits this description. This deprioritized subcategory is used at most once in the batch.
- evidence: proposal.md; batch-slot.md
- contradiction_or_rejection_risk: Release-composition adjectives (largest, smallest, single-task slice) are not quotas. The one-task rule applies only to Science, Operations, and Media.
- requirement: Visual/layout design and reconstruction. Deprioritized: one task for this subcategory this round.

## REQ-TX-009
- obligation: mandatory
- scope: task
- stages: proposal
- source: p.7 §4.2 with p.22 Algorithms and p.23 Math
- section: No contest inside the taxonomy
- explained_in: 01-taxonomy-and-batch/TAXONOMY.md
- compliance_check: The proposal's difficulty is an engineering or formal-verification constraint inside a realistic system, not a contest statement.
- evidence: proposal.md
- contradiction_or_rejection_risk: The taxonomy example does not waive p.7.
- requirement: Algorithms may include performance work, and Math may be formal proof, but LeetCode-style, olympiad, and 'invent a hard problem' tasks remain prohibited.

## REQ-AC-001
- obligation: mandatory
- scope: process
- stages: acceptance
- source: p.25
- section: Taxonomies tab
- explained_in: 00-source/INVENTORY.md
- compliance_check: Batch evidence uses that table.
- evidence: batch-slot.md
- contradiction_or_rejection_risk: Do not wait for a separate tab that is not in the file.
- requirement: Acceptance says to see the Taxonomies tab. In this PDF that content is the category table on pp. 22–24.

## REQ-AC-002
- obligation: mandatory
- scope: task
- stages: acceptance,stage2
- source: p.25
- section: Acceptance difficulty
- explained_in: 03-difficulty-and-horizon/DESIGN.md
- compliance_check: Record both the Stage 2 predicate and the acceptance pass rate. C-DIFFICULTY does not let either replace the other. The 8-hour phrase is C-TIMEOUT and is also unresolved.
- evidence: stage2.txt
- contradiction_or_rejection_risk: C-DIFFICULTY. C-TIMEOUT.
- requirement: Difficulty gate as printed: roll out with an anonymous model, timeout limit 8 hrs, 8 rollouts, pass rate ≤ 0.6. The metrics table says ≤ 0.6 i.e 4/8. The note says the anonymous model is close to GPT-6-Sol-xhigh performance.

## REQ-AC-003
- obligation: mandatory
- scope: task
- stages: acceptance,stage2
- source: p.25
- section: Acceptance horizon
- explained_in: 14-platform-review/STAGE-2.md
- compliance_check: Every full-credit trajectory that is available has more than 35 assistant turns, and the Stage 2 median is > 80.
- evidence: stage2.txt
- contradiction_or_rejection_risk: C-HORIZON. Median > 80 does not by itself prove every passing run is > 35; inspect the passing runs.
- requirement: Long horizon gate: a minimum of 35 turns of all passing runs in the Anonymous model. The table says Turns (role=assistant): Anonymous > 35 turns.

## REQ-AC-004
- obligation: unresolved
- scope: task
- stages: acceptance
- source: p.25 item 3
- section: Both columns
- explained_in: 00-source/CONFLICT-REGISTER.md
- compliance_check: Satisfy the printed column and the Stage 2 predicates. Do not invent a second model and do not waive a failure because a hidden column might exist.
- evidence: stage2.txt
- contradiction_or_rejection_risk: C-MISSING-COLUMNS.
- requirement: Tasks that fail both difficulty columns, fail solvability, or fail both turn-count columns are rejected. The printed table has a single Latest Frontier Model column.

## REQ-AC-005
- obligation: unresolved
- scope: process
- stages: acceptance
- source: p.25
- section: External automation doc
- explained_in: 14-platform-review/ACCEPTANCE.md
- compliance_check: Execute the six bullets printed under the sentence. Do not invent the rest of the missing file.
- evidence: acceptance.txt
- contradiction_or_rejection_risk: U-AUTOMATION.
- requirement: Each task must pass the full automated and human review pipeline defined in TASK_REVIEW_AUTOMATION.md before it counts as accepted. That file is not in this PDF.

## REQ-AC-006
- obligation: mandatory
- scope: task
- stages: acceptance
- source: p.25 bullet
- section: Pipeline static checks
- explained_in: 14-platform-review/ACCEPTANCE.md
- compliance_check: The static-check table passes. Canary strings are handled only through C-CANARY.
- evidence: static-checks.txt; decision-log.md
- contradiction_or_rejection_risk: C-CANARY.
- requirement: The acceptance pipeline includes static checks: path validation, Dockerfile sanity, canary strings, metadata completeness, and test-reference integrity.

## REQ-AC-007
- obligation: mandatory
- scope: task
- stages: acceptance
- source: p.25 bullet
- section: harbor check
- explained_in: 14-platform-review/ACCEPTANCE.md
- compliance_check: The command used, including arguments the pinned Harbor accepts, is archived. The rubric criteria are the 30 in this PDF.
- evidence: rubric-review.md
- contradiction_or_rejection_risk: U-HARBOR-PIN. The PDF names `harbor check` and does not give its arguments.
- requirement: Implementation rubric review is an automated harbor check scoring against the task-implementation rubric.

## REQ-AC-008
- obligation: mandatory
- scope: task
- stages: acceptance
- source: p.25 bullet
- section: Docker / Oracle / No-op
- explained_in: 14-platform-review/ACCEPTANCE.md
- compliance_check: Build log, oracle 1.0, and nop 0.0 are on the accepted SHA-256.
- evidence: oracle.txt; nop.txt
- contradiction_or_rejection_risk: A no-op that scores anything other than failure fails this bullet.
- requirement: The environment builds cleanly, the reference solution (oracle) passes, and a no-op run fails.

## REQ-AC-009
- obligation: mandatory
- scope: process
- stages: acceptance
- source: p.25 bullet
- section: Maintainer review
- explained_in: 14-platform-review/ACCEPTANCE.md
- compliance_check: acceptance.txt has a maintainer sign-off that postdates the green automated gates.
- evidence: acceptance.txt
- contradiction_or_rejection_risk: Sign-off before the gates are green does not count.
- requirement: Maintainer review is sign-off once all automated gates are green.

## REQ-AC-010
- obligation: mandatory
- scope: task
- stages: acceptance
- source: p.25 bullet
- section: Cheat trials
- explained_in: 14-platform-review/ACCEPTANCE.md
- compliance_check: cheat-trials.md records attempts that include reward-file writes, hardcoded fixtures, and reads of hidden tests, and shows they fail.
- evidence: cheat-trials.md
- contradiction_or_rejection_risk: C-LEGACY-CARDS. The old card name Cheat Trial may be absent. The printed cheat-trial obligation remains.
- requirement: Agent and cheat trials: live agent trials plus adversarial cheat trials specifically probing for reward hacking.

## REQ-AC-011
- obligation: mandatory
- scope: task
- stages: acceptance
- source: p.26 bullet
- section: Hacker-fixer loop
- explained_in: 14-platform-review/ACCEPTANCE.md
- compliance_check: The last recorded cheat attempt fails, and Oracle still scores 1.0 after the hardening.
- evidence: cheat-trials.md; oracle.txt
- contradiction_or_rejection_risk: Stopping after the first failed cheat, if a later one succeeds, does not close the loop.
- requirement: Harden iteratively until an adversarial agent can no longer exploit the verifier.

## REQ-AC-012
- obligation: unresolved
- scope: process
- stages: acceptance
- source: p.26
- section: All four criteria
- explained_in: 00-source/CONFLICT-REGISTER.md
- compliance_check: The task is not called accepted at submission or at static-check pass. All printed pipeline bullets are still required. The word four is not mapped onto a subset.
- evidence: acceptance.txt
- contradiction_or_rejection_risk: C-FOUR-CRITERIA. Six bullets are printed.
- requirement: A task is considered accepted only once it clears all four criteria and is merged following this pipeline — not upon submission or upon passing static checks alone.

## REQ-AC-013
- obligation: unresolved
- scope: process
- stages: all
- source: PDF outline
- section: Terms of use
- explained_in: 00-source/UNRESOLVED.md
- compliance_check: The human accepts the live clickwrap. This system does not restate terms that are not in the PDF.
- evidence: decision-log.md
- contradiction_or_rejection_risk: U-TERMS.
- requirement: The outline contains 'Terms of Use / Clickwrap Agreement' with no in-PDF page (target -1).

## REQ-UI-001
- obligation: platform
- scope: platform
- stages: all
- source: pp. 5, 10, 11, 13 screenshots
- section: Stage tabs
- explained_in: 14-platform-review/ACCEPTANCE.md
- compliance_check: Stage 3 is not marked passed while the badge says DEFERRED.
- evidence: stage1.txt
- contradiction_or_rejection_risk: C-LEGACY-CARDS. U-STAGE3. A deferred Stage 3 tab is not a QC pass.
- requirement: The UI tabs are Stage 0 • Task proposal, Stage 1 • Static checks, Stage 2 • Model rollout, and Stage 3 • Qualitative checks marked DEFERRED.

## REQ-UI-002
- obligation: example
- scope: process
- stages: proposal
- source: p.4 screenshot
- section: Form prompts
- explained_in: 04-proposal/PROPOSAL.md
- compliance_check: Those four prompts are covered by the six §3.3 topics inside the 2000-character cap.
- evidence: proposal.md
- contradiction_or_rejection_risk: Answering the four prompts while skipping 'why it is distinct' still fails §3.3.
- requirement: The markdown box prompts the author to describe the task, starting inputs, and expected outcome; explain how the result will be verified programmatically; explain why the task is difficult and useful; and explain why an expert can solve it within the estimated time.

## REQ-PL-I01-UPLOAD_SNAPSHOT
- obligation: platform
- scope: platform
- stages: stage1
- source: pp. 10–11 screenshots; gate prose pp. 9–11
- section: I01 Upload snapshot
- explained_in: 00-source/PLATFORM-RULE-CATALOG.md
- compliance_check: Stage 1 blocking reason is not this id, or the outcome is a documented retry rather than a task rewrite when the prose classifies it as platform-side.
- evidence: stage1.txt
- contradiction_or_rejection_risk: U-SEVERITY-ALIGNMENT. Severity badges in the screenshots were not column-aligned, so this row does not assert REQUIRED versus OPTIONAL.
- requirement: Platform phase `UPLOAD_SNAPSHOT` is visible under I01 Upload snapshot. Confidence: screenshot. The author prevents the failing condition named by the rule and archives the live text if it fires.

## REQ-PL-I01-SNAPSHOT-UNREADABLE
- obligation: platform
- scope: platform
- stages: stage1
- source: pp. 10–11 screenshots; gate prose pp. 9–11
- section: I01 Upload snapshot
- explained_in: 00-source/PLATFORM-RULE-CATALOG.md
- compliance_check: Stage 1 blocking reason is not this id, or the outcome is a documented retry rather than a task rewrite when the prose classifies it as platform-side.
- evidence: stage1.txt
- contradiction_or_rejection_risk: U-SEVERITY-ALIGNMENT. Severity badges in the screenshots were not column-aligned, so this row does not assert REQUIRED versus OPTIONAL.
- requirement: Platform rule `SNAPSHOT.UNREADABLE` is visible under I01 Upload snapshot. Confidence: screenshot. The author prevents the failing condition named by the rule and archives the live text if it fires.

## REQ-PL-I01-SNAPSHOT-MUTATING
- obligation: platform
- scope: platform
- stages: stage1
- source: pp. 10–11 screenshots; gate prose pp. 9–11
- section: I01 Upload snapshot
- explained_in: 00-source/PLATFORM-RULE-CATALOG.md
- compliance_check: Stage 1 blocking reason is not this id, or the outcome is a documented retry rather than a task rewrite when the prose classifies it as platform-side.
- evidence: stage1.txt
- contradiction_or_rejection_risk: U-SEVERITY-ALIGNMENT. Severity badges in the screenshots were not column-aligned, so this row does not assert REQUIRED versus OPTIONAL.
- requirement: Platform rule `SNAPSHOT.MUTATING` is visible under I01 Upload snapshot. Confidence: screenshot. The author prevents the failing condition named by the rule and archives the live text if it fires.

## REQ-PL-G01-ZIP_INVENTORY
- obligation: platform
- scope: platform
- stages: stage1
- source: pp. 10–11 screenshots; gate prose pp. 9–11
- section: G01 Archive safety
- explained_in: 00-source/PLATFORM-RULE-CATALOG.md
- compliance_check: Stage 1 blocking reason is not this id, or the outcome is a documented retry rather than a task rewrite when the prose classifies it as platform-side.
- evidence: stage1.txt
- contradiction_or_rejection_risk: U-SEVERITY-ALIGNMENT. Severity badges in the screenshots were not column-aligned, so this row does not assert REQUIRED versus OPTIONAL.
- requirement: Platform phase `ZIP_INVENTORY` is visible under G01 Archive safety. Confidence: screenshot. The author prevents the failing condition named by the rule and archives the live text if it fires.

## REQ-PL-G01-STREAM_READ
- obligation: platform
- scope: platform
- stages: stage1
- source: pp. 10–11 screenshots; gate prose pp. 9–11
- section: G01 Archive safety
- explained_in: 00-source/PLATFORM-RULE-CATALOG.md
- compliance_check: Stage 1 blocking reason is not this id, or the outcome is a documented retry rather than a task rewrite when the prose classifies it as platform-side.
- evidence: stage1.txt
- contradiction_or_rejection_risk: U-SEVERITY-ALIGNMENT. Severity badges in the screenshots were not column-aligned, so this row does not assert REQUIRED versus OPTIONAL.
- requirement: Platform phase `STREAM_READ` is visible under G01 Archive safety. Confidence: screenshot. The author prevents the failing condition named by the rule and archives the live text if it fires.

## REQ-PL-G01-MATERIALIZE
- obligation: platform
- scope: platform
- stages: stage1
- source: pp. 10–11 screenshots; gate prose pp. 9–11
- section: G01 Archive safety
- explained_in: 00-source/PLATFORM-RULE-CATALOG.md
- compliance_check: Stage 1 blocking reason is not this id, or the outcome is a documented retry rather than a task rewrite when the prose classifies it as platform-side.
- evidence: stage1.txt
- contradiction_or_rejection_risk: U-SEVERITY-ALIGNMENT. Severity badges in the screenshots were not column-aligned, so this row does not assert REQUIRED versus OPTIONAL.
- requirement: Platform phase `MATERIALIZE` is visible under G01 Archive safety. Confidence: screenshot. The author prevents the failing condition named by the rule and archives the live text if it fires.

## REQ-PL-G01-CANDIDATE_ROOT
- obligation: platform
- scope: platform
- stages: stage1
- source: pp. 10–11 screenshots; gate prose pp. 9–11
- section: G01 Archive safety
- explained_in: 00-source/PLATFORM-RULE-CATALOG.md
- compliance_check: Stage 1 blocking reason is not this id, or the outcome is a documented retry rather than a task rewrite when the prose classifies it as platform-side.
- evidence: stage1.txt
- contradiction_or_rejection_risk: U-SEVERITY-ALIGNMENT. Severity badges in the screenshots were not column-aligned, so this row does not assert REQUIRED versus OPTIONAL.
- requirement: Platform phase `CANDIDATE_ROOT` is visible under G01 Archive safety. Confidence: screenshot. The author prevents the failing condition named by the rule and archives the live text if it fires.

## REQ-PL-G01-ZIP-UNREADABLE
- obligation: platform
- scope: platform
- stages: stage1
- source: pp. 10–11 screenshots; gate prose pp. 9–11
- section: G01 Archive safety
- explained_in: 00-source/PLATFORM-RULE-CATALOG.md
- compliance_check: Stage 1 blocking reason is not this id, or the outcome is a documented retry rather than a task rewrite when the prose classifies it as platform-side.
- evidence: stage1.txt
- contradiction_or_rejection_risk: U-SEVERITY-ALIGNMENT. Severity badges in the screenshots were not column-aligned, so this row does not assert REQUIRED versus OPTIONAL.
- requirement: Platform rule `ZIP.UNREADABLE` is visible under G01 Archive safety. Confidence: screenshot. The author prevents the failing condition named by the rule and archives the live text if it fires.

## REQ-PL-G01-ZIP-UNSUPPORTED_COMPRESSION
- obligation: platform
- scope: platform
- stages: stage1
- source: pp. 10–11 screenshots; gate prose pp. 9–11
- section: G01 Archive safety
- explained_in: 00-source/PLATFORM-RULE-CATALOG.md
- compliance_check: Stage 1 blocking reason is not this id, or the outcome is a documented retry rather than a task rewrite when the prose classifies it as platform-side.
- evidence: stage1.txt
- contradiction_or_rejection_risk: U-SEVERITY-ALIGNMENT. Severity badges in the screenshots were not column-aligned, so this row does not assert REQUIRED versus OPTIONAL.
- requirement: Platform rule `ZIP.UNSUPPORTED_COMPRESSION` is visible under G01 Archive safety. Confidence: screenshot. The author prevents the failing condition named by the rule and archives the live text if it fires.

## REQ-PL-G01-ZIP-ENCRYPTED_MEMBER
- obligation: platform
- scope: platform
- stages: stage1
- source: pp. 10–11 screenshots; gate prose pp. 9–11
- section: G01 Archive safety
- explained_in: 00-source/PLATFORM-RULE-CATALOG.md
- compliance_check: Stage 1 blocking reason is not this id, or the outcome is a documented retry rather than a task rewrite when the prose classifies it as platform-side.
- evidence: stage1.txt
- contradiction_or_rejection_risk: U-SEVERITY-ALIGNMENT. Severity badges in the screenshots were not column-aligned, so this row does not assert REQUIRED versus OPTIONAL.
- requirement: Platform rule `ZIP.ENCRYPTED_MEMBER` is visible under G01 Archive safety. Confidence: screenshot. The author prevents the failing condition named by the rule and archives the live text if it fires.

## REQ-PL-G01-ZIP-TOO_LARGE
- obligation: platform
- scope: platform
- stages: stage1
- source: pp. 10–11 screenshots; gate prose pp. 9–11
- section: G01 Archive safety
- explained_in: 00-source/PLATFORM-RULE-CATALOG.md
- compliance_check: Stage 1 blocking reason is not this id, or the outcome is a documented retry rather than a task rewrite when the prose classifies it as platform-side.
- evidence: stage1.txt
- contradiction_or_rejection_risk: U-SEVERITY-ALIGNMENT. Severity badges in the screenshots were not column-aligned, so this row does not assert REQUIRED versus OPTIONAL.
- requirement: Platform rule `ZIP.TOO_LARGE` is visible under G01 Archive safety. Confidence: screenshot. The author prevents the failing condition named by the rule and archives the live text if it fires.

## REQ-PL-G01-ZIP-EXPANDED_TOO_LARGE
- obligation: platform
- scope: platform
- stages: stage1
- source: pp. 10–11 screenshots; gate prose pp. 9–11
- section: G01 Archive safety
- explained_in: 00-source/PLATFORM-RULE-CATALOG.md
- compliance_check: Stage 1 blocking reason is not this id, or the outcome is a documented retry rather than a task rewrite when the prose classifies it as platform-side.
- evidence: stage1.txt
- contradiction_or_rejection_risk: U-SEVERITY-ALIGNMENT. Severity badges in the screenshots were not column-aligned, so this row does not assert REQUIRED versus OPTIONAL.
- requirement: Platform rule `ZIP.EXPANDED_TOO_LARGE` is visible under G01 Archive safety. Confidence: screenshot. The author prevents the failing condition named by the rule and archives the live text if it fires.

## REQ-PL-G01-ZIP-TOO_MANY_MEMBERS
- obligation: platform
- scope: platform
- stages: stage1
- source: pp. 10–11 screenshots; gate prose pp. 9–11
- section: G01 Archive safety
- explained_in: 00-source/PLATFORM-RULE-CATALOG.md
- compliance_check: Stage 1 blocking reason is not this id, or the outcome is a documented retry rather than a task rewrite when the prose classifies it as platform-side.
- evidence: stage1.txt
- contradiction_or_rejection_risk: U-SEVERITY-ALIGNMENT. Severity badges in the screenshots were not column-aligned, so this row does not assert REQUIRED versus OPTIONAL.
- requirement: Platform rule `ZIP.TOO_MANY_MEMBERS` is visible under G01 Archive safety. Confidence: screenshot. The author prevents the failing condition named by the rule and archives the live text if it fires.

## REQ-PL-G01-ZIP-MEMBER_TOO_LARGE
- obligation: platform
- scope: platform
- stages: stage1
- source: pp. 10–11 screenshots; gate prose pp. 9–11
- section: G01 Archive safety
- explained_in: 00-source/PLATFORM-RULE-CATALOG.md
- compliance_check: Stage 1 blocking reason is not this id, or the outcome is a documented retry rather than a task rewrite when the prose classifies it as platform-side.
- evidence: stage1.txt
- contradiction_or_rejection_risk: U-SEVERITY-ALIGNMENT. Severity badges in the screenshots were not column-aligned, so this row does not assert REQUIRED versus OPTIONAL.
- requirement: Platform rule `ZIP.MEMBER_TOO_LARGE` is visible under G01 Archive safety. Confidence: screenshot. The author prevents the failing condition named by the rule and archives the live text if it fires.

## REQ-PL-G01-ZIP-COMPRESSION_RATIO
- obligation: platform
- scope: platform
- stages: stage1
- source: pp. 10–11 screenshots; gate prose pp. 9–11
- section: G01 Archive safety
- explained_in: 00-source/PLATFORM-RULE-CATALOG.md
- compliance_check: Stage 1 blocking reason is not this id, or the outcome is a documented retry rather than a task rewrite when the prose classifies it as platform-side.
- evidence: stage1.txt
- contradiction_or_rejection_risk: U-SEVERITY-ALIGNMENT. Severity badges in the screenshots were not column-aligned, so this row does not assert REQUIRED versus OPTIONAL.
- requirement: Platform rule `ZIP.COMPRESSION_RATIO` is visible under G01 Archive safety. Confidence: screenshot. The author prevents the failing condition named by the rule and archives the live text if it fires.

## REQ-PL-G01-ZIP-PATH_TRAVERSAL
- obligation: platform
- scope: platform
- stages: stage1
- source: pp. 10–11 screenshots; gate prose pp. 9–11
- section: G01 Archive safety
- explained_in: 00-source/PLATFORM-RULE-CATALOG.md
- compliance_check: Stage 1 blocking reason is not this id, or the outcome is a documented retry rather than a task rewrite when the prose classifies it as platform-side.
- evidence: stage1.txt
- contradiction_or_rejection_risk: U-SEVERITY-ALIGNMENT. Severity badges in the screenshots were not column-aligned, so this row does not assert REQUIRED versus OPTIONAL.
- requirement: Platform rule `ZIP.PATH_TRAVERSAL` is visible under G01 Archive safety. Confidence: screenshot. The author prevents the failing condition named by the rule and archives the live text if it fires.

## REQ-PL-G01-ZIP-ABSOLUTE_PATH
- obligation: platform
- scope: platform
- stages: stage1
- source: pp. 10–11 screenshots; gate prose pp. 9–11
- section: G01 Archive safety
- explained_in: 00-source/PLATFORM-RULE-CATALOG.md
- compliance_check: Stage 1 blocking reason is not this id, or the outcome is a documented retry rather than a task rewrite when the prose classifies it as platform-side.
- evidence: stage1.txt
- contradiction_or_rejection_risk: U-SEVERITY-ALIGNMENT. Severity badges in the screenshots were not column-aligned, so this row does not assert REQUIRED versus OPTIONAL.
- requirement: Platform rule `ZIP.ABSOLUTE_PATH` is visible under G01 Archive safety. Confidence: screenshot. The author prevents the failing condition named by the rule and archives the live text if it fires.

## REQ-PL-G01-ZIP-CRC_MISMATCH
- obligation: platform
- scope: platform
- stages: stage1
- source: pp. 10–11 screenshots; gate prose pp. 9–11
- section: G01 Archive safety
- explained_in: 00-source/PLATFORM-RULE-CATALOG.md
- compliance_check: Stage 1 blocking reason is not this id, or the outcome is a documented retry rather than a task rewrite when the prose classifies it as platform-side.
- evidence: stage1.txt
- contradiction_or_rejection_risk: U-SEVERITY-ALIGNMENT. Severity badges in the screenshots were not column-aligned, so this row does not assert REQUIRED versus OPTIONAL.
- requirement: Platform rule `ZIP.CRC_MISMATCH` is visible under G01 Archive safety. Confidence: screenshot. The author prevents the failing condition named by the rule and archives the live text if it fires.

## REQ-PL-G01-ZIP-SYMLINK
- obligation: platform
- scope: platform
- stages: stage1
- source: pp. 10–11 screenshots; gate prose pp. 9–11
- section: G01 Archive safety
- explained_in: 00-source/PLATFORM-RULE-CATALOG.md
- compliance_check: Stage 1 blocking reason is not this id, or the outcome is a documented retry rather than a task rewrite when the prose classifies it as platform-side.
- evidence: stage1.txt
- contradiction_or_rejection_risk: U-SEVERITY-ALIGNMENT. Severity badges in the screenshots were not column-aligned, so this row does not assert REQUIRED versus OPTIONAL.
- requirement: Platform rule `ZIP.SYMLINK` is visible under G01 Archive safety. Confidence: screenshot. The author prevents the failing condition named by the rule and archives the live text if it fires.

## REQ-PL-G01-ZIP-SPECIAL_MEMBER
- obligation: platform
- scope: platform
- stages: stage1
- source: pp. 10–11 screenshots; gate prose pp. 9–11
- section: G01 Archive safety
- explained_in: 00-source/PLATFORM-RULE-CATALOG.md
- compliance_check: Stage 1 blocking reason is not this id, or the outcome is a documented retry rather than a task rewrite when the prose classifies it as platform-side.
- evidence: stage1.txt
- contradiction_or_rejection_risk: U-SEVERITY-ALIGNMENT. Severity badges in the screenshots were not column-aligned, so this row does not assert REQUIRED versus OPTIONAL.
- requirement: Platform rule `ZIP.SPECIAL_MEMBER` is visible under G01 Archive safety. Confidence: screenshot. The author prevents the failing condition named by the rule and archives the live text if it fires.

## REQ-PL-G01-ZIP-NUL_PATH
- obligation: platform
- scope: platform
- stages: stage1
- source: pp. 10–11 screenshots; gate prose pp. 9–11
- section: G01 Archive safety
- explained_in: 00-source/PLATFORM-RULE-CATALOG.md
- compliance_check: Stage 1 blocking reason is not this id, or the outcome is a documented retry rather than a task rewrite when the prose classifies it as platform-side.
- evidence: stage1.txt
- contradiction_or_rejection_risk: U-SEVERITY-ALIGNMENT. Severity badges in the screenshots were not column-aligned, so this row does not assert REQUIRED versus OPTIONAL.
- requirement: Platform rule `ZIP.NUL_PATH` is visible under G01 Archive safety. Confidence: screenshot. The author prevents the failing condition named by the rule and archives the live text if it fires.

## REQ-PL-G01-ZIP-NORMALIZATION_COLLISION
- obligation: platform
- scope: platform
- stages: stage1
- source: pp. 10–11 screenshots; gate prose pp. 9–11
- section: G01 Archive safety
- explained_in: 00-source/PLATFORM-RULE-CATALOG.md
- compliance_check: Stage 1 blocking reason is not this id, or the outcome is a documented retry rather than a task rewrite when the prose classifies it as platform-side.
- evidence: stage1.txt
- contradiction_or_rejection_risk: U-SEVERITY-ALIGNMENT. Severity badges in the screenshots were not column-aligned, so this row does not assert REQUIRED versus OPTIONAL.
- requirement: Platform rule `ZIP.NORMALIZATION_COLLISION` is visible under G01 Archive safety. Confidence: screenshot. The author prevents the failing condition named by the rule and archives the live text if it fires.

## REQ-PL-G01-ZIP-INCOMPLETE_READ
- obligation: platform
- scope: platform
- stages: stage1
- source: pp. 10–11 screenshots; gate prose pp. 9–11
- section: G01 Archive safety
- explained_in: 00-source/PLATFORM-RULE-CATALOG.md
- compliance_check: Stage 1 blocking reason is not this id, or the outcome is a documented retry rather than a task rewrite when the prose classifies it as platform-side.
- evidence: stage1.txt
- contradiction_or_rejection_risk: U-SEVERITY-ALIGNMENT. Severity badges in the screenshots were not column-aligned, so this row does not assert REQUIRED versus OPTIONAL.
- requirement: Platform rule `ZIP.INCOMPLETE_READ` is visible under G01 Archive safety. Confidence: screenshot. The author prevents the failing condition named by the rule and archives the live text if it fires.

## REQ-PL-G01-ZIP-EXTRACTION_FAILED
- obligation: platform
- scope: platform
- stages: stage1
- source: pp. 10–11 screenshots; gate prose pp. 9–11
- section: G01 Archive safety
- explained_in: 00-source/PLATFORM-RULE-CATALOG.md
- compliance_check: Stage 1 blocking reason is not this id, or the outcome is a documented retry rather than a task rewrite when the prose classifies it as platform-side.
- evidence: stage1.txt
- contradiction_or_rejection_risk: U-SEVERITY-ALIGNMENT. Severity badges in the screenshots were not column-aligned, so this row does not assert REQUIRED versus OPTIONAL.
- requirement: Platform rule `ZIP.EXTRACTION_FAILED` is visible under G01 Archive safety. Confidence: screenshot. The author prevents the failing condition named by the rule and archives the live text if it fires.

## REQ-PL-G01-ZIP-INVALID_RECORDS
- obligation: platform
- scope: platform
- stages: stage1
- source: pp. 10–11 screenshots; gate prose pp. 9–11
- section: G01 Archive safety
- explained_in: 00-source/PLATFORM-RULE-CATALOG.md
- compliance_check: Stage 1 blocking reason is not this id, or the outcome is a documented retry rather than a task rewrite when the prose classifies it as platform-side.
- evidence: stage1.txt
- contradiction_or_rejection_risk: U-SEVERITY-ALIGNMENT. Severity badges in the screenshots were not column-aligned, so this row does not assert REQUIRED versus OPTIONAL.
- requirement: Platform rule `ZIP.INVALID_RECORDS` is visible under G01 Archive safety. Confidence: screenshot. The author prevents the failing condition named by the rule and archives the live text if it fires.

## REQ-PL-G01-META-EXCLUDED
- obligation: platform
- scope: platform
- stages: stage1
- source: pp. 10–11 screenshots; gate prose pp. 9–11
- section: G01 Archive safety
- explained_in: 00-source/PLATFORM-RULE-CATALOG.md
- compliance_check: Stage 1 blocking reason is not this id, or the outcome is a documented retry rather than a task rewrite when the prose classifies it as platform-side.
- evidence: stage1.txt
- contradiction_or_rejection_risk: U-SEVERITY-ALIGNMENT. Severity badges in the screenshots were not column-aligned, so this row does not assert REQUIRED versus OPTIONAL.
- requirement: Platform rule `META.EXCLUDED` is visible under G01 Archive safety. Confidence: screenshot. The author prevents the failing condition named by the rule and archives the live text if it fires.

## REQ-PL-G01-ROOT-ZERO_CANDIDATES
- obligation: platform
- scope: platform
- stages: stage1
- source: pp. 10–11 screenshots; gate prose pp. 9–11
- section: G01 Archive safety
- explained_in: 00-source/PLATFORM-RULE-CATALOG.md
- compliance_check: Stage 1 blocking reason is not this id, or the outcome is a documented retry rather than a task rewrite when the prose classifies it as platform-side.
- evidence: stage1.txt
- contradiction_or_rejection_risk: U-SEVERITY-ALIGNMENT. Severity badges in the screenshots were not column-aligned, so this row does not assert REQUIRED versus OPTIONAL.
- requirement: Platform rule `ROOT.ZERO_CANDIDATES` is visible under G01 Archive safety. Confidence: screenshot. The author prevents the failing condition named by the rule and archives the live text if it fires.

## REQ-PL-G01-ROOT-MULTIPLE_CANDIDATES
- obligation: platform
- scope: platform
- stages: stage1
- source: pp. 10–11 screenshots; gate prose pp. 9–11
- section: G01 Archive safety
- explained_in: 00-source/PLATFORM-RULE-CATALOG.md
- compliance_check: Stage 1 blocking reason is not this id, or the outcome is a documented retry rather than a task rewrite when the prose classifies it as platform-side.
- evidence: stage1.txt
- contradiction_or_rejection_risk: U-SEVERITY-ALIGNMENT. Severity badges in the screenshots were not column-aligned, so this row does not assert REQUIRED versus OPTIONAL.
- requirement: Platform rule `ROOT.MULTIPLE_CANDIDATES` is visible under G01 Archive safety. Confidence: screenshot. The author prevents the failing condition named by the rule and archives the live text if it fires.

## REQ-PL-G02-HARBOR_PARSE
- obligation: platform
- scope: platform
- stages: stage1
- source: pp. 10–11 screenshots; gate prose pp. 9–11
- section: G02 Harbor + TB4 contract
- explained_in: 00-source/PLATFORM-RULE-CATALOG.md
- compliance_check: Stage 1 blocking reason is not this id, or the outcome is a documented retry rather than a task rewrite when the prose classifies it as platform-side.
- evidence: stage1.txt
- contradiction_or_rejection_risk: U-SEVERITY-ALIGNMENT. Severity badges in the screenshots were not column-aligned, so this row does not assert REQUIRED versus OPTIONAL.
- requirement: Platform phase `HARBOR_PARSE` is visible under G02 Harbor + TB4 contract. Confidence: screenshot. The author prevents the failing condition named by the rule and archives the live text if it fires.

## REQ-PL-G02-REQUIRED_PATHS
- obligation: platform
- scope: platform
- stages: stage1
- source: pp. 10–11 screenshots; gate prose pp. 9–11
- section: G02 Harbor + TB4 contract
- explained_in: 00-source/PLATFORM-RULE-CATALOG.md
- compliance_check: Stage 1 blocking reason is not this id, or the outcome is a documented retry rather than a task rewrite when the prose classifies it as platform-side.
- evidence: stage1.txt
- contradiction_or_rejection_risk: U-SEVERITY-ALIGNMENT. Severity badges in the screenshots were not column-aligned, so this row does not assert REQUIRED versus OPTIONAL.
- requirement: Platform phase `REQUIRED_PATHS` is visible under G02 Harbor + TB4 contract. Confidence: screenshot. The author prevents the failing condition named by the rule and archives the live text if it fires.

## REQ-PL-G02-TB3_POLICY
- obligation: platform
- scope: platform
- stages: stage1
- source: pp. 10–11 screenshots; gate prose pp. 9–11
- section: G02 Harbor + TB4 contract
- explained_in: 00-source/PLATFORM-RULE-CATALOG.md
- compliance_check: Stage 1 blocking reason is not this id, or the outcome is a documented retry rather than a task rewrite when the prose classifies it as platform-side.
- evidence: stage1.txt
- contradiction_or_rejection_risk: U-SEVERITY-ALIGNMENT. Severity badges in the screenshots were not column-aligned, so this row does not assert REQUIRED versus OPTIONAL.
- requirement: Platform phase `TB3_POLICY` is visible under G02 Harbor + TB4 contract. Confidence: screenshot. The author prevents the failing condition named by the rule and archives the live text if it fires.

## REQ-PL-G02-CAPABILITY_PREFLIGHT
- obligation: platform
- scope: platform
- stages: stage1
- source: pp. 10–11 screenshots; gate prose pp. 9–11
- section: G02 Harbor + TB4 contract
- explained_in: 00-source/PLATFORM-RULE-CATALOG.md
- compliance_check: Stage 1 blocking reason is not this id, or the outcome is a documented retry rather than a task rewrite when the prose classifies it as platform-side.
- evidence: stage1.txt
- contradiction_or_rejection_risk: U-SEVERITY-ALIGNMENT. Severity badges in the screenshots were not column-aligned, so this row does not assert REQUIRED versus OPTIONAL.
- requirement: Platform phase `CAPABILITY_PREFLIGHT` is visible under G02 Harbor + TB4 contract. Confidence: screenshot. The author prevents the failing condition named by the rule and archives the live text if it fires.

## REQ-PL-G02-HARBOR-PARSE_INTEGRATION
- obligation: platform
- scope: platform
- stages: stage1
- source: pp. 10–11 screenshots; gate prose pp. 9–11
- section: G02 Harbor + TB4 contract
- explained_in: 00-source/PLATFORM-RULE-CATALOG.md
- compliance_check: Stage 1 blocking reason is not this id, or the outcome is a documented retry rather than a task rewrite when the prose classifies it as platform-side.
- evidence: stage1.txt
- contradiction_or_rejection_risk: U-SEVERITY-ALIGNMENT. Severity badges in the screenshots were not column-aligned, so this row does not assert REQUIRED versus OPTIONAL.
- requirement: Platform rule `HARBOR.PARSE_INTEGRATION` is visible under G02 Harbor + TB4 contract. Confidence: screenshot. The author prevents the failing condition named by the rule and archives the live text if it fires.

## REQ-PL-G02-TB3-NO_TASK_ROOT
- obligation: platform
- scope: platform
- stages: stage1
- source: pp. 10–11 screenshots; gate prose pp. 9–11
- section: G02 Harbor + TB4 contract
- explained_in: 00-source/PLATFORM-RULE-CATALOG.md
- compliance_check: Stage 1 blocking reason is not this id, or the outcome is a documented retry rather than a task rewrite when the prose classifies it as platform-side.
- evidence: stage1.txt
- contradiction_or_rejection_risk: U-SEVERITY-ALIGNMENT. Severity badges in the screenshots were not column-aligned, so this row does not assert REQUIRED versus OPTIONAL.
- requirement: Platform rule `TB3.NO_TASK_ROOT` is visible under G02 Harbor + TB4 contract. Confidence: screenshot. The author prevents the failing condition named by the rule and archives the live text if it fires.

## REQ-PL-G02-TB3-CATEGORY_INVALID
- obligation: platform
- scope: platform
- stages: stage1
- source: pp. 10–11 screenshots; gate prose pp. 9–11
- section: G02 Harbor + TB4 contract
- explained_in: 00-source/PLATFORM-RULE-CATALOG.md
- compliance_check: Stage 1 blocking reason is not this id, or the outcome is a documented retry rather than a task rewrite when the prose classifies it as platform-side.
- evidence: stage1.txt
- contradiction_or_rejection_risk: U-SEVERITY-ALIGNMENT. Severity badges in the screenshots were not column-aligned, so this row does not assert REQUIRED versus OPTIONAL.
- requirement: Platform rule `TB3.CATEGORY_INVALID` is visible under G02 Harbor + TB4 contract. Confidence: screenshot. The author prevents the failing condition named by the rule and archives the live text if it fires.

## REQ-PL-G02-TB3-METADATA_MISSING
- obligation: platform
- scope: platform
- stages: stage1
- source: pp. 10–11 screenshots; gate prose pp. 9–11
- section: G02 Harbor + TB4 contract
- explained_in: 00-source/PLATFORM-RULE-CATALOG.md
- compliance_check: Stage 1 blocking reason is not this id, or the outcome is a documented retry rather than a task rewrite when the prose classifies it as platform-side.
- evidence: stage1.txt
- contradiction_or_rejection_risk: U-SEVERITY-ALIGNMENT. Severity badges in the screenshots were not column-aligned, so this row does not assert REQUIRED versus OPTIONAL.
- requirement: Platform rule `TB3.METADATA_MISSING` is visible under G02 Harbor + TB4 contract. Confidence: screenshot. The author prevents the failing condition named by the rule and archives the live text if it fires.

## REQ-PL-G02-TB3-CANARY_MISSING
- obligation: platform
- scope: platform
- stages: stage1
- source: pp. 10–11 screenshots; gate prose pp. 9–11
- section: G02 Harbor + TB4 contract
- explained_in: 00-source/PLATFORM-RULE-CATALOG.md
- compliance_check: Stage 1 blocking reason is not this id, or the outcome is a documented retry rather than a task rewrite when the prose classifies it as platform-side.
- evidence: stage1.txt
- contradiction_or_rejection_risk: C-CANARY. U-SEVERITY-ALIGNMENT. Severity badges in the screenshots were not column-aligned, so this row does not assert REQUIRED versus OPTIONAL.
- requirement: Platform rule `TB3.CANARY_MISSING` is visible under G02 Harbor + TB4 contract. Confidence: screenshot. The author prevents the failing condition named by the rule and archives the live text if it fires.

## REQ-PL-G02-TB3-CANARY_ADVISORY
- obligation: advisory
- scope: platform
- stages: stage1
- source: pp. 10–11 screenshots; gate prose pp. 9–11
- section: G02 Harbor + TB4 contract
- explained_in: 00-source/PLATFORM-RULE-CATALOG.md
- compliance_check: Stage 1 blocking reason is not this id, or the outcome is a documented retry rather than a task rewrite when the prose classifies it as platform-side.
- evidence: stage1.txt
- contradiction_or_rejection_risk: Name contains ADVISORY, which p.9 says does not reject. C-CANARY. U-SEVERITY-ALIGNMENT. Severity badges in the screenshots were not column-aligned, so this row does not assert REQUIRED versus OPTIONAL.
- requirement: Platform rule `TB3.CANARY_ADVISORY` is visible under G02 Harbor + TB4 contract. Confidence: screenshot. The author prevents the failing condition named by the rule and archives the live text if it fires.

## REQ-PL-G02-TB3-AUTHORING_ADVISORY
- obligation: advisory
- scope: platform
- stages: stage1
- source: pp. 10–11 screenshots; gate prose pp. 9–11
- section: G02 Harbor + TB4 contract
- explained_in: 00-source/PLATFORM-RULE-CATALOG.md
- compliance_check: Stage 1 blocking reason is not this id, or the outcome is a documented retry rather than a task rewrite when the prose classifies it as platform-side.
- evidence: stage1.txt
- contradiction_or_rejection_risk: Name contains ADVISORY, which p.9 says does not reject. U-SEVERITY-ALIGNMENT. Severity badges in the screenshots were not column-aligned, so this row does not assert REQUIRED versus OPTIONAL.
- requirement: Platform rule `TB3.AUTHORING_ADVISORY` is visible under G02 Harbor + TB4 contract. Confidence: screenshot. The author prevents the failing condition named by the rule and archives the live text if it fires.

## REQ-PL-G02-HARBOR-DEPRECATED_ALLOW_INTERNET
- obligation: platform
- scope: platform
- stages: stage1
- source: pp. 10–11 screenshots; gate prose pp. 9–11
- section: G02 Harbor + TB4 contract
- explained_in: 00-source/PLATFORM-RULE-CATALOG.md
- compliance_check: Stage 1 blocking reason is not this id, or the outcome is a documented retry rather than a task rewrite when the prose classifies it as platform-side.
- evidence: stage1.txt
- contradiction_or_rejection_risk: U-SEVERITY-ALIGNMENT. Severity badges in the screenshots were not column-aligned, so this row does not assert REQUIRED versus OPTIONAL.
- requirement: Platform rule `HARBOR.DEPRECATED_ALLOW_INTERNET` is visible under G02 Harbor + TB4 contract. Confidence: screenshot. The author prevents the failing condition named by the rule and archives the live text if it fires.

## REQ-PL-G02-HARBOR-SCHEMA_VERSION_NONCANONICAL
- obligation: platform
- scope: platform
- stages: stage1
- source: pp. 10–11 screenshots; gate prose pp. 9–11
- section: G02 Harbor + TB4 contract
- explained_in: 00-source/PLATFORM-RULE-CATALOG.md
- compliance_check: Stage 1 blocking reason is not this id, or the outcome is a documented retry rather than a task rewrite when the prose classifies it as platform-side.
- evidence: stage1.txt
- contradiction_or_rejection_risk: U-SEVERITY-ALIGNMENT. Severity badges in the screenshots were not column-aligned, so this row does not assert REQUIRED versus OPTIONAL.
- requirement: Platform rule `HARBOR.SCHEMA_VERSION_NONCANONICAL` is visible under G02 Harbor + TB4 contract. Confidence: screenshot. The author prevents the failing condition named by the rule and archives the live text if it fires.

## REQ-PL-G02-HARBOR-TASK_CONFIG_INVALID
- obligation: platform
- scope: platform
- stages: stage1
- source: pp. 10–11 screenshots; gate prose pp. 9–11
- section: G02 Harbor + TB4 contract
- explained_in: 00-source/PLATFORM-RULE-CATALOG.md
- compliance_check: Stage 1 blocking reason is not this id, or the outcome is a documented retry rather than a task rewrite when the prose classifies it as platform-side.
- evidence: stage1.txt
- contradiction_or_rejection_risk: U-SEVERITY-ALIGNMENT. Severity badges in the screenshots were not column-aligned, so this row does not assert REQUIRED versus OPTIONAL.
- requirement: Platform rule `HARBOR.TASK_CONFIG_INVALID` is visible under G02 Harbor + TB4 contract. Confidence: screenshot. The author prevents the failing condition named by the rule and archives the live text if it fires.

## REQ-PL-G02-PACKAGE-EXTRA_CONTENT_ADVISORY
- obligation: advisory
- scope: platform
- stages: stage1
- source: pp. 10–11 screenshots; gate prose pp. 9–11
- section: G02 Harbor + TB4 contract
- explained_in: 00-source/PLATFORM-RULE-CATALOG.md
- compliance_check: Stage 1 blocking reason is not this id, or the outcome is a documented retry rather than a task rewrite when the prose classifies it as platform-side.
- evidence: stage1.txt
- contradiction_or_rejection_risk: Name contains ADVISORY, which p.9 says does not reject. U-SEVERITY-ALIGNMENT. Severity badges in the screenshots were not column-aligned, so this row does not assert REQUIRED versus OPTIONAL.
- requirement: Platform rule `PACKAGE.EXTRA_CONTENT_ADVISORY` is visible under G02 Harbor + TB4 contract. Confidence: screenshot. The author prevents the failing condition named by the rule and archives the live text if it fires.

## REQ-PL-G02-PACKAGE-REQUIRED_FILE_MISSING
- obligation: platform
- scope: platform
- stages: stage1
- source: pp. 10–11 screenshots; gate prose pp. 9–11
- section: G02 Harbor + TB4 contract
- explained_in: 00-source/PLATFORM-RULE-CATALOG.md
- compliance_check: Stage 1 blocking reason is not this id, or the outcome is a documented retry rather than a task rewrite when the prose classifies it as platform-side.
- evidence: stage1.txt
- contradiction_or_rejection_risk: U-SEVERITY-ALIGNMENT. Severity badges in the screenshots were not column-aligned, so this row does not assert REQUIRED versus OPTIONAL.
- requirement: Platform rule `PACKAGE.REQUIRED_FILE_MISSING` is visible under G02 Harbor + TB4 contract. Confidence: screenshot. The author prevents the failing condition named by the rule and archives the live text if it fires.

## REQ-PL-G02-PACKAGE-REQUIRED_FILE_UNREADABLE
- obligation: platform
- scope: platform
- stages: stage1
- source: pp. 10–11 screenshots; gate prose pp. 9–11
- section: G02 Harbor + TB4 contract
- explained_in: 00-source/PLATFORM-RULE-CATALOG.md
- compliance_check: Stage 1 blocking reason is not this id, or the outcome is a documented retry rather than a task rewrite when the prose classifies it as platform-side.
- evidence: stage1.txt
- contradiction_or_rejection_risk: U-SEVERITY-ALIGNMENT. Severity badges in the screenshots were not column-aligned, so this row does not assert REQUIRED versus OPTIONAL.
- requirement: Platform rule `PACKAGE.REQUIRED_FILE_UNREADABLE` is visible under G02 Harbor + TB4 contract. Confidence: screenshot. The author prevents the failing condition named by the rule and archives the live text if it fires.

## REQ-PL-G02-PROFILE-TIMEOUT_ADVISORY
- obligation: advisory
- scope: platform
- stages: stage1
- source: pp. 10–11 screenshots; gate prose pp. 9–11
- section: G02 Harbor + TB4 contract
- explained_in: 00-source/PLATFORM-RULE-CATALOG.md
- compliance_check: Stage 1 blocking reason is not this id, or the outcome is a documented retry rather than a task rewrite when the prose classifies it as platform-side.
- evidence: stage1.txt
- contradiction_or_rejection_risk: Name contains ADVISORY, which p.9 says does not reject. U-SEVERITY-ALIGNMENT. Severity badges in the screenshots were not column-aligned, so this row does not assert REQUIRED versus OPTIONAL.
- requirement: Platform rule `PROFILE.TIMEOUT_ADVISORY` is visible under G02 Harbor + TB4 contract. Confidence: screenshot. The author prevents the failing condition named by the rule and archives the live text if it fires.

## REQ-PL-G02-TB3-AGENT_NETWORK_NONPUBLIC
- obligation: platform
- scope: platform
- stages: stage1
- source: pp. 10–11 screenshots; gate prose pp. 9–11
- section: G02 Harbor + TB4 contract
- explained_in: 00-source/PLATFORM-RULE-CATALOG.md
- compliance_check: Stage 1 blocking reason is not this id, or the outcome is a documented retry rather than a task rewrite when the prose classifies it as platform-side.
- evidence: stage1.txt
- contradiction_or_rejection_risk: U-SEVERITY-ALIGNMENT. Severity badges in the screenshots were not column-aligned, so this row does not assert REQUIRED versus OPTIONAL.
- requirement: Platform rule `TB3.AGENT_NETWORK_NONPUBLIC` is visible under G02 Harbor + TB4 contract. Confidence: screenshot. The author prevents the failing condition named by the rule and archives the live text if it fires.

## REQ-PL-G02-TB3-CANARY_FORMAT
- obligation: platform
- scope: platform
- stages: stage1
- source: pp. 10–11 screenshots; gate prose pp. 9–11
- section: G02 Harbor + TB4 contract
- explained_in: 00-source/PLATFORM-RULE-CATALOG.md
- compliance_check: Stage 1 blocking reason is not this id, or the outcome is a documented retry rather than a task rewrite when the prose classifies it as platform-side.
- evidence: stage1.txt
- contradiction_or_rejection_risk: C-CANARY. U-SEVERITY-ALIGNMENT. Severity badges in the screenshots were not column-aligned, so this row does not assert REQUIRED versus OPTIONAL.
- requirement: Platform rule `TB3.CANARY_FORMAT` is visible under G02 Harbor + TB4 contract. Confidence: screenshot. The author prevents the failing condition named by the rule and archives the live text if it fires.

## REQ-PL-G02-TB3-SUBCATEGORY_INVALID
- obligation: platform
- scope: platform
- stages: stage1
- source: pp. 10–11 screenshots; gate prose pp. 9–11
- section: G02 Harbor + TB4 contract
- explained_in: 00-source/PLATFORM-RULE-CATALOG.md
- compliance_check: Stage 1 blocking reason is not this id, or the outcome is a documented retry rather than a task rewrite when the prose classifies it as platform-side.
- evidence: stage1.txt
- contradiction_or_rejection_risk: U-SEVERITY-ALIGNMENT. Severity badges in the screenshots were not column-aligned, so this row does not assert REQUIRED versus OPTIONAL.
- requirement: Platform rule `TB3.SUBCATEGORY_INVALID` is visible under G02 Harbor + TB4 contract. Confidence: screenshot. The author prevents the failing condition named by the rule and archives the live text if it fires.

## REQ-PL-G02-TB3-VERIFIER_ISOLATION_REQUIRED
- obligation: platform
- scope: platform
- stages: stage1
- source: pp. 10–11 screenshots; gate prose pp. 9–11
- section: G02 Harbor + TB4 contract
- explained_in: 00-source/PLATFORM-RULE-CATALOG.md
- compliance_check: Stage 1 blocking reason is not this id, or the outcome is a documented retry rather than a task rewrite when the prose classifies it as platform-side.
- evidence: stage1.txt
- contradiction_or_rejection_risk: U-SEVERITY-ALIGNMENT. Severity badges in the screenshots were not column-aligned, so this row does not assert REQUIRED versus OPTIONAL.
- requirement: Platform rule `TB3.VERIFIER_ISOLATION_REQUIRED` is visible under G02 Harbor + TB4 contract. Confidence: screenshot. The author prevents the failing condition named by the rule and archives the live text if it fires.

## REQ-PL-G03-CREDENTIAL_SCAN
- obligation: platform
- scope: platform
- stages: stage1
- source: pp. 10–11 screenshots; gate prose pp. 9–11
- section: G03 Static execution safety
- explained_in: 00-source/PLATFORM-RULE-CATALOG.md
- compliance_check: Stage 1 blocking reason is not this id, or the outcome is a documented retry rather than a task rewrite when the prose classifies it as platform-side.
- evidence: stage1.txt
- contradiction_or_rejection_risk: U-SEVERITY-ALIGNMENT. Severity badges in the screenshots were not column-aligned, so this row does not assert REQUIRED versus OPTIONAL.
- requirement: Platform phase `CREDENTIAL_SCAN` is visible under G03 Static execution safety. Confidence: screenshot. The author prevents the failing condition named by the rule and archives the live text if it fires.

## REQ-PL-G03-COMPOSE_DEPENDENCY_SCAN
- obligation: platform
- scope: platform
- stages: stage1
- source: pp. 10–11 screenshots; gate prose pp. 9–11
- section: G03 Static execution safety
- explained_in: 00-source/PLATFORM-RULE-CATALOG.md
- compliance_check: Stage 1 blocking reason is not this id, or the outcome is a documented retry rather than a task rewrite when the prose classifies it as platform-side.
- evidence: stage1.txt
- contradiction_or_rejection_risk: U-SEVERITY-ALIGNMENT. Severity badges in the screenshots were not column-aligned, so this row does not assert REQUIRED versus OPTIONAL.
- requirement: Platform phase `COMPOSE_DEPENDENCY_SCAN` is visible under G03 Static execution safety. Confidence: screenshot. The author prevents the failing condition named by the rule and archives the live text if it fires.

## REQ-PL-G03-COMPOSE_RESOLVE
- obligation: platform
- scope: platform
- stages: stage1
- source: pp. 10–11 screenshots; gate prose pp. 9–11
- section: G03 Static execution safety
- explained_in: 00-source/PLATFORM-RULE-CATALOG.md
- compliance_check: Stage 1 blocking reason is not this id, or the outcome is a documented retry rather than a task rewrite when the prose classifies it as platform-side.
- evidence: stage1.txt
- contradiction_or_rejection_risk: U-SEVERITY-ALIGNMENT. Severity badges in the screenshots were not column-aligned, so this row does not assert REQUIRED versus OPTIONAL.
- requirement: Platform phase `COMPOSE_RESOLVE` is visible under G03 Static execution safety. Confidence: screenshot. The author prevents the failing condition named by the rule and archives the live text if it fires.

## REQ-PL-G03-STATIC_POLICY
- obligation: platform
- scope: platform
- stages: stage1
- source: pp. 10–11 screenshots; gate prose pp. 9–11
- section: G03 Static execution safety
- explained_in: 00-source/PLATFORM-RULE-CATALOG.md
- compliance_check: Stage 1 blocking reason is not this id, or the outcome is a documented retry rather than a task rewrite when the prose classifies it as platform-side.
- evidence: stage1.txt
- contradiction_or_rejection_risk: U-SEVERITY-ALIGNMENT. Severity badges in the screenshots were not column-aligned, so this row does not assert REQUIRED versus OPTIONAL.
- requirement: Platform phase `STATIC_POLICY` is visible under G03 Static execution safety. Confidence: screenshot. The author prevents the failing condition named by the rule and archives the live text if it fires.

## REQ-PL-G03-COMPOSE-HOST_BIND
- obligation: conditional
- scope: platform
- stages: stage1
- source: pp. 10–11 screenshots; gate prose pp. 9–11
- section: G03 Static execution safety
- explained_in: 00-source/PLATFORM-RULE-CATALOG.md
- compliance_check: Stage 1 blocking reason is not this id, or the outcome is a documented retry rather than a task rewrite when the prose classifies it as platform-side.
- evidence: stage1.txt
- contradiction_or_rejection_risk: U-SEVERITY-ALIGNMENT. Severity badges in the screenshots were not column-aligned, so this row does not assert REQUIRED versus OPTIONAL.
- requirement: Platform rule `COMPOSE.HOST_BIND` is visible under G03 Static execution safety. Confidence: screenshot. The author prevents the failing condition named by the rule and archives the live text if it fires.

## REQ-PL-G03-COMPOSE-TYPE_BIND
- obligation: conditional
- scope: platform
- stages: stage1
- source: pp. 10–11 screenshots; gate prose pp. 9–11
- section: G03 Static execution safety
- explained_in: 00-source/PLATFORM-RULE-CATALOG.md
- compliance_check: Stage 1 blocking reason is not this id, or the outcome is a documented retry rather than a task rewrite when the prose classifies it as platform-side.
- evidence: stage1.txt
- contradiction_or_rejection_risk: U-SEVERITY-ALIGNMENT. Severity badges in the screenshots were not column-aligned, so this row does not assert REQUIRED versus OPTIONAL.
- requirement: Platform rule `COMPOSE.TYPE_BIND` is visible under G03 Static execution safety. Confidence: screenshot-single. The author prevents the failing condition named by the rule and archives the live text if it fires.

## REQ-PL-G03-COMPOSE-RESOURCE_ENVELOPE_BYPASS
- obligation: conditional
- scope: platform
- stages: stage1
- source: pp. 10–11 screenshots; gate prose pp. 9–11
- section: G03 Static execution safety
- explained_in: 00-source/PLATFORM-RULE-CATALOG.md
- compliance_check: Stage 1 blocking reason is not this id, or the outcome is a documented retry rather than a task rewrite when the prose classifies it as platform-side.
- evidence: stage1.txt
- contradiction_or_rejection_risk: U-SEVERITY-ALIGNMENT. Severity badges in the screenshots were not column-aligned, so this row does not assert REQUIRED versus OPTIONAL.
- requirement: Platform rule `COMPOSE.RESOURCE_ENVELOPE_BYPASS` is visible under G03 Static execution safety. Confidence: screenshot. The author prevents the failing condition named by the rule and archives the live text if it fires.

## REQ-PL-G03-COMPOSE-MAIN_BUILD_MISSING
- obligation: conditional
- scope: platform
- stages: stage1
- source: pp. 10–11 screenshots; gate prose pp. 9–11
- section: G03 Static execution safety
- explained_in: 00-source/PLATFORM-RULE-CATALOG.md
- compliance_check: Stage 1 blocking reason is not this id, or the outcome is a documented retry rather than a task rewrite when the prose classifies it as platform-side.
- evidence: stage1.txt
- contradiction_or_rejection_risk: U-SEVERITY-ALIGNMENT. Severity badges in the screenshots were not column-aligned, so this row does not assert REQUIRED versus OPTIONAL.
- requirement: Platform rule `COMPOSE.MAIN_BUILD_MISSING` is visible under G03 Static execution safety. Confidence: screenshot. The author prevents the failing condition named by the rule and archives the live text if it fires.

## REQ-PL-G03-COMPOSE-PRIVILEGED
- obligation: conditional
- scope: platform
- stages: stage1
- source: pp. 10–11 screenshots; gate prose pp. 9–11
- section: G03 Static execution safety
- explained_in: 00-source/PLATFORM-RULE-CATALOG.md
- compliance_check: Stage 1 blocking reason is not this id, or the outcome is a documented retry rather than a task rewrite when the prose classifies it as platform-side.
- evidence: stage1.txt
- contradiction_or_rejection_risk: U-SEVERITY-ALIGNMENT. Severity badges in the screenshots were not column-aligned, so this row does not assert REQUIRED versus OPTIONAL.
- requirement: Platform rule `COMPOSE.PRIVILEGED` is visible under G03 Static execution safety. Confidence: screenshot. The author prevents the failing condition named by the rule and archives the live text if it fires.

## REQ-PL-G03-COMPOSE-NETWORK_HOST
- obligation: conditional
- scope: platform
- stages: stage1
- source: pp. 10–11 screenshots; gate prose pp. 9–11
- section: G03 Static execution safety
- explained_in: 00-source/PLATFORM-RULE-CATALOG.md
- compliance_check: Stage 1 blocking reason is not this id, or the outcome is a documented retry rather than a task rewrite when the prose classifies it as platform-side.
- evidence: stage1.txt
- contradiction_or_rejection_risk: U-SEVERITY-ALIGNMENT. Severity badges in the screenshots were not column-aligned, so this row does not assert REQUIRED versus OPTIONAL.
- requirement: Platform rule `COMPOSE.NETWORK_HOST` is visible under G03 Static execution safety. Confidence: screenshot. The author prevents the failing condition named by the rule and archives the live text if it fires.

## REQ-PL-G03-COMPOSE-DEVICE
- obligation: conditional
- scope: platform
- stages: stage1
- source: pp. 10–11 screenshots; gate prose pp. 9–11
- section: G03 Static execution safety
- explained_in: 00-source/PLATFORM-RULE-CATALOG.md
- compliance_check: Stage 1 blocking reason is not this id, or the outcome is a documented retry rather than a task rewrite when the prose classifies it as platform-side.
- evidence: stage1.txt
- contradiction_or_rejection_risk: U-SEVERITY-ALIGNMENT. Severity badges in the screenshots were not column-aligned, so this row does not assert REQUIRED versus OPTIONAL.
- requirement: Platform rule `COMPOSE.DEVICE` is visible under G03 Static execution safety. Confidence: screenshot. The author prevents the failing condition named by the rule and archives the live text if it fires.

## REQ-PL-G03-COMPOSE-PACKAGED_FILE_MUTATION
- obligation: conditional
- scope: platform
- stages: stage1
- source: pp. 10–11 screenshots; gate prose pp. 9–11
- section: G03 Static execution safety
- explained_in: 00-source/PLATFORM-RULE-CATALOG.md
- compliance_check: Stage 1 blocking reason is not this id, or the outcome is a documented retry rather than a task rewrite when the prose classifies it as platform-side.
- evidence: stage1.txt
- contradiction_or_rejection_risk: U-SEVERITY-ALIGNMENT. Severity badges in the screenshots were not column-aligned, so this row does not assert REQUIRED versus OPTIONAL.
- requirement: Platform rule `COMPOSE.PACKAGED_FILE_MUTATION` is visible under G03 Static execution safety. Confidence: screenshot. The author prevents the failing condition named by the rule and archives the live text if it fires.

## REQ-PL-G03-COMPOSE-RESOLVE_FAILED
- obligation: conditional
- scope: platform
- stages: stage1
- source: pp. 10–11 screenshots; gate prose pp. 9–11
- section: G03 Static execution safety
- explained_in: 00-source/PLATFORM-RULE-CATALOG.md
- compliance_check: Stage 1 blocking reason is not this id, or the outcome is a documented retry rather than a task rewrite when the prose classifies it as platform-side.
- evidence: stage1.txt
- contradiction_or_rejection_risk: U-SEVERITY-ALIGNMENT. Severity badges in the screenshots were not column-aligned, so this row does not assert REQUIRED versus OPTIONAL.
- requirement: Platform rule `COMPOSE.RESOLVE_FAILED` is visible under G03 Static execution safety. Confidence: screenshot. The author prevents the failing condition named by the rule and archives the live text if it fires.

## REQ-PL-G03-COMPOSE-INVALID
- obligation: conditional
- scope: platform
- stages: stage1
- source: pp. 10–11 screenshots; gate prose pp. 9–11
- section: G03 Static execution safety
- explained_in: 00-source/PLATFORM-RULE-CATALOG.md
- compliance_check: Stage 1 blocking reason is not this id, or the outcome is a documented retry rather than a task rewrite when the prose classifies it as platform-side.
- evidence: stage1.txt
- contradiction_or_rejection_risk: U-SEVERITY-ALIGNMENT. Severity badges in the screenshots were not column-aligned, so this row does not assert REQUIRED versus OPTIONAL.
- requirement: Platform rule `COMPOSE.INVALID` is visible under G03 Static execution safety. Confidence: screenshot. The author prevents the failing condition named by the rule and archives the live text if it fires.

## REQ-PL-G03-COMPOSE-DEPENDENCY_ESCAPE
- obligation: conditional
- scope: platform
- stages: stage1
- source: pp. 10–11 screenshots; gate prose pp. 9–11
- section: G03 Static execution safety
- explained_in: 00-source/PLATFORM-RULE-CATALOG.md
- compliance_check: Stage 1 blocking reason is not this id, or the outcome is a documented retry rather than a task rewrite when the prose classifies it as platform-side.
- evidence: stage1.txt
- contradiction_or_rejection_risk: U-SEVERITY-ALIGNMENT. Severity badges in the screenshots were not column-aligned, so this row does not assert REQUIRED versus OPTIONAL.
- requirement: Platform rule `COMPOSE.DEPENDENCY_ESCAPE` is visible under G03 Static execution safety. Confidence: screenshot. The author prevents the failing condition named by the rule and archives the live text if it fires.

## REQ-PL-G03-CREDENTIAL-CONFIRMED
- obligation: platform
- scope: platform
- stages: stage1
- source: pp. 10–11 screenshots; gate prose pp. 9–11
- section: G03 Static execution safety
- explained_in: 00-source/PLATFORM-RULE-CATALOG.md
- compliance_check: Stage 1 blocking reason is not this id, or the outcome is a documented retry rather than a task rewrite when the prose classifies it as platform-side.
- evidence: stage1.txt
- contradiction_or_rejection_risk: U-SEVERITY-ALIGNMENT. Severity badges in the screenshots were not column-aligned, so this row does not assert REQUIRED versus OPTIONAL.
- requirement: Platform rule `CREDENTIAL.CONFIRMED` is visible under G03 Static execution safety. Confidence: screenshot. The author prevents the failing condition named by the rule and archives the live text if it fires.

## REQ-PL-G03-CREDENTIAL-SUSPECTED
- obligation: platform
- scope: platform
- stages: stage1
- source: pp. 10–11 screenshots; gate prose pp. 9–11
- section: G03 Static execution safety
- explained_in: 00-source/PLATFORM-RULE-CATALOG.md
- compliance_check: Stage 1 blocking reason is not this id, or the outcome is a documented retry rather than a task rewrite when the prose classifies it as platform-side.
- evidence: stage1.txt
- contradiction_or_rejection_risk: U-SEVERITY-ALIGNMENT. Severity badges in the screenshots were not column-aligned, so this row does not assert REQUIRED versus OPTIONAL.
- requirement: Platform rule `CREDENTIAL.SUSPECTED` is visible under G03 Static execution safety. Confidence: screenshot. The author prevents the failing condition named by the rule and archives the live text if it fires.

## REQ-PL-G03-DOCKERFILE-REFERENCE
- obligation: platform
- scope: platform
- stages: stage1
- source: pp. 10–11 screenshots; gate prose pp. 9–11
- section: G03 Static execution safety
- explained_in: 00-source/PLATFORM-RULE-CATALOG.md
- compliance_check: Stage 1 blocking reason is not this id, or the outcome is a documented retry rather than a task rewrite when the prose classifies it as platform-side.
- evidence: stage1.txt
- contradiction_or_rejection_risk: U-SEVERITY-ALIGNMENT. Severity badges in the screenshots were not column-aligned, so this row does not assert REQUIRED versus OPTIONAL.
- requirement: Platform rule `DOCKERFILE.REFERENCE` is visible under G03 Static execution safety. Confidence: screenshot. The author prevents the failing condition named by the rule and archives the live text if it fires.

## REQ-PL-G03-TRIAL-PUBLIC_FETCH
- obligation: platform
- scope: platform
- stages: stage1
- source: pp. 10–11 screenshots; gate prose pp. 9–11
- section: G03 Static execution safety
- explained_in: 00-source/PLATFORM-RULE-CATALOG.md
- compliance_check: Stage 1 blocking reason is not this id, or the outcome is a documented retry rather than a task rewrite when the prose classifies it as platform-side.
- evidence: stage1.txt
- contradiction_or_rejection_risk: U-SEVERITY-ALIGNMENT. Severity badges in the screenshots were not column-aligned, so this row does not assert REQUIRED versus OPTIONAL.
- requirement: Platform rule `TRIAL.PUBLIC_FETCH` is visible under G03 Static execution safety. Confidence: screenshot. The author prevents the failing condition named by the rule and archives the live text if it fires.

## REQ-PL-G03-POLICY-COVERAGE
- obligation: platform
- scope: platform
- stages: stage1
- source: pp. 10–11 screenshots; gate prose pp. 9–11
- section: G03 Static execution safety
- explained_in: 00-source/PLATFORM-RULE-CATALOG.md
- compliance_check: Stage 1 blocking reason is not this id, or the outcome is a documented retry rather than a task rewrite when the prose classifies it as platform-side.
- evidence: stage1.txt
- contradiction_or_rejection_risk: U-SEVERITY-ALIGNMENT. Severity badges in the screenshots were not column-aligned, so this row does not assert REQUIRED versus OPTIONAL.
- requirement: Platform rule `POLICY.COVERAGE` is visible under G03 Static execution safety. Confidence: screenshot. The author prevents the failing condition named by the rule and archives the live text if it fires.

## REQ-PL-G03-STATIC-ADVISORY
- obligation: advisory
- scope: platform
- stages: stage1
- source: pp. 10–11 screenshots; gate prose pp. 9–11
- section: G03 Static execution safety
- explained_in: 00-source/PLATFORM-RULE-CATALOG.md
- compliance_check: Stage 1 blocking reason is not this id, or the outcome is a documented retry rather than a task rewrite when the prose classifies it as platform-side.
- evidence: stage1.txt
- contradiction_or_rejection_risk: Name contains ADVISORY, which p.9 says does not reject. U-SEVERITY-ALIGNMENT. Severity badges in the screenshots were not column-aligned, so this row does not assert REQUIRED versus OPTIONAL.
- requirement: Platform rule `STATIC.ADVISORY` is visible under G03 Static execution safety. Confidence: screenshot. The author prevents the failing condition named by the rule and archives the live text if it fires.

## REQ-PL-G04-AGENT_ENV_BUILD
- obligation: platform
- scope: platform
- stages: stage1
- source: pp. 10–11 screenshots; gate prose pp. 9–11
- section: G04 Environment readiness
- explained_in: 00-source/PLATFORM-RULE-CATALOG.md
- compliance_check: Stage 1 blocking reason is not this id, or the outcome is a documented retry rather than a task rewrite when the prose classifies it as platform-side.
- evidence: stage1.txt
- contradiction_or_rejection_risk: U-SEVERITY-ALIGNMENT. Severity badges in the screenshots were not column-aligned, so this row does not assert REQUIRED versus OPTIONAL.
- requirement: Platform phase `AGENT_ENV_BUILD` is visible under G04 Environment readiness. Confidence: screenshot. The author prevents the failing condition named by the rule and archives the live text if it fires.

## REQ-PL-G04-AGENT_ENV_START
- obligation: platform
- scope: platform
- stages: stage1
- source: pp. 10–11 screenshots; gate prose pp. 9–11
- section: G04 Environment readiness
- explained_in: 00-source/PLATFORM-RULE-CATALOG.md
- compliance_check: Stage 1 blocking reason is not this id, or the outcome is a documented retry rather than a task rewrite when the prose classifies it as platform-side.
- evidence: stage1.txt
- contradiction_or_rejection_risk: U-SEVERITY-ALIGNMENT. Severity badges in the screenshots were not column-aligned, so this row does not assert REQUIRED versus OPTIONAL.
- requirement: Platform phase `AGENT_ENV_START` is visible under G04 Environment readiness. Confidence: screenshot. The author prevents the failing condition named by the rule and archives the live text if it fires.

## REQ-PL-G04-AGENT_ENV_READINESS
- obligation: platform
- scope: platform
- stages: stage1
- source: pp. 10–11 screenshots; gate prose pp. 9–11
- section: G04 Environment readiness
- explained_in: 00-source/PLATFORM-RULE-CATALOG.md
- compliance_check: Stage 1 blocking reason is not this id, or the outcome is a documented retry rather than a task rewrite when the prose classifies it as platform-side.
- evidence: stage1.txt
- contradiction_or_rejection_risk: U-SEVERITY-ALIGNMENT. Severity badges in the screenshots were not column-aligned, so this row does not assert REQUIRED versus OPTIONAL.
- requirement: Platform phase `AGENT_ENV_READINESS` is visible under G04 Environment readiness. Confidence: screenshot. The author prevents the failing condition named by the rule and archives the live text if it fires.

## REQ-PL-G04-HARBOR-START_BLOCKED
- obligation: platform
- scope: platform
- stages: stage1
- source: pp. 10–11 screenshots; gate prose pp. 9–11
- section: G04 Environment readiness
- explained_in: 00-source/PLATFORM-RULE-CATALOG.md
- compliance_check: Stage 1 blocking reason is not this id, or the outcome is a documented retry rather than a task rewrite when the prose classifies it as platform-side.
- evidence: stage1.txt
- contradiction_or_rejection_risk: U-SEVERITY-ALIGNMENT. Severity badges in the screenshots were not column-aligned, so this row does not assert REQUIRED versus OPTIONAL.
- requirement: Platform rule `HARBOR.START_BLOCKED` is visible under G04 Environment readiness. Confidence: screenshot. The author prevents the failing condition named by the rule and archives the live text if it fires.

## REQ-PL-G04-HARBOR-RUNTIME_ERROR
- obligation: platform
- scope: platform
- stages: stage1
- source: pp. 10–11 screenshots; gate prose pp. 9–11
- section: G04 Environment readiness
- explained_in: 00-source/PLATFORM-RULE-CATALOG.md
- compliance_check: Stage 1 blocking reason is not this id, or the outcome is a documented retry rather than a task rewrite when the prose classifies it as platform-side.
- evidence: stage1.txt
- contradiction_or_rejection_risk: U-SEVERITY-ALIGNMENT. Severity badges in the screenshots were not column-aligned, so this row does not assert REQUIRED versus OPTIONAL.
- requirement: Platform rule `HARBOR.RUNTIME_ERROR` is visible under G04 Environment readiness. Confidence: screenshot. The author prevents the failing condition named by the rule and archives the live text if it fires.

## REQ-PL-G04-HARBOR-ENV_START_TIMEOUT
- obligation: platform
- scope: platform
- stages: stage1
- source: pp. 10–11 screenshots; gate prose pp. 9–11
- section: G04 Environment readiness
- explained_in: 00-source/PLATFORM-RULE-CATALOG.md
- compliance_check: Stage 1 blocking reason is not this id, or the outcome is a documented retry rather than a task rewrite when the prose classifies it as platform-side.
- evidence: stage1.txt
- contradiction_or_rejection_risk: U-SEVERITY-ALIGNMENT. Severity badges in the screenshots were not column-aligned, so this row does not assert REQUIRED versus OPTIONAL.
- requirement: Platform rule `HARBOR.ENV_START_TIMEOUT` is visible under G04 Environment readiness. Confidence: screenshot. The author prevents the failing condition named by the rule and archives the live text if it fires.

## REQ-PL-G04-HARBOR-NO_AGENT_SETUP
- obligation: platform
- scope: platform
- stages: stage1
- source: pp. 10–11 screenshots; gate prose pp. 9–11
- section: G04 Environment readiness
- explained_in: 00-source/PLATFORM-RULE-CATALOG.md
- compliance_check: Stage 1 blocking reason is not this id, or the outcome is a documented retry rather than a task rewrite when the prose classifies it as platform-side.
- evidence: stage1.txt
- contradiction_or_rejection_risk: U-SEVERITY-ALIGNMENT. Severity badges in the screenshots were not column-aligned, so this row does not assert REQUIRED versus OPTIONAL.
- requirement: Platform rule `HARBOR.NO_AGENT_SETUP` is visible under G04 Environment readiness. Confidence: screenshot. The author prevents the failing condition named by the rule and archives the live text if it fires.

## REQ-PL-G04-HARBOR-RESULT_MISSING
- obligation: platform
- scope: platform
- stages: stage1
- source: pp. 10–11 screenshots; gate prose pp. 9–11
- section: G04 Environment readiness
- explained_in: 00-source/PLATFORM-RULE-CATALOG.md
- compliance_check: Stage 1 blocking reason is not this id, or the outcome is a documented retry rather than a task rewrite when the prose classifies it as platform-side.
- evidence: stage1.txt
- contradiction_or_rejection_risk: U-SEVERITY-ALIGNMENT. Severity badges in the screenshots were not column-aligned, so this row does not assert REQUIRED versus OPTIONAL.
- requirement: Platform rule `HARBOR.RESULT_MISSING` is visible under G04 Environment readiness. Confidence: screenshot. The author prevents the failing condition named by the rule and archives the live text if it fires.

## REQ-PL-G04-PROFILE-ACCELERATOR_UNSUPPORTED
- obligation: platform
- scope: platform
- stages: stage1
- source: pp. 10–11 screenshots; gate prose pp. 9–11
- section: G04 Environment readiness
- explained_in: 00-source/PLATFORM-RULE-CATALOG.md
- compliance_check: Stage 1 blocking reason is not this id, or the outcome is a documented retry rather than a task rewrite when the prose classifies it as platform-side.
- evidence: stage1.txt
- contradiction_or_rejection_risk: U-SEVERITY-ALIGNMENT. Severity badges in the screenshots were not column-aligned, so this row does not assert REQUIRED versus OPTIONAL.
- requirement: Platform rule `PROFILE.ACCELERATOR_UNSUPPORTED` is visible under G04 Environment readiness. Confidence: prose and screenshot. The author prevents the failing condition named by the rule and archives the live text if it fires.

## REQ-PL-G04-PROFILE-MULTI_STEP_UNSUPPORTED
- obligation: platform
- scope: platform
- stages: stage1
- source: pp. 10–11 screenshots; gate prose pp. 9–11
- section: G04 Environment readiness
- explained_in: 00-source/PLATFORM-RULE-CATALOG.md
- compliance_check: Stage 1 blocking reason is not this id, or the outcome is a documented retry rather than a task rewrite when the prose classifies it as platform-side.
- evidence: stage1.txt
- contradiction_or_rejection_risk: U-SEVERITY-ALIGNMENT. Severity badges in the screenshots were not column-aligned, so this row does not assert REQUIRED versus OPTIONAL.
- requirement: Platform rule `PROFILE.MULTI_STEP_UNSUPPORTED` is visible under G04 Environment readiness. Confidence: screenshot. The author prevents the failing condition named by the rule and archives the live text if it fires.

## REQ-PL-G04-PROFILE-PREBUILT_IMAGE_UNSUPPORTED
- obligation: platform
- scope: platform
- stages: stage1
- source: pp. 10–11 screenshots; gate prose pp. 9–11
- section: G04 Environment readiness
- explained_in: 00-source/PLATFORM-RULE-CATALOG.md
- compliance_check: Stage 1 blocking reason is not this id, or the outcome is a documented retry rather than a task rewrite when the prose classifies it as platform-side.
- evidence: stage1.txt
- contradiction_or_rejection_risk: U-SEVERITY-ALIGNMENT. Severity badges in the screenshots were not column-aligned, so this row does not assert REQUIRED versus OPTIONAL.
- requirement: Platform rule `PROFILE.PREBUILT_IMAGE_UNSUPPORTED` is visible under G04 Environment readiness. Confidence: screenshot. The author prevents the failing condition named by the rule and archives the live text if it fires.

## REQ-PL-G04-PROFILE-TIMEOUT_ENVELOPE_UNSUPPORTED
- obligation: platform
- scope: platform
- stages: stage1
- source: pp. 10–11 screenshots; gate prose pp. 9–11
- section: G04 Environment readiness
- explained_in: 00-source/PLATFORM-RULE-CATALOG.md
- compliance_check: Stage 1 blocking reason is not this id, or the outcome is a documented retry rather than a task rewrite when the prose classifies it as platform-side.
- evidence: stage1.txt
- contradiction_or_rejection_risk: U-SEVERITY-ALIGNMENT. Severity badges in the screenshots were not column-aligned, so this row does not assert REQUIRED versus OPTIONAL.
- requirement: Platform rule `PROFILE.TIMEOUT_ENVELOPE_UNSUPPORTED` is visible under G04 Environment readiness. Confidence: screenshot. The author prevents the failing condition named by the rule and archives the live text if it fires.

## REQ-PL-G05-ORACLE_AGENT_EXECUTION
- obligation: platform
- scope: platform
- stages: stage1
- source: pp. 10–11 screenshots; gate prose pp. 9–11
- section: G05 Verifier controls
- explained_in: 00-source/PLATFORM-RULE-CATALOG.md
- compliance_check: Stage 1 blocking reason is not this id, or the outcome is a documented retry rather than a task rewrite when the prose classifies it as platform-side.
- evidence: stage1.txt
- contradiction_or_rejection_risk: U-SEVERITY-ALIGNMENT. Severity badges in the screenshots were not column-aligned, so this row does not assert REQUIRED versus OPTIONAL.
- requirement: Platform phase `ORACLE_AGENT_EXECUTION` is visible under G05 Verifier controls. Confidence: screenshot. The author prevents the failing condition named by the rule and archives the live text if it fires.

## REQ-PL-G05-ORACLE_VERIFIER_START
- obligation: platform
- scope: platform
- stages: stage1
- source: pp. 10–11 screenshots; gate prose pp. 9–11
- section: G05 Verifier controls
- explained_in: 00-source/PLATFORM-RULE-CATALOG.md
- compliance_check: Stage 1 blocking reason is not this id, or the outcome is a documented retry rather than a task rewrite when the prose classifies it as platform-side.
- evidence: stage1.txt
- contradiction_or_rejection_risk: U-SEVERITY-ALIGNMENT. Severity badges in the screenshots were not column-aligned, so this row does not assert REQUIRED versus OPTIONAL.
- requirement: Platform phase `ORACLE_VERIFIER_START` is visible under G05 Verifier controls. Confidence: screenshot. The author prevents the failing condition named by the rule and archives the live text if it fires.

## REQ-PL-G05-ORACLE_VERIFIER_EXECUTION
- obligation: platform
- scope: platform
- stages: stage1
- source: pp. 10–11 screenshots; gate prose pp. 9–11
- section: G05 Verifier controls
- explained_in: 00-source/PLATFORM-RULE-CATALOG.md
- compliance_check: Stage 1 blocking reason is not this id, or the outcome is a documented retry rather than a task rewrite when the prose classifies it as platform-side.
- evidence: stage1.txt
- contradiction_or_rejection_risk: U-SEVERITY-ALIGNMENT. Severity badges in the screenshots were not column-aligned, so this row does not assert REQUIRED versus OPTIONAL.
- requirement: Platform phase `ORACLE_VERIFIER_EXECUTION` is visible under G05 Verifier controls. Confidence: screenshot. The author prevents the failing condition named by the rule and archives the live text if it fires.

## REQ-PL-G05-NOP_AGENT_EXECUTION
- obligation: platform
- scope: platform
- stages: stage1
- source: pp. 10–11 screenshots; gate prose pp. 9–11
- section: G05 Verifier controls
- explained_in: 00-source/PLATFORM-RULE-CATALOG.md
- compliance_check: Stage 1 blocking reason is not this id, or the outcome is a documented retry rather than a task rewrite when the prose classifies it as platform-side.
- evidence: stage1.txt
- contradiction_or_rejection_risk: U-SEVERITY-ALIGNMENT. Severity badges in the screenshots were not column-aligned, so this row does not assert REQUIRED versus OPTIONAL.
- requirement: Platform phase `NOP_AGENT_EXECUTION` is visible under G05 Verifier controls. Confidence: screenshot. The author prevents the failing condition named by the rule and archives the live text if it fires.

## REQ-PL-G05-NOP_VERIFIER_START
- obligation: platform
- scope: platform
- stages: stage1
- source: pp. 10–11 screenshots; gate prose pp. 9–11
- section: G05 Verifier controls
- explained_in: 00-source/PLATFORM-RULE-CATALOG.md
- compliance_check: Stage 1 blocking reason is not this id, or the outcome is a documented retry rather than a task rewrite when the prose classifies it as platform-side.
- evidence: stage1.txt
- contradiction_or_rejection_risk: U-SEVERITY-ALIGNMENT. Severity badges in the screenshots were not column-aligned, so this row does not assert REQUIRED versus OPTIONAL.
- requirement: Platform phase `NOP_VERIFIER_START` is visible under G05 Verifier controls. Confidence: screenshot. The author prevents the failing condition named by the rule and archives the live text if it fires.

## REQ-PL-G05-NOP_VERIFIER_EXECUTION
- obligation: platform
- scope: platform
- stages: stage1
- source: pp. 10–11 screenshots; gate prose pp. 9–11
- section: G05 Verifier controls
- explained_in: 00-source/PLATFORM-RULE-CATALOG.md
- compliance_check: Stage 1 blocking reason is not this id, or the outcome is a documented retry rather than a task rewrite when the prose classifies it as platform-side.
- evidence: stage1.txt
- contradiction_or_rejection_risk: U-SEVERITY-ALIGNMENT. Severity badges in the screenshots were not column-aligned, so this row does not assert REQUIRED versus OPTIONAL.
- requirement: Platform phase `NOP_VERIFIER_EXECUTION` is visible under G05 Verifier controls. Confidence: screenshot. The author prevents the failing condition named by the rule and archives the live text if it fires.

## REQ-PL-G05-RUNTIME_EVIDENCE_BIND
- obligation: platform
- scope: platform
- stages: stage1
- source: pp. 10–11 screenshots; gate prose pp. 9–11
- section: G05 Verifier controls
- explained_in: 00-source/PLATFORM-RULE-CATALOG.md
- compliance_check: Stage 1 blocking reason is not this id, or the outcome is a documented retry rather than a task rewrite when the prose classifies it as platform-side.
- evidence: stage1.txt
- contradiction_or_rejection_risk: U-SEVERITY-ALIGNMENT. Severity badges in the screenshots were not column-aligned, so this row does not assert REQUIRED versus OPTIONAL.
- requirement: Platform phase `RUNTIME_EVIDENCE_BIND` is visible under G05 Verifier controls. Confidence: screenshot. The author prevents the failing condition named by the rule and archives the live text if it fires.

## REQ-PL-G05-ORACLE-NONZERO_EXIT
- obligation: platform
- scope: platform
- stages: stage1
- source: pp. 10–11 screenshots; gate prose pp. 9–11
- section: G05 Verifier controls
- explained_in: 00-source/PLATFORM-RULE-CATALOG.md
- compliance_check: Stage 1 blocking reason is not this id, or the outcome is a documented retry rather than a task rewrite when the prose classifies it as platform-side.
- evidence: stage1.txt
- contradiction_or_rejection_risk: U-SEVERITY-ALIGNMENT. Severity badges in the screenshots were not column-aligned, so this row does not assert REQUIRED versus OPTIONAL.
- requirement: Platform rule `ORACLE.NONZERO_EXIT` is visible under G05 Verifier controls. Confidence: screenshot. The author prevents the failing condition named by the rule and archives the live text if it fires.

## REQ-PL-G05-ORACLE-REWARD_BELOW_FULL
- obligation: platform
- scope: platform
- stages: stage1
- source: pp. 10–11 screenshots; gate prose pp. 9–11
- section: G05 Verifier controls
- explained_in: 00-source/PLATFORM-RULE-CATALOG.md
- compliance_check: Stage 1 blocking reason is not this id, or the outcome is a documented retry rather than a task rewrite when the prose classifies it as platform-side.
- evidence: stage1.txt
- contradiction_or_rejection_risk: U-SEVERITY-ALIGNMENT. Severity badges in the screenshots were not column-aligned, so this row does not assert REQUIRED versus OPTIONAL.
- requirement: Platform rule `ORACLE.REWARD_BELOW_FULL` is visible under G05 Verifier controls. Confidence: prose and screenshot. The author prevents the failing condition named by the rule and archives the live text if it fires.

## REQ-PL-G05-NOP-FULL_REWARD
- obligation: platform
- scope: platform
- stages: stage1
- source: pp. 10–11 screenshots; gate prose pp. 9–11
- section: G05 Verifier controls
- explained_in: 00-source/PLATFORM-RULE-CATALOG.md
- compliance_check: Stage 1 blocking reason is not this id, or the outcome is a documented retry rather than a task rewrite when the prose classifies it as platform-side.
- evidence: stage1.txt
- contradiction_or_rejection_risk: U-SEVERITY-ALIGNMENT. Severity badges in the screenshots were not column-aligned, so this row does not assert REQUIRED versus OPTIONAL.
- requirement: Platform rule `NOP.FULL_REWARD` is visible under G05 Verifier controls. Confidence: screenshot. The author prevents the failing condition named by the rule and archives the live text if it fires.

## REQ-PL-G05-NOP-PARTIAL_REWARD
- obligation: platform
- scope: platform
- stages: stage1
- source: pp. 10–11 screenshots; gate prose pp. 9–11
- section: G05 Verifier controls
- explained_in: 00-source/PLATFORM-RULE-CATALOG.md
- compliance_check: Stage 1 blocking reason is not this id, or the outcome is a documented retry rather than a task rewrite when the prose classifies it as platform-side.
- evidence: stage1.txt
- contradiction_or_rejection_risk: U-SEVERITY-ALIGNMENT. Severity badges in the screenshots were not column-aligned, so this row does not assert REQUIRED versus OPTIONAL.
- requirement: Platform rule `NOP.PARTIAL_REWARD` is visible under G05 Verifier controls. Confidence: screenshot. The author prevents the failing condition named by the rule and archives the live text if it fires.

## REQ-PL-G05-HARBOR-NONZERO_AGENT_EXIT_ANOMALY
- obligation: platform
- scope: platform
- stages: stage1
- source: pp. 10–11 screenshots; gate prose pp. 9–11
- section: G05 Verifier controls
- explained_in: 00-source/PLATFORM-RULE-CATALOG.md
- compliance_check: Stage 1 blocking reason is not this id, or the outcome is a documented retry rather than a task rewrite when the prose classifies it as platform-side.
- evidence: stage1.txt
- contradiction_or_rejection_risk: U-SEVERITY-ALIGNMENT. Severity badges in the screenshots were not column-aligned, so this row does not assert REQUIRED versus OPTIONAL.
- requirement: Platform rule `HARBOR.NONZERO_AGENT_EXIT_ANOMALY` is visible under G05 Verifier controls. Confidence: screenshot. The author prevents the failing condition named by the rule and archives the live text if it fires.

## REQ-PL-G05-HARBOR-AGENT_TIMEOUT_ORACLE
- obligation: platform
- scope: platform
- stages: stage1
- source: pp. 10–11 screenshots; gate prose pp. 9–11
- section: G05 Verifier controls
- explained_in: 00-source/PLATFORM-RULE-CATALOG.md
- compliance_check: Stage 1 blocking reason is not this id, or the outcome is a documented retry rather than a task rewrite when the prose classifies it as platform-side.
- evidence: stage1.txt
- contradiction_or_rejection_risk: U-SEVERITY-ALIGNMENT. Severity badges in the screenshots were not column-aligned, so this row does not assert REQUIRED versus OPTIONAL.
- requirement: Platform rule `HARBOR.AGENT_TIMEOUT_ORACLE` is visible under G05 Verifier controls. Confidence: screenshot. The author prevents the failing condition named by the rule and archives the live text if it fires.

## REQ-PL-G05-HARBOR-AGENT_TIMEOUT_ANOMALY
- obligation: platform
- scope: platform
- stages: stage1
- source: pp. 10–11 screenshots; gate prose pp. 9–11
- section: G05 Verifier controls
- explained_in: 00-source/PLATFORM-RULE-CATALOG.md
- compliance_check: Stage 1 blocking reason is not this id, or the outcome is a documented retry rather than a task rewrite when the prose classifies it as platform-side.
- evidence: stage1.txt
- contradiction_or_rejection_risk: U-SEVERITY-ALIGNMENT. Severity badges in the screenshots were not column-aligned, so this row does not assert REQUIRED versus OPTIONAL.
- requirement: Platform rule `HARBOR.AGENT_TIMEOUT_ANOMALY` is visible under G05 Verifier controls. Confidence: screenshot. The author prevents the failing condition named by the rule and archives the live text if it fires.

## REQ-PL-G05-HARBOR-VERIFIER_TIMEOUT
- obligation: platform
- scope: platform
- stages: stage1
- source: pp. 10–11 screenshots; gate prose pp. 9–11
- section: G05 Verifier controls
- explained_in: 00-source/PLATFORM-RULE-CATALOG.md
- compliance_check: Stage 1 blocking reason is not this id, or the outcome is a documented retry rather than a task rewrite when the prose classifies it as platform-side.
- evidence: stage1.txt
- contradiction_or_rejection_risk: U-SEVERITY-ALIGNMENT. Severity badges in the screenshots were not column-aligned, so this row does not assert REQUIRED versus OPTIONAL.
- requirement: Platform rule `HARBOR.VERIFIER_TIMEOUT` is visible under G05 Verifier controls. Confidence: screenshot. The author prevents the failing condition named by the rule and archives the live text if it fires.

## REQ-PL-G05-HARBOR-REWARD_NOT_FOUND
- obligation: platform
- scope: platform
- stages: stage1
- source: pp. 10–11 screenshots; gate prose pp. 9–11
- section: G05 Verifier controls
- explained_in: 00-source/PLATFORM-RULE-CATALOG.md
- compliance_check: Stage 1 blocking reason is not this id, or the outcome is a documented retry rather than a task rewrite when the prose classifies it as platform-side.
- evidence: stage1.txt
- contradiction_or_rejection_risk: U-SEVERITY-ALIGNMENT. Severity badges in the screenshots were not column-aligned, so this row does not assert REQUIRED versus OPTIONAL.
- requirement: Platform rule `HARBOR.REWARD_NOT_FOUND` is visible under G05 Verifier controls. Confidence: screenshot. The author prevents the failing condition named by the rule and archives the live text if it fires.

## REQ-PL-G05-HARBOR-REWARD_EMPTY
- obligation: platform
- scope: platform
- stages: stage1
- source: pp. 10–11 screenshots; gate prose pp. 9–11
- section: G05 Verifier controls
- explained_in: 00-source/PLATFORM-RULE-CATALOG.md
- compliance_check: Stage 1 blocking reason is not this id, or the outcome is a documented retry rather than a task rewrite when the prose classifies it as platform-side.
- evidence: stage1.txt
- contradiction_or_rejection_risk: U-SEVERITY-ALIGNMENT. Severity badges in the screenshots were not column-aligned, so this row does not assert REQUIRED versus OPTIONAL.
- requirement: Platform rule `HARBOR.REWARD_EMPTY` is visible under G05 Verifier controls. Confidence: screenshot. The author prevents the failing condition named by the rule and archives the live text if it fires.

## REQ-PL-G05-HARBOR-REWARD_PARSE
- obligation: platform
- scope: platform
- stages: stage1
- source: pp. 10–11 screenshots; gate prose pp. 9–11
- section: G05 Verifier controls
- explained_in: 00-source/PLATFORM-RULE-CATALOG.md
- compliance_check: Stage 1 blocking reason is not this id, or the outcome is a documented retry rather than a task rewrite when the prose classifies it as platform-side.
- evidence: stage1.txt
- contradiction_or_rejection_risk: U-SEVERITY-ALIGNMENT. Severity badges in the screenshots were not column-aligned, so this row does not assert REQUIRED versus OPTIONAL.
- requirement: Platform rule `HARBOR.REWARD_PARSE` is visible under G05 Verifier controls. Confidence: screenshot. The author prevents the failing condition named by the rule and archives the live text if it fires.

## REQ-PL-G05-HARBOR-VALIDATION_ERROR
- obligation: platform
- scope: platform
- stages: stage1
- source: pp. 10–11 screenshots; gate prose pp. 9–11
- section: G05 Verifier controls
- explained_in: 00-source/PLATFORM-RULE-CATALOG.md
- compliance_check: Stage 1 blocking reason is not this id, or the outcome is a documented retry rather than a task rewrite when the prose classifies it as platform-side.
- evidence: stage1.txt
- contradiction_or_rejection_risk: U-SEVERITY-ALIGNMENT. Severity badges in the screenshots were not column-aligned, so this row does not assert REQUIRED versus OPTIONAL.
- requirement: Platform rule `HARBOR.VALIDATION_ERROR` is visible under G05 Verifier controls. Confidence: screenshot. The author prevents the failing condition named by the rule and archives the live text if it fires.

## REQ-PL-G05-HARBOR-REWARD_INVALID
- obligation: platform
- scope: platform
- stages: stage1
- source: pp. 10–11 screenshots; gate prose pp. 9–11
- section: G05 Verifier controls
- explained_in: 00-source/PLATFORM-RULE-CATALOG.md
- compliance_check: Stage 1 blocking reason is not this id, or the outcome is a documented retry rather than a task rewrite when the prose classifies it as platform-side.
- evidence: stage1.txt
- contradiction_or_rejection_risk: U-SEVERITY-ALIGNMENT. Severity badges in the screenshots were not column-aligned, so this row does not assert REQUIRED versus OPTIONAL.
- requirement: Platform rule `HARBOR.REWARD_INVALID` is visible under G05 Verifier controls. Confidence: screenshot. The author prevents the failing condition named by the rule and archives the live text if it fires.

## REQ-PL-G05-HARBOR-REWARD_AMBIGUOUS
- obligation: platform
- scope: platform
- stages: stage1
- source: pp. 10–11 screenshots; gate prose pp. 9–11
- section: G05 Verifier controls
- explained_in: 00-source/PLATFORM-RULE-CATALOG.md
- compliance_check: Stage 1 blocking reason is not this id, or the outcome is a documented retry rather than a task rewrite when the prose classifies it as platform-side.
- evidence: stage1.txt
- contradiction_or_rejection_risk: U-SEVERITY-ALIGNMENT. Severity badges in the screenshots were not column-aligned, so this row does not assert REQUIRED versus OPTIONAL.
- requirement: Platform rule `HARBOR.REWARD_AMBIGUOUS` is visible under G05 Verifier controls. Confidence: screenshot. The author prevents the failing condition named by the rule and archives the live text if it fires.

## REQ-PL-G05-HARBOR-CANCELLED
- obligation: platform
- scope: platform
- stages: stage1
- source: pp. 10–11 screenshots; gate prose pp. 9–11
- section: G05 Verifier controls
- explained_in: 00-source/PLATFORM-RULE-CATALOG.md
- compliance_check: Stage 1 blocking reason is not this id, or the outcome is a documented retry rather than a task rewrite when the prose classifies it as platform-side.
- evidence: stage1.txt
- contradiction_or_rejection_risk: U-SEVERITY-ALIGNMENT. Severity badges in the screenshots were not column-aligned, so this row does not assert REQUIRED versus OPTIONAL.
- requirement: Platform rule `HARBOR.CANCELLED` is visible under G05 Verifier controls. Confidence: screenshot. The author prevents the failing condition named by the rule and archives the live text if it fires.

## REQ-PL-G05-HARBOR-AGENT_SETUP_TIMEOUT
- obligation: platform
- scope: platform
- stages: stage1
- source: pp. 10–11 screenshots; gate prose pp. 9–11
- section: G05 Verifier controls
- explained_in: 00-source/PLATFORM-RULE-CATALOG.md
- compliance_check: Stage 1 blocking reason is not this id, or the outcome is a documented retry rather than a task rewrite when the prose classifies it as platform-side.
- evidence: stage1.txt
- contradiction_or_rejection_risk: U-SEVERITY-ALIGNMENT. Severity badges in the screenshots were not column-aligned, so this row does not assert REQUIRED versus OPTIONAL.
- requirement: Platform rule `HARBOR.AGENT_SETUP_TIMEOUT` is visible under G05 Verifier controls. Confidence: screenshot. The author prevents the failing condition named by the rule and archives the live text if it fires.

## REQ-PL-G05-HARBOR-UNKNOWN_EXCEPTION
- obligation: platform
- scope: platform
- stages: stage1
- source: pp. 10–11 screenshots; gate prose pp. 9–11
- section: G05 Verifier controls
- explained_in: 00-source/PLATFORM-RULE-CATALOG.md
- compliance_check: Stage 1 blocking reason is not this id, or the outcome is a documented retry rather than a task rewrite when the prose classifies it as platform-side.
- evidence: stage1.txt
- contradiction_or_rejection_risk: U-SEVERITY-ALIGNMENT. Severity badges in the screenshots were not column-aligned, so this row does not assert REQUIRED versus OPTIONAL.
- requirement: Platform rule `HARBOR.UNKNOWN_EXCEPTION` is visible under G05 Verifier controls. Confidence: prose and screenshot. The author prevents the failing condition named by the rule and archives the live text if it fires.

## REQ-PL-G05-HARBOR-OOM
- obligation: platform
- scope: platform
- stages: stage1
- source: pp. 10–11 screenshots; gate prose pp. 9–11
- section: G05 Verifier controls
- explained_in: 00-source/PLATFORM-RULE-CATALOG.md
- compliance_check: Stage 1 blocking reason is not this id, or the outcome is a documented retry rather than a task rewrite when the prose classifies it as platform-side.
- evidence: stage1.txt
- contradiction_or_rejection_risk: U-SEVERITY-ALIGNMENT. Severity badges in the screenshots were not column-aligned, so this row does not assert REQUIRED versus OPTIONAL.
- requirement: Platform rule `HARBOR.OOM` is visible under G05 Verifier controls. Confidence: screenshot. The author prevents the failing condition named by the rule and archives the live text if it fires.

## REQ-PL-G05-HARBOR-RESULT_MISSING
- obligation: platform
- scope: platform
- stages: stage1
- source: pp. 10–11 screenshots; gate prose pp. 9–11
- section: G05 Verifier controls
- explained_in: 00-source/PLATFORM-RULE-CATALOG.md
- compliance_check: Stage 1 blocking reason is not this id, or the outcome is a documented retry rather than a task rewrite when the prose classifies it as platform-side.
- evidence: stage1.txt
- contradiction_or_rejection_risk: U-SEVERITY-ALIGNMENT. Severity badges in the screenshots were not column-aligned, so this row does not assert REQUIRED versus OPTIONAL.
- requirement: Platform rule `HARBOR.RESULT_MISSING` is visible under G05 Verifier controls. Confidence: screenshot. The author prevents the failing condition named by the rule and archives the live text if it fires.

## REQ-PL-G05-ARTIFACT-COLLECTION_FAILED
- obligation: platform
- scope: platform
- stages: stage1
- source: pp. 10–11 screenshots; gate prose pp. 9–11
- section: G05 Verifier controls
- explained_in: 00-source/PLATFORM-RULE-CATALOG.md
- compliance_check: Stage 1 blocking reason is not this id, or the outcome is a documented retry rather than a task rewrite when the prose classifies it as platform-side.
- evidence: stage1.txt
- contradiction_or_rejection_risk: U-SEVERITY-ALIGNMENT. Severity badges in the screenshots were not column-aligned, so this row does not assert REQUIRED versus OPTIONAL.
- requirement: Platform rule `ARTIFACT.COLLECTION_FAILED` is visible under G05 Verifier controls. Confidence: screenshot. The author prevents the failing condition named by the rule and archives the live text if it fires.

## REQ-PL-P04-SANITIZE_OUTPUT
- obligation: platform
- scope: platform
- stages: stage1
- source: pp. 10–11 screenshots; gate prose pp. 9–11
- section: P04 Final publication barrier
- explained_in: 00-source/PLATFORM-RULE-CATALOG.md
- compliance_check: Stage 1 blocking reason is not this id, or the outcome is a documented retry rather than a task rewrite when the prose classifies it as platform-side.
- evidence: stage1.txt
- contradiction_or_rejection_risk: U-SEVERITY-ALIGNMENT. Severity badges in the screenshots were not column-aligned, so this row does not assert REQUIRED versus OPTIONAL.
- requirement: Platform phase `SANITIZE_OUTPUT` is visible under P04 Final publication barrier. Confidence: screenshot. The author prevents the failing condition named by the rule and archives the live text if it fires.

## REQ-PL-P04-HASH_CLOSURE
- obligation: platform
- scope: platform
- stages: stage1
- source: pp. 10–11 screenshots; gate prose pp. 9–11
- section: P04 Final publication barrier
- explained_in: 00-source/PLATFORM-RULE-CATALOG.md
- compliance_check: Stage 1 blocking reason is not this id, or the outcome is a documented retry rather than a task rewrite when the prose classifies it as platform-side.
- evidence: stage1.txt
- contradiction_or_rejection_risk: U-SEVERITY-ALIGNMENT. Severity badges in the screenshots were not column-aligned, so this row does not assert REQUIRED versus OPTIONAL.
- requirement: Platform phase `HASH_CLOSURE` is visible under P04 Final publication barrier. Confidence: screenshot. The author prevents the failing condition named by the rule and archives the live text if it fires.

## REQ-PL-P04-PERSIST_RESULT
- obligation: platform
- scope: platform
- stages: stage1
- source: pp. 10–11 screenshots; gate prose pp. 9–11
- section: P04 Final publication barrier
- explained_in: 00-source/PLATFORM-RULE-CATALOG.md
- compliance_check: Stage 1 blocking reason is not this id, or the outcome is a documented retry rather than a task rewrite when the prose classifies it as platform-side.
- evidence: stage1.txt
- contradiction_or_rejection_risk: U-SEVERITY-ALIGNMENT. Severity badges in the screenshots were not column-aligned, so this row does not assert REQUIRED versus OPTIONAL.
- requirement: Platform phase `PERSIST_RESULT` is visible under P04 Final publication barrier. Confidence: screenshot. The author prevents the failing condition named by the rule and archives the live text if it fires.

## REQ-PL-P04-PUBLISH_ADMISSION
- obligation: platform
- scope: platform
- stages: stage1
- source: pp. 10–11 screenshots; gate prose pp. 9–11
- section: P04 Final publication barrier
- explained_in: 00-source/PLATFORM-RULE-CATALOG.md
- compliance_check: Stage 1 blocking reason is not this id, or the outcome is a documented retry rather than a task rewrite when the prose classifies it as platform-side.
- evidence: stage1.txt
- contradiction_or_rejection_risk: U-SEVERITY-ALIGNMENT. Severity badges in the screenshots were not column-aligned, so this row does not assert REQUIRED versus OPTIONAL.
- requirement: Platform phase `PUBLISH_ADMISSION` is visible under P04 Final publication barrier. Confidence: screenshot. The author prevents the failing condition named by the rule and archives the live text if it fires.

## REQ-PL-P04-REDACTION-INCOMPLETE
- obligation: platform
- scope: platform
- stages: stage1
- source: pp. 10–11 screenshots; gate prose pp. 9–11
- section: P04 Final publication barrier
- explained_in: 00-source/PLATFORM-RULE-CATALOG.md
- compliance_check: Stage 1 blocking reason is not this id, or the outcome is a documented retry rather than a task rewrite when the prose classifies it as platform-side.
- evidence: stage1.txt
- contradiction_or_rejection_risk: U-SEVERITY-ALIGNMENT. Severity badges in the screenshots were not column-aligned, so this row does not assert REQUIRED versus OPTIONAL.
- requirement: Platform rule `REDACTION.INCOMPLETE` is visible under P04 Final publication barrier. Confidence: screenshot. The author prevents the failing condition named by the rule and archives the live text if it fires.

## REQ-PL-P04-METADATA-UNAVAILABLE
- obligation: platform
- scope: platform
- stages: stage1
- source: pp. 10–11 screenshots; gate prose pp. 9–11
- section: P04 Final publication barrier
- explained_in: 00-source/PLATFORM-RULE-CATALOG.md
- compliance_check: Stage 1 blocking reason is not this id, or the outcome is a documented retry rather than a task rewrite when the prose classifies it as platform-side.
- evidence: stage1.txt
- contradiction_or_rejection_risk: U-SEVERITY-ALIGNMENT. Severity badges in the screenshots were not column-aligned, so this row does not assert REQUIRED versus OPTIONAL.
- requirement: Platform rule `METADATA.UNAVAILABLE` is visible under P04 Final publication barrier. Confidence: screenshot. The author prevents the failing condition named by the rule and archives the live text if it fires.

## REQ-PL-P04-HASH_CLOSURE-FAILED
- obligation: platform
- scope: platform
- stages: stage1
- source: pp. 10–11 screenshots; gate prose pp. 9–11
- section: P04 Final publication barrier
- explained_in: 00-source/PLATFORM-RULE-CATALOG.md
- compliance_check: Stage 1 blocking reason is not this id, or the outcome is a documented retry rather than a task rewrite when the prose classifies it as platform-side.
- evidence: stage1.txt
- contradiction_or_rejection_risk: U-SEVERITY-ALIGNMENT. Severity badges in the screenshots were not column-aligned, so this row does not assert REQUIRED versus OPTIONAL.
- requirement: Platform rule `HASH_CLOSURE.FAILED` is visible under P04 Final publication barrier. Confidence: screenshot. The author prevents the failing condition named by the rule and archives the live text if it fires.

## REQ-PL-P04-PUBLICATION-FAILED
- obligation: platform
- scope: platform
- stages: stage1
- source: pp. 10–11 screenshots; gate prose pp. 9–11
- section: P04 Final publication barrier
- explained_in: 00-source/PLATFORM-RULE-CATALOG.md
- compliance_check: Stage 1 blocking reason is not this id, or the outcome is a documented retry rather than a task rewrite when the prose classifies it as platform-side.
- evidence: stage1.txt
- contradiction_or_rejection_risk: U-SEVERITY-ALIGNMENT. Severity badges in the screenshots were not column-aligned, so this row does not assert REQUIRED versus OPTIONAL.
- requirement: Platform rule `PUBLICATION.FAILED` is visible under P04 Final publication barrier. Confidence: screenshot. The author prevents the failing condition named by the rule and archives the live text if it fires.

## REQ-PL-P04-NOT_REACHED
- obligation: platform
- scope: platform
- stages: stage1
- source: pp. 10–11 screenshots; gate prose pp. 9–11
- section: P04 Final publication barrier
- explained_in: 00-source/PLATFORM-RULE-CATALOG.md
- compliance_check: Stage 1 blocking reason is not this id, or the outcome is a documented retry rather than a task rewrite when the prose classifies it as platform-side.
- evidence: stage1.txt
- contradiction_or_rejection_risk: U-SEVERITY-ALIGNMENT. Severity badges in the screenshots were not column-aligned, so this row does not assert REQUIRED versus OPTIONAL.
- requirement: Platform rule `NOT_REACHED` is visible under P04 Final publication barrier. Confidence: screenshot. The author prevents the failing condition named by the rule and archives the live text if it fires.

## REQ-PL-P04-RUNTIME_TUPLE-UNAVAILABLE
- obligation: platform
- scope: platform
- stages: stage1
- source: pp. 10–11 screenshots; gate prose pp. 9–11
- section: P04 Final publication barrier
- explained_in: 00-source/PLATFORM-RULE-CATALOG.md
- compliance_check: Stage 1 blocking reason is not this id, or the outcome is a documented retry rather than a task rewrite when the prose classifies it as platform-side.
- evidence: stage1.txt
- contradiction_or_rejection_risk: U-SEVERITY-ALIGNMENT. Severity badges in the screenshots were not column-aligned, so this row does not assert REQUIRED versus OPTIONAL.
- requirement: Platform rule `RUNTIME_TUPLE.UNAVAILABLE` is visible under P04 Final publication barrier. Confidence: screenshot. The author prevents the failing condition named by the rule and archives the live text if it fires.

## REQ-PL-P04-PLATFORM-UNKNOWN_EVIDENCE
- obligation: platform
- scope: platform
- stages: stage1
- source: pp. 10–11 screenshots; gate prose pp. 9–11
- section: P04 Final publication barrier
- explained_in: 00-source/PLATFORM-RULE-CATALOG.md
- compliance_check: Stage 1 blocking reason is not this id, or the outcome is a documented retry rather than a task rewrite when the prose classifies it as platform-side.
- evidence: stage1.txt
- contradiction_or_rejection_risk: U-SEVERITY-ALIGNMENT. Severity badges in the screenshots were not column-aligned, so this row does not assert REQUIRED versus OPTIONAL.
- requirement: Platform rule `PLATFORM.UNKNOWN_EVIDENCE` is visible under P04 Final publication barrier. Confidence: screenshot. The author prevents the failing condition named by the rule and archives the live text if it fires.

## REQ-PL-P04-PLATFORM-UNKNOWN_EXCEPTION
- obligation: platform
- scope: platform
- stages: stage1
- source: pp. 10–11 screenshots; gate prose pp. 9–11
- section: P04 Final publication barrier
- explained_in: 00-source/PLATFORM-RULE-CATALOG.md
- compliance_check: Stage 1 blocking reason is not this id, or the outcome is a documented retry rather than a task rewrite when the prose classifies it as platform-side.
- evidence: stage1.txt
- contradiction_or_rejection_risk: U-SEVERITY-ALIGNMENT. Severity badges in the screenshots were not column-aligned, so this row does not assert REQUIRED versus OPTIONAL.
- requirement: Platform rule `PLATFORM.UNKNOWN_EXCEPTION` is visible under P04 Final publication barrier. Confidence: screenshot. The author prevents the failing condition named by the rule and archives the live text if it fires.
