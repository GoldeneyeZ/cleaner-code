---
name: memento
description: Use when object state needs explicit snapshots for undo, rollback, or restore without exposing internal representation
---

# Memento

Use Memento when snapshots are required and internal state should remain encapsulated. Do not use it for casual cloning or broad persistence.

## References

- `skillsets/shared/references/pattern-safety-rules.md`
- `skillsets/shared/references/pattern-output-contract.md`
- `skillsets/shared/references/refactoring-safety-rules.md`

## Use When

- Undo, rollback, or restore is a current requirement.
- State can be captured safely without exposing internals.
- Snapshot size, lifecycle, and ownership are understood.
- Tests can protect restore, identity, and invalid snapshot behavior.

## Do Not Use When

- Recomputing state is simpler.
- Event sourcing, persistence, or transaction rollback is the real need.
- Snapshots would expose mutable internals.
- State includes resources that cannot be restored safely.
- Memory cost is unknown and potentially high.

## Evidence Checklist

- Cite current undo, rollback, or state-copying logic with file and line references when available.
- Name state included in and excluded from the snapshot.
- Compare copy methods, transactions, and event logs.
- Confirm tests cover capture, restore, invalid snapshots, and resource boundaries.

## Application Steps

1. Characterize current state transitions.
2. Define snapshot ownership and lifecycle.
3. Add a minimal memento representation.
4. Restore through the originator without exposing internals.
5. Re-run tests for restore and edge cases.

## Output

Follow `skillsets/shared/references/pattern-output-contract.md`. The final decision must be `Apply pattern`, `Use simpler refactor`, or `Do not change`.
