---
name: cleaner-code:observer
description: Use when state changes need to notify multiple dependents without hard-coding those dependents into the subject
---

# Observer

Use Observer when notification decoupling is necessary. Do not use it when explicit calls are clearer and the dependent set is stable.

## References

- `references/pattern-safety-rules.md`
- `references/pattern-output-contract.md`
- `references/refactoring-safety-rules.md`

## Use When

- Multiple dependents react to the same subject change.
- The subject should not know concrete dependent types.
- Dependents can be added or removed at runtime or by composition.
- Tests can protect notification order, filtering, and failure behavior.

## Do Not Use When

- There is one stable dependent.
- Direct method calls make dependencies easier to reason about.
- Notification order, threading, or error handling is undefined.
- Events would hide important business flow.
- A message bus or domain event pattern is the actual architectural need.

## Evidence Checklist

- Cite hard-coded notification or dependent update logic with file and line references when available.
- Name the subject event and observer contract.
- Compare direct calls, callbacks, and domain events.
- Confirm tests cover subscription, unsubscription, ordering, and observer failure.

## Application Steps

1. Characterize current notification behavior.
2. Define the smallest event or observer interface.
3. Move one dependent behind subscription.
4. Make error and ordering policy explicit.
5. Re-run notification tests.

## Output

Follow `references/pattern-output-contract.md`. The final decision must be `Apply pattern`, `Use simpler refactor`, or `Do not change`.
