# Review

- **What it is:** A person or an AI reviewer reading what changed, here the diff of the tests, before the change is accepted.
- **Use when:** the agent may have made a red run green by weakening, deleting or special-casing tests, and no computational check can tell a real fix from a gamed pass.

This is a stance, not a proven fix. The [position on testing as the agent's feedback loop](../../research/testing-feedback-loop/position.md#a-green-run-from-an-agent-is-weaker-evidence) has no tested answer to an agent getting green by cheating. It pairs the loop with a check on what changed in the tests and treats a green run as necessary but not sufficient. Nothing measures how well review catches this.

## Where it sits

Review is a sensor: it looks after the agent has acted. There are two variants.

- **AI reviewer:** an inferential control. It judges with a model, so it is slower and non-deterministic. It can miss a weakened test on one run and catch it on the next.
- **Human review:** the alternative, and the fallback when the AI reviewer is not trusted or the change matters. It is slower still but does not share the agent's blind spots.

A commit hook does not replace it. A hook only checks that the tests pass, so a gamed pass gets through. Read-only tests stop test editing but not special-casing, where the code detects the test and returns the expected answer. Review is the one control here that can see special-casing, because it reads the code.

## When review suits

- The tests carry real weight and a green run is what people rely on.
- The task is ambiguous or may be unsolvable, where the sources see gaming rise.
- The agent has failed repeatedly, since cheating appears most after repeated failure.

It suits less when the change is small and low risk, or when nobody will actually read the diff. A review that is skipped is no control.

## How it differs from reviewing the code

Reviewing the code asks whether it is correct. Reviewing the test changes asks whether the tests still check what they did before.

- Read the test diff on its own, before the code diff. Passing tests are the claim under check, not evidence.
- Look for removed tests, removed or loosened assertions, added skips or expected failures, widened tolerances, and mocks that replace the behaviour under test.
- Look in the code for special-casing: branches on test inputs, hard-coded expected values, checks for a test environment.
- A test change with no matching change in requirements is suspect. A test edited in the same change that makes it pass deserves the most attention.
- Ask the agent to explain each test change, then check the explanation against the diff.

## Writing a good one

Give an AI reviewer only the diff and the task, not the agent's own account of the work, so it judges independently. Tell it what to look for using the list above. Have it flag and not fix, and escalate what it flags to a human. Treat its silence as weak evidence.
