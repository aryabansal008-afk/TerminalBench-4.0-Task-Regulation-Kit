# Referenced but unavailable sources

These names appear in the PDF or its outline. Their text is not in the PDF. They are not conflicts, and they are not filled from memory or from the web. No external source was consulted for the conflict register. Audit date: 2026-11-03.

| ID | Name as printed | Where it is referenced | What this system does not do |
| --- | --- | --- | --- |
| U-TERMS | Terms of Use / Clickwrap Agreement | PDF outline, destination page `-1`. No body text. | Does not restate terms. The human accepts whatever the live platform presents. |
| U-AUTOMATION | `TASK_REVIEW_AUTOMATION.md` | Page 25: the task must pass the pipeline defined in that file. | Does not reconstruct the file. The six bullets printed under the sentence are the only local text. `C-FOUR-CRITERIA` is about those bullets, not about unseen sections of the file. |
| U-HARBOR-PIN | “the pinned Harbor version” | Page 9, G02. No version identifier. | Does not name a Harbor release, image tag, or schema version. |
| U-DUPLICATE-THRESHOLD | “similarity above threshold” | Page 20, duplicate troubleshooting. No number. | Does not invent a similarity percentage. |
| U-CTRF-FLAG | “pytest with CTRF output” | Page 8. No flag, plugin, or report path. | Does not invent a pytest argument. The command that is actually run is recorded after it is known. |
| U-LANGUAGE-FIELD | Programming language, locked at creation | Page 20. The proposal form’s five fields do not include it. | Does not invent the field name. The authoring agent chooses the language in `selection.md` and records the control the UI actually shows, or that no control appeared. |
| U-66 | “rough numbers out of 66 total tasks” | Page 24. No distribution table. | Does not invent per-category counts out of 66. Printed quotas stay the 20% cap and one task per deprioritized subcategory. |
| U-GITHUB | Link text `github` inside taxonomy cells | Pages 22–23. No URL in the text layer. | Does not guess the repository. |
| U-TAGS | “categories and tags used across TB4” | Pages 8, 15, and 22. Subcategories are listed. A separate tag enum is not. | Does not publish an official tag list. `tags` must still be non-empty because `check-task-fields` requires the field. |
| U-CANARY-FORMAT | `TB3.CANARY_FORMAT` | Pages 10–11 screenshots. No format. Page 1 says nothing issues a canary. | Does not mint a format. See `C-CANARY`. |
| U-SCHEMA | Keys required by `HARBOR.SCHEMA_VERSION_NONCANONICAL` and `HARBOR.TASK_CONFIG_INVALID` | Pages 9–11. The failing key names are not listed. | Does not add schema keys the PDF does not name. |
| U-SUBCATEGORY-KEY | Subcategory as TB4 metadata | Page 9 G02 requires a subcategory. `check-task-fields` does not list the key. | Does not assert that the toml key is spelled `subcategory`. The template uses that spelling because it is the form’s label. That spelling is provisional until a live schema error names the key. |
| U-IMAGES-RCA | `IMAGES R / C / A` | Pages 5–6 screenshots. Examples are `0 / 0 / 0`. The letters are not defined. | Does not invent image quotas. |
| U-SEVERITY-ALIGNMENT | Per-rule REQUIRED / OPTIONAL badges in the Stage 1 screenshots | Pages 10–11. The badge column could not be reliably aligned to rule rows. | Does not publish a severity matrix. Page 9’s three severity classes still apply as prose. A rule name containing `ADVISORY` is advisory by that prose, not by a badge reading. |
| U-STAGE3 | `Stage 3 • Qualitative checks` | Screenshots, badge `DEFERRED`. No criteria. | Does not list Stage 3 checks or mark the tab passed. See `C-LEGACY-CARDS`. |
| U-SUPER-QC | “Super QC (a second, expert layer)” | Page 2 change table. No criteria. | Does not write a Super QC rubric. `C-QC-LAYERS` still requires the layer after QC. |
| U-POLICY-DIGEST | A policy digest hash, `effort high`, `K=8` | Page 13 screenshot, under the frozen policy. | Does not copy the sample hash into a task and does not treat effort or K as author settings. |
| U-EXPERT-EMAIL-DOMAIN | Owner addresses on the dashboard screenshot | Page 2. No rule requires that domain. | Does not copy the sample addresses. `author_email` is the author’s own address. |
| U-ZIP-ROOT | “a single candidate root” | Page 9, G01. The example tree is `tasks/<task-name>/`. The ZIP’s top-level shape is not stated. | Does not claim that one top-level slug directory is the required shape. `tools/package_task.py` writes that shape as a **provisional** pack. If G01 rejects it, the receipt decides the next shape. The provisional pack is not a resolution. |

`UNRESOLVED.md` repeats the gaps that also appear as register rows. This file is the list of missing sources. The conflict register does not cite anything in this table as evidence for a `SUPERSEDED` status.
