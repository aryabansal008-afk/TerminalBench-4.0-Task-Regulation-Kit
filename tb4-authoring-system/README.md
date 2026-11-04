# TB4 / Thanos task-authoring system

Reusable system for designing, building, validating, and packaging Terminal-Bench 4 tasks. It encodes the 26-page source `Freelancers | Thanos | Guidelines`. This folder does not contain a benchmark task.

The numbered folders follow the lifecycle. The PDF’s rules are stated once, in the file the requirements register points at. Other files cite that file. A paragraph marked Practice is an engineering recommendation. It does not add a source requirement and it does not decide an unresolved conflict.

## Read this first

1. [AGENTS.md](AGENTS.md) — operating rules for an authoring agent.
2. [00-source/HOW-TO-READ.md](00-source/HOW-TO-READ.md) — source versus practice, obligation classes, and where a rule lives.
3. [00-source/CONFLICT-REGISTER.md](00-source/CONFLICT-REGISTER.md) — both sides of each conflict. A later page is not a repeal.
4. [00-source/REGISTER.md](00-source/REGISTER.md) — every extracted requirement. The same rows are in `REGISTER.csv`.
5. [material/MATERIAL-CLASSES.md](material/MATERIAL-CLASSES.md) — what the benchmark agent may see, what the verifier may see, and what stays private.
6. [13-packaging/ARCHIVE-MEMBERSHIP.md](13-packaging/ARCHIVE-MEMBERSHIP.md) — what is inside the submission ZIP.
7. [17-conversation-flow/START-FRESH.md](17-conversation-flow/START-FRESH.md) — how to start a task in a new conversation, stage by stage, including a folder-coverage table.
8. [17-conversation-flow/BUILD-ZIP.md](17-conversation-flow/BUILD-ZIP.md) — how to turn a completed tree into a ZIP, including a folder-coverage table.
9. [17-conversation-flow/TRACEABILITY.md](17-conversation-flow/TRACEABILITY.md) — requirement prefix to guidance file, checkpoint, artifact, and evidence.

## Lifecycle

| Folder | Responsibility |
| --- | --- |
| `00-source/` | Inventory, interpretation, the register, conflicts, unavailable documents, platform rule catalog. |
| `01-taxonomy-and-batch/` | Categories, subcategories, and batch distribution. |
| `02-ideation/` | The agent explores the full taxonomy, compares candidates, and records the category, subcategory, language, and task. It does not ask the user. |
| `03-difficulty-and-horizon/` | Genuine complexity, and the separate records for proposed targets, local measurements, and platform verdicts. The two numeric ceilings stay unresolved. |
| `04-proposal/` | Fields, length, review, grant, frozen scope. |
| `05-instruction/` | The agent-facing contract and the timeout suffix. |
| `06-harbor-task/` | Layout, metadata, resources, timeouts. |
| `07-agent-environment/` | Agent image, fixtures, dependencies, reproducible builds. |
| `08-reference-solution/` | Reference solution and independent ground truth. |
| `09-verifier/` | Separate verifier, artifact transfer, grading, rewards. |
| `10-checks-and-coverage/` | Static checks, all 30 rubric criteria, requirement-to-test coverage. |
| `11-validation/` | Oracle, NOP, negative cases, adversarial attempts, reward hacking. |
| `12-local-trials/` | Local agent trials and what they do not prove. |
| `13-packaging/` | Archive membership, immutable versions, checksums. |
| `14-platform-review/` | Stage 1, Stage 2, QC, and the printed acceptance bullets. |
| `15-revision/` | Diagnosis, change impact, revalidation. |
| `16-evidence-and-handoff/` | Evidence records, human gates, handoffs, upload readiness. |
| `17-conversation-flow/` | What to attach in a fresh Grok conversation, how to resume, and how to review before packaging. |

## Material that is not guidance

| Folder | Class | In the ZIP |
| --- | --- | --- |
| `material/agent-visible/` | Instruction, `task.toml`, agent image | Yes |
| `material/verifier-and-solution/` | `solution/` and `tests/` | Yes, and not inside the agent image |
| `material/private-authoring/` | Proposal skeleton, decision log, compliance report | No |
| `tools/` | Local preflight and packaging | No |

Assemble each task at `tasks/<slug>/`. Keep that task’s evidence at `evidence/<slug>/`. Write a finished ZIP to `tasks/<slug>.zip`, beside the tree, not inside it. `tools/check_task.py` and `tools/package_task.py` read the assembled tree. They do not replace Harbor or the platform.

No document outside the PDF was used to settle a rule. Names the PDF cites and does not contain are in `00-source/UNAVAILABLE-SOURCES.md`.
