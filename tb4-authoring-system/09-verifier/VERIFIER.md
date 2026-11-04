# Separate verifier, artifacts, grading, reporting, and rewards

The verifier runs in its own container after the agent container is gone. Construction rules that overlap the task layout are in `06-harbor-task/LAYOUT.md`. This file is the grading contract.

## Artifact transfer

**Source.** Top-level `artifacts` lists the directories the agent is required to produce. The source’s example is `artifacts = ["/app/"]`. `tests/Dockerfile` pre-creates those parents with `RUN mkdir -p`. The verifier then sees the agent’s outputs. It does not see the agent’s process, and the agent does not see the verifier.

**Practice.** Grade files under the declared artifact roots only. If a test reads a path outside `artifacts` and outside `/tests`, record why Harbor still presents that path. Do not invent a transfer flag the PDF does not name.

## Deterministic grading

**Source.**

- Execute the agent’s output and check it. Avoid grep-for-keywords tests. They are gameable.
- Outcome-based: the final output or artifact, not the specific steps or method.
- No LLM-as-judge. No fuzzy matching that could pass a wrong answer or fail a right one.
- Full required output: every field and the edge cases, not a happy-path subset.
- A do-nothing attempt fails. A partial attempt fails. The obvious naive approach fails.
- If the instruction does not name a condition, do not grade it. If you grade it, the instruction must state it.

## Reward

**Source.** Write the reward to `/logs/verifier/reward.txt`. On pass write `1.0`. On fail write `0.0`. Always write the file, including when pytest fails. A missing file is `HARBOR.REWARD_NOT_FOUND`. An empty file is `HARBOR.REWARD_EMPTY`. Two tokens or a sentence is `HARBOR.REWARD_AMBIGUOUS` or `HARBOR.REWARD_PARSE`.

Local NOP command: `harbor run --path . --agent nop`. Expected result: 100% fail, reward `0.0`. G05 says NOP must not score 1.0. A partial NOP reward sits between those sentences (`C-REWARD-LITERAL`). Local authoring still follows the local table: Oracle `1.0`, NOP `0.0`. That does not decide whether `NOP.PARTIAL_REWARD` rejects the task. Screenshot severity badges were not reliably column-aligned (`U-SEVERITY-ALIGNMENT`).

`test.sh` runs pytest with CTRF output. The flag and report path are not in the PDF (`U-CTRF-FLAG`). Record the exact command once the pinned Harbor version is known. Do not invent the flag.

## Verifier image and test.sh

**Source.**

- `COPY` the tests into `/tests`.
- `RUN mkdir -p` for artifact parents and for `/logs/verifier`.
- Pre-install every grader dependency with pins.
- `tests/test.sh` must not run `apt-get install`, `pip install`, `curl | sh`, `wget | sh`, or `git clone` of an external URL (`check-trial-network-fetch`).
- `check-test-sh-sanity`: isolate Python with `uv venv`, or document system-wide Python in `task.toml` or `instruction.md`. Creating the venv at verify time is the isolation step. Installing packages into it at verify time is the forbidden step. `uv` itself is baked into the verifier image.

## Reporting

**Source.** The platform’s rubric command is named `harbor check`. Arguments are not given. Record the arguments the pinned Harbor version accepts (`U-HARBOR-PIN`).

**Practice.** The reward file is the machine-readable result. A human-readable note of which assertions failed belongs in the private evidence pack, not in a file the agent can write in order to influence the grade.
