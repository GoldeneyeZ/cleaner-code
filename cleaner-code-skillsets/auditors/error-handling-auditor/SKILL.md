---
name: error-handling-auditor
description: Use when reviewing exception flow, error contracts, retries, fallbacks, logging, recovery, and failure-mode clarity
---

# Error Handling Auditor

Review error-handling risks. Report findings first, ordered by severity.

## Reference

Use `references/audit-severity-rubric.md`.

## Check

- Swallowed errors or overly broad catches.
- Lost context, incorrect wrapping, or unsafe retries.
- Missing fallback, rollback, or cleanup paths.
- User-visible errors that leak internals or hide actionability.
- Logs that miss correlation, severity, or cause.

## Output

1. Findings first, ordered by severity, with file and line references when code is available.
2. Open questions or assumptions.
3. Short summary after findings.
