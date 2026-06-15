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

- `cleaner-code-skillsets/auditors/`
- `cleaner-code-skillsets/design-patterns/`
- `cleaner-code-skillsets/architecture/`
- `cleaner-code-skillsets/conventions/`
- `cleaner-code-skillsets/shared/references/`
- `cleaner-code-skillsets/shared/templates/`
- `docs/plan/goal-progression.md`
- `docs/plan/context-GD-001.md`

Created shared reference files:
- `cleaner-code-skillsets/shared/references/pattern-safety-rules.md`
- `cleaner-code-skillsets/shared/references/pattern-output-contract.md`
- `cleaner-code-skillsets/shared/references/pattern-selection-rubric.md`
- `cleaner-code-skillsets/shared/references/audit-severity-rubric.md`
- `cleaner-code-skillsets/shared/references/convention-discovery.md`
- `cleaner-code-skillsets/shared/references/architecture-decision-rubric.md`
- `cleaner-code-skillsets/shared/references/architecture-output-contract.md`
- `cleaner-code-skillsets/shared/references/refactoring-safety-rules.md`
- `cleaner-code-skillsets/shared/references/skill-frontmatter-contract.md`

Created shared template files:
- `cleaner-code-skillsets/shared/templates/design-pattern-skill-template.md`
- `cleaner-code-skillsets/shared/templates/auditor-skill-template.md`
- `cleaner-code-skillsets/shared/templates/convention-skill-template.md`
- `cleaner-code-skillsets/shared/templates/architecture-skill-template.md`

## Handoff Notes

The next loop should read `docs/plan/goal-progression.md`, select GD-002, and create `cleaner-code-skillsets/design-patterns/advisors/pattern-advisor/SKILL.md`.

Shared references are intentionally concise. They define reusable contracts and rubrics without duplicating every individual skill.

## Validation To Record

- Directory listing showing expected shared directories:
  `find cleaner-code-skillsets -maxdepth 2 -type d | sort`
  produced `cleaner-code-skillsets/architecture`, `cleaner-code-skillsets/auditors`, `cleaner-code-skillsets/conventions`, `cleaner-code-skillsets/design-patterns`, `cleaner-code-skillsets/shared`, `cleaner-code-skillsets/shared/references`, and `cleaner-code-skillsets/shared/templates`.
- Shared file counts:
  `find cleaner-code-skillsets/shared/references -maxdepth 1 -type f | wc -l` produced `9`.
  `find cleaner-code-skillsets/shared/templates -maxdepth 1 -type f | wc -l` produced `4`.
- Red-flag scan across `cleaner-code-skillsets/shared` returned no matches for unresolved markers or bracket-slot text.

## Open Risks

- Later leaf skills must use these shared contracts without expanding them into generic boilerplate.
