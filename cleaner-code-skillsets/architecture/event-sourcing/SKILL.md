---
name: cleaner-code:event-sourcing
description: Use when durable event history, auditability, temporal reconstruction, or replay is a core business requirement
---

# Event Sourcing

Use Event Sourcing when history is the source of truth. Do not use it only because events sound flexible.

## References

- `references/architecture-decision-rubric.md`
- `references/architecture-output-contract.md`

## Fit

- Scale: domains where audit, replay, or temporal state matters.
- Use when current-state persistence loses required business facts.
- Migrate with one aggregate stream and replay tests.

## Do Not Use When

- Current state is enough.
- Event schema evolution and replay operations are not supported.
- The team cannot operate projections and rebuilds.

## Tradeoffs

Adds event versioning, projection lag, and operational complexity. Define replay and migration policy early.
