---
name: adapter
description: Use when existing code must integrate an incompatible interface while preserving the client contract or external dependency boundary
---

# Adapter

Use Adapter when a client expects one interface and an existing collaborator exposes another interface that cannot or should not be changed. Do not use it as a generic wrapper.

## References

- `references/pattern-safety-rules.md`
- `references/pattern-output-contract.md`
- `references/refactoring-safety-rules.md`

## Use When

- A client contract is stable but a collaborator has an incompatible API.
- An external library, legacy module, or service boundary should stay isolated.
- Translation between models or protocols is required.
- Tests can protect client behavior and mapping rules.

## Do Not Use When

- Both interfaces are under local control and one can be renamed or simplified.
- The wrapper only forwards calls without translation or boundary value.
- The mismatch is caused by poor local naming.
- A direct function or mapper would be clearer.
- The adapter would conceal important errors or semantics.

## Evidence Checklist

- Cite the incompatible interfaces with file and line references when code is available.
- Identify the client contract that should remain stable.
- Identify the collaborator boundary that should not leak inward.
- Compare renaming, direct mapping, and changing the local interface.
- Confirm tests cover mapping, error handling, and client behavior.

## Application Steps

1. Characterize current client behavior and interface mapping.
2. Define the narrow client-facing interface.
3. Implement translation in one adapter.
4. Keep external dependency details inside the adapter.
5. Re-run focused tests and remove leaked boundary logic.

## Output

Follow `references/pattern-output-contract.md`. The final decision must be `Apply pattern`, `Use simpler refactor`, or `Do not change`.
