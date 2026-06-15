# Architecture Decision Rubric

Architecture skills should recommend structure only when the scale and forces justify it.

## Decision Inputs

Identify:

- Current system size and ownership boundaries.
- Change frequency and known axes of variation.
- Runtime, deployment, data, and integration constraints.
- Team familiarity and operational maturity.
- Existing tests and migration safety.

## Fit Checks

An architecture is a fit when it:

- Reduces a present coupling or coordination cost.
- Gives important policies a clear home.
- Preserves simple local reasoning for common changes.
- Can be introduced incrementally.
- Has tests or characterization around affected boundaries.

## Refusal Conditions

Recommend against an architecture when:

- The system is too small for the added ceremony.
- The pattern mainly copies a reference diagram.
- The migration would outpace test coverage.
- Operational needs are not mature enough for the split.
- The design hides dependencies instead of controlling them.

## Decision Record

Architecture advice should end with:

- `Adopt`: use the architecture now.
- `Defer`: gather evidence, tests, or scale first.
- `Use smaller boundary`: apply a narrower modular refactor.
- `Reject`: the architecture adds more cost than value.
