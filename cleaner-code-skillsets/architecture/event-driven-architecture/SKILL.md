---
name: event-driven-architecture
description: Use when decoupled components need to react to business or system events with explicit delivery and consistency tradeoffs
---

# Event-Driven Architecture

Use Event-Driven Architecture when decoupled reaction to events is required and operations can handle the tradeoffs.

## References

- `references/architecture-decision-rubric.md`
- `references/architecture-output-contract.md`

## Fit

- Scale: systems with independent consumers, integrations, or asynchronous workflows.
- Use when direct calls create coupling or availability problems.
- Migrate with one event, one producer, one consumer, and delivery tests.

## Do Not Use When

- Synchronous consistency is required.
- Event ownership, ordering, and retry policy are unclear.
- Events only hide simple local calls.

## Tradeoffs

Adds eventual consistency, observability, and replay concerns. Define idempotency and failure handling.
