# Ideation, novelty, realism, and feasibility

The authoring agent invents the task. It does not ask the user for an idea, a category, a subcategory, or a programming language. Comparison stays internal. The written result is `evidence/<slug>/selection.md`, produced by `SELECTION.md`.

Do this before drafting the proposal. The proposal is a compressed statement of a task that already has a verifiable outcome. It is not the place to discover the outcome.

## Novelty and duplicate risk

**Source.** The Proposal Review Bot runs duplicate and novelty checks. A red block despite a good rubric verdict can be “Duplicate detected — similarity above threshold.” Rework it into something genuinely distinct. The threshold number is not in the PDF (`U-DUPLICATE-THRESHOLD`). “Proposal rejected for novelty” means the idea is semantically the same as an existing task. Surface-level changes are not enough. The proposal’s sixth topic is one sentence on how the task differs from existing TB tasks and from obvious public problems.

**Practice.** The nearest public problem, the nearest Terminal-Bench-shaped problem, and the concrete difference in inputs, artifact, or failure mode go in `selection.md` as `nearest_public_problem` and `difference`. A renamed dataset, a swapped language, or a changed filename is a surface change. Do not invent a similarity percentage, and do not claim the bot will accept the difference.

## Realism

**Source.** Interesting: someone could be paid to do this, or a real group wants it solved. Obscure for its own sake does not count. Rubric E, real-world relevance: a realistic, valuable scenario someone would actually do, not a contrived puzzle. Page 7 prohibits a toy, a demo, a LeetCode-style problem, a math olympiad problem, and any task whose premise is “invent a hard problem to test the model.”

Review examples contain a “Client-fit note”: industrial purpose, not a toy, contest problem, or mathematical exercise. That note is observed reviewer practice in the PDF’s examples. It is not a seventh named proposal criterion. Do not add a “Client-fit” heading to the proposal.

## Feasibility

**Source.** Solvable: a solution exists, or a convincing argument one exists. An expert who already knows the answer can implement it in a few hours. The environment and inputs either already exist or the proposal says they must be built. The task must be achievable inside `[agent].timeout_sec` once that integer is chosen. The reference solution must pass every test.

**Practice.** `selection.md` records the graded artifact and whether the inputs are frozen or must be built. If the design needs a network fetch at verify time, or ground truth that only exists on the public web, reject that candidate. Those designs fail `check-trial-network-fetch` and the rubric’s “no shortcut via internet,” regardless of `C-INTERNET`. Do not write a separate feasibility essay.

The expert-time form field is the time to build the task, not the few hours in the Solvable criterion, and not the time spent writing the proposal (`C-EXPERT-TIME`). The meaning of `expert_time_estimate_hours` in `task.toml` is unresolved. State in the decision log which quantity you entered.

## Task shape that survives review

**Source.** One focused objective. Outcome-verified: the final state, not the route. No prescribed tools and no enumerated step lists. The anti-AI trap is named in the proposal: the naive approach an LLM tries first, and why it fails. The source’s examples of that trap are cross-source correlation, adversarial noise, and cascading errors.

**Practice.** Reject the idea, before any files exist, if the only way to make it hard is to hide a field, lengthen the instruction, or add clerical steps. Those repairs are forbidden later, and they are cheaper to refuse now.
