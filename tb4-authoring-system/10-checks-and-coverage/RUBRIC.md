# Rubric criteria

The rubric asks whether the task is good. Static checks only ask whether it is well-formed. The platform runs the rubric as a quality review. The author runs it locally first with a free or open-source LLM. The source’s examples of “enough to catch obvious gaps” are Llama-class or Kimi-class models. A local pass is a signal, not a platform pass. A local fail is a defect to fix before upload.

Each criterion is `PASS` or `FAIL` with a justification. Aim for every criterion to `PASS`. There are 30, in five groups. Page 21’s “9 Quality Dimensions” is `C-NINE-DIMENSIONS` and is unresolved. Do not collapse this list into nine names, and do not write “9 Quality Dimensions: green.”

How to run it locally: give the model the instruction, environment, solution, and tests, and this page. Read each `FAIL`, fix the underlying issue, re-run. Do not argue the model out of a fail that matches the criterion text. Store the 30 justifications in the private evidence pack.

## Group A — Verifiability and correctness

| Criterion | What the reviewer looks for |
| --- | --- |
| Deterministic verification | Fully deterministic. No LLM-as-judge. No fuzzy matching that could pass wrong answers or fail right ones. |
| Outcome-based grading | Tests check the agent’s final output or artifact, not the steps or method. |
| Frozen ground truth | Expected values come from frozen, in-image fixtures. Results are reproducible and not time- or network-dependent. |
| Complete coverage | Tests cover the full required output, all fields and edge cases, not a happy-path subset. |
| Correct expected values | The answers the tests assert are themselves correct, independently derived or verified. |
| Strict failure on no-op | A do-nothing or partial attempt fails. The verifier is not lenient. |

## Group B — Solvability

| Criterion | What the reviewer looks for |
| --- | --- |
| Reference solution exists | A correct reference solution is provided and passes all tests (Oracle = 1.0). |
| Solvable from instruction alone | Everything needed is in the instruction and the environment. No external or hidden knowledge and no missing inputs. |
| Environment is self-contained | Required tools, data, and dependencies are in the container. The task does not rely on flaky external resources. |
| Achievable in the time budget | A capable agent can plausibly finish within `[agent].timeout_sec`. |
| No ambiguity in the goal | One clearly correct interpretation of “done.” |
| Output schema fully specified | Exact output path, format, schema, ordering, and formatting, so a correct attempt is not failed on a guessable detail. |

## Group C — Difficulty and anti-cheat

| Criterion | What the reviewer looks for |
| --- | --- |
| Genuinely difficult | Hard for a strong agent. Not a trivial one-liner or an obvious lookup. |
| Non-trivial (NOP fails) | Doing nothing, or an obvious naive approach, does not pass. |
| Difficulty is legitimate | Real reasoning or engineering. Not obscure trivia, trick wording, or guess-the-format. |
| Resistant to reward hacking | The agent cannot game the verifier by hardcoding expected values, writing reward files, or reading hidden tests or the solution. |
| Answer not leaked | Instruction, environment, and data do not reveal the expected answer or the test internals. |
| No shortcut via internet | The answer cannot simply be looked up online or copied from a public source. |

## Group D — Instruction clarity and quality

| Criterion | What the reviewer looks for |
| --- | --- |
| Clear and well-written | Unambiguous, well-structured, and free of contradictions. Structure here does not mean `##` headings (`C-HEADINGS`). |
| No hidden hints or leakage | Does not hint at the solution method or leak verifier details. |
| Absolute paths and concrete I/O | All file paths are absolute and every required input and output is named explicitly. |
| Required suffix present | Ends with the exact timeout / anti-cheat line matching the agent timeout. |
| Self-consistent with tests | What the instruction asks for is exactly what the tests check. No drift. |
| Appropriately scoped | One focused objective, not a sprawling bundle of unrelated sub-tasks. |

## Group E — Structure, environment, and realism

| Criterion | What the reviewer looks for |
| --- | --- |
| Separate verifier configured | Tests run in their own container after the agent. The agent image is clean. |
| Dependencies pinned and baked | Dependencies are version-pinned and pre-installed in the right image. No runtime installs at verify time. |
| Sensible resources | CPU, memory, storage, and timeouts are appropriate. Not wastefully large. Not too tight to solve. |
| Reproducible build | Images build cleanly and deterministically on a fresh machine. |
| Real-world relevance | A realistic, valuable scenario someone would actually do. Not a contrived puzzle. |
| Correct and complete metadata | Difficulty, solution, and verification explanations, category, tags, and time estimate are filled in and accurate. |

## Not this list

The six proposal criteria are Verifiable, Well-specified, Solvable, Difficult, Interesting, and Outcome-verified. Interesting has no identical rubric row. Real-world relevance is the closest, and the proposal criterion is still mandatory at proposal time. Do not substitute one list for the other.
