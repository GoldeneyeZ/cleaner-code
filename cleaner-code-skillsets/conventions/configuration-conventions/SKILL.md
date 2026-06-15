---
name: configuration-conventions
description: Use when environment variables, config files, defaults, secrets, feature flags, or runtime options should match local conventions
---

# Configuration Conventions

Discover local style before recommending changes.

## Reference

Use `references/convention-discovery.md`.

## Check

- Existing config loading, naming, defaults, and validation.
- Secret handling and environment-specific overrides.
- Feature flag and runtime option patterns.

## Recommend

- Keep configuration explicit and validated.
- Match local naming and default behavior.
- Avoid config that changes behavior invisibly.
