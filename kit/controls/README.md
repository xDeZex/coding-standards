# Controls

One Markdown file per control: `kit/controls/<control>.md`. A control is one part of the harness that regulates the agent (a hook, a linter, a review; see `CONTEXT.md`). Each file is a control handbook: it teaches what the control is, what it is good and bad at, and how to write a good one.

## Who reads it

An AI working with a human on a specific cause in a specific repo. The AI reasons from the cause to a control and the human decides. The kit does not map catalogue entries or problems to controls, because a countermeasure is chosen for a specific cause and is a hypothesis until checked. A handbook is therefore written so a reader can judge whether their case fits, from general properties of the control. It is not a list of problems to look yours up in.

Controls not yet covered: linter, tests, type checker and review. A handbook's `Good at` and `Bad at` are written only from research aimed at the handbook's purpose: when to use this control, across its uses. Research on one use of a control (hooks as a test gate) feeds a handbook but does not stand for the whole control.

## Dimensions

Every handbook addresses the same six questions in its prose, so controls can be compared. Put the answers wherever they fit under `Good at` and `Bad at`; they are not headings or fields.

1. **When does it act?** Before the agent acts (guide), after (sensor), or at a gate such as a commit or the end of a turn.
2. **Who judges?** Deterministic code, a model or the agent itself: computational or inferential, and how reliable the verdict is.
3. **Can it be bypassed or ignored?** By the agent, by a tool flag, or by being deprioritised in a crowded context. Whether it takes effect at all.
4. **What does it cost?** Context tokens, run time, maintenance, and what happens when it goes stale.
5. **What does a failure look like?** A clear signal the agent can act on, a silent miss, or a loop. What happens once it does take effect.
6. **What does it need to exist?** A tool, a vendor feature, a test suite, a decision about what "correct" means.

One control can sit in several places on these (a hook can report or block), so say where its variants sit.

## File format

```markdown
# Hook

- **What it is:** A script the agent harness runs at a fixed point, such as before a tool call or at the end of a turn.

## Good at

Prose: what it does well and why, in general terms.

## Bad at

Prose: where it fails and why.

## How to write a good one

May be empty.
```

- The `#` title is the control's name and the filename is its lowercase-hyphen slug.
- The `What it is` line and the three `##` headings are required and checked. Anything else is free prose.
- Write in general terms, describing how the control works so a reader can reason about their own case. Do not list problems the control solves.
- Link claims to positions, not to sources. Say plainly when a point is our inference rather than a finding. A handbook with no link to a `position.md` gets a validator warning: it has nothing behind it yet.
- `How to write a good one` may link to external docs instead of copying them.

Run the validator after editing: `.venv/bin/python scripts/validate.py`.
