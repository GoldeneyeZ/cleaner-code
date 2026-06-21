---
name: cleaner-code:singleton
description: Use when evaluating whether one shared instance is truly required for identity, coordination, or resource ownership constraints
---

# Singleton

Use Singleton with suspicion. Most requests for Singleton are better served by dependency injection, explicit lifetime management, or a module-level value.

## References

- `references/pattern-safety-rules.md`
- `references/pattern-output-contract.md`
- `references/refactoring-safety-rules.md`

## Use When

- Exactly one instance is required for correctness, not convenience.
- The object owns a scarce resource or process-wide coordination point.
- The lifecycle is explicit and test isolation remains possible.
- Tests can protect initialization, teardown, and concurrent access behavior.

## Do Not Use When

- The goal is easy global access.
- Dependency injection or passing an explicit collaborator is feasible.
- Tests would need hidden resets or shared mutable global state.
- Multiple instances might be needed for tenants, tests, workers, or future processes.
- The singleton would hide configuration or ordering dependencies.

## Evidence Checklist

- Cite the resource or identity constraint with file and line references when code is available.
- Prove why multiple instances would be incorrect.
- Compare dependency injection, explicit lifetime scope, and module-level ownership.
- Confirm tests cover lifecycle, reset or teardown, and concurrency when relevant.

## Application Steps

1. Protect current lifecycle behavior with focused tests.
2. Define the narrow access boundary and ownership rules.
3. Prefer explicit injection unless the single-instance invariant is required.
4. If applying Singleton, isolate initialization and teardown.
5. Re-run tests for lifecycle, concurrency, and dependent behavior.

## Output

Follow `references/pattern-output-contract.md`. The final decision must be `Apply pattern`, `Use simpler refactor`, or `Do not change`.
