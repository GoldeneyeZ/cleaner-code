# Design Pattern Skill Template

Use this structure for leaf design pattern skills. Replace the example identity with the actual pattern identity before saving a leaf `SKILL.md`.

## Frontmatter

Use a lowercase kebab-case `name` matching the leaf directory. The `description` starts with `Use when` and names concrete trigger conditions, not the workflow.

Example:

```yaml
---
name: strategy
description: Use when existing code has multiple interchangeable algorithms selected by conditionals or configuration
---
```

## Required Body

- `Purpose`: the design pressure this pattern addresses.
- `Use When`: current smells and variation axes that justify the pattern.
- `Do Not Use When`: simpler refactors, speculative needs, and abstraction risks.
- `Evidence Checklist`: code smell, behavior at risk, simpler refactor comparison, and test coverage.
- `Application Steps`: protect behavior, introduce the smallest structure, migrate one variation, remove obsolete branching, re-run tests.
- `Output`: follow `skillsets/shared/references/pattern-output-contract.md`.
