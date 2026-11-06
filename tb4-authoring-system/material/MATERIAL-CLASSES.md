# Material classes

Four kinds of material. They are not four copies of the same rules. The rules stay in `00-source/` and the numbered lifecycle folders. These folders hold skeletons and private records.

| Class | Folder | Who may read it during a trial | In the submission ZIP |
| --- | --- | --- | --- |
| Reusable authoring guidance | `00-source/` through `16-evidence-and-handoff/`, plus `tools/` | The author and the authoring agent. Never the benchmark agent. | No |
| Private authoring evidence | `material/private-authoring/` and the per-task evidence directory created from it | The author, reviewers, and QC. Never the benchmark agent. | No |
| Agent-visible task material | `material/agent-visible/` | The benchmark agent, because it is copied into the agent image or given as `instruction.md`. | Yes |
| Verifier and reference solution | `material/verifier-and-solution/` | The oracle and the verifier container. The benchmark agent must not receive it. | Yes, beside the agent material, not inside the agent image |

## How a task directory is assembled

Copy into `tasks/<slug>/`:

- everything under `material/agent-visible/`
- everything under `material/verifier-and-solution/`

Leave `material/private-authoring/` outside that directory. The proposal, the decision log, the rubric review, Oracle and NOP transcripts, checksums, and platform receipts stay in `evidence/<slug>/`.

The resulting tree is what `tools/check_task.py` and `tools/package_task.py` read. This system folder is not a task and is not a ZIP.

## What the agent image may contain

`environment/Dockerfile` may copy `environment/data/` and other inputs the instruction names. It must not copy `tests/` or `solution/`. Ground truth used only by the grader is verifier material, even if a careless layout would put it next to the inputs.

`task.toml` is task configuration. It is part of the ZIP. Do not put the expected answer, the test internals, or a solution walkthrough into `instruction.md` even though `solution_explanation` and `verification_explanation` live in `task.toml`. Those explanation fields are metadata for review. They are not a second instruction.

## Canary lines in these skeletons

Skeletons include the two SOP v3.0 Harbor canary lines, using `PRIVATE_PROPOSAL_CANARY_REPLACE_ME` unless a proposal-specific value was issued. Do not invent a third value. Do not put markers in binary fixtures.
