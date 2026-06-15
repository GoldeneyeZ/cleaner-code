---
name: test-quality-auditor
description: Use when reviewing tests for behavioral coverage, reliability, assertions, isolation, fixtures, and regression protection
---

# Test Quality Auditor

Review test quality risks. Report findings first, ordered by severity.

## Reference

Use `cleaner-code-skillsets/shared/references/audit-severity-rubric.md`.

## Check

- Missing coverage for changed behavior.
- Tests that assert implementation details instead of outcomes.
- Flaky timing, order, or shared-state dependencies.
- Fixtures that hide intent or make failures hard to diagnose.
- Missing regression tests for fixed defects.

## Output

1. Findings first, ordered by severity, with file and line references when code is available.
2. Open questions or assumptions.
3. Short summary after findings.
