---
name: clean-architecture
description: Use when business rules need stable independence from frameworks, UI, databases, and external delivery mechanisms
---

# Clean Architecture

Use Clean Architecture when business rules are valuable enough to protect from outer details.

## References

- `references/architecture-decision-rubric.md`
- `references/architecture-output-contract.md`

## Fit

- Scale: systems with durable domain rules and changing frameworks or integrations.
- Use when dependency direction currently points inward to details.
- Migrate by isolating one use case and its boundary models.

## Do Not Use When

- The app is mostly framework glue or CRUD screens.
- Layer count would exceed domain complexity.
- Boundary models only duplicate data structures.

## Tradeoffs

Adds mapping and structure. Keep boundaries meaningful and avoid ceremony-only layers.
