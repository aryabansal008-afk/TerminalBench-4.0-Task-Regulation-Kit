# Unresolved items

Numeric and terminology conflicts are decided only in `CONFLICT-REGISTER.md`. Sources named and missing are in `UNAVAILABLE-SOURCES.md`. Pages below are SOP v3.0.

These are gaps in the PDF. Do not fill them with a plausible Harbor convention. Each one is also a register row.

| ID | What is missing | Where the source points | Agent action |
| --- | --- | --- | --- |
| U-TERMS | Terms of Use / Clickwrap Agreement. Outline entry points at page `-1`. | PDF outline only | Do not invent terms. The human accepts the live clickwrap. |
| U-AUTOMATION | `TASK_REVIEW_AUTOMATION.md` is not in the PDF. | p.31 | Follow the six bullets printed under that sentence. |
| U-HARBOR-PIN | “the pinned Harbor version” is required by G02 and not identified. | p.10 | Use the version the platform documents at upload time. |
| U-DUPLICATE-THRESHOLD | Duplicate block is “similarity above threshold.” No number. | p.26 | Do not target a similarity score. |
| U-CTRF-FLAG | “pytest with CTRF output.” No flag, plugin, or report path. | p.9 | Do not invent a pytest flag. Leave the command `NOT VERIFIED` until named. |
| U-LANGUAGE-FIELD | Category and programming language are locked at creation. The proposal form’s five fields do not include a language field. | p.26 | Choose language in `selection.md`. Record the UI label or `not shown`. |
| U-66 | “rough numbers out of 66 total tasks.” No table. | p.30 | Enforce only printed quotas: 20% cap, one task per deprioritized subcategory. |
| U-GITHUB | Taxonomy cells contain the link text `github` with no URL. | pp. 28–29 | Do not guess the repository. |
| U-TAGS | `tags` is required. No official tag enum. | pp. 9, 19, 28 | Non-empty tags naming subcategory and techniques. |
| U-CANARY-FORMAT | §4.3 includes `GUID` on line 1; p.21 omits `GUID`. | pp. 8–9, 21 | Skeletons follow §4.3. Checker accepts both documented forms. |
| U-SCHEMA | Extra keys for `HARBOR.SCHEMA_VERSION_NONCANONICAL` / `HARBOR.TASK_CONFIG_INVALID`. | pp. 10–11 | Add a key only when a rejection names it. `[task] name` is required by v3.0. |
| U-SUBCATEGORY-KEY | G02 requires subcategory. `check-task-fields` lists `category` and `tags` but not `subcategory`. | pp. 10, 19 | Write top-level `subcategory`. Follow a live schema error if it names another key. |
| U-IMAGES-RCA | `IMAGES R / C / A` undefined. | pp. 5–6 screenshots | Archive the receipt. |
| U-SEVERITY-ALIGNMENT | Screenshot severity column not reliably paired. | pp. 11–12 | Use p.11 severity classes. |
| U-SECOND-MODEL | “both difficulty columns” / “both turn-count columns” with one printed column. | p.31 | See `C-MISSING-COLUMNS`. |
| U-FOUR | “all four criteria” with six pipeline bullets. | p.32 | See `C-FOUR-CRITERIA`. |
| U-REUPLOAD-COUNTER | Table 7 versus leftover “three reuploads” / “3 versions.” | pp. 20, 26–27 | See `C-REUPLOADS`. Workflow uses 7. |
| U-TOTAL-SUBMISSIONS | `1 (account-wide)` beside creation limit 2. | p.26 | See `C-ACCOUNT-LIMITS`. |
| U-ZIP-ROOT | Single candidate root; wrapping vs flat both allowed in the change table. | p.10 G01; p.2 #10; pp. 7–8 example | Packager supports `--layout wrapped` (default) and `flat`. |
| U-NET-CONFIG | “supported network configuration” unnamed. | pp. 1–2 | Do not invent the key. See `C-INTERNET`. |
| U-ADMIN-POLICY | Ownership, inactivity, off-boarding, appeals, integrity procedures | Not in the SOP v3.0 text layer | Do not invent administrative enforcement. |
| U-SUPER-QC | Super QC named; no criteria. | p.2 | Evidence pack must let a second reviewer re-grade the rubric. |
| U-POLICY-DIGEST | Policy digest, `effort high`, `K=8` | p.15 screenshot | Not author-set knobs. |
| U-EXPERT-EMAIL-DOMAIN | Sample `@experts.ru` owners | p.2 screenshot | Use the author’s real `author_email`. |

## Observed UI strings that are examples, not quotas

The dashboard screenshot shows sample tasks and custom subcategories. Custom subcategory text is allowed by p.4. Those titles are not tasks to reproduce. Follow the taxonomy table on pp. 28–30, not a screenshot category chip.
