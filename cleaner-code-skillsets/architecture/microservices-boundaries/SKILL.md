---
name: microservices-boundaries
description: Use when evaluating service boundaries, independent deployment, ownership, data separation, and distributed-system tradeoffs
---

# Microservices Boundaries

Use this when service extraction is being considered. Prefer a modular monolith until independent deployment or ownership is proven necessary.

## References

- `references/architecture-decision-rubric.md`
- `references/architecture-output-contract.md`

## Fit

- Scale: teams and domains that need independent deployability or scaling.
- Use when ownership, data, and runtime boundaries are already clear.
- Migrate by splitting one bounded capability with monitoring and rollback.

## Do Not Use When

- The goal is only code organization.
- Shared database ownership remains unresolved.
- The team cannot operate distributed failures.

## Tradeoffs

Adds network, deployment, observability, and data consistency costs. Demand strong boundary evidence.
