# Batch distribution

Source quotas, pages 22–24. One author does not satisfy the batch alone. The batch owner keeps the running counts. `C-ACCOUNT-LIMITS` is unresolved: the same table says total submissions `1 (account-wide)` and task creation limit `2`. Whether one account can create a second task is not decided here. Quote the live quota.

## Source quotas

- No single category may exceed 20% of the delivered batch.
- Do not concentrate the batch in Software and Science.
- Operations, Hardware, Security, Media, and ML are in scope on equal footing, subject to the 20% cap.
- Science, Operations, and Media are deprioritized this round: 1 task for each subcategory in those categories, so the bench covers more of the official taxonomy without displacing the Software / ML / Security / Hardware focus.

## What is not a quota

“The distributions are just rough numbers out of 66 total tasks.” The numbers are not printed (`U-66`). Do not invent a 66-row quota. Remarks such as “largest subcategory in the release” describe the official bench. They are not freelancer targets. The printed quotas are the 20% cap, the instruction not to concentrate Software and Science, and one task per deprioritized subcategory.

## Counting, and what is missing

**Source.** Count platform tasks that are actually delivered, not proposals that died.

**Practice.** Delivered counts are known only when a batch record lists them. The authoring agent then applies the quotas above and writes the category, subcategory, and resulting fraction in `evidence/<slug>/batch-slot.md`.

When no delivered-count record exists, batch context is missing. Do not invent the current fractions, do not treat every slot as empty, and do not treat every slot as full. Do not reserve a favorite category. `02-ideation/SELECTION.md` says which checks are skipped, and the selection record says `batch_context: missing`. A later batch owner can still apply the cap. This file does not name a preferred category.

Page 7: difficulty, turn count, category distribution, and instruction style must all align with Terminal-Bench 3/4. Use this file, `TAXONOMY.md`, `05-instruction/INSTRUCTION.md`, and `03-difficulty-and-horizon/DESIGN.md`. Do not import a TB1 category list. The TB3 label on the taxonomy versus TB4 prose is `C-TB3-LABEL` and is unresolved. Follow the category spellings printed in this PDF.
