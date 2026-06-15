---
name: hexagonal-architecture
description: Use when application core logic needs clearer boundaries from delivery mechanisms, persistence, or external services
---

# Hexagonal Architecture

Use Hexagonal Architecture when external adapters are distorting core application logic.

## References

- `cleaner-code-skillsets/shared/references/architecture-decision-rubric.md`
- `cleaner-code-skillsets/shared/references/architecture-output-contract.md`

## Fit

- Scale: applications with multiple inbound or outbound adapters.
- Use when framework, database, or service details leak into core use cases.
- Migrate by defining one port from an existing use case.

## Do Not Use When

- There is one simple delivery path and one simple storage path.
- Ports mirror adapters without policy value.
- The team will not maintain adapter boundaries.

## Tradeoffs

Adds port and adapter structure. Keep ports driven by core needs, not infrastructure names.
