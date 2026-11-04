# Static checks

Static checks are fast, deterministic, and need no API key and no LLM. They do not judge whether the task is good or hard. Run them locally before every upload. The platform runs them too. A local failure costs nothing. A failure after upload costs a version (`C-REUPLOADS`).

The introductory sentence on page 15 says static checks catch “a missing canary.” The table has no canary check. That disagreement is `C-CANARY`, which is unresolved. Do not add a canary to satisfy the introductory sentence, and do not treat the table’s silence as proof the platform will not ask for one.

| Check | What it enforces | Where the rule is applied |
| --- | --- | --- |
| `check-dockerfile-references` | Agent Dockerfile does not copy `solution/solve.sh`, `tests/test.sh`, or `tests/test_*.py`. | `07-agent-environment/ENVIRONMENT.md` |
| `check-dockerfile-sanity` | Apt is unpinned. `apt-get update` before install. `rm -rf /var/lib/apt/lists/*` after. | `07-agent-environment/ENVIRONMENT.md` |
| `check-dockerfile-platform` | No `FROM --platform=...`. | `07-agent-environment/ENVIRONMENT.md` |
| `check-task-absolute-path` | Absolute paths in the instruction. | `05-instruction/INSTRUCTION.md` |
| `check-test-file-references` | Every output file referenced by both tests and solution is documented in `instruction.md` or `task.toml`. | `09-verifier/VERIFIER.md` |
| `check-test-sh-sanity` | `uv venv`, or system-wide Python documented. | `09-verifier/VERIFIER.md` |
| `check-task-fields` | `author_name`, `author_email`, `difficulty_explanation`, `solution_explanation`, `verification_explanation`, `category`, `tags`, `expert_time_estimate_hours`. | `06-harbor-task/METADATA.md` |
| `check-task-timeout` | Both `timeout_sec` values ≤ `18000`. The 8-hour acceptance phrase is `C-TIMEOUT`. | `06-harbor-task/METADATA.md` |
| `check-instruction-suffix` | Exact timeout line, own paragraph, single trailing newline, `N` = `[agent].timeout_sec`. | `05-instruction/INSTRUCTION.md` |
| `check-gpu-types` | If present: `T4`, `L4`, `A10`, `L40S`, `A100-40GB`, `A100-80GB`, `H100`, `H200`, `B200`, or `any`. | `06-harbor-task/METADATA.md` |
| `check-task-slug` | At most 3 hyphen-separated lowercase kebab tokens. | `06-harbor-task/LAYOUT.md` |
| `check-allow-internet` | Do not set `[environment].allow_internet = false`. | `C-INTERNET` |
| `check-separate-verifier` | `environment_mode = "separate"`, top-level `artifacts`, `tests/Dockerfile` copies into `/tests`, `RUN mkdir -p`. | `06-harbor-task/LAYOUT.md` |
| `check-trial-network-fetch` | `tests/test.sh` does not fetch at verify time. | `09-verifier/VERIFIER.md` |
| `check-pip-pinning` | `pip` / `uv pip` / `uvx` / `uv tool` use `==`, with the exceptions in the environment file. | `07-agent-environment/ENVIRONMENT.md` |
| `check-nproc` | No bare `nproc`. | `07-agent-environment/ENVIRONMENT.md` |
| `check-ai-prompt-sanitization` | Prompts do not leak the solution or hidden data. | `08-reference-solution/SOLUTION.md` |

`tools/check_task.py` implements a mechanical subset. It is a preflight, not Harbor and not the platform. Passing it does not mark G06 passed. G06’s prose is the platform’s package-quality gate over this same surface. `HARBOR.DEPRECATED_ALLOW_INTERNET`, `DOCKERFILE.REFERENCE`, and `TRIAL.PUBLIC_FETCH` are platform-side siblings visible in the Stage 1 screenshots. The full screenshot catalog is `00-source/PLATFORM-RULE-CATALOG.md`.
