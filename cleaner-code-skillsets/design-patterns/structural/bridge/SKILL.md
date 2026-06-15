---
name: bridge
description: Use when an abstraction and its implementation vary independently and inheritance or conditionals are coupling both dimensions
---

# Bridge

Use Bridge when two dimensions of change are tangled and both need independent variation. Do not use it to split a class without evidence of independent axes.

## References

- `references/pattern-safety-rules.md`
- `references/pattern-output-contract.md`
- `references/refactoring-safety-rules.md`

## Use When

- A class hierarchy is growing across two independent dimensions.
- Conditionals combine high-level operations with platform, backend, or renderer details.
- Clients should depend on an abstraction while implementations vary separately.
- Tests can protect behavior across both dimensions.

## Do Not Use When

- There is only one implementation dimension.
- A simple interface extraction or dependency injection is enough.
- The abstraction and implementation change together.
- The split would create parallel types with no current variation.
- The bridge hides important implementation constraints from callers.

## Evidence Checklist

- Cite the tangled dimensions with file and line references when code is available.
- Name the abstraction axis and implementation axis.
- Compare interface extraction, composition, and Strategy.
- Confirm tests cover representative combinations across both axes.

## Application Steps

1. Protect current behavior for each relevant combination.
2. Extract the implementation interface from actual calls.
3. Move implementation details behind that interface.
4. Keep the abstraction focused on client operations.
5. Remove duplicated conditionals after tests pass.

## Output

Follow `references/pattern-output-contract.md`. The final decision must be `Apply pattern`, `Use simpler refactor`, or `Do not change`.
