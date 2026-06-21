---
name: cleaner-code:service-layer
description: Use when application workflows need an explicit orchestration boundary between delivery mechanisms and domain or data logic
---

# Service Layer

Use Service Layer to coordinate application use cases. Do not use it as a dumping ground for all business logic.

## References

- `references/architecture-decision-rubric.md`
- `references/architecture-output-contract.md`

## Fit

- Scale: applications with multiple delivery mechanisms or workflow orchestration.
- Use when controllers, jobs, or handlers duplicate use-case flow.
- Migrate by extracting one use case with focused tests.

## Do Not Use When

- A simple handler or domain method is enough.
- Services become anemic procedural containers.
- Boundaries only rename existing functions.

## Tradeoffs

Adds another layer. Keep services use-case focused and avoid generic manager names.
