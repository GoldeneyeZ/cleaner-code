---
name: facade
description: Use when clients need a simpler stable entry point over a complex subsystem without hiding required domain decisions
---

# Facade

Use Facade to simplify a real subsystem boundary. Do not use it to create a vague service object or to hide complexity that callers must control.

## References

- `cleaner-code-skillsets/shared/references/pattern-safety-rules.md`
- `cleaner-code-skillsets/shared/references/pattern-output-contract.md`
- `cleaner-code-skillsets/shared/references/refactoring-safety-rules.md`

## Use When

- Many clients repeat the same sequence across subsystem APIs.
- A subsystem has a stable high-level use case with noisy low-level steps.
- The facade can reduce coupling without hiding necessary choices.
- Tests can protect the high-level workflow and subsystem interactions.

## Do Not Use When

- Only one caller uses the subsystem.
- The facade would become a catch-all service.
- Clients need fine-grained control over the steps.
- A small helper function is enough.
- The subsystem boundary is not stable.

## Evidence Checklist

- Cite repeated subsystem interaction sequences with file and line references when code is available.
- Name the high-level operation the facade should expose.
- Identify decisions that must remain visible to callers.
- Compare helper extraction and direct client cleanup.
- Confirm tests cover workflow success, failure, and important subsystem calls.

## Application Steps

1. Characterize existing subsystem workflows.
2. Extract one high-level operation with a narrow API.
3. Keep domain decisions explicit in parameters or caller code.
4. Migrate repeated client sequences incrementally.
5. Re-run workflow and failure-path tests.

## Output

Follow `cleaner-code-skillsets/shared/references/pattern-output-contract.md`. The final decision must be `Apply pattern`, `Use simpler refactor`, or `Do not change`.
