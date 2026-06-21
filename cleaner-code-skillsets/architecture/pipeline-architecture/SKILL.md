---
name: cleaner-code:pipeline-architecture
description: Use when data or requests move through ordered processing stages that need explicit composition, validation, or transformation
---

# Pipeline Architecture

Use Pipeline Architecture when ordered stages are the core structure.

## References

- `references/architecture-decision-rubric.md`
- `references/architecture-output-contract.md`

## Fit

- Scale: workflows with repeated parse, validate, transform, enrich, or publish stages.
- Use when stage order and failure handling are duplicated.
- Migrate by extracting one stable stage sequence and tests.

## Do Not Use When

- A simple function call sequence is clearer.
- Stages need heavy bidirectional communication.
- Error and rollback policy is undefined.

## Tradeoffs

Clarifies flow but can make debugging cross-stage state harder. Keep stage contracts explicit.
