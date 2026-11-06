# Local agent trials and measured evidence

**Source.** Dry-run on a free or open-source agent before spending platform trials. The source asks for a signal that the task is solvable, the instruction is clear, it is not trivially easy, and the trajectory is long. Page 18 names this dry-run in the author checklist.

The frontier measurement is Stage 2, not the dry-run. Stage 2 predicates and the acceptance ceilings are both recorded and are not collapsed (`03-difficulty-and-horizon/DESIGN.md`). The author does not set `effort high` or `K=8`. Those are properties of the frozen policy. Do not copy the sample policy digest into a task (`U-POLICY-DIGEST`).

**Practice.** In `evidence/<slug>/dry-run.md` record the model name, the date, whether the run finished inside the provisional `timeout_sec`, the assistant-message count if the runner exposes it, and the reward token. Copy those figures into the local-measurement block of `complexity.md`. Do not also write them into the platform-verdict block.

A local open model that finishes in a handful of turns is a local signal the task is too easy or too short. Strengthen it under `03-difficulty-and-horizon/GENUINE-COMPLEXITY.md` before upload. A local open model that fails is not evidence that `count_true(full_credit_boolean) ≤ 4` will hold, and it is not evidence that the median will exceed 35. Do not write either claim. Sounding complex is not a measurement.

Do not pad the trajectory to move a count. Page 15 forbids busywork. If the local transcript shows the agent guessing a format the instruction never stated, fix the contract in `05-instruction/INSTRUCTION.md` and update the coverage table. Do not add a hint.

Platform trajectories, when a human is allowed to download them, go in the evidence pack as `stage2-trajectories/`. They are not ZIP members. Use them to tell hardness from ambiguity. Do not “fix” ambiguity by hiding information.
