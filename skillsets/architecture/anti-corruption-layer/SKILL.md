---
name: anti-corruption-layer
description: Use when integrating with legacy, vendor, or external models that should not leak into the local domain model
---

# Anti-Corruption Layer

Use an Anti-Corruption Layer when external concepts would corrupt local domain language or invariants.

## References

- `skillsets/shared/references/architecture-decision-rubric.md`
- `skillsets/shared/references/architecture-output-contract.md`

## Fit

- Scale: integrations with mismatched models, legacy systems, or vendors.
- Use when translation rules are repeated or leaking inward.
- Migrate by isolating one external interaction and mapping contract.

## Do Not Use When

- Models already align.
- A simple adapter or mapper is enough.
- Translation rules are not stable or understood.

## Tradeoffs

Adds mapping and maintenance overhead. Keep translation explicit and tested.
