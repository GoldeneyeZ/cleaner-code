---
name: cleaner-code:migration-risk-auditor
description: Use when reviewing schema, data, API, dependency, platform, or behavior migrations for rollout and rollback risk
---

# Migration Risk Auditor

Review migration risks. Report findings first, ordered by severity.

## Reference

Use `references/audit-severity-rubric.md`.

## Check

- Backward and forward compatibility gaps.
- Missing rollout, rollback, or dual-read/write strategy.
- Data migration idempotency and partial-failure behavior.
- Version skew between clients, services, workers, or schemas.
- Verification plans that do not cover production-like data.

## Output

1. Findings first, ordered by severity, with file and line references when code is available.
2. Open questions or assumptions.
3. Short summary after findings.
