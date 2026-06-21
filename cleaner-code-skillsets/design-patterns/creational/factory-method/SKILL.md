---
name: cleaner-code:factory-method
description: Use when object creation varies by stable policy or subtype and callers should depend on a creator hook instead of concrete constructors
---

# Factory Method

Use Factory Method when creation logic varies in subclasses or creator implementations while callers can stay coupled to a common product contract. Do not use it to hide ordinary constructor calls.

## References

- `references/pattern-safety-rules.md`
- `references/pattern-output-contract.md`
- `references/refactoring-safety-rules.md`

## Use When

- A creator must choose a concrete product while exposing a stable product interface.
- Subclasses or implementations need to customize creation without changing client flow.
- Creation branching is duplicated across clients.
- Product construction has behavior that tests can characterize.

## Do Not Use When

- A direct constructor, static helper, or dependency injection is clearer.
- The only issue is a long constructor parameter list.
- Product types do not share a meaningful contract.
- Creation variation is speculative.
- The factory would only mirror constructors without simplifying callers.

## Evidence Checklist

- Cite duplicated or unstable creation logic with file and line references when code is available.
- Identify the product contract clients should depend on.
- Name the creation policy that varies.
- Compare direct construction, dependency injection, and a simple factory function.
- Confirm tests cover product selection and client behavior.

## Application Steps

1. Protect existing creation behavior with focused tests.
2. Extract the smallest product contract clients already use.
3. Introduce the factory method at the creator boundary.
4. Move one product creation path at a time.
5. Remove duplicated creation branches after tests pass.

## Output

Follow `references/pattern-output-contract.md`. The final decision must be `Apply pattern`, `Use simpler refactor`, or `Do not change`.
