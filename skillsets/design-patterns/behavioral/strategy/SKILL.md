---
name: strategy
description: Use when existing code has multiple interchangeable algorithms selected by conditionals, configuration, type checks, or duplicated variants
---

# Strategy

Use Strategy only when callers need to choose between interchangeable algorithms through a stable interface. Do not use it just to make a small conditional look more object-oriented.

## References

- `skillsets/shared/references/pattern-safety-rules.md`
- `skillsets/shared/references/pattern-output-contract.md`
- `skillsets/shared/references/refactoring-safety-rules.md`

## Use When

- A conditional selects among algorithms that share the same inputs and outputs.
- Multiple classes duplicate the same operation with small algorithm differences.
- The selection rule changes independently from the algorithms.
- Tests can protect the current behavior before moving logic.

## Do Not Use When

- There are only one or two simple branches and extraction would be clearer.
- The variants do not share a stable interface.
- The real problem is unclear naming or misplaced data.
- The algorithm set is speculative.
- Adding classes would hide simple business rules.

## Evidence Checklist

- Cite the branching or duplication with file and line references when code is available.
- Name the algorithms and the shared contract they already imply.
- Identify how the strategy is selected.
- Compare a simpler extraction or guard-clause refactor.
- Confirm tests or characterization cover each current variant.

## Application Steps

1. Add or identify tests for each existing algorithm variant.
2. Define the narrow strategy interface from current call sites.
3. Move one algorithm at a time behind the interface.
4. Keep selection logic explicit in one place.
5. Remove obsolete conditionals only after equivalent tests pass.

## Output

Follow `skillsets/shared/references/pattern-output-contract.md`. The final decision must be `Apply pattern`, `Use simpler refactor`, or `Do not change`.
