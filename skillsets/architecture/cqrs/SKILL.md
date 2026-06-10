---
name: cqrs
description: Use when read and write models have proven different scale, consistency, authorization, or shape requirements
---

# CQRS

Use CQRS when separating commands and queries solves a present pressure. Do not split models by default.

## References

- `skillsets/shared/references/architecture-decision-rubric.md`
- `skillsets/shared/references/architecture-output-contract.md`

## Fit

- Scale: systems where reads and writes differ materially.
- Use when one model causes performance, security, or consistency compromises.
- Migrate by separating one hot read or command path first.

## Do Not Use When

- Reads and writes share simple CRUD needs.
- Eventual consistency is not acceptable or understood.
- The split would duplicate logic without benefit.

## Tradeoffs

Adds synchronization and consistency complexity. State stale-read behavior explicitly.
