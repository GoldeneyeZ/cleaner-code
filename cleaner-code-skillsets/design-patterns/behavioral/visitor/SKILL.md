---
name: cleaner-code:visitor
description: Use when many operations must run across a stable object structure without putting every operation on each element type
---

# Visitor

Use Visitor when the element structure is stable but operations over it vary. Do not use it when adding element types is common.

## References

- `references/pattern-safety-rules.md`
- `references/pattern-output-contract.md`
- `references/refactoring-safety-rules.md`

## Use When

- Many operations traverse the same stable element hierarchy.
- Adding operations is more common than adding element types.
- Type checks or duplicated traversal are spreading across clients.
- Tests can protect traversal, dispatch, and each operation.

## Do Not Use When

- New element types are frequent.
- A simple polymorphic method belongs on the elements.
- Pattern matching or direct functions are clearer in the language.
- The visitor would expose internal element details.
- The hierarchy is not stable.

## Evidence Checklist

- Cite repeated type checks or traversal with file and line references when available.
- Name the stable element types and operation families.
- Compare polymorphism, pattern matching, and external functions.
- Confirm tests cover each element type, each operation, and traversal behavior.

## Application Steps

1. Characterize existing operations over the element structure.
2. Define the minimal visitor interface for current element types.
3. Move one operation into a visitor.
4. Keep traversal ownership explicit.
5. Re-run operation and dispatch tests.

## Output

Follow `references/pattern-output-contract.md`. The final decision must be `Apply pattern`, `Use simpler refactor`, or `Do not change`.
