# Goal-Based Agent - Warehouse Navigation

This is my implementation for the **Agents: Laboratory Exercise – Constructing a Goal-Based Agent using a Large Language Model**.

The laboratory asks for a goal-based warehouse vehicle that has an explicit destination and has to find a collision-free route through the grid. It also asks us to use an LLM as a software engineering assistant and then test the generated program.

## Problem specification

The environment is the warehouse grid given in the lab.

- `S` = starting position
- `G` = goal
- `#` = obstacle
- `.` = free cell
- Actions = Up, Down, Left, Right

The agent's goal is to reach `G` without moving through an obstacle. These are the exact environment/action definitions given in the laboratory.

### Why is it goal-based?

The agent does not simply react to the current square. It has an explicit goal, keeps track of explored states and searches for a sequence of actions that reaches the destination.

## Implementation

I used breadth-first search because every movement has the same cost and the state space is small.

The program:

1. Finds `S` and `G`.
2. Adds the start position to a queue.
3. Expands valid neighbouring cells.
4. Stores the parent of every newly discovered cell.
5. Stops when the goal is reached.
6. Reconstructs the sequence of moves.

The lab's suggested LLM prompt also asks for a collision-free path, a suitable search explanation and testing.

## Running

```bash
python warehouse_agent.py
python tests.py
```

## Task 1 answers

**1. What is the environment?**  
A 2-D warehouse grid containing free cells and shelving/obstacle cells.

**2. What is the goal?**  
Move the vehicle from `S` to `G`.

**3. What actions are available?**  
Up, Down, Left and Right.

**4. What information must the agent maintain?**  
Its current position, which positions have already been explored, and enough parent information to reconstruct the path.

**5. Why is it goal-based?**  
Because action selection is directed towards achieving an explicitly specified goal rather than only reacting to the current percept.

## Testing

The tests include:

- Original warehouse
- A one-step/trivial case
- A map with no possible solution

The laboratory specifically asks whether the program works on the warehouse map and encourages improving the prompt if the first generated program does not work.

## LLM usage

I used the prompt in `llm_prompt.txt` to generate the initial implementation and then ran the program and test cases. The generated code was treated as an implementation suggestion rather than something to accept without checking.

## Files

```text
warehouse_agent.py
tests.py
llm_prompt.txt
README.md
```
