# Logical Planning Agent

This repository contains my implementation for the **Artificial Intelligence Laboratory – Logical Planning**.

The laboratory describes planning using an initial state `I`, actions `A` and a goal `G`. Each action has preconditions and effects, and the central idea is:

```text
Logic + Search = Planning
```

This is the main structure given in the laboratory.

## Warehouse planning problem

The warehouse has three locations:

```text
A, B, C
```

Initially:

```text
At(Robot,A)
At(Package,A)
```

The goal is:

```text
At(Package,C)
```

The laboratory defines movement actions, pickup actions and drop actions using logical preconditions and effects.

## Manual plan

A valid plan is:

```text
Move(A, B)
PickUp(Package, B)
Move(B, C)
Drop(Package, C)
```

The important point is that each action has to be applicable in the state in which it is executed. The lab gives the same type of sequence as an example and asks for the state after every action.

The states are:

```text
S0:
At(Robot,A), At(Package,A)

S1:
At(Robot,B), At(Package,A)

S2:
At(Robot,B), Holding(Package)

S3:
At(Robot,C), Holding(Package)

S4:
At(Robot,C), At(Package,C)
```

## Implementation

Each action stores:

```text
positive_preconditions
negative_preconditions
positive_effects
negative_effects
```

An action is applicable when its preconditions are satisfied.

When it is applied:

```text
new_state = old_state
remove negative effects
add positive effects
```

Breadth-first search is then used to explore different sequences of applicable actions. This matches the implementation specification in the laboratory.

Run:

```bash
python planner.py
```

## Tests

The laboratory asks for at least three tests.

### Test A - Solvable

Use the original problem.

Expected:

```text
A valid plan is found.
The final state contains At(Package,C).
```

### Test B - Impossible

Remove the pickup action.

Expected:

```text
No plan found.
```

The planner must not invent an action that is not available.

### Test C - Irrelevant action

Add an action that moves the robot but does not move the package.

The planner should still check the actual goal:

```text
At(Package,C)
```

It should not confuse the robot being at C with the package being at C.

Run:

```bash
python tests.py
```

## Logic and search

The logical part checks:

```text
S |= Preconditions(a)
```

If this is true, the action can be applied to generate a successor state.

The search part decides which sequence of applicable actions to explore.

A useful summary from the laboratory is:

```text
Logic determines what is possible;
search determines what to try.
```

This distinction is explicitly discussed in the laboratory.

## LLM usage

The initial implementation was specified using the prompt in `llm_prompt.txt`.

The laboratory requires the LLM-generated implementation to be tested independently and asks students to identify which parts came from the specification, which were suggested by the LLM and which were modified or tested.

I therefore checked:

- action applicability;
- state transitions;
- successful planning;
- failure when pickup is unavailable;
- the irrelevant-action case.

## Reflection

### Why specify preconditions and effects first?

Because the planner needs a precise definition of when an action is legal and exactly how the state changes. Without this, an LLM could produce code that appears to work but does not implement the intended planning problem.

### What happens if preconditions are ignored?

The planner could pick up a package when the robot is somewhere else or drop a package when it is not holding it. Such a sequence may look reasonable but would not be logically valid.

### Why is a reasonable-looking plan not necessarily valid?

Every action must be applicable in the actual state immediately before it is executed.

### What did the LLM contribute?

It helped translate the planning specification into Python data structures, action checks and BFS code.

### What needed independent verification?

The action preconditions, effects, goal test, state transitions and no-solution behaviour.

### Where is logical reasoning used?

In checking whether all action preconditions are satisfied.

### How is planning related to search?

Once applicable actions are generated using logical reasoning, search explores different possible action sequences until a goal state is reached.

## Files

```text
planner.py
tests.py
llm_prompt.txt
README.md
```
