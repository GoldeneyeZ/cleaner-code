# Context GD-006: Behavioral Pattern Skills

Last updated: 2026-06-10 17:39

## Task

Create the behavioral design pattern skills and verify the full behavioral family has valid frontmatter and refusal criteria.

## Current Status

Done. The full behavioral pattern family has been created and verified.

## Files To Create Or Update

- `skillsets/design-patterns/behavioral/chain-of-responsibility/SKILL.md`
- `skillsets/design-patterns/behavioral/command/SKILL.md`
- `skillsets/design-patterns/behavioral/iterator/SKILL.md`
- `skillsets/design-patterns/behavioral/mediator/SKILL.md`
- `skillsets/design-patterns/behavioral/memento/SKILL.md`
- `skillsets/design-patterns/behavioral/observer/SKILL.md`
- `skillsets/design-patterns/behavioral/state/SKILL.md`
- `skillsets/design-patterns/behavioral/strategy/SKILL.md`
- `skillsets/design-patterns/behavioral/template-method/SKILL.md`
- `skillsets/design-patterns/behavioral/visitor/SKILL.md`
- `docs/plan/goal-progression.md`
- `docs/plan/context-GD-006.md`

## Handoff Notes

The next loop should read `docs/plan/goal-progression.md`, select GD-007, and create `skillsets/auditors/code-quality-auditor/SKILL.md`.

All behavioral pattern skills should follow the representative Strategy structure unless a pattern-specific section is justified.

## Validation To Record

- File existence:
  `find skillsets/design-patterns/behavioral -mindepth 2 -maxdepth 2 -name SKILL.md -type f | sort`
  returned all ten behavioral skill files.
- Frontmatter:
  `rg -n "^name: |^description: Use when" skillsets/design-patterns/behavioral/*/SKILL.md`
  found `name` and trigger-oriented `description` entries for all ten skills.
- Refusal criteria, behavior protection, and output contract:
  `rg -n "## Do Not Use When|tests|characterization|pattern-output-contract|Use simpler refactor|Do not change" skillsets/design-patterns/behavioral/*/SKILL.md`
  found refusal sections, test or characterization expectations, and output-contract references.
- Generated-text scan across behavioral skills returned no matches for unresolved markers or bracket-slot text.

## Open Risks

- Future installer or packaging work should include all ten behavioral skills.
