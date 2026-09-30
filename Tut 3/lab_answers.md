# Lab Answers

## Task 0

| Component | Specification |
|---|---|
| State | Robot grid position `(row, column)` |
| Actions | Up, Down, Left, Right |
| Transition | Move to an adjacent free cell |
| Initial state | `S` |
| Goal | `G` |
| Cost | 1 per move |

### (a)
A state needs the robot's current row and column.

### (b)
An action is invalid if it leaves the grid or enters an obstacle.

### (c)
Yes. The result of an action is determined by the current state and selected movement.

### (d)
A solution is a sequence of valid moves from `S` to `G`.

## Task 4

- **State:** `(row, column)`
- **Action:** neighbour generation
- **Transition:** a valid adjacent cell
- **Goal test:** `current == goal`
- **g(n):** stored in `g_cost`
- **h(n):** the selected heuristic function
- **f(n):** `g + h`
- **Frontier:** Python `heapq`
- **Visited / explored information:** `g_cost` and parent records
- **Path reconstruction:** `reconstruct()`

### Questions

**(a)** The A* frontier is a priority queue.

**(b)** The state with the smallest priority value `f(n)` is expanded next.

**(c)** The heuristic is calculated in `manhattan()` or the selected alternative heuristic.

**(d)** Yes. The code explicitly computes `f = new_cost + h`.

**(e)** The `g_cost` dictionary prevents a state from being repeatedly added when no cheaper route has been found.

## Task 5

Both BFS and A* found a solution on the supplied map.

For the tested implementation:

```text
BFS             path = 40
A* Manhattan    path = 40
```

The exact number of expanded states depends on tie-breaking and implementation details. A* uses goal information through its heuristic, so a useful heuristic can focus the search.

## Task 6

### h(n) = 0

This removes the heuristic component, so A* behaves like uniform-cost search. With unit costs this is closely related to BFS.

### Euclidean distance

Euclidean distance is a lower bound on the number of horizontal/vertical moves, so it can be useful, although Manhattan distance better matches the movement geometry.

### 2 * Manhattan

This makes the heuristic more aggressive. It is not guaranteed to remain admissible, because it can exceed the true remaining cost.

The experiments in `search_agent.py` record solution status, path length and expanded states for all three variants.

## Task 7 reflection

The generated implementation was treated as a starting point rather than proof of correctness.

The most useful tests were:
- the original map;
- the one-step map;
- the impossible map.

These tests check both normal behaviour and failure behaviour. The impossible case is particularly useful because an implementation with a bad termination condition could search indefinitely.

I also checked the path length and verified that every consecutive pair of positions differs by one legal movement.

## LLM reflection

The LLM was useful for translating the search specification into Python data structures and the A* loop. Independent verification was still necessary because a program can produce a plausible path while implementing the algorithm incorrectly.
