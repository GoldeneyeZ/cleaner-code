---
name: maintainability-auditor
description: Use when reviewing code for change difficulty, ownership clarity, local reasoning, module size, and long-term maintenance risk
---

# Maintainability Auditor

Review maintainability risks. Report findings first, ordered by severity.

## Reference

Use `skillsets/shared/references/audit-severity-rubric.md`.

## Check

- Files or modules with too many responsibilities.
- Changes that require edits across unrelated areas.
- Hidden coupling through globals, reflection, or implicit contracts.
- Comments or documentation that disagree with behavior.
- Hard-to-test boundaries or setup-heavy workflows.

## Output

1. Findings first, ordered by severity, with file and line references when code is available.
2. Open questions or assumptions.
3. Short summary after findings.
