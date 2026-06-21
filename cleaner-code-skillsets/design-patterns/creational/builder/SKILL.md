---
name: cleaner-code:builder
description: Use when constructing an object requires ordered steps, validation, optional parts, or readable assembly beyond what constructors can express
---

# Builder

Use Builder when construction is a meaningful process. Do not use it only to avoid a constructor or to add fluent syntax.

## References

- `references/pattern-safety-rules.md`
- `references/pattern-output-contract.md`
- `references/refactoring-safety-rules.md`

## Use When

- Object construction has multiple optional parts with validation rules.
- Construction order matters or has named phases.
- Call sites repeat long setup sequences.
- Tests can protect validation, defaults, and assembled output.

## Do Not Use When

- A constructor, named constructor, parameter object, or defaults are clearer.
- The object has only a few independent fields.
- Fluent chaining adds style but no safety.
- The builder can create invalid intermediate states without clear checks.
- The construction process is not reused.

## Evidence Checklist

- Cite long or duplicated construction sequences with file and line references when code is available.
- Name the construction rules the builder would centralize.
- Compare parameter object, named constructor, and direct construction.
- Confirm tests cover required fields, defaults, validation, and assembled output.

## Application Steps

1. Protect current construction behavior with focused tests.
2. Extract validation and defaults into one construction path.
3. Introduce the builder with the smallest required API.
4. Migrate duplicated call sites incrementally.
5. Remove obsolete setup helpers after tests pass.

## Output

Follow `references/pattern-output-contract.md`. The final decision must be `Apply pattern`, `Use simpler refactor`, or `Do not change`.
