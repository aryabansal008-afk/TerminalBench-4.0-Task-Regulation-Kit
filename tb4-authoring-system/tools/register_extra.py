import re

EXTRA = []

def add(*args):
    EXTRA.append(row(*args))

CHECKS = [
    ("check-dockerfile-references", "The agent Dockerfile does not copy solution/solve.sh, tests/test.sh, or tests/test_*.py into the image. The agent must never see the tests or solution.", "p.15"),
    ("check-dockerfile-sanity", "Apt packages are NOT pinned to versions. apt install is preceded by apt-get update and followed by rm -rf /var/lib/apt/lists/* cleanup.", "p.15"),
    ("check-dockerfile-platform", "No Dockerfile hardcodes a CPU architecture via FROM --platform=..., so the task runs on x86-64 or arm64 without slow emulation.", "p.15"),
    ("check-task-absolute-path", "Instructions use absolute paths (example /app/data.csv), never relative ones (data.csv).", "p.15"),
    ("check-test-file-references", "Every output file referenced by both the tests and the solution is documented in instruction.md or task.toml.", "p.15"),
    ("check-test-sh-sanity", "test.sh isolates Python using uv venv, or task.toml / instruction.md explicitly documents system-wide Python usage.", "p.15"),
    ("check-task-fields", "All required task.toml metadata is present: author_name, author_email, difficulty_explanation, solution_explanation, verification_explanation, category, tags, expert_time_estimate_hours.", "p.15"),
    ("check-task-timeout", "[agent] and [verifier] timeout_sec are capped at 18000s (5 hours), leaving headroom under the CI runner's 6-hour job limit.", "p.16"),
    ("check-instruction-suffix", "instruction.md ends with the exact timeout / anti-cheat line, N equal to [agent].timeout_sec, as its own paragraph with a single trailing newline.", "p.16"),
    ("check-gpu-types", "Any gpu_types values are canonical Modal GPU strings: T4, L4, A10, L40S, A100-40GB, A100-80GB, H100, H200, B200, or any.", "p.16"),
    ("check-task-slug", "The task folder name is at most 3 hyphen-separated tokens, lowercase kebab-case.", "p.16"),
    ("check-allow-internet", "task.toml does not set [environment].allow_internet = false. Tasks run with open internet by default.", "p.16"),
    ("check-separate-verifier", 'The task is fully configured for separate verifier mode: environment_mode = "separate", artifacts declared at top level, tests/Dockerfile exists and COPYs into /tests, and artifact parent directories are pre-created with RUN mkdir -p.', "p.16"),
    ("check-trial-network-fetch", "tests/test.sh does not fetch external resources at verify time (no curl|sh / wget|sh installers, no external curl/wget, no git clone of external URLs). This is a known reward-hacking surface.", "p.16"),
    ("check-pip-pinning", "Every pip / uv pip / uvx / uv tool install pins an explicit ==<version>. Manifest (-r requirements.txt), local (-e . or .), pip self-upgrade, and VCS URLs with an @ref are allowed.", "p.16"),
    ("check-nproc", "No bare nproc. It returns the host CPU count inside a container, causing over-parallel OOM/timeouts. Use [environment].cpus or a fixed value instead.", "p.16"),
    ("check-ai-prompt-sanitization", "AI prompts do not leak the task solution or hidden data to the model.", "p.16"),
]
for name, text, page in CHECKS:
    risk = "None beyond a failed upload."
    if name == "check-allow-internet":
        risk = "C-INTERNET. G02 also says agent networking is non-public."
    if name == "check-task-timeout":
        risk = "C-TIMEOUT. The acceptance page says an 8-hour rollout limit, which is 28800s and would fail this cap if copied into timeout_sec."
    if name == "check-instruction-suffix":
        risk = "C-REWARD-LITERAL does not apply. A wrong N fails the check."
    add(
        f"REQ-SC-{name}",
        "conditional" if name == "check-gpu-types" else "mandatory",
        "task",
        "build,self-test,stage1",
        page,
        name,
        text,
        f"Local preflight plus the platform static runner. The local script approximates {name}.",
        "checker-report.txt; static-checks.txt",
        risk,
        "10-checks-and-coverage/STATIC-CHECKS.md",
    )

add("REQ-BD-026", "mandatory", "task", "build,self-test", "pp. 6–7 example; p.15 check-dockerfile-references", "Oracle entry point",
    "The oracle entry point is solution/solve.sh. The static check names that path specifically when it forbids copying it into the agent image. The preferred body of a long solution is solution/solve.py, launched by solve.sh with python3 /solution/solve.py.",
    "solution/solve.sh exists, is not copied into the agent image, and is what the local oracle run executes.",
    "solution/solve.sh; oracle.txt",
    "A solution that lives only in the agent image is visible to the agent and is not an oracle.",
    "09-verifier/VERIFIER.md")
add("REQ-SC-REUPLOAD-SENTENCE", "unresolved", "account", "package", "p.16 closing", "Static checks close",
    "Fixing a static-check failure after upload costs one of your three reuploads.",
    "Do not rely on this sentence or on the table value 7. Follow C-REUPLOADS.",
    "decision-log.md",
    "C-REUPLOADS. The limits table says 7.",
    "00-source/CONFLICT-REGISTER.md")

RUBRIC = [
    ("A", "Deterministic verification", "Verification is fully deterministic — no LLM-as-judge, no fuzzy matching that could pass wrong answers or fail right ones."),
    ("A", "Outcome-based grading", "Tests check the agent's final output / artifact, not the specific steps or method used to get there."),
    ("A", "Frozen ground truth", "Expected values come from frozen, in-image fixtures so results are reproducible and not time/network dependent."),
    ("A", "Complete coverage", "Tests cover the full required output (all fields, edge cases), not just a happy-path subset."),
    ("A", "Correct expected values", "The expected answers the tests assert are themselves correct (independently derived / verified)."),
    ("A", "Strict failure on no-op", "A do-nothing or partial attempt fails — the verifier is not lenient."),
    ("B", "Reference solution exists", "A correct reference solution is provided and passes all tests (Oracle = 1.0)."),
    ("B", "Solvable from instruction alone", "Everything needed to solve the task is in the instruction and environment — no external/hidden knowledge or missing inputs."),
    ("B", "Environment is self-contained", "All required tools, data, and dependencies are present in the container; the task does not rely on flaky external resources."),
    ("B", "Achievable in the time budget", "A capable agent can plausibly finish within [agent].timeout_sec."),
    ("B", "No ambiguity in the goal", "The success condition is unambiguous — there is one clearly correct interpretation of done."),
    ("B", "Output schema fully specified", "The exact output path, format, schema, ordering, and formatting are spelled out so a correct attempt is not failed on a guessable detail."),
    ("C", "Genuinely difficult", "The task is hard for a strong agent — not solvable by a trivial one-liner or obvious lookup."),
    ("C", "Non-trivial (NOP fails)", "Doing nothing, or an obvious naive approach, does not pass."),
    ("C", "Difficulty is legitimate", "Hardness comes from real reasoning/engineering, not from obscure trivia, trick wording, or guess-the-format."),
    ("C", "Resistant to reward hacking", "The agent cannot game the verifier (hardcoding expected values, writing to reward files, reading hidden tests/solution)."),
    ("C", "Answer not leaked", "The instruction, environment, and data do not reveal the expected answer or the test internals."),
    ("C", "No shortcut via internet", "The answer cannot simply be looked up online or copied from a public source."),
    ("D", "Clear and well-written", "The instruction is unambiguous, well-structured, and free of contradictions."),
    ("D", "No hidden hints or leakage", "The instruction does not hint at the solution method or leak verifier details."),
    ("D", "Absolute paths and concrete I/O", "All file paths are absolute and every required input/output is named explicitly."),
    ("D", "Required suffix present", "The instruction ends with the exact timeout / anti-cheat line matching the agent timeout."),
    ("D", "Self-consistent with tests", "What the instruction asks for is exactly what the tests check — no drift between statement and grading."),
    ("D", "Appropriately scoped", "The task is a focused, single objective — not a sprawling bundle of unrelated sub-tasks."),
    ("E", "Separate verifier configured", "Tests run in their own container after the agent; the agent image is clean (no tests/solution)."),
    ("E", "Dependencies pinned and baked", "All deps are version-pinned and pre-installed in the right image; no runtime installs at verify time."),
    ("E", "Sensible resources", "CPU / memory / storage / timeouts are appropriate — not wastefully large, not too tight to solve."),
    ("E", "Reproducible build", "The images build cleanly and deterministically on a fresh machine."),
    ("E", "Real-world relevance", "The task reflects a realistic, valuable scenario someone would actually do — not a contrived puzzle."),
    ("E", "Correct and complete metadata", "task.toml metadata (difficulty, solution, verification explanations, category, tags, time estimate) is filled in and accurate."),
]
for index, (group, name, text) in enumerate(RUBRIC, start=1):
    risk = "A FAIL uploaded anyway spends a version."
    if name == "Clear and well-written":
        risk = "C-HEADINGS. Well-structured does not mean ## headings."
    if name == "No shortcut via internet":
        risk = "C-INTERNET. Open internet by default does not make a public answer acceptable."
    slug = re.sub(r"[^a-z0-9]+", "-", name.lower()).strip("-")
    add(f"REQ-RB-{index:02d}", "mandatory", "task", "self-test,acceptance", "pp. 17–19",
        f"Group {group} — {name}", text,
        "Local rubric review records PASS with a justification tied to a file. Platform quality review, when it runs, agrees.",
        "rubric-review.md", risk, "10-checks-and-coverage/RUBRIC.md")

add("REQ-RB-LOCAL", "mandatory", "process", "self-test", "p.19 closing", "How to use the rubric locally",
    "Run the rubric review with a free / open-source LLM before uploading. Read each FAIL with its justification, fix the underlying issue, and re-run. The page says arriving already passing protects your 3 reuploads.",
    "The rubric report has no unexplained FAIL and predates the ZIP.",
    "rubric-review.md",
    "C-REUPLOADS. C-NINE-DIMENSIONS. There are 30 criteria here, not 9 named dimensions.",
    "10-checks-and-coverage/RUBRIC.md")

add("REQ-G-001", "platform", "platform", "package,stage1", "p.8 §5; p.5 screenshot", "Upload",
    "Upload Harbor task ZIP is inactive until an ACTIVE grant exists. The ZIP is immutable once uploaded: the platform binds its SHA-256 and an upload generation, and Stage 1 begins automatically.",
    "The archived SHA-256 matches the uploaded bytes. Stage 1 starts on that generation.",
    "sha256.txt; stage1.txt",
    "File hash already exists if the same bytes are uploaded again.",
    "14-platform-review/STAGE-1.md")
add("REQ-G-002", "platform", "platform", "stage1", "p.8 §5", "Stage 1 job",
    "Stage 1 is a sequenced job, not cards triggered one by one. It runs I01 (upload snapshot), gates G01 through G06, and then P04 (the publication barrier). A typical clean run finishes in well under a minute, most of it in G04 through G06.",
    "The event log shows that order. The author does not mark individual gates passed.",
    "stage1.txt",
    "NOT_REACHED on a later gate means an earlier gate stopped the job.",
    "00-source/PLATFORM-RULE-CATALOG.md")
add("REQ-G-003", "platform", "platform", "stage1", "p.9 §5.1", "I01",
    "I01 Upload snapshot binds the immutable upload generation and SHA-256 snapshot of the ZIP before anything reads it.",
    "The receipt shows the bound hash.", "stage1.txt", "SNAPSHOT.UNREADABLE or SNAPSHOT.MUTATING means the archive was not a stable snapshot.",
    "00-source/PLATFORM-RULE-CATALOG.md")
add("REQ-G-004", "platform", "task", "package,stage1", "p.9 §5.1", "G01",
    "G01 Archive safety: exact ZIP inventory, safe extract, and a single candidate root. It catches path traversal, absolute paths, symlinks, encrypted members, CRC mismatches, archive bombs, and multiple or zero task roots.",
    "The ZIP has one top-level directory, no symlinks, no absolute member names, and is not encrypted.",
    "sha256.txt; stage1.txt",
    "U-ZIP-ROOT. The exact top-level shape is unspecified beyond a single candidate root. The packager's single top-level directory is provisional.",
    "14-platform-review/STAGE-1.md")
add("REQ-G-005", "platform", "task", "stage1", "p.9 §5.1", "G02",
    "G02 Harbor + TB4 contract: Harbor layout parses under the pinned Harbor version; required paths are present and readable; TB4 metadata is valid (category, subcategory, required fields); agent networking is non-public; verifier isolation is declared.",
    "The layout matches the required tree and task.toml. The Harbor version is recorded when known.",
    "stage1.txt; task.toml",
    "C-TB3-LABEL. U-HARBOR-PIN. C-INTERNET. The screenshot labels this gate Harbor + TB3.",
    "00-source/PLATFORM-RULE-CATALOG.md")
add("REQ-G-006", "platform", "task", "stage1", "p.9 §5.1", "G03",
    "G03 Static execution safety: no hidden runtime, credentials, or network reach-out. It covers credential scanning, Compose dependency and provenance scanning, host binds, privileged containers, host networking, devices, packaged-file mutation, Dockerfile references, and verifier fetch patterns.",
    "No secrets, no privileged or host-network compose, no verifier fetch, no tests copied into the agent image.",
    "stage1.txt",
    "Compose rules are IF APPLICABLE.",
    "07-agent-environment/ENVIRONMENT.md")
add("REQ-G-007", "platform", "task", "stage1", "p.9 §5.1", "G04",
    "G04 Environment readiness: Harbor can build and start the declared image and Compose environment and reach bound agent-setup evidence. Unsupported profiles, accelerators, prebuilt images, and timeout envelopes fail here.",
    "A local image build succeeds from a clean context. The declared accelerator exists in the allowed profile.",
    "stage1.txt",
    "G04.PROFILE.ACCELERATOR_UNSUPPORTED is the prose's example of a retry, not an automatic rewrite.",
    "07-agent-environment/ENVIRONMENT.md")
add("REQ-G-008", "platform", "task", "stage1", "p.9 §5.1", "G05",
    "G05 Verifier controls: Oracle and NOP run as one Harbor job. Oracle must score 1.0 and exit cleanly. NOP must not score 1.0. The reward must be found, parseable, unambiguous, and finite. This is where most real task defects surface.",
    "Local Oracle shows reward 1.0 and local NOP shows reward 0.0, which is what section 4.4 requires of those commands. Whether a partial NOP reward fails Stage 1 is C-REWARD-LITERAL and is unresolved.",
    "oracle.txt; nop.txt; stage1.txt",
    "The prose's defect example is G05.ORACLE.REWARD_BELOW_FULL. G05.HARBOR.UNKNOWN_EXCEPTION is a retry example.",
    "09-verifier/VERIFIER.md")
add("REQ-G-009", "platform", "task", "stage1", "p.9 §5.1", "G06",
    "G06 Package quality: static package quality covering instruction, tests, mapping, and related criteria.",
    "The static-check table is clean. G06 is not marked passed from the local script alone.",
    "static-checks.txt; stage1.txt",
    "The screenshots do not show a separate G06 rule list beyond PACKAGE.* rules under G02.",
    "10-checks-and-coverage/STATIC-CHECKS.md")
add("REQ-G-010", "platform", "platform", "stage1", "p.9 §5.1", "P04",
    "P04 Final publication barrier binds this ZIP, its receipt, and its artifacts. It sanitises output, closes hashes, persists the result, and publishes the admission — or stops.",
    "P04 is read only after G01–G06. NOT_REACHED is traced to the earlier gate.",
    "stage1.txt",
    "A hash-closure or publication failure is platform-side unless the log says the ZIP changed.",
    "00-source/PLATFORM-RULE-CATALOG.md")
add("REQ-G-011", "mandatory", "platform", "stage1", "p.9 §5.1", "Severity model",
    "REQUIRED rejects the task, or for platform-side rules marks Stage 1 incomplete. OPTIONAL / ADVISORY does not reject; a run can read 'Stage 1 accepted · 2 warnings' and still be fine. IF APPLICABLE is evaluated only when the task uses the feature. Compose-specific rules are the source's example.",
    "A warning is archived and not treated as PASSED failing. A REQUIRED id is fixed or retried according to the outcome class.",
    "stage1.txt",
    "U-SEVERITY-ALIGNMENT. Do not invent a per-rule severity the screenshot does not reliably show.",
    "00-source/HOW-TO-READ.md")
add("REQ-G-012", "platform", "platform", "stage1", "p.9–10 §5.2", "Outcomes",
    "Stage 1 ends in exactly one of: 'Stage 1 accepted / PASSED STAGE 1 (READY_FOR_STAGE2)' when all gates passed; 'Stage 1 rejected — upload a corrected ZIP' when a REQUIRED rule found a defect; 'Stage 1 could not complete — retry' when the platform will not attribute the failure to the task.",
    "The archived outcome is one of those three strings, plus the blocking rule when present.",
    "stage1.txt",
    "The platform fails closed rather than inventing a task defect, so 'could not complete' is never a verdict on the work.",
    "14-platform-review/STAGE-1.md")
add("REQ-G-013", "platform", "platform", "stage1", "p.10 §5.2", "Named examples",
    "Blocking-reason example for a task defect: G05.ORACLE.REWARD_BELOW_FULL. Retry examples: G05.HARBOR.UNKNOWN_EXCEPTION and G04.PROFILE.ACCELERATOR_UNSUPPORTED, also Harbor anomaly, unclassified exception, OOM or eviction, cancellation, unsupported accelerator profile.",
    "Those ids are classified with the prose, not rewritten by habit.",
    "stage1.txt",
    "Rewriting a task because of UNKNOWN_EXCEPTION spends a version on a non-defect.",
    "14-platform-review/STAGE-1.md")
add("REQ-G-014", "mandatory", "process", "stage1", "p.11 §5.3", "Re-upload",
    "Open the failing gate and read the rule. Use the durable event log for phase order. Fix locally, re-run local static checks and Oracle/NOP, then upload a corrected ZIP. Only one thing reaches Stage 2: every gate green on a single version. Partial credit across versions does not count.",
    "The passing Stage 1 receipt is for one SHA-256, and the local Oracle/NOP for that tree predate it.",
    "stage1.txt; oracle.txt; nop.txt",
    "C-REUPLOADS.",
    "14-platform-review/STAGE-1.md")
add("REQ-G-015", "example", "platform", "stage1", "p.10 screenshot", "Clean Stage 1 illustration",
    "The clean screenshot shows READY_FOR_STAGE2, 6 gates passed, 94 rules passed, 2 warnings, 5 artifacts bound, elapsed 1:12, and Stage 3 Qualitative checks DEFERRED.",
    "These numbers are an illustration of one run, not quotas.",
    "stage1.txt",
    "Do not pad the task until a local counter reads 94.",
    "00-source/PLATFORM-RULE-CATALOG.md")

add("REQ-S2-001", "platform", "platform", "stage2", "p.12 §6", "Stage 2 flow",
    "Stage 2 moves QUEUED → PREPARING → RUNNING → COLLECTING → CLOSING → COMPLETE and can sit at 'Stage 2 running · waiting on provider'. The author does not drive it.",
    "The author does not mark Stage 2 passed while the status is waiting or indeterminate.",
    "stage2.txt",
    "Forcing Stop during an active provider attempt makes the run noncanonical rather than retryable.",
    "14-platform-review/STAGE-2.md")
add("REQ-S2-002", "platform", "platform", "stage2", "p.12 §6.1; p.13 screenshot", "Eight rollouts",
    "Stage 2 runs 8 rollouts under a frozen policy. Policy key and digest, capacity profile, and retention profile are recorded. The UI shows 1 MODEL • 8 ROLLOUTS REQUIRED, Anonymous model, messages, effort high, K=8, policy FROZEN.",
    "The receipt shows 8 of 8 reconciled on the frozen policy. The author does not set effort or K.",
    "stage2.txt",
    "U-POLICY-DIGEST. The sample hash in the screenshot is not a task field.",
    "14-platform-review/STAGE-2.md")
add("REQ-S2-003", "mandatory", "task", "stage2", "p.12 §6.2; p.13 screenshot", "difficulty predicate",
    "Predicate difficulty: count_true(full_credit_boolean) ≤ 2. At most 2 of the 8 rollouts may earn full credit. More than that and the task is too easy. UI: Required: ≤2.",
    "The observed value on the passing run is ≤ 2.",
    "stage2.txt",
    "C-DIFFICULTY is unresolved. Do not treat ≤2 as the acceptance pass rate, and do not treat 4/8 as a Stage 2 pass.",
    "03-difficulty-and-horizon/DESIGN.md")
add("REQ-S2-004", "mandatory", "task", "stage2", "p.12 §6.2; p.13 screenshot", "long_horizon predicate",
    "Predicate long_horizon: median(assistant_message_count) > 80. A median of about 48 turns fails this even when difficulty passes. UI label: Median assistant turns, Required: >80.",
    "The observed median on the passing run is greater than 80.",
    "stage2.txt",
    "C-HORIZON is unresolved. The acceptance page states a different statistic: more than 35 turns of all passing runs. Do not treat the median rule as that test.",
    "03-difficulty-and-horizon/DESIGN.md")
add("REQ-S2-005", "mandatory", "task", "stage2", "p.12 §6.2", "Both predicates",
    "Every predicate must hold. The overall verdict is PASS or FAIL, and the header names the predicate that sank it (example: Failed on long_horizon).",
    "A PASS receipt has both predicates true. A FAIL receipt names which one.",
    "stage2.txt",
    "Fixing one predicate usually moves the other. Re-check both before resubmitting.",
    "14-platform-review/STAGE-2.md")
add("REQ-S2-006", "mandatory", "task", "stage2", "p.13 §6.3", "Too easy",
    "If too many rollouts earn full credit, add depth: more cross-source correlation, more state that must stay consistent, stricter exactness in the output contract. Do not fix it by hiding information in the instruction.",
    "complexity.md names the page 13 move and the instruction sentence added with it. The coverage table gained a row for that sentence. No test asserts an unstated condition.",
    "complexity.md; instruction.md",
    "Hidden information fails Well-specified and Solvable from instruction alone. A task that sounds hard is not this row.",
    "03-difficulty-and-horizon/GENUINE-COMPLEXITY.md")
add("REQ-S2-007", "mandatory", "task", "stage2", "p.13 §6.3", "Too short",
    "If the median turn count is too low, add genuine sequential work: more components that must all hold together, and more recovery and boundary conditions the agent has to discover and handle. Padding with busywork does not survive the later review and will read as busywork.",
    "complexity.md names the new component or boundary condition and the instruction sentence that states it. The local-measurement block is re-run. The platform-verdict block is not filled from that rerun.",
    "complexity.md",
    "Busywork is a later-review failure even if a local transcript gets longer. Artificial turn inflation is not long horizon.",
    "03-difficulty-and-horizon/GENUINE-COMPLEXITY.md")
add("REQ-S2-008", "platform", "platform", "stage2", "p.13 screenshot", "Indeterminate",
    "A blocked rollout shows INDETERMINATE, population incomplete, and in the example RUNNER_EXECUTION_FAILED with 'Blocked with 0 of 8 rollouts reconciled. No predicate can move until the blocker clears.' Platform on-call unblocks it.",
    "Indeterminate is not recorded as a difficulty FAIL and the task is not rewritten for it.",
    "stage2.txt",
    "Pressing Stop while a provider attempt is active makes the run noncanonical rather than retryable.",
    "14-platform-review/STAGE-2.md")

add("REQ-LM-001", "unresolved", "account", "package", "p.20 limits table", "Reuploads",
    "The limits table sets Reuploads (new versions) per task to 7.",
    "Both 7 and 3 are recorded. C-REUPLOADS is unresolved. Do not upload a 4th through 7th version, and do not stop at 3, unless the live counter is quoted in the decision log.",
    "decision-log.md",
    "C-REUPLOADS. Prose in four places says 3.",
    "00-source/CONFLICT-REGISTER.md")
add("REQ-LM-002", "unresolved", "account", "proposal", "p.20 limits table", "Total submissions",
    "Total submissions is 1 (account-wide).",
    "Human gate before creating a task. The term submission is not defined.",
    "decision-log.md",
    "C-ACCOUNT-LIMITS is unresolved. The same table also says task creation limit 2. Do not treat either cell as the account quota.",
    "00-source/CONFLICT-REGISTER.md")
add("REQ-LM-003", "mandatory", "account", "package", "p.20 limits table", "Hourly evaluation limit",
    "Hourly evaluation limit: 2 unique versions.",
    "No third distinct ZIP is uploaded in the same hour.",
    "stage1.txt",
    "A unique version is a content change, not a re-click. Identical bytes fail with File hash already exists.",
    "14-platform-review/STAGE-1.md")
add("REQ-LM-004", "mandatory", "account", "package", "p.20 limits table", "Daily evaluation limit",
    "Daily evaluation limit: 5 unique versions.",
    "The day's uploads stay at or under 5 unique versions.",
    "stage1.txt",
    "Five mechanical failures exhaust the day.",
    "14-platform-review/STAGE-1.md")
add("REQ-LM-005", "unresolved", "account", "proposal", "p.20 limits table", "Task creation limit",
    "Task creation limit: 2 tasks.",
    "Before a second platform task, record the live quota if the UI shows it. Do not ask the user to choose a category or a task idea.",
    "decision-log.md",
    "C-ACCOUNT-LIMITS is unresolved. The same table also says total submissions 1 (account-wide).",
    "00-source/CONFLICT-REGISTER.md")
add("REQ-LM-006", "mandatory", "task", "proposal", "p.20", "Locked at creation",
    "Once a task is created you cannot change its category or programming language. Choose carefully.",
    "selection.md records category and programming language before the platform task exists. The agent chooses them and does not ask the user. U-LANGUAGE-FIELD: the proposal form's five fields do not include a language field, so the UI control's label is recorded when it appears, or as not shown.",
    "selection.md; proposal-receipt.txt",
    "A wrong category cannot be repaired by a later ZIP.",
    "02-ideation/SELECTION.md")
add("REQ-LM-007", "mandatory", "process", "package", "p.21", "Identical ZIP",
    "The error 'File hash already exists' means the identical ZIP was uploaded again. Make a real change first.",
    "A new upload has a new SHA-256 and a real content change.",
    "sha256.txt",
    "Touching a comment only to change the hash, without fixing the defect, fails again and spends a version.",
    "14-platform-review/STAGE-1.md")
add("REQ-LM-008", "unresolved", "process", "all", "pp. 20–21 troubleshooting and checklist", "Legacy pipeline names",
    "The troubleshooting table and final checklist still require a canary DM, canary_string, Proposal Match, Agent Trials, Cheat Trial, Harbor Analyze, and 'All 9 Quality Dimensions green'. They also say 'You hit 3 versions for that task.'",
    "Do not execute the legacy cards as if the change table retired them. C-LEGACY-CARDS is unresolved. C-CANARY, C-NINE-DIMENSIONS, and C-REUPLOADS stay open. Keep the acceptance obligations that are reprinted on pp. 25–26.",
    "decision-log.md",
    "Following this checklist literally contradicts pp. 1–14.",
    "00-source/CONFLICT-REGISTER.md")

add("REQ-TX-001", "mandatory", "batch", "batch", "p.22", "Taxonomy source",
    "Follow the official taxonomy of Terminal Bench 3. Delivered tasks must broadly cover the categories and tags used across TB4.",
    "Every delivered task uses a category and subcategory from the printed table, or a justified custom subcategory.",
    "batch-slot.md",
    "U-TAGS. U-GITHUB. The github hyperlink targets are not in the PDF.",
    "01-taxonomy-and-batch/TAXONOMY.md")
add("REQ-TX-002", "mandatory", "batch", "batch", "p.22", "20% cap",
    "No single category may exceed 20% of the delivered batch.",
    "The batch count by category stays at or under 20% of delivered tasks.",
    "batch-slot.md",
    "A one-task delivery cannot satisfy the cap by itself; the slot is still recorded.",
    "01-taxonomy-and-batch/BATCH.md")
add("REQ-TX-003", "mandatory", "batch", "batch", "p.22", "Deprioritized slices",
    "Science, Operations, and Media are deprioritized and included as thin presence slices: 1 task each subcategory. They must not displace the Software / ML / Security / Hardware focus.",
    "The batch plan has one slot per subcategory in those three categories and does not fill the batch with them.",
    "batch-slot.md",
    "Science has 7 subcategories, Operations 6, Media 2. That is 15 slots, not a license to add more in those categories.",
    "01-taxonomy-and-batch/TAXONOMY.md")
add("REQ-TX-004", "mandatory", "batch", "batch", "p.22", "Do not concentrate",
    "Do not concentrate the batch in Software and Science. Operations, Hardware, Security, Media, and ML tags are in scope on equal footing, subject to the 20% cap.",
    "The plan shows non-zero room for Hardware, Security, and ML, and does not make Software plus Science the bulk.",
    "batch-slot.md",
    "Equal footing is subject to the cap and to the one-each rule for deprioritized subcategories.",
    "01-taxonomy-and-batch/BATCH.md")
add("REQ-TX-005", "unresolved", "batch", "batch", "p.24 note", "66 tasks",
    "The note says the distributions are just rough numbers out of 66 total tasks. No distribution table is printed.",
    "No numeric target out of 66 is invented or enforced.",
    "batch-slot.md",
    "U-66.",
    "00-source/UNRESOLVED.md")
add("REQ-TX-006", "mandatory", "task", "build", "p.23 Training", "Single H100",
    "GPU training tasks are bounded by the hardware limit: GPU tasks get a single H100.",
    "gpu_types for a training task is a single H100, which is in the canonical list.",
    "task.toml",
    "Requesting a second GPU or a non-canonical name fails check-gpu-types or the hardware limit.",
    "01-taxonomy-and-batch/TAXONOMY.md")
add("REQ-TX-007", "advisory", "task", "proposal", "pp. 22–24", "Release-composition remarks",
    "Remarks such as 'largest single subcategory', 'largest ML subcategory', 'smallest ML bucket', and RTL as 'a single-task slice' describe the official release, not a freelancer quota.",
    "Those phrases are not turned into submission quotas.",
    "batch-slot.md",
    "The printed quotas are only the 20% cap and one task per deprioritized subcategory.",
    "01-taxonomy-and-batch/TAXONOMY.md")
add("REQ-TX-008", "mandatory", "task", "proposal", "pp. 22–24", "Subcategory catalog",
    "Use the printed subcategory for the chosen category: Software — Systems, Algorithms, Frontend, Data engineering, Databases; ML — Inference, Evaluation, Training, Kernels; Security — Cryptography, Forensics, AppSec; Hardware — CAD, RTL; Science — Biology, Chemistry, Physics, Earth, Robotics, Math, Linguistics; Operations — Finance, Logistics, Supply chain, Claims, Compliance, Marketing; Media — Music, Design. The full scope sentences live in the taxonomy guidance.",
    "The subcategory string matches one of these unless a custom value was justified.",
    "task.toml; 01-taxonomy-and-batch/TAXONOMY.md",
    "The p.2 screenshot chips are examples. Cryptography is under Security in the table, even if a screenshot chip places a sample elsewhere.",
    "01-taxonomy-and-batch/TAXONOMY.md")
SUBS = [
    ("Software", "Systems", "p.22", "Low-level and infrastructure work: storage engines, concurrency, crash recovery, schedulers, sysadmin-grade debugging. Source example: fix write-ahead-log recovery so a storage engine survives crash-and-replay with correct ordering semantics. Described as the largest single subcategory in the official release, which is not a quota."),
    ("Software", "Algorithms", "p.22", "Correctness- and complexity-driven problems whose difficulty is in the logic, not the environment. Includes performance work. The source says speed and efficiency are first-class and correctness alone is not enough. Contest and LeetCode premises remain prohibited."),
    ("Software", "Frontend", "p.22", "Browser-facing application work: UI state, validation, client/server contracts. Source example: a broken React/TypeScript lead-intake app whose submission pipeline must stay consistent across validation, ledger reconciliation, and CRM export."),
    ("Software", "Data engineering", "p.22", "Streaming and batch pipelines. Source example: debugging five interacting failures in a stream-processing engine's session-window GC, merge, and watermark logic, each guarded by a misleading comment."),
    ("Software", "Databases", "p.22", "Query engines, schema and migration work, transactional semantics, performance tuning. The source says these often run multi-container because databases are one of the richer environments agents must explore. Multi-container is descriptive, not mandatory for every database task."),
    ("ML", "Inference", "p.22", "Serving-side work: latency, throughput, batching, deployment config. Framed as LLM inference optimization. Described as the largest ML subcategory in the official release, which is not a quota."),
    ("ML", "Evaluation", "p.22", "Building and repairing measurement machinery: metrics, statistical tests, monitoring. Source example: repairing a drift monitor whose statistical tests and alerting layer break in ways that mimic real production noise."),
    ("ML", "Training", "p.22", "Post-training and optimization loops: SFT and RL of small language models. GPU tasks get a single H100. See also REQ-TX-006."),
    ("ML", "Kernels", "p.23", "GPU programming: writing and optimizing CUDA or Triton kernels, enabled by GPU resource containers. Described as the smallest ML bucket in the official release, which is not a quota."),
    ("Security", "Cryptography", "p.23", "Breaking or correctly implementing cryptographic constructions: weak primitives, protocol flaws, key recovery. The source's verification note is that you recovered the plaintext or you did not."),
    ("Security", "Forensics", "p.23", "Reconstructing events from artifacts: packet captures, logs, disk images, memory dumps. Evidence-chaining over long horizons. The source prefers iterative tasks solved through trial and error, not read-and-solve."),
    ("Security", "AppSec", "p.23", "Application-layer vulnerability discovery and remediation: injection, auth flaws, unsafe deserialization, dependency risk. Described as the smallest security bucket and the closest in shape to ordinary software engineering. Graded output is a repaired behavior or a verified finding, not a procedure for attacking a real system."),
    ("Hardware", "CAD", "p.23", "Programmatic mechanical and geometric modelling: parametric solids, tolerances, exported artifacts checked against geometric ground truth. Described as the larger of the two hardware buckets in the official release."),
    ("Hardware", "RTL", "p.23", "Register-transfer-level digital design: Verilog/VHDL, testbenches, simulation, synthesis-aware correctness. Described as a single-task slice of the official release, which is a description of that release, not a freelancer quota."),
    ("Science", "Biology", "p.23", "Genomics, proteomics, structural/computational biology, bioinformatics. Deprioritized: one task for this subcategory this round. Computational only."),
    ("Science", "Chemistry", "p.23", "Molecular structure, spectra, crystallography, reaction/property analysis. Deprioritized: one task for this subcategory this round. Computational analysis, not a production procedure."),
    ("Science", "Physics", "p.23", "Simulation and numerical modeling of physical systems, including electromagnetic/FDTD device simulation and inverse design. Deprioritized: one task for this subcategory this round."),
    ("Science", "Earth", "p.23", "Earth, climate, hydrology, and environmental modeling. Deprioritized: one task for this subcategory this round."),
    ("Science", "Robotics", "p.23", "Dynamics, trajectory optimization, control. Deprioritized: one task for this subcategory this round."),
    ("Science", "Math", "p.23", "Formalized mathematics and theorem proving (Coq/Lean/Isabelle), formal verification. Deprioritized: one task for this subcategory this round. Olympiad and contest problems remain prohibited."),
    ("Science", "Linguistics", "p.23", "Computational and historical linguistics. Deprioritized: one task for this subcategory this round."),
    ("Operations", "Finance", "p.23", "Quantitative finance, risk, regulatory capital. Deprioritized: one task for this subcategory this round."),
    ("Operations", "Logistics", "p.23", "Dispatch, routing, fleet/flight planning, transportation. Deprioritized: one task for this subcategory this round."),
    ("Operations", "Supply chain", "p.23", "Procurement, production planning, manufacturing, ERP. Deprioritized: one task for this subcategory this round."),
    ("Operations", "Claims", "p.24", "Insurance/utility claims, billing rules, adjudication. Deprioritized: one task for this subcategory this round."),
    ("Operations", "Compliance", "p.24", "Regulatory reporting and compliance workflows. Deprioritized: one task for this subcategory this round."),
    ("Operations", "Marketing", "p.24", "Ads, CTR, marketing analytics. Deprioritized: one task for this subcategory this round."),
    ("Media", "Music", "p.24", "Music theory, audio transcription and processing. Deprioritized: one task for this subcategory this round."),
    ("Media", "Design", "p.24", "Visual/layout design and reconstruction. Deprioritized: one task for this subcategory this round."),
]
for category, sub, page, text in SUBS:
    slug = re.sub(r"[^a-z0-9]+", "-", sub.lower()).strip("-")
    obligation = "conditional"
    scope = "task"
    add(
        f"REQ-SUB-{category[:3].upper()}-{slug}",
        obligation,
        scope,
        "proposal,batch",
        page,
        f"{category} / {sub}",
        text,
        "If this subcategory is selected, the task fits this description."
        + (" This deprioritized subcategory is used at most once in the batch." if category in {"Science", "Operations", "Media"} else ""),
        "proposal.md; batch-slot.md",
        "Release-composition adjectives (largest, smallest, single-task slice) are not quotas. The one-task rule applies only to Science, Operations, and Media.",
        "01-taxonomy-and-batch/TAXONOMY.md",
    )

add("REQ-TX-009", "mandatory", "task", "proposal", "p.7 §4.2 with p.22 Algorithms and p.23 Math", "No contest inside the taxonomy",
    "Algorithms may include performance work, and Math may be formal proof, but LeetCode-style, olympiad, and 'invent a hard problem' tasks remain prohibited.",
    "The proposal's difficulty is an engineering or formal-verification constraint inside a realistic system, not a contest statement.",
    "proposal.md",
    "The taxonomy example does not waive p.7.",
    "01-taxonomy-and-batch/TAXONOMY.md")

add("REQ-AC-001", "mandatory", "process", "acceptance", "p.25", "Taxonomies tab",
    "Acceptance says to see the Taxonomies tab. In this PDF that content is the category table on pp. 22–24.",
    "Batch evidence uses that table.",
    "batch-slot.md",
    "Do not wait for a separate tab that is not in the file.",
    "00-source/INVENTORY.md")
add("REQ-AC-002", "mandatory", "task", "acceptance,stage2", "p.25", "Acceptance difficulty",
    "Difficulty gate as printed: roll out with an anonymous model, timeout limit 8 hrs, 8 rollouts, pass rate ≤ 0.6. The metrics table says ≤ 0.6 i.e 4/8. The note says the anonymous model is close to GPT-6-Sol-xhigh performance.",
    "Record both the Stage 2 predicate and the acceptance pass rate. C-DIFFICULTY does not let either replace the other. The 8-hour phrase is C-TIMEOUT and is also unresolved.",
    "stage2.txt",
    "C-DIFFICULTY. C-TIMEOUT.",
    "03-difficulty-and-horizon/DESIGN.md")
add("REQ-AC-003", "mandatory", "task", "acceptance,stage2", "p.25", "Acceptance horizon",
    "Long horizon gate: a minimum of 35 turns of all passing runs in the Anonymous model. The table says Turns (role=assistant): Anonymous > 35 turns.",
    "Every full-credit trajectory that is available has more than 35 assistant turns, and the Stage 2 median is > 80.",
    "stage2.txt",
    "C-HORIZON. Median > 80 does not by itself prove every passing run is > 35; inspect the passing runs.",
    "14-platform-review/STAGE-2.md")
add("REQ-AC-004", "unresolved", "task", "acceptance", "p.25 item 3", "Both columns",
    "Tasks that fail both difficulty columns, fail solvability, or fail both turn-count columns are rejected. The printed table has a single Latest Frontier Model column.",
    "Satisfy the printed column and the Stage 2 predicates. Do not invent a second model and do not waive a failure because a hidden column might exist.",
    "stage2.txt",
    "C-MISSING-COLUMNS.",
    "00-source/CONFLICT-REGISTER.md")
add("REQ-AC-005", "unresolved", "process", "acceptance", "p.25", "External automation doc",
    "Each task must pass the full automated and human review pipeline defined in TASK_REVIEW_AUTOMATION.md before it counts as accepted. That file is not in this PDF.",
    "Execute the six bullets printed under the sentence. Do not invent the rest of the missing file.",
    "acceptance.txt",
    "U-AUTOMATION.",
    "14-platform-review/ACCEPTANCE.md")
add("REQ-AC-006", "mandatory", "task", "acceptance", "p.25 bullet", "Pipeline static checks",
    "The acceptance pipeline includes static checks: path validation, Dockerfile sanity, canary strings, metadata completeness, and test-reference integrity.",
    "The static-check table passes. Canary strings are handled only through C-CANARY.",
    "static-checks.txt; decision-log.md",
    "C-CANARY.",
    "14-platform-review/ACCEPTANCE.md")
add("REQ-AC-007", "mandatory", "task", "acceptance", "p.25 bullet", "harbor check",
    "Implementation rubric review is an automated harbor check scoring against the task-implementation rubric.",
    "The command used, including arguments the pinned Harbor accepts, is archived. The rubric criteria are the 30 in this PDF.",
    "rubric-review.md",
    "U-HARBOR-PIN. The PDF names `harbor check` and does not give its arguments.",
    "14-platform-review/ACCEPTANCE.md")
add("REQ-AC-008", "mandatory", "task", "acceptance", "p.25 bullet", "Docker / Oracle / No-op",
    "The environment builds cleanly, the reference solution (oracle) passes, and a no-op run fails.",
    "Build log, oracle 1.0, and nop 0.0 are on the accepted SHA-256.",
    "oracle.txt; nop.txt",
    "A no-op that scores anything other than failure fails this bullet.",
    "14-platform-review/ACCEPTANCE.md")
add("REQ-AC-009", "mandatory", "process", "acceptance", "p.25 bullet", "Maintainer review",
    "Maintainer review is sign-off once all automated gates are green.",
    "acceptance.txt has a maintainer sign-off that postdates the green automated gates.",
    "acceptance.txt",
    "Sign-off before the gates are green does not count.",
    "14-platform-review/ACCEPTANCE.md")
add("REQ-AC-010", "mandatory", "task", "acceptance", "p.25 bullet", "Cheat trials",
    "Agent and cheat trials: live agent trials plus adversarial cheat trials specifically probing for reward hacking.",
    "cheat-trials.md records attempts that include reward-file writes, hardcoded fixtures, and reads of hidden tests, and shows they fail.",
    "cheat-trials.md",
    "C-LEGACY-CARDS. The old card name Cheat Trial may be absent. The printed cheat-trial obligation remains.",
    "14-platform-review/ACCEPTANCE.md")
add("REQ-AC-011", "mandatory", "task", "acceptance", "p.26 bullet", "Hacker-fixer loop",
    "Harden iteratively until an adversarial agent can no longer exploit the verifier.",
    "The last recorded cheat attempt fails, and Oracle still scores 1.0 after the hardening.",
    "cheat-trials.md; oracle.txt",
    "Stopping after the first failed cheat, if a later one succeeds, does not close the loop.",
    "14-platform-review/ACCEPTANCE.md")
add("REQ-AC-012", "unresolved", "process", "acceptance", "p.26", "All four criteria",
    "A task is considered accepted only once it clears all four criteria and is merged following this pipeline — not upon submission or upon passing static checks alone.",
    "The task is not called accepted at submission or at static-check pass. All printed pipeline bullets are still required. The word four is not mapped onto a subset.",
    "acceptance.txt",
    "C-FOUR-CRITERIA. Six bullets are printed.",
    "00-source/CONFLICT-REGISTER.md")
add("REQ-AC-013", "unresolved", "process", "all", "PDF outline", "Terms of use",
    "The outline contains 'Terms of Use / Clickwrap Agreement' with no in-PDF page (target -1).",
    "The human accepts the live clickwrap. This system does not restate terms that are not in the PDF.",
    "decision-log.md",
    "U-TERMS.",
    "00-source/UNRESOLVED.md")
add("REQ-UI-001", "platform", "platform", "all", "pp. 5, 10, 11, 13 screenshots", "Stage tabs",
    "The UI tabs are Stage 0 • Task proposal, Stage 1 • Static checks, Stage 2 • Model rollout, and Stage 3 • Qualitative checks marked DEFERRED.",
    "Stage 3 is not marked passed while the badge says DEFERRED.",
    "stage1.txt",
    "C-LEGACY-CARDS. U-STAGE3. A deferred Stage 3 tab is not a QC pass.",
    "14-platform-review/ACCEPTANCE.md")
add("REQ-UI-002", "example", "process", "proposal", "p.4 screenshot", "Form prompts",
    "The markdown box prompts the author to describe the task, starting inputs, and expected outcome; explain how the result will be verified programmatically; explain why the task is difficult and useful; and explain why an expert can solve it within the estimated time.",
    "Those four prompts are covered by the six §3.3 topics inside the 2000-character cap.",
    "proposal.md",
    "Answering the four prompts while skipping 'why it is distinct' still fails §3.3.",
    "04-proposal/PROPOSAL.md")
