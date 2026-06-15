# Auditor Skill Template

Use this structure for leaf auditor skills. Replace the example identity with the actual audit area before saving a leaf `SKILL.md`.

## Frontmatter

Use a lowercase kebab-case `name` matching the leaf directory. The `description` starts with `Use when` and names the review context or risk signal.

Example:

```yaml
---
name: code-quality-auditor
description: Use when reviewing code for maintainability, clarity, coupling, duplication, and avoidable complexity risks
---
```

## Required Body

- `Purpose`: the risk area this auditor evaluates.
- `Review Scope`: files, modules, tests, configuration, and runtime context.
- `Findings First`: require `cleaner-code-skillsets/shared/references/audit-severity-rubric.md`.
- `Review Checklist`: correctness, safety, maintainability, test coverage, and evidence.
- `Output`: findings ordered by severity, open questions, then short summary.
