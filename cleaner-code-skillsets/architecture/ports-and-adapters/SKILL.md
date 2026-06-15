---
name: ports-and-adapters
description: Use when core use cases need explicit inbound and outbound boundaries around external systems or delivery mechanisms
---

# Ports and Adapters

Use Ports and Adapters to separate core use cases from external mechanisms.

## References

- `cleaner-code-skillsets/shared/references/architecture-decision-rubric.md`
- `cleaner-code-skillsets/shared/references/architecture-output-contract.md`

## Fit

- Scale: applications with meaningful external integrations or multiple entry points.
- Use when external APIs shape core logic.
- Migrate by introducing one outbound port or inbound adapter around a real use case.

## Do Not Use When

- Ports mirror one adapter without policy value.
- A local helper or direct dependency is clearer.
- Boundaries would scatter simple logic.

## Tradeoffs

Adds interfaces and mapping. Keep ports named for core needs, not vendor details.
