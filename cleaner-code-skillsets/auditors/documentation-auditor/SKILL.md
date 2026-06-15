---
name: documentation-auditor
description: Use when reviewing comments, README files, API docs, runbooks, examples, and documentation accuracy against behavior
---

# Documentation Auditor

Review documentation risks. Report findings first, ordered by severity.

## Reference

Use `references/audit-severity-rubric.md`.

## Check

- Documentation that contradicts current behavior.
- Missing setup, usage, migration, or operational instructions.
- Examples that cannot run or omit important failure cases.
- Comments explaining stale intent instead of current code.
- Public API docs missing contracts, errors, or constraints.

## Output

1. Findings first, ordered by severity, with file and line references when code is available.
2. Open questions or assumptions.
3. Short summary after findings.
