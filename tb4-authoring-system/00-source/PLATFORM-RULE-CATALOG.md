# Platform rule catalog

Normative gate behavior is the prose on pp. 9–11. The rule IDs below are the IDs visible in the Stage 1 screenshots on pp. 10–11. They are platform-controlled. This catalog is not a claim that the screenshot lists every rule the platform will ever run.

Confidence:

- `prose` — the PDF text states the behavior or the exact ID.
- `screenshot` — the ID is legible in both the clean and the rejected screenshots, or legible once and consistent with the gate’s prose. Spelling is normalized (`ORACLE.REWARD_BELOW_FULL`, not the OCR miss).
- `screenshot-single` — seen clearly on one screenshot only. Treat the ID as real but re-read the live log before writing a fixer that depends on the exact string.

Severity badges are not copied into this catalog. See `U-SEVERITY-ALIGNMENT`. Names containing `ADVISORY` are advisory by the naming rule on p.9. Compose rules are the source’s example of `IF APPLICABLE`.

Header facts that are in the screenshots and the prose:

- Tabs: `Stage 0 • Task proposal`, `Stage 1 • Static checks`, `Stage 2 • Model rollout`, `Stage 3 • Qualitative checks` with badge `DEFERRED`.
- Pass banner: `READY_FOR_STAGE2`. The clean example shows `1:12 ELAPSED`, `5 artifacts bound • 2 warnings`, `All gates passed`, `6` gates passed, `94` rules passed, `2` warnings.
- Fail banner on the example: `NOT_READY`, `Stopped at G05`.
- A warning count greater than zero can still be `READY_FOR_STAGE2`.

## I01 Upload snapshot

Prose: binds the immutable upload generation and SHA-256 snapshot of the ZIP before anything reads it.

| Phase or rule | Kind | Confidence |
| --- | --- | --- |
| `UPLOAD_SNAPSHOT` | phase | screenshot |
| `SNAPSHOT.UNREADABLE` | rule | screenshot |
| `SNAPSHOT.MUTATING` | rule | screenshot |

## G01 Archive safety

Prose: exact ZIP inventory, safe extract, and a single candidate root. Catches path traversal, absolute paths, symlinks, encrypted members, CRC mismatches, archive bombs, and multiple or zero task roots.

| Phase or rule | Kind | Confidence |
| --- | --- | --- |
| `ZIP_INVENTORY` | phase | screenshot |
| `STREAM_READ` | phase | screenshot |
| `MATERIALIZE` | phase | screenshot |
| `CANDIDATE_ROOT` | phase | screenshot |
| `ZIP.UNREADABLE` | rule | screenshot |
| `ZIP.UNSUPPORTED_COMPRESSION` | rule | screenshot |
| `ZIP.ENCRYPTED_MEMBER` | rule | screenshot |
| `ZIP.TOO_LARGE` | rule | screenshot |
| `ZIP.EXPANDED_TOO_LARGE` | rule | screenshot |
| `ZIP.TOO_MANY_MEMBERS` | rule | screenshot |
| `ZIP.MEMBER_TOO_LARGE` | rule | screenshot |
| `ZIP.COMPRESSION_RATIO` | rule | screenshot |
| `ZIP.PATH_TRAVERSAL` | rule | screenshot |
| `ZIP.ABSOLUTE_PATH` | rule | screenshot |
| `ZIP.CRC_MISMATCH` | rule | screenshot |
| `ZIP.SYMLINK` | rule | screenshot |
| `ZIP.SPECIAL_MEMBER` | rule | screenshot |
| `ZIP.NUL_PATH` | rule | screenshot |
| `ZIP.NORMALIZATION_COLLISION` | rule | screenshot |
| `ZIP.INCOMPLETE_READ` | rule | screenshot |
| `ZIP.EXTRACTION_FAILED` | rule | screenshot |
| `ZIP.INVALID_RECORDS` | rule | screenshot |
| `META.EXCLUDED` | rule | screenshot |
| `ROOT.ZERO_CANDIDATES` | rule | screenshot |
| `ROOT.MULTIPLE_CANDIDATES` | rule | screenshot |

`ZIP.ABSOLUTE_PATH` is about members inside the archive. `check-task-absolute-path` is about paths written in the instruction. They are different checks.

## G02 Harbor + TB4 contract

Prose name: `Harbor + TB4 contract`. Screenshot label: `Harbor + TB3`. See `C-TB3-LABEL`.

Prose checks: Harbor layout parses under the pinned Harbor version; required paths present and readable; TB4 metadata valid (category, subcategory, required fields); agent networking non-public; verifier isolation declared.

| Phase or rule | Kind | Confidence |
| --- | --- | --- |
| `HARBOR_PARSE` | phase | screenshot |
| `REQUIRED_PATHS` | phase | screenshot |
| `TB3_POLICY` | phase | screenshot |
| `CAPABILITY_PREFLIGHT` | phase | screenshot |
| `HARBOR.PARSE_INTEGRATION` | rule | screenshot |
| `TB3.NO_TASK_ROOT` | rule | screenshot |
| `TB3.CATEGORY_INVALID` | rule | screenshot |
| `TB3.METADATA_MISSING` | rule | screenshot |
| `TB3.CANARY_MISSING` | rule | screenshot |
| `TB3.CANARY_ADVISORY` | rule | screenshot |
| `TB3.AUTHORING_ADVISORY` | rule | screenshot |
| `HARBOR.DEPRECATED_ALLOW_INTERNET` | rule | screenshot |
| `HARBOR.SCHEMA_VERSION_NONCANONICAL` | rule | screenshot |
| `HARBOR.TASK_CONFIG_INVALID` | rule | screenshot |
| `PACKAGE.EXTRA_CONTENT_ADVISORY` | rule | screenshot |
| `PACKAGE.REQUIRED_FILE_MISSING` | rule | screenshot |
| `PACKAGE.REQUIRED_FILE_UNREADABLE` | rule | screenshot |
| `PROFILE.TIMEOUT_ADVISORY` | rule | screenshot |
| `TB3.AGENT_NETWORK_NONPUBLIC` | rule | screenshot |
| `TB3.CANARY_FORMAT` | rule | screenshot |
| `TB3.SUBCATEGORY_INVALID` | rule | screenshot |
| `TB3.VERIFIER_ISOLATION_REQUIRED` | rule | screenshot |

Canary rules are governed by `C-CANARY`, not by this table alone.

## G03 Static execution safety

Prose: no hidden runtime, credentials, or network reach-out. Credential scanning, Compose dependency and provenance scanning, host binds, privileged containers, host networking, devices, packaged-file mutation, Dockerfile references, and verifier fetch patterns.

| Phase or rule | Kind | Confidence |
| --- | --- | --- |
| `CREDENTIAL_SCAN` | phase | screenshot |
| `COMPOSE_DEPENDENCY_SCAN` | phase | screenshot |
| `COMPOSE_RESOLVE` | phase | screenshot |
| `STATIC_POLICY` | phase | screenshot |
| `COMPOSE.HOST_BIND` | rule | screenshot |
| `COMPOSE.TYPE_BIND` | rule | screenshot-single |
| `COMPOSE.RESOURCE_ENVELOPE_BYPASS` | rule | screenshot |
| `COMPOSE.MAIN_BUILD_MISSING` | rule | screenshot |
| `COMPOSE.PRIVILEGED` | rule | screenshot |
| `COMPOSE.NETWORK_HOST` | rule | screenshot |
| `COMPOSE.DEVICE` | rule | screenshot |
| `COMPOSE.PACKAGED_FILE_MUTATION` | rule | screenshot |
| `COMPOSE.RESOLVE_FAILED` | rule | screenshot |
| `COMPOSE.INVALID` | rule | screenshot |
| `COMPOSE.DEPENDENCY_ESCAPE` | rule | screenshot |
| `CREDENTIAL.CONFIRMED` | rule | screenshot |
| `CREDENTIAL.SUSPECTED` | rule | screenshot |
| `DOCKERFILE.REFERENCE` | rule | screenshot |
| `TRIAL.PUBLIC_FETCH` | rule | screenshot |
| `POLICY.COVERAGE` | rule | screenshot |
| `STATIC.ADVISORY` | rule | screenshot |

Compose rows are conditional. A task with no Compose file still has to pass credential, Dockerfile-reference, and verifier-fetch rules.

## G04 Environment readiness

Prose: Harbor can build and start the declared image and Compose environment and reach bound agent-setup evidence. Unsupported profiles, accelerators, prebuilt images, and timeout envelopes fail here.

| Phase or rule | Kind | Confidence |
| --- | --- | --- |
| `AGENT_ENV_BUILD` | phase | screenshot |
| `AGENT_ENV_START` | phase | screenshot |
| `AGENT_ENV_READINESS` | phase | screenshot |
| `HARBOR.START_BLOCKED` | rule | screenshot |
| `HARBOR.RUNTIME_ERROR` | rule | screenshot |
| `HARBOR.ENV_START_TIMEOUT` | rule | screenshot |
| `HARBOR.NO_AGENT_SETUP` | rule | screenshot |
| `HARBOR.RESULT_MISSING` | rule | screenshot |
| `PROFILE.ACCELERATOR_UNSUPPORTED` | rule | prose and screenshot |
| `PROFILE.MULTI_STEP_UNSUPPORTED` | rule | screenshot |
| `PROFILE.PREBUILT_IMAGE_UNSUPPORTED` | rule | screenshot |
| `PROFILE.TIMEOUT_ENVELOPE_UNSUPPORTED` | rule | screenshot |

`G04.PROFILE.ACCELERATOR_UNSUPPORTED` is the prose’s example of `Stage 1 could not complete — retry`, not a reason to rewrite the task until the declared profile is wrong.

## G05 Verifier controls

Prose: Oracle and NOP run as one Harbor job. Oracle must score 1.0 and exit cleanly. NOP must not score 1.0. Reward must be found, parseable, unambiguous, and finite. “This is where most real task defects surface.”

| Phase or rule | Kind | Confidence |
| --- | --- | --- |
| `ORACLE_AGENT_EXECUTION` | phase | screenshot |
| `ORACLE_VERIFIER_START` | phase | screenshot |
| `ORACLE_VERIFIER_EXECUTION` | phase | screenshot |
| `NOP_AGENT_EXECUTION` | phase | screenshot |
| `NOP_VERIFIER_START` | phase | screenshot |
| `NOP_VERIFIER_EXECUTION` | phase | screenshot |
| `RUNTIME_EVIDENCE_BIND` | phase | screenshot |
| `ORACLE.NONZERO_EXIT` | rule | screenshot |
| `ORACLE.REWARD_BELOW_FULL` | rule | prose and screenshot |
| `NOP.FULL_REWARD` | rule | screenshot |
| `NOP.PARTIAL_REWARD` | rule | screenshot |
| `HARBOR.NONZERO_AGENT_EXIT_ANOMALY` | rule | screenshot |
| `HARBOR.AGENT_TIMEOUT_ORACLE` | rule | screenshot |
| `HARBOR.AGENT_TIMEOUT_ANOMALY` | rule | screenshot |
| `HARBOR.VERIFIER_TIMEOUT` | rule | screenshot |
| `HARBOR.REWARD_NOT_FOUND` | rule | screenshot |
| `HARBOR.REWARD_EMPTY` | rule | screenshot |
| `HARBOR.REWARD_PARSE` | rule | screenshot |
| `HARBOR.VALIDATION_ERROR` | rule | screenshot |
| `HARBOR.REWARD_INVALID` | rule | screenshot |
| `HARBOR.REWARD_AMBIGUOUS` | rule | screenshot |
| `HARBOR.CANCELLED` | rule | screenshot |
| `HARBOR.AGENT_SETUP_TIMEOUT` | rule | screenshot |
| `HARBOR.UNKNOWN_EXCEPTION` | rule | prose and screenshot |
| `HARBOR.OOM` | rule | screenshot |
| `HARBOR.RESULT_MISSING` | rule | screenshot |
| `ARTIFACT.COLLECTION_FAILED` | rule | screenshot |

Prose examples of “could not complete”: `G05.HARBOR.UNKNOWN_EXCEPTION`, and also OOM, eviction, cancellation, unsupported accelerator profile. Those are retries, not automatic rewrites. `G05.ORACLE.REWARD_BELOW_FULL` is the prose’s example of a task defect.

## G06 Package quality

Prose: “Static package quality - instruction, tests, mapping, and related criteria.” The screenshot does not expand a distinct G06 rule list separate from the package rules shown under G02 (`PACKAGE.*`). No additional G06-only IDs were legible.

## P04 Final publication barrier

Prose: binds this ZIP, its receipt, and its artifacts. Sanitises output, closes hashes, persists the result, and publishes the admission — or stops.

| Phase or rule | Kind | Confidence |
| --- | --- | --- |
| `SANITIZE_OUTPUT` | phase | screenshot |
| `HASH_CLOSURE` | phase | screenshot |
| `PERSIST_RESULT` | phase | screenshot |
| `PUBLISH_ADMISSION` | phase | screenshot |
| `REDACTION.INCOMPLETE` | rule | screenshot |
| `METADATA.UNAVAILABLE` | rule | screenshot |
| `HASH_CLOSURE.FAILED` | rule | screenshot |
| `PUBLICATION.FAILED` | rule | screenshot |
| `NOT_REACHED` | rule | screenshot |
| `RUNTIME_TUPLE.UNAVAILABLE` | rule | screenshot |
| `PLATFORM.UNKNOWN_EVIDENCE` | rule | screenshot |
| `PLATFORM.UNKNOWN_EXCEPTION` | rule | screenshot |

`NOT_REACHED` means an earlier gate stopped the job. Fix the earlier gate. Do not treat P04 as the cause.

## How to triage a Stage 1 row

1. Read the rule the UI names in the Blocking reason column. The source says it tells you what the rule enforces, what happened, and the fix.
2. If the outcome is `Stage 1 could not complete — retry`, check the declared profile and re-run. Do not rewrite the task to satisfy an invented defect. The platform “fails closed rather than inventing a task defect.”
3. If the outcome is `Stage 1 rejected — upload a corrected ZIP`, fix locally, re-run static checks and Oracle/NOP, then upload a new immutable version.
4. Only one fully green version reaches Stage 2. Partial credit across versions does not count.
5. Use the durable event log at the bottom of the Stage 1 tab for phase order.

## Stage 2 identifiers confirmed on the p.13 screenshot

These match the prose and are not author-editable:

- Flow: `QUEUED → PREPARING → RUNNING → COLLECTING → CLOSING → COMPLETE`
- `1 MODEL • 8 ROLLOUTS REQUIRED`
- Model label: `Anonymous model`
- `messages • effort high • K=8`
- `policy FROZEN`
- Predicates: `count_true(full_credit_boolean) ≤ 2` and `median(assistant_message_count) > 80`
- Overall verdict values include `PASS`, `FAIL`, and, when the population is incomplete, `INDETERMINATE`
- Blocked example state: `RUNNER_EXECUTION_FAILED`, “Blocked with 0 of 8 rollouts reconciled.”
- “Platform on-call. No rollout can reconcile and no predicate can move until the blocker clears.”
- “If a provider attempt is active when Stop is forced, the missing trustworthy grade makes this run noncanonical rather than retryable.”

The author does not press Stop to improve a score. Stopping can make the run noncanonical.
