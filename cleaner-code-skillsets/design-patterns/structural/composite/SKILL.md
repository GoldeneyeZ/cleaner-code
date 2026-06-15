---
name: composite
description: Use when clients need to treat individual objects and object trees uniformly through a stable component contract
---

# Composite

Use Composite when tree structure is already part of the domain and clients need uniform operations over leaves and groups. Do not use it just to store nested data.

## References

- `cleaner-code-skillsets/shared/references/pattern-safety-rules.md`
- `cleaner-code-skillsets/shared/references/pattern-output-contract.md`
- `cleaner-code-skillsets/shared/references/refactoring-safety-rules.md`

## Use When

- Code handles leaves and groups with repeated branching.
- A tree or part-whole relationship is a real domain concept.
- Clients need the same operation across individual and grouped elements.
- Tests can protect traversal, aggregation, and edge cases.

## Do Not Use When

- The structure is a simple list or map.
- Leaves and groups do not share meaningful behavior.
- The composite would hide expensive traversal or mutation semantics.
- A direct recursive function is clearer.
- The tree shape is speculative.

## Evidence Checklist

- Cite repeated leaf/group handling with file and line references when code is available.
- Name the component contract shared by leaves and composites.
- Compare direct recursion, collection helpers, and a simpler interface.
- Confirm tests cover empty groups, nested groups, leaf behavior, and aggregation.

## Application Steps

1. Characterize current leaf and group behavior.
2. Extract the smallest shared component operation.
3. Implement leaf and composite behavior separately.
4. Move traversal or aggregation behind the composite only where useful.
5. Re-run tests for nested and edge-case structures.

## Output

Follow `cleaner-code-skillsets/shared/references/pattern-output-contract.md`. The final decision must be `Apply pattern`, `Use simpler refactor`, or `Do not change`.
