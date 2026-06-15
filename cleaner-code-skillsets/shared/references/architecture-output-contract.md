# Architecture Output Contract

Architecture skills produce tradeoff-aware guidance, not generic diagrams.

## Required Sections

1. `Decision`: adopt, defer, use a smaller boundary, or reject.
2. `Context`: current constraints and evidence.
3. `Forces`: coupling, scale, team, runtime, data, and deployment pressures.
4. `Recommended Shape`: modules, boundaries, ownership, and dependency direction.
5. `Migration Plan`: incremental steps with rollback points.
6. `Validation`: tests, checks, or reviews that prove the boundary works.
7. `Tradeoffs`: costs introduced by the recommendation.

## Quality Rules

- Name what should not be abstracted.
- Keep boundaries aligned with business or operational change.
- Avoid introducing distributed systems as a default answer.
- Prefer reversible migration steps.
- Include refusal criteria when the architecture does not fit.
