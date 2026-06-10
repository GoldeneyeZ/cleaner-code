# Skill Frontmatter Contract

Every leaf skill must have valid YAML frontmatter with `name` and `description`.

## Required Fields

```yaml
---
name: kebab-case-skill-name
description: Use when specific triggering conditions tell Codex this skill should be loaded
---
```

## Name Rules

- Use lowercase letters, numbers, and hyphens.
- Match the leaf directory name unless there is a strong reason not to.
- Do not include spaces, punctuation, or parenthetical labels.

## Description Rules

- Start with `Use when`.
- Describe triggering conditions, not the workflow.
- Include concrete symptoms, contexts, or user intents.
- Keep it concise enough to scan.
- Do not promise outcomes.

## Body Rules

The body should include:

- A short purpose statement.
- When to use and when not to use the skill.
- Evidence requirements.
- Step-by-step guidance.
- Output expectations.
- References to shared contracts when relevant.

Leaf skills should stay concise and link to shared references for repeated rules.
