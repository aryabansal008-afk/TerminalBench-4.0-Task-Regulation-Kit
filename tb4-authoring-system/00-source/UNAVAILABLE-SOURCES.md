# Referenced but unavailable sources

These names appear in SOP v3.0 or its outline. Their text is not in the PDF. They are not conflicts, and they are not filled from memory or from the web. Audit date: 2026-11-06.

| ID | Name as printed | Where it is referenced | What this system does not do |
| --- | --- | --- | --- |
| U-TERMS | Terms of Use / Clickwrap Agreement | PDF outline, destination page `-1`. No body text. | Does not restate terms. The human accepts whatever the live platform presents. |
| U-AUTOMATION | `TASK_REVIEW_AUTOMATION.md` | Page 31: the task must pass the pipeline defined in that file. | Does not reconstruct the file. The six bullets printed under the sentence are the only local text. `C-FOUR-CRITERIA` is about those bullets, not about unseen sections of the file. |
| U-HARBOR-PIN | “the pinned Harbor version” | Page 10, G02. No version identifier. | Does not name a Harbor release, image tag, or schema version. |
| U-DUPLICATE-THRESHOLD | “similarity above threshold” | Page 26, duplicate troubleshooting. No number. | Does not invent a similarity percentage. |
| U-CTRF-FLAG | “pytest with CTRF output” | Page 9. No flag, plugin, or report path. | Does not invent a pytest argument. The command that is actually run is recorded after it is known. |
| U-LANGUAGE-FIELD | Programming language, locked at creation | Page 26. The proposal form’s five fields do not include it. | Does not invent the field name. The authoring agent chooses the language in `selection.md` and records the control the UI actually shows, or that no control appeared. |
| U-66 | “rough numbers out of 66 total tasks” | Page 30. No distribution table. | Does not invent per-category counts out of 66. Printed quotas stay the 20% cap and one task per deprioritized subcategory. |
| U-GITHUB | Link text `github` inside taxonomy cells | Pages 28–29. No URL in the text layer. | Does not guess the repository. |
| U-TAGS | “categories and tags used across TB4” | Pages 9, 19, and 28. Subcategories are listed. A separate tag enum is not. | Does not publish an official tag list. `tags` must still be non-empty because `check-task-fields` requires the field. |
| U-CANARY-FORMAT | GUID-token spelling | §4.3 versus p.21 | Does not invent a third format. Skeletons follow §4.3. |
| U-SCHEMA | Keys required by `HARBOR.SCHEMA_VERSION_NONCANONICAL` and `HARBOR.TASK_CONFIG_INVALID` | Pages 10–11. The failing key names are not listed. | Does not add schema keys the PDF does not name. |
| U-SUBCATEGORY-KEY | Subcategory as TB4 metadata | Page 10 G02 requires a subcategory. `check-task-fields` does not list the key. | Does not assert that the toml key is spelled `subcategory`. The template uses that spelling because it is the form’s label. That spelling is provisional until a live schema error names the key. |
| U-IMAGES-RCA | `IMAGES R / C / A` | Pages 5–6 screenshots. Examples are `0 / 0 / 0`. The letters are not defined. | Does not invent image quotas. |
| U-SEVERITY-ALIGNMENT | Per-rule REQUIRED / OPTIONAL badges in the Stage 1 screenshots | Pages 12–13. The badge column could not be reliably aligned to rule rows. | Does not publish a severity matrix. Page 11’s three severity classes still apply as prose. A rule name containing `ADVISORY` is advisory by that prose, not by a badge reading. |
| U-NET-CONFIG | “supported network configuration” | pp. 1–2 change table | Does not invent a TOML key. |
| U-ADMIN-POLICY | Onboarding HR / integrity procedures | Not in the 32-page text layer | Does not invent inactivity, appeal, or off-boarding rules. |
| U-SUPER-QC | “Super QC (a second, expert layer)” | Page 2 change table. No criteria. | Does not write a Super QC rubric. `C-QC-LAYERS` still requires the layer after QC. |
| U-POLICY-DIGEST | A policy digest hash, `effort high`, `K=8` | Page 15 screenshot, under the frozen policy. | Does not copy the sample hash into a task and does not treat effort or K as author settings. |
| U-EXPERT-EMAIL-DOMAIN | Owner addresses on the dashboard screenshot | Page 2. No rule requires that domain. | Does not copy the sample addresses. `author_email` is the author’s own address. |
| U-ZIP-ROOT | “a single candidate root” | Page 10 G01; p.2 publication-name row allows wrapping or flat. | `package_task.py --layout wrapped` is the default. `--layout flat` is also allowed. |

`UNRESOLVED.md` repeats the gaps that also appear as register rows. This file is the list of missing sources. The conflict register does not cite anything in this table as evidence for a `SUPERSEDED` status.
