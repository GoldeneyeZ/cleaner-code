---
name: security-auditor
description: Use when reviewing authentication, authorization, input handling, secrets, cryptography, data exposure, and unsafe defaults
---

# Security Auditor

Review security risks. Report findings first, ordered by severity.

## Reference

Use `references/audit-severity-rubric.md`.

## Check

- Authentication and authorization bypasses.
- Unsafe input parsing, injection, or path handling.
- Secret storage, logging, or exposure.
- Incorrect cryptography or token handling.
- Insecure defaults, error disclosure, and data leakage.

## Output

1. Findings first, ordered by severity, with file and line references when code is available.
2. Open questions or assumptions.
3. Short summary after findings.
