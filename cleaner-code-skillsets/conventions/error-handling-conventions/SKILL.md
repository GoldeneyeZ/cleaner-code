---
name: cleaner-code:error-handling-conventions
description: Use when errors, exceptions, retries, fallbacks, messages, or result types should match local handling style
---

# Error Handling Conventions

Discover local style before recommending changes.

## Reference

Use `references/convention-discovery.md`.

## Check

- Nearby exception, result, retry, and fallback patterns.
- Error message tone, structure, and user-facing detail.
- Logging, wrapping, and propagation conventions.

## Recommend

- Preserve actionable context without leaking internals.
- Align with local recovery and retry policy.
- Keep error contracts consistent for callers.
