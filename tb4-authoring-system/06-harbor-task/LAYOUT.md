# Harbor task structure

A TB4 task is a Harbor task with a separate verifier. The verifier container runs after the agent container is torn down, so the agent cannot read or tamper with tests, the solution, or ground-truth data.

## Source shape

```
<task-slug>/
  instruction.md
  README.md
  task.toml
  environment/
    Dockerfile
  solution/
    solve.sh
  tests/
    Dockerfile
    test.sh
```

`check-task-slug`: the folder name is at most 3 hyphen-separated tokens, lowercase kebab-case. `wal-recovery` is legal. `fix-the-wal-recovery` is four tokens and is not.

The DFIR tree on pages 7–8 is an example, not a required file list. Extra files such as `environment/data/`, `solution/solve.py`, and `tests/test_outputs.py` are the usual way to meet the rules below. Copy the pattern when the task needs it. Do not copy those filenames into an unrelated task.

TB1/TB2 tasks were often a handful of files. A real TB4 task usually has more: input fixtures, a multi-file solution, and a real verifier image. Extra files of that kind are expected. “More than five files” does not mean a second task root, a hidden `.git` directory, a credential file, or a copy of the tests inside `environment/`.

## Separate verifier

In `task.toml`:

- `[verifier] environment_mode = "separate"`
- `artifacts = [...]` at the top level, not nested. The source’s example value is `artifacts = ["/app/"]`. In TOML, a key written after `[verifier]` becomes part of that table. Put `artifacts` before any `[table]` header.
- `tests/Dockerfile` copies the verifier into `/tests`.
- `tests/Dockerfile` pre-creates artifact parent directories with `RUN mkdir -p`.

`check-separate-verifier` fails the task if any of those are missing.

## Clean agent image

`environment/Dockerfile` does not copy `solution/solve.sh`, `tests/test.sh`, or `tests/test_*.py`. The broader rule on page 9 is that it must not copy `tests/` or `solution/` at all, and it must not contain test-only dependencies. Input fixtures the agent is supposed to see live under `environment/` and are copied in by the agent Dockerfile.

Ground truth used only by the grader belongs in the verifier image. That follows “the agent can never read ground-truth data,” together with rubric “Answer not leaked” and “Frozen ground truth.”

## Canary

SOP v3.0 §4.3 requires two Harbor canary comment lines at the top of every checked text file (`instruction.md`, `task.toml`, `environment/Dockerfile`, every text file under `solution/` and `tests/`). Markdown uses `<!-- ... -->`. TOML, Dockerfiles, shell, and Python use `#`. Skip binaries and `environment/data/` fixtures. Use `PRIVATE_PROPOSAL_CANARY_REPLACE_ME` unless a proposal-specific canary was issued. Do not invent a third value. Missing markers are advisory (`TB4.CANARY_*`), not blocking. There is no `canary_string` upload field. Page 8 includes the word `GUID` on line 1; page 21 omits it (`C-CANARY`). Skeletons follow §4.3.

## Task README

The task `README.md` (not this repository’s root README) must contain these headings exactly:

- `## Difficulty explanation`
- `## Solution explanation`
- `## Verification explanation`
- `## Relevant experience`

Missing or misspelled headings fail `tools/check_task.py`.

## Solution entry

The oracle entry point the source names is `solve.sh`. Preferred split when the logic is longer than about 20 lines: `solve.sh` launches `python3 /solution/solve.py`. Shorter solutions may stay in `solve.sh`. The 20-line split is the PDF’s preference, not a second entry point.
