# Hook

- **What it is:** A script the agent harness runs at a fixed point, such as before a tool call or at the end of a turn.
- **Use when:** the error is mechanical and can be detected or blocked without judgment.

## Where it sits

A hook is a computational sensor placed at a fixed point: it runs the same check every time the agent reaches that point, whatever the agent decided. Used to run tests, it complements the agent running its own tests and does not replace them. The agent's own runs give it feedback while it works; the hook is the backstop that runs regardless. See the [position on testing as the agent's feedback loop](../../research/testing-feedback-loop/position.md).

## Two ways to run the tests

- **Commit hook.** A [git hook](https://git-scm.com/docs/githooks) that runs the tests the human wants and blocks the commit on red. It is the guarantee: it runs all the tests, deterministically, even if the agent never ran them.
- **Stop hook.** A hook on the agent's stop event that runs the check and, while it fails, keeps the agent working instead of letting it finish. Guard against loops: the check should see when a stop hook is already forcing a continuation, and the product may cap consecutive blocks.

Events, exit codes, the input a hook receives and the loop cap differ by product and version. Read the vendor docs for them, for example the [Claude Code hooks guide](https://code.claude.com/docs/en/hooks-guide), and do not copy them here.

## Limit: green is not proof

A hook checks that the tests pass, not that they still mean something. An agent can make a red run green by editing, deleting or special-casing tests, and a passing hook does not show the tests are unweakened. So a hook does not stop test tampering. Pair it with a check on what changed in the tests, such as human review of test diffs or an AI reviewer, and treat green as necessary but not sufficient.

## When it is a poor gate

A slow or flaky suite makes the hook a poor gate: a red run is only worth acting on when the tests are fast and deterministic, and a slow gate stalls every commit or stop. Fix the suite first, then add the hook.
