---
name: prototype
description: Use when new objects should be created by copying configured exemplars while preserving complex setup or runtime-selected variants
---

# Prototype

Use Prototype when copying an existing configured object is safer or clearer than rebuilding it. Do not use it as a substitute for understanding object construction.

## References

- `skillsets/shared/references/pattern-safety-rules.md`
- `skillsets/shared/references/pattern-output-contract.md`
- `skillsets/shared/references/refactoring-safety-rules.md`

## Use When

- Object setup is expensive, complex, or runtime-configured.
- Variants are best represented as configured exemplars.
- Rebuilding from constructors duplicates setup logic.
- Tests can protect clone independence and copied state.

## Do Not Use When

- A constructor, factory, or copy method is clearer.
- Object identity, resources, or ownership make copying unsafe.
- Shallow copying would share mutable state accidentally.
- The prototype registry would hide important configuration.
- The only goal is avoiding constructor parameters.

## Evidence Checklist

- Cite duplicated setup or costly construction with file and line references when code is available.
- Identify which state must be copied and which must be reset.
- Compare copy constructor, factory, and explicit clone method.
- Confirm tests cover independence, identity, mutable state, and resource handling.

## Application Steps

1. Characterize current setup and copy expectations.
2. Define explicit clone semantics for state, identity, and resources.
3. Introduce the prototype boundary for one exemplar.
4. Migrate repeated setup to cloning only where semantics are safe.
5. Re-run tests that cover copy independence and behavior.

## Output

Follow `skillsets/shared/references/pattern-output-contract.md`. The final decision must be `Apply pattern`, `Use simpler refactor`, or `Do not change`.
