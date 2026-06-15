---
name: layered-architecture
description: Use when code needs clear dependency direction across presentation, application, domain, and infrastructure layers
---

# Layered Architecture

Use Layered Architecture when enforcing dependency direction improves local reasoning.

## References

- `cleaner-code-skillsets/shared/references/architecture-decision-rubric.md`
- `cleaner-code-skillsets/shared/references/architecture-output-contract.md`

## Fit

- Scale: applications with enough surface area to benefit from stable layer roles.
- Use when UI, workflow, domain, and infrastructure concerns are mixed.
- Migrate by untangling one dependency direction at a time.

## Do Not Use When

- The project is small enough that layers add navigation cost.
- Layers are bypassed routinely.
- Domain rules do not need a separate home.

## Tradeoffs

Can slow simple changes and encourage pass-through files. Keep layer boundaries purposeful.
