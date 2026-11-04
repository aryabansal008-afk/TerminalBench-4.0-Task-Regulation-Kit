# Instruction and the input/output contract

`instruction.md` is the agent-facing task statement. It is not the proposal and it is not a solution sketch. It is agent-visible and it is in the ZIP. See `material/MATERIAL-CLASSES.md`.

## Source limits

- `content.split()` must not exceed 1500. The TB4 reference distribution is average 267 words, maximum 1406. Aim near the average. `content.split()` splits on whitespace. Count the whole file, including the suffix. The PDF does not say the suffix is excluded.
- No leading or suggestive phrasing. The source’s examples are “please think step by step” and “you are an expert in xxx.”
- No hints. The example tree’s comment on the instruction is “No hints.”
- Absolute paths only. `/app/data.csv`, never `data.csv` or `./data.csv`. The source also gives `/app/solve.py` and `/app/report.json` as shapes.
- No tidy `##` headings and no excessive length. Page 7 calls that shape “pure LLM synthesis without human review.” `C-HEADINGS` is compatible: “well-structured” in the rubric does not mean `##` headings.
- One focused objective. Do not enumerate the steps the agent must follow. Do not prescribe tools.
- No statement of the expected answer, the test internals, or the solution method.

## The contract

**Source.** A solver who has only the instruction and the container must be able to produce the graded artifact.

- One correct interpretation of “done.”
- Exact output path, format, schema, ordering, and formatting. A correct attempt must not fail on a guessable detail.
- Every required input and every required output named explicitly, with absolute paths.
- Every output file that both the tests and the solution reference is documented in `instruction.md` or `task.toml` (`check-test-file-references`).
- If Python is system-wide rather than isolated with `uv venv`, say so here or in `task.toml` (`check-test-sh-sanity`).
- What the instruction asks for is exactly what the tests check.

## Required closing line

`check-instruction-suffix` requires `instruction.md` to end with this exact line, where `N` is the integer in `[agent].timeout_sec`:

```
You have N seconds to complete this task. Do not cheat by using online solutions or hints specific to this task.
```

The line is its own paragraph and the file has a single trailing newline. The curly quotes in the PDF wrap the sentence; they are not part of the line. `N` matches `[agent].timeout_sec` exactly, with no thousands separator. Which integer is allowed is `C-TIMEOUT` and is unresolved. The equality of the suffix and the field is not in conflict.

## Consistency review

**Practice.** Build a three-column list before the first Oracle run: each graded condition, the absolute path and schema field it concerns, and the test function that asserts it. A condition in the instruction with no test is ungraded scope. A test with no condition is hidden grading. Either one fails “Self-consistent with tests” or “Well-specified.” Keep the list in the private evidence pack, not in `instruction.md`. The method is in `10-checks-and-coverage/COVERAGE.md`.
