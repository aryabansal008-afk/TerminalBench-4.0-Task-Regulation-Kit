# Selecting the task, category, subcategory, and language

The authoring agent makes these choices. It does not ask the user for a category, a subcategory, a programming language, or a task idea. It does the comparison internally. The only record is `evidence/<slug>/selection.md`, filled from `material/private-authoring/selection.md`. That file is a decision and its justification. It is not a transcript of private reasoning.

No category in this system is a default. The skeletons leave `category` and `subcategory` as `REPLACE_ME`. The examples in `01-taxonomy-and-batch/TAXONOMY.md` show what a subcategory means. They are not candidate tasks, and they are not copied into `instruction.md`, the proposal, or the fixtures.

## What is immutable

**Source.** Page 26: once a task is created, its category and programming language cannot be changed. Category and subcategory are stored on every revision, and the reviewer reads both. The proposal form’s five fields do not include a language field (`U-LANGUAGE-FIELD`). Do not invent a `task.toml` key for language.

**Practice.** Write `selection.md` before the platform task is created. After creation, do not try to repair a wrong category or a wrong language with a later ZIP. Subcategory is not in that lock sentence. Do not assume a later revision can change it, and do not assume it is frozen, until the UI shows which. The language the agent chose is what gets entered if a language control appears. Record that control’s visible label. If the form has no language control, write `language_control: not shown`. Keep the chosen language in `selection.md` either way.

## Explore the taxonomy

Read every category and every listed subcategory in `01-taxonomy-and-batch/TAXONOMY.md` before generating candidates. The set is:

- Software: Systems, Algorithms, Frontend, Data engineering, Databases
- ML: Inference, Evaluation, Training, Kernels
- Security: Cryptography, Forensics, AppSec
- Hardware: CAD, RTL
- Science: Biology, Chemistry, Physics, Earth, Robotics, Math, Linguistics
- Operations: Finance, Logistics, Supply chain, Claims, Compliance, Marketing
- Media: Music, Design

A custom subcategory is allowed only when no listed one fits, and it must be broad and reusable. Prefer a listed subcategory when one fits.

## Known batch constraints and missing batch context

The quotas are in `01-taxonomy-and-batch/BATCH.md`. They are not restated here.

**Known, and applied only when delivered counts are in hand.** The 20% category cap, the instruction not to concentrate Software and Science, and one delivered task per subcategory in Science, Operations, and Media. Count delivered tasks, not dead proposals. Release-composition remarks and the unprinted “out of 66” figures are not quotas (`U-66`).

**Missing, when no delivered-count record is available.** Current category fractions, which deprioritized subcategory slots are filled, and the batch size. Write `batch_context: missing`. Do not treat a missing count as zero, and do not treat it as full. Do not drop Software, or any other category, to satisfy a concentration rule you cannot compute. Do not fill a deprioritized slot just because its category is deprioritized. Selection then uses fit, feasibility, novelty, and realism. Say which checks were not applied.

**Supplied, when `evidence/<slug>/batch-slot.md` or a batch owner’s count file lists delivered tasks.** Apply every quota in `BATCH.md` that those counts make computable. Reject a candidate that would break one. If the account UI shows a creation or submission quota, copy that figure into the record. `C-ACCOUNT-LIMITS` stays unresolved: total submissions `1 (account-wide)` and task creation limit `2` are both printed. Do not ask the user to pick a different category because of that conflict. If the UI shows nothing, write `account_quota: not visible`. Before creating a second platform task, do not assume either cell.

## Compare candidates

Generate several realistic candidates across more than one category. Keep the comparison internal. For each candidate, judge:

| Test | Passes when |
| --- | --- |
| Fit | The closest listed subcategory in `TAXONOMY.md` describes this task. The title, category, and body will name the same task. |
| Feasibility | The graded artifact is named. Inputs can be frozen in the images, or the proposal will say they must be built. An expert who knows the answer can implement it in a few hours. Grading does not need a verify-time fetch or a public-web answer. |
| Novelty | The difference from the nearest public problem and from the nearest Terminal-Bench-shaped problem is a change in inputs, artifact, or failure mode. A renamed dataset, a swapped language, or a changed filename fails. The similarity threshold is unknown (`U-DUPLICATE-THRESHOLD`). |
| Distribution | Every computable quota in `BATCH.md` still holds if this candidate is delivered. Missing counts are not used as a reason to prefer a category. |
| Realism | Someone could be paid to do this. It is not a toy, a demo, a contest problem, an olympiad problem, or a task whose premise is to invent a hard problem. |

Reject a candidate whose only path to difficulty is hiding a field, lengthening the instruction, or adding clerical steps.

## What `selection.md` contains

One block, filled in. No discarded drafts and no step-by-step deliberation.

- `category` and `subcategory`. If custom, one sentence on why no listed subcategory fits.
- `programming_language`, chosen because the task needs it.
- `task_identity`: one sentence naming the graded artifact and the work.
- `fit`: the taxonomy sentence this subcategory matches.
- `nearest_public_problem` and `difference`.
- `artifact` and `inputs` (frozen, or must be built).
- `batch_context`: `missing` or `supplied`, and one sentence. If supplied, the category fraction after this task.
- `not_selected`: each other candidate as category, subcategory, one line, and one reason (`fit`, `feasibility`, `novelty`, or the named quota).
- `immutable_recorded_before_creation`: `yes`, written before the platform task exists.

The proposal is drafted from this block. A material change to the artifact, the inputs, or the graded conditions after an `ACTIVE` grant is a new task, not a quiet edit.

Do not write, in this file or in the proposal, that the task is difficult or long-horizon because the idea sounds complex. Those are measured properties. Construction is `03-difficulty-and-horizon/GENUINE-COMPLEXITY.md`. Proposed targets, local measurements, and platform verdicts stay in separate blocks of `complexity.md`.
