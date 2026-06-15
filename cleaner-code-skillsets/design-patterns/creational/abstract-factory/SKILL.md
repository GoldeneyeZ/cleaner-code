---
name: abstract-factory
description: Use when families of related objects must vary together by platform, environment, tenant, or product line without mixing incompatible products
---

# Abstract Factory

Use Abstract Factory when clients need families of related products that must be created together. Do not use it for a single product type or speculative product families.

## References

- `references/pattern-safety-rules.md`
- `references/pattern-output-contract.md`
- `references/refactoring-safety-rules.md`

## Use When

- Multiple related product types must be selected as a compatible family.
- Client code currently mixes platform, tenant, or environment-specific constructors.
- Product families change independently from client workflows.
- Tests can protect product compatibility and client behavior.

## Do Not Use When

- Only one product type varies.
- A simple factory function or dependency injection is clearer.
- Compatibility between products is not a real constraint.
- Product families are imagined future variants.
- The abstraction would duplicate constructors without reducing client branching.

## Evidence Checklist

- Cite mixed or duplicated family creation with file and line references when code is available.
- Name each product family and the compatibility rule.
- Identify clients that should stop choosing concrete products.
- Compare Factory Method, direct dependency injection, and a simple factory.
- Confirm tests cover family selection and incompatible combinations.

## Application Steps

1. Protect current product-family behavior with focused tests.
2. Define the narrow product interfaces clients already use.
3. Introduce one factory interface for the related product family.
4. Move one family behind the factory at a time.
5. Remove client-side family branching after tests pass.

## Output

Follow `references/pattern-output-contract.md`. The final decision must be `Apply pattern`, `Use simpler refactor`, or `Do not change`.
