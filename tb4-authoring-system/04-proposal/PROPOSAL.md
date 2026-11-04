# Proposal, review, grant, and frozen scope

Platform path: `New proposal` → five fields → `SUBMIT PROPOSAL`. Submitting writes revision 1 and dispatches review in one step. There is no Discord step (`C-DISCORD`).

Category, subcategory, and the task identity come from `evidence/<slug>/selection.md`. The authoring agent already chose them. Do not ask the user, and do not swap in a taxonomy example at draft time. The title and the body must name that same task.

## Five fields

| Field | Source rule |
| --- | --- |
| `TITLE` | Specific. The placeholder is “What the task asks for, in one line.” The title must name the same task the body describes. |
| `CATEGORY` | One of `Science`, `Software`, `ML`, `Operations`, `Security`, `Hardware`, `Media`. Locked at creation. |
| `SUBCATEGORY` | Closest listed subcategory in `01-taxonomy-and-batch/TAXONOMY.md`. Custom only when none fits, and then broad and reusable. |
| `EXPERT TIME` | Hours an expert should need to build the task, not hours spent writing the proposal. See `C-EXPERT-TIME`. |
| `PROPOSAL MARKDOWN` | The proposal. Use Write / Preview and read the preview before submitting. |

## Shape

**Source.** Under 2000 characters. Two or three paragraphs. State the goal up front, then everything the verifier will check. Do not enumerate the steps the agent must follow. That reads as overspecification and costs the outcome-verified criterion.

These six topics must be understandable in a couple of minutes:

1. Summary and objective, including the exact deliverable path and type, for example `/app/report.json`.
2. Environment and inputs: binaries, a repo, datasets, logs, an API, and any helper tools or pinned engines pre-installed.
3. Why it is hard: the naive approach and why it fails.
4. Verification and grading: deterministic checks, no LLM judges, how many checks, and how hardcoding is stopped. The source’s examples are fresh or frozen fixtures and exact-value checks.
5. Real-world relevance and feasibility: who does this work, and whether the data and environment already exist or must be built.
6. Why it is distinct: one sentence against existing TB tasks and obvious public problems.

The form’s four prompts are the same content, slightly compressed: task, inputs, and outcome; programmatic verification; why it is difficult and useful; why an expert can solve it within the estimated time.

## Review

**Source.** Every criterion is judged separately, then once overall. A proposal is accepted only if it is correct, solvable, verifiable, well-specified, and hard for an interesting reason.

| Criterion | Bar |
| --- | --- |
| Verifiable | A program separates correct from incorrect, and any other reasonable verifier would agree. Subjective grading is rejected. |
| Well-specified | Everything the verifier checks is stated. Two readers should independently write verifiers that agree. |
| Solvable | A solution, or a convincing argument one exists. A few hours for an expert who knows the answer. |
| Difficult | Years of domain expertise, not volume. An average undergraduate finishing it in a few days is too easy. |
| Interesting | Someone could be paid to do this, or a real group wants it solved. |
| Outcome-verified | Grade the final state, not the route. No prescribed tools and no enumerated step lists. |

Verdict values: `Accept`, `Uncertain`, `Reject`. Read the `Final analysis` and the `Problem statement, as reviewed`. If the restatement does not match what you meant, the proposal is not yet well-specified, whatever the verdict says.

Vague proposals tend to score `Uncertain` or get rejected. Status `Proposal rejected — revise proposal` means read the final analysis, address the specific criterion, and submit a new immutable revision. No grant was issued, so Stage 1 stays closed. Revision submission is disabled for anyone except the expert who owns the task.

## Grant and frozen scope

**Source.** An `ACTIVE` grant on the accepted revision is the permission to upload. The screenshot text: “An ACTIVE grant is recorded for this revision; one immutable task ZIP version may be uploaded. Its checks begin at Stage 1.” `Upload Harbor task ZIP` stays inactive until that grant exists. The proposal text is frozen at the grant. To change the proposal materially, create a new task. An administrator can suspend or revoke a grant. Either closes Stage 1 upload and is recorded with their reason.

**Practice.** Diff the built instruction’s inputs, output path, and graded conditions against the granted problem statement before packaging. The legacy troubleshooting name `Proposal Match FAILED` includes “the built task diverged from the approved proposal.” That card name is `C-LEGACY-CARDS` and is unresolved as a button. Divergence from the frozen text is still a rejection risk because the grant freezes the text. Do not look for a Proposal Match button if the live UI only shows Stage 0–3. Do record the diff in the evidence pack.
