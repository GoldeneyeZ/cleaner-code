# Context GD-002: Design Pattern Advisor

Last updated: 2026-06-10 17:39

## Task

Create the design pattern advisor skill that helps Codex decide whether a pattern is justified, recommends simpler refactors when appropriate, and routes justified cases to creational, structural, or behavioral pattern skills.

## Current Status

Done. The pattern advisor skill has been created and verified against all GD-002 requirements.

## Files To Create Or Update

- `cleaner-code-skillsets/design-patterns/advisors/pattern-advisor/SKILL.md`
- `docs/plan/goal-progression.md`
- `docs/plan/context-GD-002.md`

## Handoff Notes

The next loop should read `docs/plan/goal-progression.md`, select GD-003, and create `cleaner-code-skillsets/design-patterns/behavioral/strategy/SKILL.md`.

The advisor should use the shared pattern safety rules, selection rubric, and output contract. It must be able to recommend no pattern when a smaller refactor fits.

## Validation To Record

- File existence:
  `test -f cleaner-code-skillsets/design-patterns/advisors/pattern-advisor/SKILL.md` exited `0`.
- Frontmatter:
  `sed -n '1,12p' cleaner-code-skillsets/design-patterns/advisors/pattern-advisor/SKILL.md`
  showed `name: pattern-advisor` and a `description` starting with `Use when`.
- No-pattern and simpler-refactor support:
  `rg -n "Do not use a pattern|Use simpler refactor|smaller refactor|no pattern" cleaner-code-skillsets/design-patterns/advisors/pattern-advisor/SKILL.md`
  found the decision labels and simpler-refactor checks.
- Pattern family routing:
  `rg -n "creational|structural|behavioral" cleaner-code-skillsets/design-patterns/advisors/pattern-advisor/SKILL.md`
  found all three routing families in the description and output decisions.

## Open Risks

- Future pattern skills should preserve the advisor's gatekeeping role instead of bypassing it with direct pattern application.
