---
name: module-boundary-conventions
description: Use when imports, exports, package boundaries, visibility, layering, or ownership should match local module structure
---

# Module Boundary Conventions

Discover local style before recommending changes.

## Reference

Use `references/convention-discovery.md`.

## Check

- Existing import direction, export surfaces, and visibility rules.
- Layer, feature, package, or ownership boundaries.
- Test-only helpers and internal APIs.

## Recommend

- Keep dependencies flowing in the local intended direction.
- Avoid widening public surfaces for convenience.
- Move code only when it clarifies ownership.
