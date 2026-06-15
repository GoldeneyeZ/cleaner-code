# Audit Severity Rubric

Auditor skills report findings first, ordered by severity, with concrete evidence.

## Severity Levels

| Severity | Use when | Expected action |
| --- | --- | --- |
| Critical | The issue can cause data loss, security exposure, production outage, or silent corruption. | Fix before release. |
| High | The issue can break user-visible behavior, block maintenance, or create hard-to-debug failures. | Fix in the current change set. |
| Medium | The issue increases complexity, fragility, or inconsistency with a clear path to improvement. | Fix soon or document why deferred. |
| Low | The issue is localized, low-risk, or mostly cleanup. | Fix opportunistically. |
| Note | The observation is useful context but not a defect. | No required action. |

## Finding Format

Each finding should include:

- Severity.
- File and line reference when code is available.
- What is wrong.
- Why it matters.
- A concrete fix direction.

## Ordering Rules

- Findings come before summary.
- Higher severity comes first.
- Within a severity, list issues with the broadest blast radius first.
- Do not pad reviews with style preferences unless they affect maintainability or correctness.
