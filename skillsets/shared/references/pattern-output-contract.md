# Pattern Output Contract

Pattern skills must produce decision-focused guidance that a reviewer can audit.

## Required Sections

1. `Decision`: apply the pattern, use a simpler refactor, or do not change.
2. `Evidence`: cite the code smell, relevant files, and behavior at risk.
3. `Rejected Alternatives`: name simpler options considered and why they do or do not fit.
4. `Implementation Plan`: list small behavior-preserving steps.
5. `Test Plan`: name existing or new tests that protect the behavior.
6. `Risks`: call out new abstraction, migration, or readability costs.

## Review Rules

- Findings and decisions come before explanation.
- File and line references are required when reviewing existing code.
- Avoid pattern vocabulary unless it clarifies the change.
- Do not provide a large implementation before proving the pattern is justified.
- Prefer examples that mirror the local codebase over generic textbook examples.

## Final Decision Labels

Use exactly one final label:

- `Apply pattern`
- `Use simpler refactor`
- `Do not change`
