---
name: cleaner-code:concurrency-auditor
description: Use when reviewing async behavior, locking, shared state, races, deadlocks, ordering, cancellation, and parallel execution risk
---

# Concurrency Auditor

Review concurrency risks. Report findings first, ordered by severity.

## Reference

Use `references/audit-severity-rubric.md`.

## Check

- Races on shared mutable state.
- Deadlocks, lock ordering, and missed unlocks.
- Missing cancellation, timeout, or backpressure handling.
- Assumptions about callback, task, or event ordering.
- Tests that cannot expose concurrent failure modes.

## Output

1. Findings first, ordered by severity, with file and line references when code is available.
2. Open questions or assumptions.
3. Short summary after findings.
