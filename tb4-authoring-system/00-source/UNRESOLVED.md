# Unresolved items

Numeric and terminology conflicts are decided only in `CONFLICT-REGISTER.md`. This file is the older gap list. Sources that are named and missing are listed again, with the rule that they were not consulted, in `UNAVAILABLE-SOURCES.md`.

These are gaps in the PDF. Do not fill them with a plausible Harbor convention. Each one is also a register row.

| ID | What is missing | Where the source points | Agent action |
| --- | --- | --- | --- |
| U-TERMS | Terms of Use / Clickwrap Agreement. Outline entry points at page `-1`. | PDF outline only | Do not invent terms. The human accepts the live clickwrap. |
| U-AUTOMATION | `TASK_REVIEW_AUTOMATION.md` is not in the PDF. | p.25 | Follow the six bullets printed under that sentence. Do not fetch or assume the rest of the file. |
| U-HARBOR-PIN | “the pinned Harbor version” is required by G02 and not identified. | p.9 | Use the version the platform documents at upload time. Record the version in the evidence pack. |
| U-DUPLICATE-THRESHOLD | Duplicate block is “similarity above threshold.” No number. | p.20 | Do not target a similarity score. Make the proposal’s “why it is distinct” sentence specific. |
| U-CTRF-FLAG | “pytest with CTRF output.” No flag, plugin, or report path. | p.8 | Do not invent a pytest flag, plugin, or report path. Leave the command `NOT VERIFIED` until the pinned Harbor version or a receipt names it. Record that command after it is known. |
| U-LANGUAGE-FIELD | Category and programming language are locked at creation. The proposal form’s five fields do not include a language field. | p.20 | The authoring agent chooses the language in `selection.md` before creation. When the form is open, record the control’s visible label, or `not shown`. Do not invent the field name. Do not ask the user. |
| U-66 | “The distributions are just rough numbers out of 66 total tasks.” No table of those numbers is printed. | p.24 | Enforce only the quotas that are printed: 20% category cap, and 1 task per subcategory in Science, Operations, and Media. |
| U-GITHUB | Taxonomy cells contain the link text `github` with no URL in the text layer. | pp. 22–23 | Do not guess the repository. |
| U-TAGS | `tags` is required. The source says to cover “categories and tags used across TB4” and then lists categories and subcategories, not a separate tag enum. | pp. 8, 15, 22 | Use non-empty tags that name the subcategory and the real techniques. Do not invent an official enum. |
| U-CANARY-FORMAT | UI rule `TB3.CANARY_FORMAT`. No format is specified. Page 1 says no canary is issued. | pp. 1, 10–11 | See `C-CANARY`. Do not mint a format. |
| U-SCHEMA | Extra Harbor / `task.toml` keys required by `HARBOR.SCHEMA_VERSION_NONCANONICAL` and `HARBOR.TASK_CONFIG_INVALID`. | pp. 9–11 | Add a key only when the pinned Harbor version or a live rejection names it. |
| U-SUBCATEGORY-KEY | G02 requires a valid subcategory. `check-task-fields` lists `category` and `tags` but not `subcategory`. | pp. 9, 15 | Write `subcategory = "..."` at the top level of `task.toml` because that is the form’s field name. If the live schema wants a different key, follow the rejection text. |
| U-IMAGES-RCA | Review receipt shows `IMAGES R / C / A`. The examples are `0 / 0 / 0`. The letters are not defined. | pp. 5–6 screenshots | Archive the receipt. Do not invent image requirements. |
| U-SEVERITY-ALIGNMENT | Stage 1 screenshots show a severity word beside rules, but the columns cannot be reliably paired from the image. | pp. 10–11 | Use the p.9 severity model and the rule name. Do not publish a guessed REQUIRED/OPTIONAL matrix. |
| U-SECOND-MODEL | “both difficulty columns” and “both turn-count columns” with only one printed column. | p.25 | See `C-MISSING-COLUMNS`. |
| U-FOUR | “all four criteria” with six pipeline bullets. | p.26 | See `C-FOUR-CRITERIA`. |
| U-REUPLOAD-COUNTER | 7 in the table, 3 in the prose. | pp. 16, 19–21 | See `C-REUPLOADS`. |
| U-TOTAL-SUBMISSIONS | `1 (account-wide)` beside a creation limit of 2 tasks. | p.20 | Same conflict as `C-ACCOUNT-LIMITS`. Unresolved. |
| U-ZIP-ROOT | Single candidate root, directory shape not specified. | p.9 G01; pp. 6–7 example | The packager writes one top-level slug directory. That shape is provisional. See `13-packaging/ARCHIVE-MEMBERSHIP.md`. |
| U-STAGE3 | Stage 3 exists and is marked `DEFERRED`. Its criteria are not listed. | screenshots pp. 5, 10, 11, 13 | Do not mark Stage 3 passed. Continue the stages the source says to run. |
| U-SUPER-QC | “QC review and then Super QC (a second, expert layer).” No criteria. | p.2 | Prepare the evidence pack so a second reviewer can re-check the rubric without asking for missing files. |
| U-POLICY-DIGEST | Screenshot shows a policy digest hash and `effort high`, `K=8`. These describe the frozen policy. They are not author-set knobs. | p.13 | Do not copy the sample hash into a task. Do not try to set effort or K. |
| U-EXPERT-EMAIL-DOMAIN | Dashboard owners look like `@experts.ru` under `stlabs.ai`. No authoring rule requires that domain. | p.2 screenshot | Use the author’s real `author_email`. Do not copy the sample addresses. |

## Observed UI strings that are examples, not quotas

The p.2 dashboard shows sample tasks and custom subcategories (`RTL`, `Physics`, `Rail Yard Operations`, `Distributed Training Systems`, `Cryptography`). Custom subcategory text is allowed by p.3. Those task titles are not tasks to reproduce. `Cryptography` appears under `Science` in that screenshot and under `Security` in the taxonomy table. Follow the taxonomy table, not the screenshot’s category chip.
