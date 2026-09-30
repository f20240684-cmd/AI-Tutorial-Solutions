# Lab Answers

## Task 1

1. **Environment:** A two-dimensional warehouse grid containing obstacles and free cells.
2. **Goal:** Move the vehicle from `S` to `G` without crossing an obstacle.
3. **Actions:** Up, Down, Left and Right.
4. **Information maintained:** Current position, discovered states and parent information used to reconstruct the route.
5. **Goal-based vs reflex:** The agent has an explicit destination and searches for a sequence of actions that achieves it.

### Think About It

For a larger warehouse the same BFS idea can still work, but it may require much more memory and may expand many more states. A larger state space makes the choice of search strategy more important.

## Task 2

The design is:

```text
Warehouse grid
      |
      v
Current state
      |
      v
Valid actions
      |
      v
Search / decision component
      |
      v
Goal test
      |
      v
Path
```

## Task 3

The program was tested on the original map, a trivial one-step map and a map with no solution.

The original map produced a path of length 20. The no-solution test terminated and reported failure.

## LLM questions

**Did the LLM generate a working program on the first attempt?**  
The generated implementation was used as a starting point and was then tested rather than assumed to be correct.

**How can the prompt be improved?**  
The prompt should specify the grid representation, movement rules, expected output, search requirements and edge cases.

**What search algorithm was used?**  
Breadth-first search.

**Why?**  
The state space is small and every move has the same cost. BFS also gives a shortest path in terms of number of moves.
