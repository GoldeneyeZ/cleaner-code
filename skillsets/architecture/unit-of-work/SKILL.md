---
name: unit-of-work
description: Use when multiple repository or persistence operations must commit or roll back as one explicit consistency boundary
---

# Unit of Work

Use Unit of Work when coordinating persistence changes is a real consistency requirement.

## References

- `skillsets/shared/references/architecture-decision-rubric.md`
- `skillsets/shared/references/architecture-output-contract.md`

## Fit

- Scale: workflows spanning multiple aggregates, repositories, or writes.
- Use when partial commits create correctness risk.
- Migrate by wrapping one transactional workflow and testing commit and rollback.

## Do Not Use When

- Each operation is already atomic.
- The storage layer already provides a clear transaction boundary.
- The pattern would obscure transaction lifetime.

## Tradeoffs

Adds lifecycle complexity. Make ownership, nesting, and failure behavior explicit.
