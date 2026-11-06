# Agent environment, fixtures, dependencies, and reproducible builds

Two images. Only the agent image is visible to the benchmark agent.

| Image | File | Contains | Must not contain |
| --- | --- | --- | --- |
| Agent | `environment/Dockerfile` | The starting system, the inputs the instruction names, pinned engines the agent is meant to use | `tests/`, `solution/`, ground truth, test-only packages, credentials |
| Verifier | `tests/Dockerfile` | pytest, CTRF tooling, scoring libraries, oracle binaries the grader needs, frozen ground truth, `uv` if `test.sh` uses it | Nothing fetched at verify time |

## Dockerfile rules

**Source.**

- `check-dockerfile-references`: the agent Dockerfile does not copy `solution/solve.sh`, `tests/test.sh`, or `tests/test_*.py`. Page 9: do not copy `tests/` or `solution/` at all.
- `check-dockerfile-platform`: no `FROM --platform=...`. The task must run on x86-64 or arm64 without forced emulation.
- `check-dockerfile-sanity`: apt packages are not version-pinned; `apt-get update` precedes the install; the same layer removes `/var/lib/apt/lists/*`.
- `check-pip-pinning`: every `pip`, `uv pip`, `uvx`, and `uv tool` install pins an explicit `==` version. Allowed without that pin style: a manifest install (`-r requirements.txt`), a local install (`-e .` or `.`), pip self-upgrade, and a VCS URL that has an `@ref`.
- `check-nproc`: do not call bare `nproc`. It returns the host CPU count inside a container. Use `[environment].cpus` or a fixed value.

## Fixtures

**Source.** Inputs the agent must see are copied by the agent Dockerfile from `environment/`. The example uses `environment/data/`. Absolute paths in the instruction must match those destinations.

**Practice.** Keep a fixture manifest in the private evidence pack: path inside the image, whether the agent may read it, and whether the verifier also has a copy. If both images contain a file, say so. A file that is the expected answer belongs only in the verifier image.

## Reproducible build

**Source.** Rubric E: images build cleanly and deterministically on a fresh machine. The task does not rely on flaky external resources. G04 fails the upload if Harbor cannot build and start the declared image. Do not use a prebuilt image profile the platform does not support (`PROFILE.PREBUILT_IMAGE_UNSUPPORTED`). Do not declare an accelerator the profile cannot provide (`PROFILE.ACCELERATOR_UNSUPPORTED`).

The pinned Harbor version is named and not identified (`U-HARBOR-PIN`). Do not invent a release tag.

## Compose, when used

**Source.** Conditional. If a `docker-compose` file exists, G03 scans dependency provenance, host binds, privileged mode, host networking, devices, resource-envelope bypass, and packaged-file mutation. Do not use `network_mode: host`, `privileged: true`, host bind mounts, or device mappings.

## Credentials and networking

**Source.** G03 credential scanning rejects confirmed credentials. Do not put keys, tokens, or live secrets in the image, the fixtures, or the ZIP. `CREDENTIAL.SUSPECTED` is the advisory sibling; still remove the suspect.

`C-INTERNET` is unresolved inside SOP v3.0. The change table requires public network access for the agent environment and the agent phase. `check-allow-internet` forbids `allow_internet = false`. G02 still says agent networking is non-public. The replacement for the deprecated `allow_internet` field is not named (`U-NET-CONFIG`). Do not invent that key. Do not set `allow_internet = false`. Do not give the verifier public networking because the agent side requires it. Host networking, privileged mode, and verifier-time fetches remain forbidden. The answer still must not be a public lookup.
