---
name: cleaner-code:iterator
description: Use when clients need sequential traversal over a collection without depending on its internal representation
---

# Iterator

Use Iterator when traversal must be decoupled from collection internals. Do not use it when native language iteration already communicates the intent.

## References

- `references/pattern-safety-rules.md`
- `references/pattern-output-contract.md`
- `references/refactoring-safety-rules.md`

## Use When

- Clients duplicate traversal over a nontrivial internal structure.
- The collection representation should remain hidden.
- Multiple traversal orders are real requirements.
- Tests can protect order, boundary, and mutation behavior.

## Do Not Use When

- A language-native iterator, generator, or collection API is enough.
- Traversal is a simple loop over a public list.
- Exposing iteration would leak unstable internals.
- Mutation during traversal is undefined.
- The only goal is making code look pattern-based.

## Evidence Checklist

- Cite duplicated traversal or representation leakage with file and line references when available.
- Name the collection boundary and traversal order.
- Compare native iteration, generators, and simple collection methods.
- Confirm tests cover empty, single, multiple, and mutation cases.

## Application Steps

1. Characterize current traversal behavior.
2. Define the smallest traversal contract.
3. Move traversal state out of clients.
4. Preserve collection invariants.
5. Re-run tests for order and edge cases.

## Output

Follow `references/pattern-output-contract.md`. The final decision must be `Apply pattern`, `Use simpler refactor`, or `Do not change`.
