---
name: data-flow-auditor
description: Use when reviewing how data moves through parsing, validation, transformation, storage, caching, and output boundaries
---

# Data Flow Auditor

Review data-flow risks. Report findings first, ordered by severity.

## Reference

Use `skillsets/shared/references/audit-severity-rubric.md`.

## Check

- Missing validation or normalization at boundaries.
- Data transformed without preserving required invariants.
- Ambiguous ownership of mutable data.
- Cache, persistence, and output paths diverging.
- Sensitive data flowing into logs, errors, or responses.

## Output

1. Findings first, ordered by severity, with file and line references when code is available.
2. Open questions or assumptions.
3. Short summary after findings.
