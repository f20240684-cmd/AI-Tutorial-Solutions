# Lab Answers

## Task 0

### Initial state

```text
{At(Robot,A), At(Package,A)}
```

### Goal

```text
{At(Package,C)}
```

### Actions

The action set contains:
- Move(A,B)
- Move(B,A)
- Move(B,C)
- Move(C,B)
- PickUp(Package,A/B/C)
- Drop(Package,A/B/C)

Each action has logical preconditions and effects.

### Initially applicable actions

`PickUp(Package,A)` is applicable because both:

```text
At(Robot,A)
At(Package,A)
```

are true.

`Drop(Package,C)` is not applicable because:

```text
At(Robot,C)
Holding(Package)
```

are not both true.

## Task 1

A valid plan is:

```text
PickUp(Package,A)
Move(A,B)
Move(B,C)
Drop(Package,C)
```

This is valid even though the laboratory also gives a move-first sequence as an example. The important condition is that every action's preconditions are satisfied when the action is executed.

## Task 4

The planner can be viewed as:

```text
Current state
      |
      v
Check action preconditions
      |
      v
Select an applicable action
      |
      v
Generate successor state
      |
      v
Search over alternatives
      |
      v
Goal?
```

Logic determines which actions are possible from the current state. Search determines which sequence of possible actions should be explored.

## Task 5

The independently executed state transitions should be trusted more than an LLM explanation because the transitions are actually computed by the program and can be checked directly. A generated explanation is not independent verification.

## Reflection Questions

### 1. Why specify preconditions and effects first?

They define exactly when an action is legal and exactly how it changes the state. This gives the LLM a precise target instead of leaving important behaviour implicit.

### 2. Example of an error if preconditions are ignored

The planner could execute `Drop(Package,C)` while the robot is still at A or while it is not holding the package.

### 3. Why is a reasonable-looking plan not necessarily valid?

Because every action must satisfy its logical preconditions in the state immediately before execution.

### 4. What did the LLM contribute?

It helped turn the planning specification into Python classes, applicability checks, state updates and BFS.

### 5. What had to be verified independently?

The action preconditions, effects, state transitions, goal condition, returned plan and failure cases.

### 6. Where is logical reasoning used?

When checking whether:

```text
S |= Preconditions(a)
```

for an action.

### 7. How is planning related to search?

Planning searches through possible sequences of logically applicable actions. BFS is the search mechanism used in this implementation.
