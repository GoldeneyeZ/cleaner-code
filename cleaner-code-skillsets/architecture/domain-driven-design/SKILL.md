---
name: cleaner-code:domain-driven-design
description: Use when complex business rules, ubiquitous language, aggregates, bounded contexts, or domain modeling need architectural guidance
---

# Domain-Driven Design

Use Domain-Driven Design for complex domains, not for CRUD naming polish.

## References

- `references/architecture-decision-rubric.md`
- `references/architecture-output-contract.md`

## Fit

- Scale: domains with nuanced rules and multiple expert vocabularies.
- Use when business language and code structure diverge.
- Migrate by clarifying one bounded context or aggregate boundary.

## Do Not Use When

- The system is mostly data entry and reporting.
- Domain terms are not stable enough to model.
- Tactical patterns would add ceremony without shared language.

## Tradeoffs

Requires domain collaboration and disciplined boundaries. Avoid pattern-heavy modeling without business evidence.
