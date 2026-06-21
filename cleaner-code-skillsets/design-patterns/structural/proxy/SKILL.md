---
name: cleaner-code:proxy
description: Use when access to another object needs controlled lazy loading, authorization, remoting, caching, or instrumentation behind the same interface
---

# Proxy

Use Proxy when access control around an object is the point. Do not use it as a generic wrapper when the client should know the behavior changed.

## References

- `references/pattern-safety-rules.md`
- `references/pattern-output-contract.md`
- `references/refactoring-safety-rules.md`

## Use When

- Lazy loading, authorization, remoting, caching, or instrumentation must preserve the same interface.
- Clients should depend on a stable subject contract.
- Access rules are repeated or leaking into callers.
- Tests can protect delegation, access control, failure, and timing behavior.

## Do Not Use When

- The behavior should be explicit at the call site.
- A decorator, adapter, middleware, or direct helper is clearer.
- The proxy would hide network, security, or caching semantics that affect correctness.
- There is no stable subject interface.
- Only one call site needs a small guard.

## Evidence Checklist

- Cite repeated access-control or delegation logic with file and line references when code is available.
- Name the subject interface and the controlled access behavior.
- Compare Decorator, Adapter, middleware, and direct guard clauses.
- Confirm tests cover allowed access, denied access, delegation, and failure behavior.

## Application Steps

1. Characterize current subject behavior and access rules.
2. Define or confirm the narrow subject interface.
3. Move one access concern into the proxy.
4. Keep proxy construction explicit at the boundary.
5. Re-run focused tests for delegation and access outcomes.

## Output

Follow `references/pattern-output-contract.md`. The final decision must be `Apply pattern`, `Use simpler refactor`, or `Do not change`.
