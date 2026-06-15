---
name: flyweight
description: Use when many objects duplicate immutable intrinsic state and memory or allocation pressure is proven by evidence
---

# Flyweight

Use Flyweight only for proven scale pressure. Do not use it before memory, allocation, or object-count evidence exists.

## References

- `references/pattern-safety-rules.md`
- `references/pattern-output-contract.md`
- `references/refactoring-safety-rules.md`

## Use When

- Many objects duplicate the same immutable intrinsic state.
- Profiling or measurement shows meaningful memory or allocation pressure.
- Extrinsic state can remain outside the shared object.
- Tests can protect identity, equality, and mutation boundaries.

## Do Not Use When

- There is no measured scale problem.
- Shared state might be mutated.
- A cache, enum, interned value, or lookup table is clearer.
- Object creation is not a bottleneck.
- The split between intrinsic and extrinsic state is unclear.

## Evidence Checklist

- Cite object duplication and measurement evidence when available.
- Name intrinsic shared state and extrinsic caller-owned state.
- Compare caching, pooling, enum values, and direct construction.
- Confirm tests cover immutability, identity expectations, and behavior with extrinsic state.

## Application Steps

1. Record baseline memory or allocation evidence.
2. Characterize behavior before sharing state.
3. Extract immutable intrinsic state.
4. Introduce a controlled factory or registry only where needed.
5. Re-run behavior tests and compare the measured pressure.

## Output

Follow `references/pattern-output-contract.md`. The final decision must be `Apply pattern`, `Use simpler refactor`, or `Do not change`.
