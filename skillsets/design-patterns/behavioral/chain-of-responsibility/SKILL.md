---
name: chain-of-responsibility
description: Use when a request may be handled by one of several ordered handlers and sender code should not know which handler applies
---

# Chain of Responsibility

Use Chain of Responsibility when request handling is naturally delegated through an ordered set of handlers. Do not use it to obscure simple conditionals.

## References

- `skillsets/shared/references/pattern-safety-rules.md`
- `skillsets/shared/references/pattern-output-contract.md`
- `skillsets/shared/references/refactoring-safety-rules.md`

## Use When

- Multiple handlers can process, reject, or pass along the same request.
- Handler order is meaningful and already appears in branching logic.
- Senders should not depend on concrete handler selection.
- Tests can protect handled, unhandled, and ordering behavior.

## Do Not Use When

- A direct conditional or map lookup is clearer.
- Every handler always runs; use a pipeline instead.
- Handler order is unclear or accidental.
- Failures would be hidden by silent pass-through.
- The request shape is not stable.

## Evidence Checklist

- Cite the branching or duplicated handler selection with file and line references when available.
- Name the request contract and each current handler.
- Compare guard clauses, dispatch maps, and pipelines.
- Confirm tests cover order, stop conditions, and unhandled requests.

## Application Steps

1. Characterize current request handling behavior.
2. Define the narrow request and handler contract.
3. Move one handler at a time into the chain.
4. Make ordering explicit at assembly.
5. Re-run focused tests for handling and pass-through cases.

## Output

Follow `skillsets/shared/references/pattern-output-contract.md`. The final decision must be `Apply pattern`, `Use simpler refactor`, or `Do not change`.
