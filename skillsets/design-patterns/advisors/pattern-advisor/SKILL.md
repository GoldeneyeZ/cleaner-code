---
name: pattern-advisor
description: Use when deciding whether code needs a design pattern, a simpler refactor, or routing to a creational, structural, or behavioral pattern skill
---

# Pattern Advisor

Use this skill before recommending or applying a design pattern. The advisor is a decision gate: it may route to a pattern skill, recommend a smaller refactor, or reject pattern use.

## Core Rule

Do not start from a pattern name. Start from evidence in the code.

Follow:

- `skillsets/shared/references/pattern-safety-rules.md`
- `skillsets/shared/references/pattern-selection-rubric.md`
- `skillsets/shared/references/pattern-output-contract.md`

## Use When

- The user asks which design pattern fits a code problem.
- Code has duplication, conditional complexity, creation branching, boundary mismatch, or collaborator coupling.
- A previous suggestion named a pattern but did not prove it is justified.
- A refactor may need routing to a creational, structural, or behavioral pattern skill.

## Do Not Use When

- The user asks about a specific pattern's mechanics without applying it to code.
- The task is only naming, formatting, or local extraction.
- No concrete code or scenario is available to inspect.

When evidence is missing, ask for code or state that a pattern recommendation would be speculative.

## Decision Process

1. Identify the current smell and cite files and lines when code is available.
2. Name the behavior that must remain unchanged.
3. Check whether a smaller refactor solves the smell.
4. Identify the axis of variation already present in the code.
5. Pick the least abstract decision that improves clarity.

## Simpler Refactor Checks

Recommend no pattern when one of these is enough:

- Rename confusing concepts.
- Extract a function or class.
- Introduce a parameter object.
- Move behavior to the data owner.
- Replace a long conditional with clear guard clauses.
- Split a module along an existing boundary.
- Use direct composition without a named pattern.

## Routing

Route only after evidence supports a pattern family.

| Route | Use when evidence shows | Example target skills |
| --- | --- | --- |
| Creational | Object creation varies by stable policy, product family, environment, or lifecycle. | factory-method, abstract-factory, builder, prototype, singleton |
| Structural | Existing interfaces, wrappers, composition boundaries, or client compatibility create the pressure. | adapter, bridge, composite, decorator, facade, flyweight, proxy |
| Behavioral | Algorithms, commands, notifications, state transitions, traversal, or collaboration rules vary independently. | strategy, command, observer, state, iterator, mediator |

## Output

Start with one decision:

- `Do not use a pattern`
- `Use simpler refactor`
- `Route to creational pattern`
- `Route to structural pattern`
- `Route to behavioral pattern`

Then provide:

1. Evidence from the code or scenario.
2. Simpler options considered.
3. Recommended next skill when routing.
4. Test or characterization needed before refactoring.
5. Risks and tradeoffs.
