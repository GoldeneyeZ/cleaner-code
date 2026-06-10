# Pattern Safety Rules

Use design patterns only when the code already shows pressure that the pattern directly relieves. A pattern is a tool for reducing proven complexity, not a default destination.

## Required Evidence

Before recommending or applying a pattern, identify:

- The concrete code smell, with file and line references when code is available.
- The behavior that must stay unchanged.
- The simpler refactor that was considered first.
- The cost the pattern adds, including new types, indirection, and maintenance burden.

## Refusal Conditions

Refuse pattern application when:

- The problem is speculative or future-facing.
- A rename, extraction, parameter object, small interface, or direct composition solves it.
- The code lacks tests or characterization for the behavior being moved.
- The pattern would hide business rules behind generic abstractions.
- The implementation would create parallel hierarchies without a stable reason.

## Behavior Protection

Before refactoring:

1. Locate existing tests that cover the behavior.
2. Add characterization tests when coverage is missing.
3. Run the focused test command and record the result.
4. Make the smallest behavior-preserving change.
5. Re-run the same test command.

If tests cannot be added, state the risk and stop before applying the pattern unless the user explicitly accepts the risk.

## Output Requirements

Pattern guidance must end with one of these decisions:

- `Apply pattern`: evidence supports the pattern and tests protect behavior.
- `Use simpler refactor`: a smaller change solves the smell.
- `Do not change`: evidence is insufficient or risk is too high.
