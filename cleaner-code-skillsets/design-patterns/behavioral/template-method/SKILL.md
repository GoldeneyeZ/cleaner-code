---
name: cleaner-code:template-method
description: Use when related algorithms share a stable skeleton but need controlled variation in specific steps
---

# Template Method

Use Template Method when the algorithm skeleton is stable and variation points are narrow. Do not use it to force inheritance where composition is clearer.

## References

- `references/pattern-safety-rules.md`
- `references/pattern-output-contract.md`
- `references/refactoring-safety-rules.md`

## Use When

- Several algorithms duplicate the same step order.
- Only specific steps vary.
- The base algorithm can enforce required ordering.
- Tests can protect shared flow and overridden steps.

## Do Not Use When

- Strategy or composition would keep variation simpler.
- The step order is not stable.
- Subclasses would override too many hooks.
- Inheritance would expose internals or create fragile base-class behavior.
- The duplicated logic is small enough for extraction.

## Evidence Checklist

- Cite duplicated algorithm skeletons with file and line references when available.
- Name the invariant steps and variation points.
- Compare Strategy, helper extraction, and composition.
- Confirm tests cover shared ordering, default hooks, and variant behavior.

## Application Steps

1. Characterize the duplicated algorithm flow.
2. Extract the stable skeleton without changing behavior.
3. Introduce narrow hook methods only for real variation.
4. Migrate one variant at a time.
5. Re-run tests for flow order and variant behavior.

## Output

Follow `references/pattern-output-contract.md`. The final decision must be `Apply pattern`, `Use simpler refactor`, or `Do not change`.
