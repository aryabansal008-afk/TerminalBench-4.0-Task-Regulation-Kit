# Genuine complexity

This is how the authoring agent builds a hard task. It is not a measurement of difficulty or of long horizon. Those are recorded in three separate places, defined at the end of this file. A task that sounds complex has not met either property.

Numeric ceilings stay in `DESIGN.md`. `C-DIFFICULTY` and `C-HORIZON` are unresolved. This file does not pick a ceiling to design toward.

## What the work is

**Source.** Difficulty is years of domain expertise, not volume. An average undergraduate finishing the task in a few days is too easy. An expert who already knows the answer can implement it in a few hours. Rubric C: hardness comes from real reasoning or engineering. The proposal’s examples of a real trap are cross-source correlation, adversarial noise, and cascading errors. When a Stage 2 difficulty fail says the task is too easy, add depth: more cross-source correlation, more state that must stay consistent, stricter exactness in the output contract. When the trajectory is too short, add genuine sequential work: more components that must all hold together, and more recovery and boundary conditions the agent has to discover and handle.

**Practice.** Build the task so the graded artifact depends on all of the following, each of which is visible in the instruction:

- Expertise: a method a newcomer would not already be carrying, applied to this system’s inputs.
- Coherent multistage work: later state is wrong unless earlier state was right. The stages are the author’s private description of that dependence. They are not a step list in `instruction.md`.
- Investigation: the inputs contain the evidence that decides which constraint binds. The instruction says what the artifact must satisfy. It does not name the line, file, or constant that is the answer.
- Interacting constraints: at least two stated requirements that cannot be satisfied one at a time. The obvious way to meet one of them breaks the other.

One focused objective. A bundle of unrelated sub-tasks is not complexity.

## Preconditions

Do not start a difficulty argument until these four are true. They are source requirements. Meeting them does not establish difficulty or long horizon.

| Precondition | Source rule | Not yet met when |
| --- | --- | --- |
| Focused objective | One correct interpretation of “done.” Rubric D, appropriately scoped. | The instruction has two unrelated deliverables, or two readers would disagree about success. |
| Feasible reference solution | A solution exists. An expert who knows the answer can implement it in a few hours. Oracle reward `1.0`. | No solution is written, or the oracle cannot finish inside the provisional `timeout_sec`. A limit the reference solution cannot meet is a broken budget, not a source of difficulty (`C-TIMEOUT` remains unresolved). |
| Complete inputs | Everything needed is in the instruction and the environment. No hidden knowledge and no missing inputs. | A fact required to grade the artifact is absent from both. |
| Deterministic outcome verification | Grade the final artifact. No LLM judge. No fuzzy match that can pass a wrong answer. | The test checks the route, a keyword, or a step the instruction never stated. |

## Substitutes that are not difficulty

| Do not use | Why it is not difficulty |
| --- | --- |
| Ambiguity | Two correct artifacts would disagree. Fix the contract. Do not hope the model guesses. |
| Withheld requirements | Page 15 forbids hiding information. A test that checks an unstated condition is hidden grading. Add the condition to the instruction and the coverage table together, or delete the test. |
| Arbitrary formatting traps | Rubric C forbids guess-the-format and trick wording. Exact schema, order, and formatting are legitimate only when the instruction states them so a correct attempt is not failed on a guessable detail. |
| Impossible resource limits | Rubric E: timeouts and resources must not be too tight to solve. The reference solution has to finish. Tightness the oracle cannot survive is a defect. |
| Irrelevant busywork | Page 15: padding does not survive later review. Extra commands, repeated files, or a longer instruction do not add horizon. The word-count cap is 1500 by `content.split()`. Length is not difficulty. |
| Forced tool use | Outcome-verified grading forbids prescribed tools. Name the artifact, not the program that must produce it. |
| Prescribed solution steps | Enumerated steps cost the outcome-verified criterion. The author’s private stage list stays in `complexity.md`. |
| Artificial turn inflation | A longer transcript is not long horizon. Do not add chatter, retries of the same command, or filler the verifier ignores. |

## Naive approaches

**Source.** The proposal names the naive approach an LLM tries first and the mechanical reason it fails. Doing nothing, or an obvious naive approach, does not pass.

**Practice.** The proposal names the naive approach and the mechanical reason it fails, inside the length cap. The private record names that approach and at least one more. For each, write the stated requirement it violates. “Stated” means a sentence that will be in `instruction.md`, not a test-only rule.

Then, once the verifier exists, implement each approach as an author-built attempt and record its reward under local measurements. The reward has to be `0.0`. If it is `1.0`, that approach meets the stated requirements and the task is the easy version. Do not respond by adding a hidden assertion. Either the approach is actually inadequate and a stated requirement already says so, in which case the test must assert that requirement, or the task needs a new stated constraint from the page 15 list.

## Shortcuts

Check these before calling the construction finished. A pass here is not a difficulty measurement.

- The answer is not a public page the agent can copy.
- One fixture’s output cannot be pasted for every input. If it can, hardcoding is the correct solution.
- Tests execute or compare the artifact. They do not grep the agent’s source for keywords.
- The agent image has no copy of `tests/`, `solution/`, or the expected values.
- `test.sh` does not fetch. The agent does not get credit for writing `/logs/verifier/reward.txt`.
- The instruction and the fixtures do not contain the expected answer.

The adversarial loop in `11-validation/VALIDATION.md` is the place those attempts are run. Record the rewards in this file’s local-measurement section, not as a platform verdict.

## Strengthening

Use this only after a local naive attempt scores `1.0`, a dry-run finishes in a handful of turns, or a platform receipt says the task is too easy or too short. Quote the receipt if one exists. Do not strengthen because the prose “feels” short.

Allowed moves, from page 15:

- More cross-source correlation: the artifact is right only when two or more inputs agree.
- More state that must stay consistent: a change that satisfies one output field breaks another unless both are recomputed.
- Stricter exactness in the output contract: the instruction states the tighter schema, and the test asserts that same sentence.
- More components that must all hold together, or more recovery and boundary conditions the agent has to discover in the inputs.

Each move adds a sentence to the instruction and a row to the coverage table in the same edit. If the granted proposal’s graded conditions change, that is a new task (`04-proposal/PROPOSAL.md`). Re-run Oracle, NOP, and the naive attempts. Re-measure locally. Leave the platform fields blank until a new receipt exists.

## Three records that stay separate

Copy `material/private-authoring/complexity.md` to `evidence/<slug>/complexity.md`. Fill it in three blocks. Do not write a sentence that treats one block as another.

| Block | What may appear there | What must not |
| --- | --- | --- |
| Proposed targets | The qualitative bars on page 4, and both written ceilings from `DESIGN.md`, each marked with its page. Status of the numeric pair: unresolved. | An observed count. The word “passed.” |
| Local measurements | Oracle reward, NOP reward, each naive attempt’s reward, and the dry-run’s model, date, reward, and assistant-message count if the runner exposed one. | A claim that Stage 2 or acceptance will pass or fail. A claim that the task “is” long-horizon. |
| Platform verdicts | The Stage 2 observed full-credit count, the observed median, the verdict string, and any acceptance numbers a reviewer actually quoted. Blank until those receipts exist. | A number copied from the proposed-target block. A local dry-run count labeled as the median of the eight rollouts. |

`difficulty_explanation` in `task.toml` names the engineering constraint. It does not say “≤4”, “4/8”, or “>35”, and it does not say the task has passed a gate that has not been run.
