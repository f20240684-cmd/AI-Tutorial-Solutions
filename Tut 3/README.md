# Search and A*

This repository contains my implementation for the **Artificial Intelligence Laboratory – Search and A***.

The lab models warehouse navigation as a search problem with states, actions, transitions, an initial state, goals and costs. A* uses:

```text
f(n) = g(n) + h(n)
```

where `g(n)` is the cost from the start and `h(n)` is the estimated cost to the goal.

## Warehouse problem

The robot can move:

```text
Up
Down
Left
Right
```

Every movement has cost 1. The warehouse map is the one supplied in the laboratory.

## Search formulation

| Component | Specification |
|---|---|
| State | Robot's `(row, column)` position |
| Actions | Up, Down, Left, Right |
| Transition | Move to an adjacent non-obstacle cell |
| Initial state | Cell containing `S` |
| Goal | Cell containing `G` |
| Cost | 1 per movement |

The problem is deterministic because an action from a particular state has a fixed result.

## A* implementation

The program uses:

- a priority queue for the frontier;
- `g_cost` for the cost from the start;
- Manhattan distance for `h(n)`;
- `f(n) = g(n) + h(n)`;
- a parent dictionary for path reconstruction.

The laboratory specifically asks the implementation to report whether a solution exists, path length and number of expanded states.

Run:

```bash
python search_agent.py
```

## Tests

The tests cover:

1. Original warehouse
2. Trivial one-step case
3. No-solution case

The lab also asks for an alternative-path test and checking that the returned path is shortest.

Run:

```bash
python tests.py
```

## BFS comparison

BFS is included because it is a blind-search baseline. With unit movement costs, BFS can find a shortest path.

Run:

```bash
python search_agent.py
```

The program reports both BFS and A* results on the same warehouse.

The comparison requested by the lab is based on:

- solution found
- path length
- states expanded

and asks why A* can expand fewer states when the heuristic gives useful information about the goal.

## Heuristic experiment

The program also compares:

```text
h(n) = Manhattan distance
h(n) = 0
h(n) = Euclidean distance
h(n) = 2 * Manhattan distance
```

The laboratory asks for exactly these variations and asks for solution status, path length and states expanded.

The Manhattan heuristic is natural here because movement is restricted to horizontal and vertical steps. It gives the minimum number of grid moves when there are no obstacles blocking the direct route.

Multiplying the heuristic by 2 makes it more aggressive and can remove the usual admissibility guarantee. The lab explicitly introduces admissibility as `h(n) <= h*(n)` and asks students to investigate what happens when the heuristic becomes too aggressive.

## LLM usage

The prompt used to generate the initial implementation is stored in `llm_prompt.txt`.

I did not treat the generated code as automatically correct. I ran the original, trivial and impossible cases and checked the returned path lengths and termination behaviour. This follows the laboratory's emphasis that working output is not the same as a validated algorithm.

## Files

```text
search_agent.py
tests.py
llm_prompt.txt
README.md
```
