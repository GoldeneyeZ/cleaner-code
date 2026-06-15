---
name: dependency-auditor
description: Use when reviewing third-party dependencies, version risk, transitive exposure, licensing, supply chain, and unnecessary package use
---

# Dependency Auditor

Review dependency risks. Report findings first, ordered by severity.

## Reference

Use `cleaner-code-skillsets/shared/references/audit-severity-rubric.md`.

## Check

- New dependencies without clear value over local code.
- Security, license, or maintenance concerns.
- Transitive dependency exposure and package size.
- Version pinning, update policy, and compatibility risk.
- Runtime dependencies used only for build-time or test-time needs.

## Output

1. Findings first, ordered by severity, with file and line references when code is available.
2. Open questions or assumptions.
3. Short summary after findings.
