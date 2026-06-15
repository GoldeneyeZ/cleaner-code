---
name: decorator
description: Use when behavior must be added around an object dynamically while preserving the same client-facing interface
---

# Decorator

Use Decorator when optional behavior layers need to compose around the same interface. Do not use it for one-off wrappers or hidden side effects.

## References

- `cleaner-code-skillsets/shared/references/pattern-safety-rules.md`
- `cleaner-code-skillsets/shared/references/pattern-output-contract.md`
- `cleaner-code-skillsets/shared/references/refactoring-safety-rules.md`

## Use When

- Multiple optional behaviors wrap the same operation.
- Subclass combinations are multiplying.
- Clients should keep using the same interface.
- Tests can protect ordering, delegation, and failure behavior.

## Do Not Use When

- A direct function call or middleware chain is clearer.
- The wrapper changes the interface.
- The behavior order is implicit or hard to reason about.
- Only one static variant exists.
- The decorator would hide I/O, caching, or retries from callers that need to know.

## Evidence Checklist

- Cite duplicated wrapper behavior or subclass combinations with file and line references when code is available.
- Name the stable interface being preserved.
- Identify each optional behavior and its required order.
- Compare middleware, direct composition, and a simple helper.
- Confirm tests cover delegation, ordering, and error propagation.

## Application Steps

1. Protect current wrapped behavior with focused tests.
2. Extract or confirm the stable component interface.
3. Implement one decorator at a time.
4. Make composition order explicit at the assembly point.
5. Remove duplicated wrapper logic after tests pass.

## Output

Follow `cleaner-code-skillsets/shared/references/pattern-output-contract.md`. The final decision must be `Apply pattern`, `Use simpler refactor`, or `Do not change`.
