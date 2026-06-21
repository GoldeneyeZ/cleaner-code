---
name: cleaner-code:code-quality-auditor
description: Use when reviewing code for clarity, correctness, coupling, cohesion, duplication, naming, and avoidable complexity risks
---

# Code Quality Auditor

Review code quality risks. Report findings first, ordered by severity.

## Reference

Use `references/audit-severity-rubric.md`.

## Check

- Correctness risks hidden by unclear control flow.
- Names that obscure domain intent.
- Coupling, low cohesion, and unnecessary indirection.
- Duplication that can drift.
- Complexity that blocks local reasoning.

## Output

1. Findings first, ordered by severity, with file and line references when code is available.
2. Open questions or assumptions.
3. Short summary after findings.
