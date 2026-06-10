---
name: modular-monolith
description: Use when a single deployable needs stronger internal module boundaries without microservice operational cost
---

# Modular Monolith

Use Modular Monolith when module boundaries matter but independent deployment is not justified.

## References

- `skillsets/shared/references/architecture-decision-rubric.md`
- `skillsets/shared/references/architecture-output-contract.md`

## Fit

- Scale: growing monoliths with feature ownership or boundary pain.
- Use when cycles and cross-module data access slow change.
- Migrate by defining one module API and blocking direct internal imports.

## Do Not Use When

- The codebase is too small for module ceremony.
- Teams need independent deployment and operations now.
- Boundaries cannot be enforced by tests, tooling, or review.

## Tradeoffs

Improves internal clarity but keeps shared runtime coupling. Make module APIs explicit.
