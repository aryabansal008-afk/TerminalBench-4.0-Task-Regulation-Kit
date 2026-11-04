# Reference solution and independently verified ground truth

The reference solution is verifier-side material. It is in the ZIP. It is not in the agent image. The oracle entry point is `solution/solve.sh`.

## Source

- A correct reference solution is provided and passes every test. Local Oracle command: `harbor run --path . --agent oracle`. Expected result: 100% pass, reward `1.0`.
- G05: Oracle must score 1.0 and exit cleanly. Reward must be found, parseable, unambiguous, and finite.
- The solution may be longer than the instruction. Preferred split over about 20 lines: `solve.sh` runs `python3 /solution/solve.py`.
- The solution and the tests must agree on every output path, and each such path must be named in `instruction.md` or `task.toml`.
- Expected values are themselves correct and were derived independently of a single unreviewed model draft. Rubric A: “Correct expected values.”
- Frozen ground truth comes from fixtures inside the verifier image, not from the clock and not from the network.

## Independent ground truth

**Practice, in service of “independently derived.”** Produce the expected artifact by a method you can re-run, and record that method in the private evidence pack. Acceptable records are: a short derivation from the fixture, a second implementation that does not import the solution under test, or a hand check of a small frozen output with the intermediate values written down. “The model wrote both the solution and the expected file” is not independent. Do not put that derivation in `instruction.md` or in the agent image.

If the solution and the tests share one generator script, say so in `verification_explanation` and keep the generator on the verifier side. Sharing the generator is not independent verification. Add the second check above.

## What the solution must not do

**Source.** It must not be copied into the agent image. `check-ai-prompt-sanitization`: prompts inside the task must not leak the solution or hidden data to the model.

**Practice.** The solution does not write `/logs/verifier/reward.txt`. The verifier writes the reward after the agent container is gone. The solution does not read `/tests`.
