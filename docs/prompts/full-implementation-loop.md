# Full Implementation Loop Prompt

Use this prompt to start or resume a goal-driven Codex session for building the cleaner-code skill suite.

```text
We are working in the cleaner-code repo.

Objective:
Build the complete Codex-installable cleaner-code skill suite for code quality auditing, design pattern advice, design pattern application, architecture guidance, and coding conventions.

Authoritative plan:
- `docs/plan/goal-progression.md` defines the full task list, skill inventory, step order, status rules, and loop mechanics.
- `docs/plan/context-<task-id>.md` files are task-local handoff records for future loops.
- Do not duplicate or reinterpret the task inventory from memory. Read the plan file.

Use the goal tool for the full implementation loop:
- First call `get_goal` to check whether a goal is already active.
- If no goal is active, call `create_goal` with this objective:
  "Build the complete cleaner-code Codex skill suite according to docs/plan/goal-progression.md."
- Do not call `create_goal` if a goal already exists.
- Use `get_goal` during long work to check status and remaining budget.
- Only call `update_goal(status: "complete")` when every task in `docs/plan/goal-progression.md` is done, final validation passes, and no required work remains.
- Only call `update_goal(status: "blocked")` after the same blocking condition has repeated for at least three consecutive goal turns and meaningful progress cannot continue without user input or an external-state change.

Execution loop:
1. Read `docs/plan/goal-progression.md`.
2. Select the first task whose `Task status` is not `done`.
3. Read or create that task's `docs/plan/context-<task-id>.md`.
4. Mark the selected task `in-progress` before changing files for that task.
5. Complete the first unchecked step for the selected task.
6. Verify the completed step.
7. Update the task context file with:
   - what was done
   - files changed
   - validation evidence
   - open risks
   - exact next step for the next loop
8. Update `docs/plan/goal-progression.md`:
   - mark completed steps done by changing `- [ ]` to `- [x]`
   - mark the task done only when all its steps are done
   - update `Last updated`
   - keep detailed notes in the context file, not the progression file
9. Continue without pausing unless blocked or all tasks are done.

Implementation rules:
- Every leaf skill folder must contain a valid `SKILL.md`.
- Every `SKILL.md` must have YAML frontmatter with `name` and `description`.
- Descriptions must be trigger-oriented: explain when Codex should use the skill.
- Keep each skill concise. Put repeated or detailed guidance into shared references.
- Each design pattern skill must be able to refuse itself when the pattern is not justified.
- Pattern skills must require evidence of a real code smell before applying the pattern.
- Pattern skills must prefer simpler refactors when a pattern would add unnecessary abstraction.
- Pattern skills must require behavior protection through tests or characterization before refactoring.
- Auditors must report findings first, ordered by severity, with concrete file and line references when code is being reviewed.
- Convention skills must discover local style before enforcing changes.
- Do not create installer code yet.
- Do not add unrelated build systems or package managers yet.
- Do not commit unless explicitly asked.

Quality bar:
This project should prevent stupid pattern application. The skills should improve code quality through evidence, restraint, tests, and local convention discovery. A correct answer may say "do not use this pattern here."
```
