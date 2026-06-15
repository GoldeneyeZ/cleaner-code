# Refactoring Safety Rules

Refactoring must preserve behavior while improving structure.

## Before Changing Code

1. Identify the behavior that must remain unchanged.
2. Find the tests that protect it.
3. Add characterization tests when behavior is untested.
4. Record the focused verification command.
5. Choose the smallest structural move that advances the goal.

## During Refactoring

- Keep behavior and structure changes separate when possible.
- Prefer small commits or clear checkpoints.
- Preserve public APIs unless the task explicitly changes them.
- Avoid broad formatting churn.
- Stop when tests fail for an unclear reason and diagnose before continuing.

## After Refactoring

Verify:

- Focused tests pass.
- Broader relevant tests pass when the change crosses boundaries.
- The new structure removes the named smell.
- The change did not introduce unused abstraction.

## Escalation

If behavior cannot be protected with tests, report the gap and ask before making high-risk changes.
