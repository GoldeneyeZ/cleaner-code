---
name: performance-auditor
description: Use when reviewing latency, throughput, memory, allocation, caching, query, algorithm, and scalability risks
---

# Performance Auditor

Review performance risks. Report findings first, ordered by severity.

## Reference

Use `cleaner-code-skillsets/shared/references/audit-severity-rubric.md`.

## Check

- Algorithmic complexity and repeated work.
- Unbounded memory, allocation, or collection growth.
- Inefficient I/O, queries, or network calls.
- Caching that is missing, stale, or unsafe.
- Performance claims without measurement evidence.

## Output

1. Findings first, ordered by severity, with file and line references when code is available.
2. Open questions or assumptions.
3. Short summary after findings.
