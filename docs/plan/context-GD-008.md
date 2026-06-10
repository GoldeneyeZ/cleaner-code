# Context GD-008: Convention Skills

Last updated: 2026-06-10 17:39

## Task

Create convention skills for clean code, naming, testing, errors, APIs, docs, logging, dependencies, immutability, async code, module boundaries, configuration, language style, and framework style.

## Current Status

Done. All convention skills have been created and verified.

## Files To Create Or Update

- `skillsets/conventions/*/SKILL.md`
- `docs/plan/goal-progression.md`
- `docs/plan/context-GD-008.md`

## Handoff Notes

The next loop should read `docs/plan/goal-progression.md`, select GD-009, and create `skillsets/architecture/dependency-inversion/SKILL.md`.

Every convention skill must discover local style before enforcing changes and should reference `skillsets/shared/references/convention-discovery.md`.

## Validation To Record

- File count:
  `find skillsets/conventions -mindepth 2 -maxdepth 2 -name SKILL.md -type f | sort | wc -l`
  returned `14`.
- Frontmatter:
  `rg -n "^name: |^description: Use when" skillsets/conventions/*/SKILL.md`
  found `name` and trigger-oriented `description` entries for all convention skills.
- Local discovery:
  `rg -n "Discover local style before recommending changes|convention-discovery" skillsets/conventions/*/SKILL.md`
  found explicit local-discovery requirements and shared guide references in all convention skills.
- Generated-text scan across convention skills returned no matches for unresolved markers or bracket-slot text.

## Open Risks

- Later packaging should include all 14 convention skills.
