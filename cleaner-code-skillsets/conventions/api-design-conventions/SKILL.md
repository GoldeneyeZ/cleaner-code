---
name: api-design-conventions
description: Use when public interfaces, method signatures, request shapes, response shapes, or error contracts need local consistency
---

# API Design Conventions

Discover local style before recommending changes.

## Reference

Use `cleaner-code-skillsets/shared/references/convention-discovery.md`.

## Check

- Existing API naming, parameter, response, and error patterns.
- Versioning, pagination, idempotency, and compatibility conventions.
- Client ergonomics in nearby call sites or tests.

## Recommend

- Keep public contracts stable unless change is explicit.
- Prefer consistency with existing clients.
- Document deviations that affect consumers.
