# Catalogue

One YAML file per topic: `kit/catalogue/<topic>.yaml`, a list of catalogue entries. The filename is the topic, matching `research/<topic>/`.

## Entry fields

| Field | Meaning |
| --- | --- |
| `id` | Descriptive slug, unique within the topic file, never renamed. Referenced elsewhere as `<topic>/<id>`. |
| `statement` | The instruction. |
| `rationale` | Why. |
| `applies_when` | Loose free text the AI judges against a target repo, such as "when there are tests" or "when doing UI". Absent means always. |
| `position` | Repo-relative path to the position the entry comes from, with an optional `#anchor`. Search for the path to find the entries a changed position affects. |

Sources are not on the entry. They are reached through the position to its source notes, which carry the source, source date and researched date.

To retire an entry, delete it. Git history keeps it.

## Example (format only, not a real standard)

```yaml
# kit/catalogue/testing.yaml
- id: run-tests-before-commit
  statement: Run the test suite before every commit.
  rationale: Catches regressions while the change is still small.
  applies_when: when there are tests
  position: research/testing/position.md#tests-first
```
