---
name: cleaner-code:vertical-slice-architecture
description: Use when features should be organized by use case to reduce cross-layer editing and improve local change ownership
---

# Vertical Slice Architecture

Use Vertical Slice Architecture when feature cohesion matters more than horizontal layer grouping.

## References

- `references/architecture-decision-rubric.md`
- `references/architecture-output-contract.md`

## Fit

- Scale: applications where use cases change independently.
- Use when a feature change requires edits across many generic layers.
- Migrate by moving one use case into a cohesive slice.

## Do Not Use When

- Shared domain rules would be duplicated across slices.
- The app is small enough that slices add navigation cost.
- Cross-cutting policy lacks a clear shared home.

## Tradeoffs

Improves feature locality but can duplicate patterns. Extract shared concepts only after repetition is proven.
