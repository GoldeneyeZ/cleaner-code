# Convention Discovery

Convention skills must discover local style before recommending changes.

## Discovery Sources

Inspect the smallest useful set of sources:

- Existing files in the same directory or module.
- Tests near the changed code.
- Project configuration for linters, formatters, or type checkers.
- Contributor docs, README files, and existing style guides.
- Recent similar changes when available.

## Discovery Questions

- How are names, modules, errors, tests, and boundaries already shaped?
- Which rules are enforced by tooling and which are only conventions?
- Are there multiple local styles because of age, framework, or ownership boundaries?
- Does the requested change touch code that should preserve a legacy style for consistency?

## Recommendation Rules

- Prefer local consistency over a generic external rule.
- Call out conflicts between local style and broader best practice.
- Make narrow recommendations tied to touched code.
- Avoid rewriting unrelated areas to satisfy a convention.
- When evidence is mixed, state the dominant pattern and the exception.
