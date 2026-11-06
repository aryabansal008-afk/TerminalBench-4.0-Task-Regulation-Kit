# Stage 1

Stage 1 is one sequenced job: `I01`, then `G01` through `G06`, then `P04`. The author does not click gates one by one. A clean run is described as well under a minute, with most of the time in G04 through G06 (environment build, verifier controls, package quality). `I01` binds the snapshot first. `NOT_REACHED` on a later gate means an earlier gate stopped the job. The platform fails closed.

The durable event log is the phase order. Rule IDs visible in the screenshots are catalogued in `00-source/PLATFORM-RULE-CATALOG.md`. Severity badges in those screenshots were not reliably column-aligned (`U-SEVERITY-ALIGNMENT`). Page 11’s three classes still apply: `REQUIRED`, `OPTIONAL / ADVISORY`, `IF APPLICABLE`.

## Outcomes

| Outcome | Meaning | Action |
| --- | --- | --- |
| `Stage 1 accepted` / `PASSED STAGE 1` / `READY_FOR_STAGE2` | All gates passed. Warnings may still be listed. The example UI allows `Stage 1 accepted · 2 warnings`. | Archive the receipt. Go to Stage 2. Do not upload a new ZIP only to clear an advisory unless a human asks. |
| `Stage 1 rejected — upload a corrected ZIP` | A `REQUIRED` rule found a defect. The blocking-reason example is `G05.ORACLE.REWARD_BELOW_FULL`. | Read the rule text. Fix locally. Re-run static checks, Oracle, and NOP. Upload a new version. |
| `Stage 1 could not complete — retry` | The platform will not attribute this to the task. Examples: `G05.HARBOR.UNKNOWN_EXCEPTION`, `G04.PROFILE.ACCELERATOR_UNSUPPORTED`. | Retry, not a rewrite, after checking the profile you declared. |

Partial green across versions does not count.

## Gates, in the prose’s own words

Use the catalog for rule IDs. The gate responsibilities are:

- `I01` binds the uploaded snapshot.
- `G01` checks the archive: a single candidate root, no symlinks, no archive bomb.
- `G02` checks task metadata, subcategory, separate verifier, and says agent networking is non-public. “Non-public” is undefined (`C-INTERNET`). The pinned Harbor version is unnamed (`U-HARBOR-PIN`).
- `G03` checks the environment build inputs: credentials, and Compose only if Compose is present.
- `G04` builds and starts the declared image.
- `G05` runs Oracle and NOP.
- `G06` is package quality over instruction, tests, mapping, and related criteria.
- `P04` is the publication barrier after those gates.

The screenshots label a gate “Harbor + TB3” while the prose is TB4. That label conflict is `C-TB3-LABEL` and is unresolved. Follow the rule text you can read. Do not invent a TB3 procedure that this PDF does not print.

SOP v3.0 names `TB4.CANARY_MISSING`, `TB4.CANARY_FORMAT`, and `TB4.CANARY_ADVISORY` as advisory G02 rules. Older screenshots showed `TB3.CANARY_*`. Archive whatever id the live log prints. Missing markers must not be treated as a Stage 1 rejection.

## Upload limits that bind this stage

These sentences are the source limits. The packing procedure is `13-packaging/PACKAGE.md`.

- `Upload Harbor task ZIP` stays inactive until an `ACTIVE` grant exists. One immutable ZIP version may be uploaded against that grant, and Stage 1 begins automatically. The platform binds SHA-256 and an upload generation.
- Each corrected ZIP is Version N of N. Stage 1 re-runs from the start. Only one version with every gate green reaches Stage 2. Partial credit across versions does not count. Arrive green.
- Identical bytes fail with `File hash already exists`.
- Hourly evaluation limit: 2 unique versions. Daily evaluation limit: 5 unique versions.
- Reuploads per task: limits table 7. Leftover “3” sentences are flagged (`C-REUPLOADS`) and are not the budget.
