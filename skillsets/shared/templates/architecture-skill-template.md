# Architecture Skill Template

Use this structure for leaf architecture skills. Replace the example identity with the actual architecture before saving a leaf `SKILL.md`.

## Frontmatter

Use a lowercase kebab-case `name` matching the leaf directory. The `description` starts with `Use when` and names the scale, coupling, or boundary pressure that triggers the skill.

Example:

```yaml
---
name: hexagonal-architecture
description: Use when application core logic needs clearer boundaries from delivery mechanisms, persistence, or external services
---
```

## Required Body

- `Purpose`: the architectural pressure this skill addresses.
- `Use When`: present boundary pain, operational fit, and verifiable migration path.
- `Do Not Use When`: small-system ceremony, smaller boundary fit, or insufficient behavior protection.
- `Decision Process`: require `skillsets/shared/references/architecture-decision-rubric.md`.
- `Output`: follow `skillsets/shared/references/architecture-output-contract.md`.
