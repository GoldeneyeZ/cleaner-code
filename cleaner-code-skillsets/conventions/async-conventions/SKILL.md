---
name: async-conventions
description: Use when async code, promises, tasks, callbacks, cancellation, timeouts, or concurrency style should match local practice
---

# Async Conventions

Discover local style before recommending changes.

## Reference

Use `references/convention-discovery.md`.

## Check

- Existing async primitives, naming, and error handling.
- Cancellation, timeout, retry, and backpressure patterns.
- Test conventions for async behavior.

## Recommend

- Match local async control-flow style.
- Make cancellation and failure behavior explicit.
- Avoid timing assumptions in tests.
