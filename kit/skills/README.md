# Skills list

Pointers to skills that live elsewhere. No skill content is stored here.

One Markdown file: `kit/skills/skills.md`, one `##` entry per skill. The guide to writing a skill is a control, [`kit/controls/skill.md`](../controls/README.md), and may link here.

## Entry format

```markdown
# Skills

## grilling

- **Where:** [grilling](../../.claude/skills/grilling/SKILL.md)
- **Why:** Stress-tests a plan by asking questions until both sides agree.
- **Use when:** a decision needs thinking through with a human before anything is built.
```

- The `##` heading is the id: a lowercase-hyphen slug, unique in the file, never renamed.
- All three lines are required and checked. `Where` is a Markdown link to where the skill lives (a relative link for a skill in this repo, a URL otherwise). `Why` is why it is recommended. `Use when` is loose free text the AI judges against a target repo.
- Catalogue entries do not name skills, and skills do not name entries. At adoption the AI proposes skills from the `Use when` lines and the human confirms, as for controls.
- To retire a skill, delete its entry.

Run the validator after editing: `.venv/bin/python scripts/validate.py`.
