---
name: cleaner-code:immutability-conventions
description: Use when mutation, copying, value objects, collections, or state updates should match local immutability style
---

# Immutability Conventions

Discover local style before recommending changes.

## Reference

Use `references/convention-discovery.md`.

## Check

- Existing mutation, copying, and value-object patterns.
- Collection update style and ownership boundaries.
- Language or framework conventions for immutable state.

## Recommend

- Prefer local state-management idioms.
- Avoid defensive copying where ownership is already clear.
- Require tests for changes to mutation semantics.
