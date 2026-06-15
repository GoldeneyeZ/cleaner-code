---
name: onion-architecture
description: Use when domain model independence and inward dependency direction need protection from infrastructure and application services
---

# Onion Architecture

Use Onion Architecture when the domain model should sit at the center of dependency direction.

## References

- `cleaner-code-skillsets/shared/references/architecture-decision-rubric.md`
- `cleaner-code-skillsets/shared/references/architecture-output-contract.md`

## Fit

- Scale: domain-centered systems with infrastructure churn.
- Use when domain code imports persistence, UI, or framework concerns.
- Migrate by moving one infrastructure dependency outward behind an interface.

## Do Not Use When

- There is no meaningful domain model.
- Application services are mistaken for domain behavior.
- The onion creates circular mappings and pass-through layers.

## Tradeoffs

Protects domain independence but adds mapping cost. Keep inner layers free of detail dependencies.
