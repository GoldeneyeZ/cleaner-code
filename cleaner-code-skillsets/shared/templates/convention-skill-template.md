# Convention Skill Template

Use this structure for leaf convention skills. Replace the example identity with the actual convention area before saving a leaf `SKILL.md`.

## Frontmatter

Use a lowercase kebab-case `name` matching the leaf directory. The `description` starts with `Use when` and names the convention area to inspect.

Example:

```yaml
---
name: naming-conventions
description: Use when code names should be checked against local naming style for modules, types, functions, variables, or tests
---
```

## Required Body

- `Purpose`: the convention area covered by this skill.
- `Discover Local Style First`: require `cleaner-code-skillsets/shared/references/convention-discovery.md`.
- `Check`: nearby code, tests, config, docs, dominant patterns, and exceptions.
- `Recommend`: scoped local consistency, explicit best-practice conflicts, and no unrelated cleanup.
- `Output`: local evidence, recommended changes, and cases intentionally left unchanged.
