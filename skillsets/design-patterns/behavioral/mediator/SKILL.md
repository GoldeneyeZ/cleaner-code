---
name: mediator
description: Use when many collaborators communicate through tangled direct references and coordination rules need one explicit home
---

# Mediator

Use Mediator when collaboration logic is the problem. Do not use it to create a central object that knows everything.

## References

- `skillsets/shared/references/pattern-safety-rules.md`
- `skillsets/shared/references/pattern-output-contract.md`
- `skillsets/shared/references/refactoring-safety-rules.md`

## Use When

- Multiple peers call each other directly and coordination rules are duplicated.
- Adding a collaborator requires changing many existing collaborators.
- Communication policy should be explicit and testable.
- Tests can protect interaction order and failure behavior.

## Do Not Use When

- There are only two collaborators with a clear dependency direction.
- A domain service, event, or direct dependency is clearer.
- The mediator would become a large procedural controller.
- Collaborators no longer have clear responsibilities.
- The coordination rules are speculative.

## Evidence Checklist

- Cite tangled collaborator calls with file and line references when available.
- Name the coordination rules currently spread across peers.
- Compare direct dependency cleanup, events, and service extraction.
- Confirm tests cover collaborator interactions and error paths.

## Application Steps

1. Characterize current collaboration behavior.
2. Extract one coordination rule into a mediator.
3. Keep collaborator responsibilities intact.
4. Replace direct peer calls incrementally.
5. Re-run interaction and failure tests.

## Output

Follow `skillsets/shared/references/pattern-output-contract.md`. The final decision must be `Apply pattern`, `Use simpler refactor`, or `Do not change`.
