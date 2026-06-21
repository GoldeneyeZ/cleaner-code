---
name: cleaner-code:command
description: Use when actions need to be represented as objects for queuing, undo, logging, retries, scheduling, or decoupled invocation
---

# Command

Use Command when an action needs its own identity and lifecycle. Do not use it just to replace a function call with a class.

## References

- `references/pattern-safety-rules.md`
- `references/pattern-output-contract.md`
- `references/refactoring-safety-rules.md`

## Use When

- Actions must be queued, retried, logged, scheduled, serialized, or undone.
- Invokers should not know receiver details.
- Request data and execution behavior need to travel together.
- Tests can protect execution, failure, idempotency, and undo behavior when relevant.

## Do Not Use When

- A direct function or callback is clearer.
- There is no lifecycle beyond immediate invocation.
- The command object would only wrap one method call.
- Receiver dependencies become hidden and hard to test.
- Undo or retry semantics are not defined.

## Evidence Checklist

- Cite repeated invocation, retry, queue, or undo logic with file and line references when available.
- Name the command data, receiver, and execution boundary.
- Compare callbacks, functions, and small request objects.
- Confirm tests cover execution, failure, and lifecycle behavior.

## Application Steps

1. Characterize current action behavior and side effects.
2. Define a minimal command interface.
3. Move one action into a command object.
4. Keep receiver dependencies explicit.
5. Re-run tests for execution and failure paths.

## Output

Follow `references/pattern-output-contract.md`. The final decision must be `Apply pattern`, `Use simpler refactor`, or `Do not change`.
