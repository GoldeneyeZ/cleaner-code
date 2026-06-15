---
name: state
description: Use when an object's behavior changes by lifecycle state and conditionals for state-specific behavior are growing or duplicated
---

# State

Use State when lifecycle state changes behavior enough to deserve separate state objects. Do not use it for a small enum with simple checks.

## References

- `cleaner-code-skillsets/shared/references/pattern-safety-rules.md`
- `cleaner-code-skillsets/shared/references/pattern-output-contract.md`
- `cleaner-code-skillsets/shared/references/refactoring-safety-rules.md`

## Use When

- Many methods branch on the same state.
- Transitions have rules that are duplicated or hard to test.
- State-specific behavior changes independently.
- Tests can protect transitions, invalid operations, and behavior in each state.

## Do Not Use When

- A simple state enum and guard clauses are clearer.
- There are few states with little behavior.
- Transitions are not well defined.
- State objects would need to reach deeply into the context.
- The pattern would hide business rules from the domain model.

## Evidence Checklist

- Cite repeated state conditionals with file and line references when available.
- Name each state, transition, and state-specific behavior.
- Compare guard clauses, transition tables, and Strategy.
- Confirm tests cover valid transitions, invalid transitions, and per-state behavior.

## Application Steps

1. Characterize current state behavior and transitions.
2. Extract one state-specific behavior behind a state interface.
3. Move transitions incrementally.
4. Keep context responsibilities narrow.
5. Re-run transition and per-state tests.

## Output

Follow `cleaner-code-skillsets/shared/references/pattern-output-contract.md`. The final decision must be `Apply pattern`, `Use simpler refactor`, or `Do not change`.
