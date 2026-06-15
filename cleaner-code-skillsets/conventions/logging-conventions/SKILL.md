---
name: logging-conventions
description: Use when logs, events, correlation fields, severity, message style, or diagnostic context should match local logging practice
---

# Logging Conventions

Discover local style before recommending changes.

## Reference

Use `references/convention-discovery.md`.

## Check

- Existing logger APIs, severity levels, fields, and message style.
- Correlation, request, tenant, and user identifiers.
- Sensitive-data and high-cardinality logging rules.

## Recommend

- Preserve local structured logging conventions.
- Include diagnostic context that supports action.
- Avoid noisy or sensitive logs.
