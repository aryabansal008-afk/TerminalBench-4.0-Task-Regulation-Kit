# Metadata, resources, and timeouts

Empty defaults fail checks. Fill every required field with a statement that is true of this task.

## Fields `check-task-fields` names

`author_name`, `author_email`, `difficulty_explanation`, `solution_explanation`, `verification_explanation`, `category`, `tags`, `expert_time_estimate_hours`.

G02 also requires a subcategory and `[verifier] environment_mode = "separate"`. Category must be one of the seven form names. `category` and the programming language are locked at creation. Both were chosen in `selection.md` before the platform task existed. Do not ask the user, and do not change them in a later ZIP.

## Timeouts

```
[agent]
timeout_sec = <N>

[verifier]
timeout_sec = <M>
```

**Source.** `check-task-timeout` caps both at `18000` seconds (5 hours), “leaving headroom under the CI runner's 6-hour job limit.” The acceptance page states a rollout “timeout limit 8 hrs.” `C-TIMEOUT` is unresolved. Any integer written here is a provisional human choice. The instruction suffix uses the same integer as `[agent].timeout_sec` because `check-instruction-suffix` says so. `M` must be long enough for the verifier, not for the agent’s exploration. Do not describe 18000 as the resolved timeout, and do not copy 8 hours into the field as if the cap had been repealed.

`PROFILE.TIMEOUT_ADVISORY` and `PROFILE.TIMEOUT_ENVELOPE_UNSUPPORTED` are platform checks on the envelope. The PDF does not say what envelope they accept.

## Environment keys the source names

- Do not set `[environment].allow_internet = false` while following `check-allow-internet`. That is provisional. `C-INTERNET` is unresolved, and leaving the key unset is not a finding that networking is non-public.
- `[environment].cpus` is the value to use instead of bare `nproc`.
- `gpu_types`, only if the task needs a GPU. Canonical strings: `T4`, `L4`, `A10`, `L40S`, `A100-40GB`, `A100-80GB`, `H100`, `H200`, `B200`, or `any`.
- GPU training tasks: a single `H100`. Do not request a second GPU.

Rubric E, sensible resources: CPU, memory, storage, and timeouts are appropriate — not wastefully large, not too tight to solve. The PDF does not print numeric CPU or memory defaults beyond `cpus` as the replacement for `nproc`.

## Explanations

- `difficulty_explanation` names the real source of hardness, not trivia or guess-the-format. State which quantity `expert_time_estimate_hours` measures (`C-EXPERT-TIME`).
- `solution_explanation` describes the reference approach. Do not copy it into `instruction.md`.
- `verification_explanation` states that grading is deterministic and outcome-based, and names the artifact.
- `tags` is a non-empty list. There is no official tag enum in the PDF (`U-TAGS`).

## Keys this PDF does not specify

`U-SCHEMA`. Do not add `schema_version`, a canary field, or a language field until a rejection message names that key. `HARBOR.SCHEMA_VERSION_NONCANONICAL` and `HARBOR.TASK_CONFIG_INVALID` are the platform errors when the schema is wrong.
