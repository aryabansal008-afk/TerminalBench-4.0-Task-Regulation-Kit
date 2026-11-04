# What goes in the submission archive

The platform asks for one immutable Harbor task ZIP. `tools/package_task.py` writes a single top-level slug directory. That shape is **provisional** (`U-ZIP-ROOT`). Page 9 G01 asks for a single candidate root and does not state the ZIP’s top-level shape. If G01 rejects the shape, the receipt decides the next one.

## Include

These paths, after placeholders are replaced and the local checks pass:

| Path | Class | Why it is in the ZIP |
| --- | --- | --- |
| `instruction.md` | Agent-visible | The task statement the agent is given. |
| `task.toml` | Agent-visible configuration | Metadata, timeouts, verifier mode, artifacts, resources. |
| `environment/Dockerfile` | Agent-visible | The agent image. |
| `environment/data/` and other input fixtures the instruction names | Agent-visible | Starting inputs. |
| `solution/solve.sh` | Verifier-side reference | Oracle entry point. Not copied into the agent image. |
| `solution/solve.py` when the logic needs it | Verifier-side reference | Reference logic. Not copied into the agent image. |
| `tests/Dockerfile` | Verifier | Separate verifier image. |
| `tests/test.sh` | Verifier | Verifier entry. Writes the reward. |
| `tests/test_outputs.py` and other grader files | Verifier | Deterministic checks and frozen expected values. |

## Exclude

| Material | Where it lives instead |
| --- | --- |
| This authoring system, including the register and the conflict register | Stays in `tb4-authoring-system/`. |
| The proposal markdown and the grant receipt | `evidence/<slug>/`. The proposal was already submitted on the platform as its own revision. |
| Decision log, rubric review, checker report, Oracle and NOP transcripts, dry-run notes, cheat-trial notes | `evidence/<slug>/`. |
| The ZIP’s own SHA-256 note | `evidence/<slug>/sha256.txt`. The platform binds the digest of the ZIP; the note is not a member of the ZIP. |
| Stage 1 and Stage 2 receipts, trajectories | `evidence/<slug>/`. |
| `.git`, symlinks, credential files, a second task root, a copy of `tests/` or `solution/` under `environment/` | Nowhere. G01 rejects multiple roots, symlinks, and archive bombs. G03 rejects confirmed credentials. |
| A canary string this system invented | Nowhere. `C-CANARY`. |

## Checksums and versions

**Source.** Each corrected ZIP is Version N of N. Stage 1 re-runs from the start. Partial credit across versions does not count. Re-uploading identical bytes fails with `File hash already exists`.

**Practice.** Record `shasum -a 256` of the file that was uploaded, next to the version number, in the evidence pack. Do not put the digest inside the ZIP and then hash the ZIP again.

How many versions are allowed is `C-REUPLOADS` and is unresolved. Hourly limit 2 unique versions and daily limit 5 unique versions are separate table cells.
