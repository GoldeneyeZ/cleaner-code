---
name: repository
description: Use when domain code needs collection-like access to persisted aggregates without leaking query or storage details
---

# Repository

Use Repository to protect domain logic from persistence details. Do not use it as a generic data access layer for every table.

## References

- `skillsets/shared/references/architecture-decision-rubric.md`
- `skillsets/shared/references/architecture-output-contract.md`

## Fit

- Scale: domain models with meaningful aggregate or entity boundaries.
- Use when persistence code leaks into business decisions.
- Migrate by wrapping one aggregate access path and preserving behavior tests.

## Do Not Use When

- The app is CRUD-only and active records or direct queries are clearer.
- The repository would expose every storage query unchanged.
- Transaction and consistency boundaries are undefined.

## Tradeoffs

Can hide query cost and create leaky abstractions. Keep query shapes explicit where performance matters.
