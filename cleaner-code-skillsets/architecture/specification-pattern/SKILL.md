---
name: cleaner-code:specification-pattern
description: Use when business rules need composable predicates for validation, selection, or policy without scattering conditionals
---

# Specification Pattern

Use Specification when business predicates need names, composition, and reuse. Do not use it for one-off conditions.

## References

- `references/architecture-decision-rubric.md`
- `references/architecture-output-contract.md`

## Fit

- Scale: domains with repeated, composable eligibility or policy rules.
- Use when predicates are duplicated across validation, filtering, or decisions.
- Migrate by extracting one named rule with characterization tests.

## Do Not Use When

- A direct conditional is clearer.
- Rules need database translation but no translation strategy exists.
- Composition would hide important business wording.

## Tradeoffs

Improves rule reuse but can create abstraction-heavy predicate trees. Keep rule names domain-specific.
