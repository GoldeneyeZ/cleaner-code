# Context GD-003: Representative Pattern Skills

Last updated: 2026-06-10 17:39

## Task

Create one representative design pattern skill from each family:
- behavioral: strategy
- creational: factory method
- structural: adapter

Review the three skills for consistent structure, refusal criteria, testing expectations, and output contract.

## Current Status

Done. The representative Strategy, Factory Method, and Adapter pattern skills have been created and reviewed.

## Files To Create Or Update

- `skillsets/design-patterns/behavioral/strategy/SKILL.md`
- `skillsets/design-patterns/creational/factory-method/SKILL.md`
- `skillsets/design-patterns/structural/adapter/SKILL.md`
- `docs/plan/goal-progression.md`
- `docs/plan/context-GD-003.md`

## Handoff Notes

The next loop should read `docs/plan/goal-progression.md`, select GD-004, and create `skillsets/design-patterns/creational/abstract-factory/SKILL.md`.

Each representative skill should follow the shared pattern safety rules, selection rubric, and output contract. Each must refuse itself when the pattern is not justified.

## Validation To Record

- File existence:
  `find skillsets/design-patterns/behavioral/strategy skillsets/design-patterns/creational/factory-method skillsets/design-patterns/structural/adapter -name SKILL.md -type f | sort`
  returned all three representative files.
- Frontmatter:
  `rg -n "^name: |^description: Use when" ...`
  found `name` and trigger-oriented `description` entries for Strategy, Factory Method, and Adapter.
- Refusal criteria, behavior protection, and output contract:
  `rg -n "## Do Not Use When|Use simpler refactor|Do not change|tests|characterization|pattern-output-contract" ...`
  found the required sections and terms across all three files.
- Generated-text scan returned no matches for unresolved markers or bracket-slot text.
- Consistency review:
  `rg -n "^## " ...`
  showed the same section structure in all three representative skills: References, Use When, Do Not Use When, Evidence Checklist, Application Steps, and Output.

## Open Risks

- Later pattern skills should follow the representative section structure unless a pattern needs a narrowly justified variation.
