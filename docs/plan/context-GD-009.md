# Context GD-009: Architecture Skills

Last updated: 2026-06-10 17:39

## Task

Create architecture skills for dependency inversion, repositories, unit of work, service layer, layered architecture, hexagonal architecture, clean architecture, onion architecture, CQRS, event sourcing, domain-driven design, modular monoliths, ports and adapters, vertical slices, pipelines, event-driven architecture, microservice boundaries, anti-corruption layers, and specification pattern.

## Current Status

Done. All architecture skills have been created and verified.

## Files To Create Or Update

- `cleaner-code-skillsets/architecture/*/SKILL.md`
- `docs/plan/goal-progression.md`
- `docs/plan/context-GD-009.md`

## Handoff Notes

The next loop should read `docs/plan/goal-progression.md`, select GD-010, and run final repository validation.

Every architecture skill must define fit by scale, tradeoffs, migration safety, and refusal criteria. Skills should reference the shared architecture decision rubric and output contract.

## Validation To Record

- File count:
  `find cleaner-code-skillsets/architecture -mindepth 2 -maxdepth 2 -name SKILL.md -type f | sort | wc -l`
  returned `19`.
- Frontmatter:
  `rg -n "^name: |^description: Use when" cleaner-code-skillsets/architecture/*/SKILL.md`
  found `name` and trigger-oriented `description` entries for all architecture skills.
- Shared references, scale, tradeoffs, and refusal criteria:
  `rg -n "architecture-decision-rubric|architecture-output-contract|Scale:|## Do Not Use When|## Tradeoffs" cleaner-code-skillsets/architecture/*/SKILL.md`
  found the required references and sections in all architecture skills.
- Generated-text scan across architecture skills returned no matches for unresolved markers or bracket-slot text.

## Open Risks

- Later packaging should include all 19 architecture skills.
