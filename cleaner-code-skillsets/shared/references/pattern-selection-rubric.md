# Pattern Selection Rubric

Use this rubric to decide whether any design pattern is warranted and which family to inspect.

## First Question

Can a small local refactor remove the smell without adding a named pattern?

If yes, recommend the smaller refactor.

## Pattern Family Signals

| Family | Strong signal | Common false positive |
| --- | --- | --- |
| Creational | Object creation varies by stable product family, environment, or policy. | A constructor has many parameters that a parameter object would fix. |
| Structural | Existing interfaces cannot change, but clients need a stable way to compose or adapt collaborators. | A wrapper is used only to rename one method. |
| Behavioral | Algorithms, state transitions, notifications, commands, or traversal rules vary independently from callers. | A single conditional can be made clearer with extraction. |

## Selection Steps

1. Name the current pain: duplication, coupling, conditional complexity, lifecycle confusion, or boundary mismatch.
2. Identify the axis of variation that is already present.
3. Check whether the variation is stable enough to justify abstraction.
4. Compare the smallest local refactor against the candidate pattern.
5. Choose the least abstract option that protects behavior and improves clarity.

## Rejection Standard

Reject a candidate pattern when it needs imagined future cases to sound useful.
