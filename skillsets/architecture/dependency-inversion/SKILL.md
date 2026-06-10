---
name: dependency-inversion
description: Use when high-level policy depends on low-level details and dependency direction may be blocking testing or change
---

# Dependency Inversion

Use this when dependency direction is the problem, not as a default interface rule.

## References

- `skillsets/shared/references/architecture-decision-rubric.md`
- `skillsets/shared/references/architecture-output-contract.md`

## Fit

- Scale: modules or services where policy and details change independently.
- Use when tests or changes are blocked by direct detail dependencies.
- Migrate by extracting one narrow port from actual policy needs.

## Do Not Use When

- A concrete dependency is stable, local, and clearer.
- The interface would mirror one implementation.
- The abstraction only exists for test mocks.

## Tradeoffs

Adds indirection and naming burden. Keep ports small and owned by the policy side.
