---
name: cleaner-code:duplication-auditor
description: Use when reviewing repeated logic, copy-pasted branches, parallel structures, duplicated tests, and drift-prone implementations
---

# Duplication Auditor

Review duplication risks. Report findings first, ordered by severity.

## Reference

Use `references/audit-severity-rubric.md`.

## Check

- Repeated business rules or validation logic.
- Parallel structures that must change together.
- Copy-pasted tests that hide missing behavior cases.
- Duplication that would drift across modules or services.
- Over-eager abstraction where duplication is harmless.

## Output

1. Findings first, ordered by severity, with file and line references when code is available.
2. Open questions or assumptions.
3. Short summary after findings.
