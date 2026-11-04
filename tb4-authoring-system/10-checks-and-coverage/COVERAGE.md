# Requirement-to-test coverage

**Source.** Complete coverage: tests cover the full required output, all fields and edge cases, not a happy-path subset. Self-consistent with tests: what the instruction asks for is exactly what the tests check. Well-specified: two readers should independently write verifiers that agree. `check-test-file-references` is the mechanical slice of the same idea for output paths.

**Practice.** Keep `coverage.md` in the private evidence pack. It is not a ZIP member. One row per graded condition:

| Column | Content |
| --- | --- |
| Condition | The sentence in `instruction.md`, quoted. |
| Path and schema | Absolute output path and the field, order, or format. |
| Test | The function that fails when this condition is wrong. |
| Negative | The input or mutation that must fail, if the condition has an edge. |
| Ground truth | Where the expected value lives, and how it was derived (`08-reference-solution/SOLUTION.md`). |

A condition with no test is ungraded scope. A test with no condition is hidden grading. An edge named in the instruction with only a happy-path assertion fails Complete coverage. Do not add a test for a behavior the instruction does not state in order to make the table look full. Change the instruction and the granted-scope diff together if the behavior is part of the task (`04-proposal/PROPOSAL.md`).

The register’s requirement IDs are not test names. Do not generate one test per register row. Generate one test per condition the instruction states.
