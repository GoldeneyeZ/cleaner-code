# Context GD-001: Shared Foundation

Last updated: 2026-06-10 17:39

## Task

Create the shared foundation for the cleaner-code skill suite:
- base skillset directories
- shared references
- reusable skill templates

## Current Status

Done. The base skillset directory structure, shared references, and reusable templates have been created and verified.

## Files To Create Or Update

- `skillsets/auditors/`
- `skillsets/design-patterns/`
- `skillsets/architecture/`
- `skillsets/conventions/`
- `skillsets/shared/references/`
- `skillsets/shared/templates/`
- `docs/plan/goal-progression.md`
- `docs/plan/context-GD-001.md`

Created shared reference files:
- `skillsets/shared/references/pattern-safety-rules.md`
- `skillsets/shared/references/pattern-output-contract.md`
- `skillsets/shared/references/pattern-selection-rubric.md`
- `skillsets/shared/references/audit-severity-rubric.md`
- `skillsets/shared/references/convention-discovery.md`
- `skillsets/shared/references/architecture-decision-rubric.md`
- `skillsets/shared/references/architecture-output-contract.md`
- `skillsets/shared/references/refactoring-safety-rules.md`
- `skillsets/shared/references/skill-frontmatter-contract.md`

Created shared template files:
- `skillsets/shared/templates/design-pattern-skill-template.md`
- `skillsets/shared/templates/auditor-skill-template.md`
- `skillsets/shared/templates/convention-skill-template.md`
- `skillsets/shared/templates/architecture-skill-template.md`

## Handoff Notes

The next loop should read `docs/plan/goal-progression.md`, select GD-002, and create `skillsets/design-patterns/advisors/pattern-advisor/SKILL.md`.

Shared references are intentionally concise. They define reusable contracts and rubrics without duplicating every individual skill.

## Validation To Record

- Directory listing showing expected shared directories:
  `find skillsets -maxdepth 2 -type d | sort`
  produced `skillsets/architecture`, `skillsets/auditors`, `skillsets/conventions`, `skillsets/design-patterns`, `skillsets/shared`, `skillsets/shared/references`, and `skillsets/shared/templates`.
- Shared file counts:
  `find skillsets/shared/references -maxdepth 1 -type f | wc -l` produced `9`.
  `find skillsets/shared/templates -maxdepth 1 -type f | wc -l` produced `4`.
- Red-flag scan across `skillsets/shared` returned no matches for unresolved markers or bracket-slot text.

## Open Risks

- Later leaf skills must use these shared contracts without expanding them into generic boilerplate.
