# Metadata, resources, and timeouts

Empty defaults fail checks. Fill every required field with a statement that is true of this task.

## Fields `check-task-fields` names

`author_name`, `author_email`, `difficulty_explanation`, `solution_explanation`, `verification_explanation`, `category`, `tags`, `expert_time_estimate_hours`.

G02 also requires a subcategory and `[verifier] environment_mode = "separate"`. Category must be one of the seven form names. `category` and the programming language are locked at creation. Both were chosen in `selection.md` before the platform task existed. Do not ask the user, and do not change them in a later ZIP.

## Publication name

SOP v3.0 requires:

```
[task]
name = "terminal-bench/<slug>"
```

The slug is the task directory name, at most three hyphen-separated lowercase tokens. A wrapping ZIP directory must match that slug. Flat ZIPs are allowed (`tools/package_task.py --layout flat`).

## Timeouts

```
[agent]
timeout_sec = 28800

[verifier]
timeout_sec = <M>
```

**Source.** SOP v3.0 requires `[agent].timeout_sec = 28800` exactly, and the instruction footer must state 28800 seconds. `check-task-timeout` caps both fields at 28800s. The same check still says this leaves headroom under a 6-hour CI job (`C-TIMEOUT`). Do not copy 28800 onto `[verifier].timeout_sec` unless the verifier actually needs that budget. `M` must be a positive integer ≤ 28800 and long enough to grade. Do not write any `[agent]` timeout other than 28800.

`PROFILE.TIMEOUT_ADVISORY` and `PROFILE.TIMEOUT_ENVELOPE_UNSUPPORTED` are platform checks on the envelope. The PDF does not say what envelope they accept.

## Environment keys the source names

- Do not set `[environment].allow_internet = false` while following `check-allow-internet`. Do not invent the unnamed “supported network configuration” key (`U-NET-CONFIG`). `C-INTERNET`: the change table requires public agent access; G02 still says non-public; the verifier stays isolated and must not fetch at verify time.
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

`U-SCHEMA`. Do not add `schema_version` or a language field until a rejection message names that key. `[task] name` is required by SOP v3.0. `HARBOR.SCHEMA_VERSION_NONCANONICAL` and `HARBOR.TASK_CONFIG_INVALID` are the platform errors when the schema is wrong.
