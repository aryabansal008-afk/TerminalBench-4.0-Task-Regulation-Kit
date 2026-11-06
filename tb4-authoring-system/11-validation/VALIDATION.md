# Oracle, NOP, negative cases, adversarial attempts, and reward hacking

## Local Oracle and NOP

**Source.** From page 8:

```
harbor run --path . --agent oracle
harbor run --path . --agent nop
```

| Agent | Required local result | If it is wrong |
| --- | --- | --- |
| Oracle | 100% pass, reward `1.0` | The solution or the verifier is broken: bad `test.sh` logic, or a dependency missing from the verifier image. |
| NOP | 100% fail, reward `0.0` | The verifier is weak. It passes when nothing was done. Tighten the tests. |

G05 runs both as one Harbor job. Oracle must score 1.0 and exit cleanly. NOP must not score 1.0. Local NOP at 0.0 follows the local table. Whether a partial NOP reward fails the platform is `C-REWARD-LITERAL` and is unresolved. Do not treat 0.0 as a finding about `NOP.PARTIAL_REWARD`.

Archive the command, the exit, and the reward token in the private evidence pack. Before those commands, the same tree must already have a local static-check run and a 30-criterion rubric review. Static checks do not judge quality. The rubric may be run with a free or open-source LLM. The source’s examples are Llama-class or Kimi-class models. Both reports predate the ZIP.

## Negative cases

**Source.** A do-nothing attempt fails. A partial attempt fails. The obvious naive approach fails. Tests cover edge cases the instruction names, not only the happy path.

**Practice.** Before upload, run at least these author-built attempts and record each reward in the local-measurement block of `complexity.md`:

- NOP, the empty workspace.
- A partial artifact that has the right path and the wrong values.
- Each naive approach named in `03-difficulty-and-horizon/GENUINE-COMPLEXITY.md`.

Each must score `0.0`. If a naive approach scores `1.0`, that approach meets the stated requirements. Strengthen by a page 15 move that is also added to the instruction. Do not hide a field, and do not add a test for a condition the instruction does not state.

## Adversarial attempts and reward hacking

**Source.** The agent must not be able to hardcode expected values that the tests will accept for any input, write the reward file and have that count, read hidden tests or the solution, fetch the answer at verify time, or pass by satisfying a keyword search. Acceptance still names adversarial cheat trials and a hacker–fixer loop until an adversarial agent can no longer exploit the verifier. Those bullets are on pages 25–26. Whether they are a platform card named Cheat Trial is `C-LEGACY-CARDS` and is unresolved. The bullets themselves are printed requirements. Do not check them off because Stage 2 passed.

**Practice, authoring-time loop, not a substitute for the platform’s trials.**

- A solution that writes `/logs/verifier/reward.txt` and does nothing else scores `0.0`. The verifier container writes the reward after the agent is gone. Do not grade a reward file the agent left behind.
- A solution that prints example values scores `0.0` if an example was included. Prefer not to include example outputs that are the real answer.
- A solution that hardcodes one fixture’s answer fails when a second condition must be computed. If there is only one public fixture and the answer is a pure function of it, hardcoding is the correct solution and the task is too easy.
- The agent image has no path to `/tests`, `/solution`, or the verifier’s expected-value files.
- `test.sh` does not download anything.

If a cheat succeeds, fix the verifier or the layout and re-run Oracle and NOP. Record the attempt and the result in `evidence/<slug>/cheat-trials.md`.
