# Goal Progression

Last updated: 2026-06-10 18:01

Task status values: `pending`, `in-progress`, `done`, `blocked`.
Step status values: unchecked `- [ ]` means not done; checked `- [x]` means done.

Loop rule:
- Read this file first.
- Select the first task whose `Task status` is not `done`.
- Mark the selected task `in-progress` before changing files for that task.
- In that task, complete the first unchecked step.
- Mark a completed step by changing `- [ ]` to `- [x]`.
- Update the matching `docs/plan/context-<task-id>.md` file before ending the loop.
- If the context file does not exist yet, create it with sections for task, current status, files changed, validation evidence, handoff notes, and open risks.
- Mark a step done only after implementation and verification.
- Mark a task `done` only after all its steps are `done`.

## GD-001: Shared Foundation

- Task status: done
- Context file: `docs/plan/context-GD-001.md`
- Next action: Task complete; continue to GD-002.

Steps:
- [x] Create base directories: `cleaner-code-skillsets/auditors`, `cleaner-code-skillsets/design-patterns`, `cleaner-code-skillsets/architecture`, `cleaner-code-skillsets/conventions`, `cleaner-code-skillsets/shared`.
- [x] Create `cleaner-code-skillsets/shared/references/pattern-safety-rules.md`.
- [x] Create `cleaner-code-skillsets/shared/references/pattern-output-contract.md`.
- [x] Create `cleaner-code-skillsets/shared/references/pattern-selection-rubric.md`.
- [x] Create `cleaner-code-skillsets/shared/references/audit-severity-rubric.md`.
- [x] Create `cleaner-code-skillsets/shared/references/convention-discovery.md`.
- [x] Create `cleaner-code-skillsets/shared/references/architecture-decision-rubric.md`.
- [x] Create `cleaner-code-skillsets/shared/references/architecture-output-contract.md`.
- [x] Create `cleaner-code-skillsets/shared/references/refactoring-safety-rules.md`.
- [x] Create `cleaner-code-skillsets/shared/references/skill-frontmatter-contract.md`.
- [x] Create `cleaner-code-skillsets/shared/templates/design-pattern-skill-template.md`.
- [x] Create `cleaner-code-skillsets/shared/templates/auditor-skill-template.md`.
- [x] Create `cleaner-code-skillsets/shared/templates/convention-skill-template.md`.
- [x] Create `cleaner-code-skillsets/shared/templates/architecture-skill-template.md`.
- [x] Verify shared files contain no placeholder text.

## GD-002: Design Pattern Advisor

- Task status: done
- Context file: `docs/plan/context-GD-002.md`
- Next action: Task complete; continue to GD-003.

Steps:
- [x] Create `cleaner-code-skillsets/design-patterns/advisors/pattern-advisor/SKILL.md`.
- [x] Verify the advisor can recommend no pattern when a simpler refactor is better.
- [x] Verify the advisor can route to creational, structural, and behavioral pattern skills.

## GD-003: Representative Pattern Skills

- Task status: done
- Context file: `docs/plan/context-GD-003.md`
- Next action: Task complete; continue to GD-004.

Steps:
- [x] Create `cleaner-code-skillsets/design-patterns/behavioral/strategy/SKILL.md`.
- [x] Create `cleaner-code-skillsets/design-patterns/creational/factory-method/SKILL.md`.
- [x] Create `cleaner-code-skillsets/design-patterns/structural/adapter/SKILL.md`.
- [x] Review these three skills for consistent structure, refusal criteria, testing expectations, and output contract.

## GD-004: Creational Pattern Skills

- Task status: done
- Context file: `docs/plan/context-GD-004.md`
- Next action: Task complete; continue to GD-005.

Steps:
- [x] Create `cleaner-code-skillsets/design-patterns/creational/abstract-factory/SKILL.md`.
- [x] Create `cleaner-code-skillsets/design-patterns/creational/builder/SKILL.md`.
- [x] Confirm `cleaner-code-skillsets/design-patterns/creational/factory-method/SKILL.md` is complete.
- [x] Create `cleaner-code-skillsets/design-patterns/creational/prototype/SKILL.md`.
- [x] Create `cleaner-code-skillsets/design-patterns/creational/singleton/SKILL.md`.
- [x] Verify all creational pattern skills have valid frontmatter and refusal criteria.

## GD-005: Structural Pattern Skills

- Task status: done
- Context file: `docs/plan/context-GD-005.md`
- Next action: Task complete; continue to GD-006.

Steps:
- [x] Confirm `cleaner-code-skillsets/design-patterns/structural/adapter/SKILL.md` is complete.
- [x] Create `cleaner-code-skillsets/design-patterns/structural/bridge/SKILL.md`.
- [x] Create `cleaner-code-skillsets/design-patterns/structural/composite/SKILL.md`.
- [x] Create `cleaner-code-skillsets/design-patterns/structural/decorator/SKILL.md`.
- [x] Create `cleaner-code-skillsets/design-patterns/structural/facade/SKILL.md`.
- [x] Create `cleaner-code-skillsets/design-patterns/structural/flyweight/SKILL.md`.
- [x] Create `cleaner-code-skillsets/design-patterns/structural/proxy/SKILL.md`.
- [x] Verify all structural pattern skills have valid frontmatter and refusal criteria.

## GD-006: Behavioral Pattern Skills

- Task status: done
- Context file: `docs/plan/context-GD-006.md`
- Next action: Task complete; continue to GD-007.

Steps:
- [x] Create `cleaner-code-skillsets/design-patterns/behavioral/chain-of-responsibility/SKILL.md`.
- [x] Create `cleaner-code-skillsets/design-patterns/behavioral/command/SKILL.md`.
- [x] Create `cleaner-code-skillsets/design-patterns/behavioral/iterator/SKILL.md`.
- [x] Create `cleaner-code-skillsets/design-patterns/behavioral/mediator/SKILL.md`.
- [x] Create `cleaner-code-skillsets/design-patterns/behavioral/memento/SKILL.md`.
- [x] Create `cleaner-code-skillsets/design-patterns/behavioral/observer/SKILL.md`.
- [x] Create `cleaner-code-skillsets/design-patterns/behavioral/state/SKILL.md`.
- [x] Confirm `cleaner-code-skillsets/design-patterns/behavioral/strategy/SKILL.md` is complete.
- [x] Create `cleaner-code-skillsets/design-patterns/behavioral/template-method/SKILL.md`.
- [x] Create `cleaner-code-skillsets/design-patterns/behavioral/visitor/SKILL.md`.
- [x] Verify all behavioral pattern skills have valid frontmatter and refusal criteria.

## GD-007: Auditor Skills

- Task status: done
- Context file: `docs/plan/context-GD-007.md`
- Next action: Task complete; continue to GD-008.

Steps:
- [x] Create `cleaner-code-skillsets/auditors/code-quality-auditor/SKILL.md`.
- [x] Create `cleaner-code-skillsets/auditors/architecture-auditor/SKILL.md`.
- [x] Create `cleaner-code-skillsets/auditors/test-quality-auditor/SKILL.md`.
- [x] Create `cleaner-code-skillsets/auditors/maintainability-auditor/SKILL.md`.
- [x] Create `cleaner-code-skillsets/auditors/dependency-auditor/SKILL.md`.
- [x] Create `cleaner-code-skillsets/auditors/security-auditor/SKILL.md`.
- [x] Create `cleaner-code-skillsets/auditors/performance-auditor/SKILL.md`.
- [x] Create `cleaner-code-skillsets/auditors/api-design-auditor/SKILL.md`.
- [x] Create `cleaner-code-skillsets/auditors/error-handling-auditor/SKILL.md`.
- [x] Create `cleaner-code-skillsets/auditors/concurrency-auditor/SKILL.md`.
- [x] Create `cleaner-code-skillsets/auditors/data-flow-auditor/SKILL.md`.
- [x] Create `cleaner-code-skillsets/auditors/duplication-auditor/SKILL.md`.
- [x] Create `cleaner-code-skillsets/auditors/complexity-auditor/SKILL.md`.
- [x] Create `cleaner-code-skillsets/auditors/documentation-auditor/SKILL.md`.
- [x] Create `cleaner-code-skillsets/auditors/observability-auditor/SKILL.md`.
- [x] Create `cleaner-code-skillsets/auditors/migration-risk-auditor/SKILL.md`.
- [x] Verify every auditor reports findings first, ordered by severity.

## GD-008: Convention Skills

- Task status: done
- Context file: `docs/plan/context-GD-008.md`
- Next action: Task complete; continue to GD-009.

Steps:
- [x] Create `cleaner-code-skillsets/conventions/clean-code-conventions/SKILL.md`.
- [x] Create `cleaner-code-skillsets/conventions/naming-conventions/SKILL.md`.
- [x] Create `cleaner-code-skillsets/conventions/testing-conventions/SKILL.md`.
- [x] Create `cleaner-code-skillsets/conventions/error-handling-conventions/SKILL.md`.
- [x] Create `cleaner-code-skillsets/conventions/api-design-conventions/SKILL.md`.
- [x] Create `cleaner-code-skillsets/conventions/documentation-conventions/SKILL.md`.
- [x] Create `cleaner-code-skillsets/conventions/logging-conventions/SKILL.md`.
- [x] Create `cleaner-code-skillsets/conventions/dependency-conventions/SKILL.md`.
- [x] Create `cleaner-code-skillsets/conventions/immutability-conventions/SKILL.md`.
- [x] Create `cleaner-code-skillsets/conventions/async-conventions/SKILL.md`.
- [x] Create `cleaner-code-skillsets/conventions/module-boundary-conventions/SKILL.md`.
- [x] Create `cleaner-code-skillsets/conventions/configuration-conventions/SKILL.md`.
- [x] Create `cleaner-code-skillsets/conventions/language-conventions/SKILL.md`.
- [x] Create `cleaner-code-skillsets/conventions/framework-conventions/SKILL.md`.
- [x] Verify every convention skill discovers local style before enforcing changes.

## GD-009: Architecture Skills

- Task status: done
- Context file: `docs/plan/context-GD-009.md`
- Next action: Task complete; continue to GD-010.

Steps:
- [x] Create `cleaner-code-skillsets/architecture/dependency-inversion/SKILL.md`.
- [x] Create `cleaner-code-skillsets/architecture/repository/SKILL.md`.
- [x] Create `cleaner-code-skillsets/architecture/unit-of-work/SKILL.md`.
- [x] Create `cleaner-code-skillsets/architecture/service-layer/SKILL.md`.
- [x] Create `cleaner-code-skillsets/architecture/layered-architecture/SKILL.md`.
- [x] Create `cleaner-code-skillsets/architecture/hexagonal-architecture/SKILL.md`.
- [x] Create `cleaner-code-skillsets/architecture/clean-architecture/SKILL.md`.
- [x] Create `cleaner-code-skillsets/architecture/onion-architecture/SKILL.md`.
- [x] Create `cleaner-code-skillsets/architecture/cqrs/SKILL.md`.
- [x] Create `cleaner-code-skillsets/architecture/event-sourcing/SKILL.md`.
- [x] Create `cleaner-code-skillsets/architecture/domain-driven-design/SKILL.md`.
- [x] Create `cleaner-code-skillsets/architecture/modular-monolith/SKILL.md`.
- [x] Create `cleaner-code-skillsets/architecture/ports-and-adapters/SKILL.md`.
- [x] Create `cleaner-code-skillsets/architecture/vertical-slice-architecture/SKILL.md`.
- [x] Create `cleaner-code-skillsets/architecture/pipeline-architecture/SKILL.md`.
- [x] Create `cleaner-code-skillsets/architecture/event-driven-architecture/SKILL.md`.
- [x] Create `cleaner-code-skillsets/architecture/microservices-boundaries/SKILL.md`.
- [x] Create `cleaner-code-skillsets/architecture/anti-corruption-layer/SKILL.md`.
- [x] Create `cleaner-code-skillsets/architecture/specification-pattern/SKILL.md`.
- [x] Verify architecture skills define scale, tradeoffs, and refusal criteria.

## GD-010: Final Validation

- Task status: done
- Context file: `docs/plan/context-GD-010.md`
- Next action: Final validation complete.

Steps:
- [x] Verify every listed `SKILL.md` file exists.
- [x] Verify every `SKILL.md` has valid `name` and `description` frontmatter.
- [x] Verify descriptions are trigger-oriented.
- [x] Verify no generated file contains TODO, TBD, FIXME, or placeholder content.
- [x] Verify no installer, package manager, or unrelated build-system files were added.
- [x] Verify `docs/plan/goal-progression.md` and all `docs/plan/context-<task-id>.md` files are up to date.
- [x] Summarize completed work and remaining risk.
