---
name: framework-conventions
description: Use when framework components, lifecycle hooks, routing, dependency injection, data access, or tests should match local framework style
---

# Framework Conventions

Discover local style before recommending changes.

## Reference

Use `cleaner-code-skillsets/shared/references/convention-discovery.md`.

## Check

- Existing framework layout, lifecycle, and integration patterns.
- Local helpers that wrap framework APIs.
- Test setup and fixtures for framework behavior.

## Recommend

- Use established project wrappers before raw framework APIs.
- Keep framework-specific code inside existing boundaries.
- Avoid introducing a second style for the same workflow.
