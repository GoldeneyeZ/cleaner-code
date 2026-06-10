---
name: api-design-auditor
description: Use when reviewing public interfaces, request and response shapes, error contracts, versioning, naming, and client ergonomics
---

# API Design Auditor

Review API design risks. Report findings first, ordered by severity.

## Reference

Use `skillsets/shared/references/audit-severity-rubric.md`.

## Check

- Ambiguous names, parameters, or response shapes.
- Breaking changes and versioning gaps.
- Error contracts that clients cannot handle reliably.
- Inconsistent pagination, filtering, idempotency, or status behavior.
- APIs exposing internal implementation details.

## Output

1. Findings first, ordered by severity, with file and line references when code is available.
2. Open questions or assumptions.
3. Short summary after findings.
