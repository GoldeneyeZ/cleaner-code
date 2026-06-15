---
name: architecture-auditor
description: Use when reviewing module boundaries, dependency direction, layering, coupling, and architecture decision risks
---

# Architecture Auditor

Review architecture risks. Report findings first, ordered by severity.

## Reference

Use `references/audit-severity-rubric.md`.

## Check

- Dependency direction and boundary leaks.
- Layering violations or misplaced policies.
- Cycles and unstable ownership boundaries.
- Architectural decisions that exceed current scale.
- Migration paths and rollback safety.

## Output

1. Findings first, ordered by severity, with file and line references when code is available.
2. Open questions or assumptions.
3. Short summary after findings.
