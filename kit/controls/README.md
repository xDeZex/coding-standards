# Controls

One Markdown file per control: `kit/controls/<control>.md`. A control is one part of the harness that regulates the agent (a hook, a linter, a review; see `CONTEXT.md`). Each file is a guide to that control: when it suits, and how to write a good one.

The kit does not map catalogue entries to controls. A countermeasure is chosen for a specific cause in a specific repo, so the adopting AI picks a control per entry from the **Use when** lines and proposes it for the human to confirm. Controls with their own kit artifact ([AGENTS.md template](../agents-md/README.md), [Skills list](../skills/README.md)) still get a file here: the guide to using them well.

## File format

```markdown
# Hook

- **What it is:** A script the agent harness runs at a fixed point, such as before a tool call or at the end of a turn.
- **Use when:** the error is mechanical and can be detected or blocked without judgment.

Free prose: how to write a good one.
```

- The `#` title is the control's name and the filename is its lowercase-hyphen slug.
- Both lines are required and checked. `Use when` is about the problem the control suits.
- The prose is unstructured. Say where the control's variants sit: guide or sensor, computational or inferential. One control can be both (a hook can report or block), so this is not a field.
- Link to external docs for tool specifics instead of copying them.

Run the validator after editing: `.venv/bin/python scripts/validate.py`.
