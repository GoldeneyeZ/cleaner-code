# Context GD-007: Auditor Skills

Last updated: 2026-06-10 17:39

## Task

Create auditor skills for code quality, architecture, tests, maintainability, dependencies, security, performance, APIs, errors, concurrency, data flow, duplication, complexity, documentation, observability, and migration risk.

## Current Status

Done. All auditor skills have been created and verified.

## Files To Create Or Update

- `skillsets/auditors/*/SKILL.md`
- `docs/plan/goal-progression.md`
- `docs/plan/context-GD-007.md`

## Handoff Notes

The next loop should read `docs/plan/goal-progression.md`, select GD-008, and create `skillsets/conventions/clean-code-conventions/SKILL.md`.

Every auditor must report findings first, ordered by severity, and cite concrete file and line references when code is available.

## Validation To Record

- File count:
  `find skillsets/auditors -mindepth 2 -maxdepth 2 -name SKILL.md -type f | sort | wc -l`
  returned `16`.
- Frontmatter:
  `rg -n "^name: |^description: Use when" skillsets/auditors/*/SKILL.md`
  found `name` and trigger-oriented `description` entries for all auditor skills.
- Findings-first and severity rubric:
  `rg -n "audit-severity-rubric|Findings first|ordered by severity|file and line references" skillsets/auditors/*/SKILL.md`
  found shared rubric references and findings-first output wording in all auditor skills.
- Generated-text scan across auditor skills returned no matches for unresolved markers or bracket-slot text.

## Open Risks

- Later packaging should include all 16 auditor skills.
