---
name: observability-auditor
description: Use when reviewing logging, metrics, tracing, alerting, correlation, diagnostics, and production failure visibility
---

# Observability Auditor

Review observability risks. Report findings first, ordered by severity.

## Reference

Use `cleaner-code-skillsets/shared/references/audit-severity-rubric.md`.

## Check

- Missing logs, metrics, traces, or correlation identifiers.
- No visibility into critical failures or degraded paths.
- High-cardinality or sensitive telemetry.
- Alerts without actionable ownership or thresholds.
- Diagnostics that cannot distinguish expected from unexpected failures.

## Output

1. Findings first, ordered by severity, with file and line references when code is available.
2. Open questions or assumptions.
3. Short summary after findings.
