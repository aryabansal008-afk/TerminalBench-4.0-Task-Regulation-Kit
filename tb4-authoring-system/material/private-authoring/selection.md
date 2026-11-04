# Selection

The authoring agent fills this before the platform task is created. Do not ask the user for a category, subcategory, programming language, or task idea. Do not paste a reasoning transcript. Do not copy a taxonomy example into these fields.

Status values: `NOT STARTED`, `IN PROGRESS`, `PASS`, `FAIL`, `BLOCKED`, `NOT VERIFIED`, `NOT APPLICABLE`. Do not mark this record `PASS` because the idea sounds difficult.

```
record_status: NOT STARTED
category:
subcategory:
custom_subcategory_reason:
programming_language:
task_identity:
fit:
nearest_public_problem:
difference:
artifact:
inputs:
batch_context:
batch_note:
account_quota:
language_control:
not_selected:
immutable_recorded_before_creation:
```

`batch_context` is `missing` or `supplied`. `account_quota` is the figure the UI shows, or `not visible`. `language_control` is the label of the control that was filled, or `not shown`. `not_selected` is one line per rejected candidate: category, subcategory, task identity, and one reason.
