import heapq
from collections import deque


WAREHOUSE = [
    "#################",
    "#S....#.........#",
    "#.###.#.#######.#",
    "#...#.#.......#.#",
    "###.#.#######.#.#",
    "#...#.........#.#",
    "#.###########.#.#",
    "#.............#G#",
    "#################",
]

MOVES = [
    (-1, 0),
    (1, 0),
    (0, -1),
    (0, 1),
]


def find(grid, symbol):
    for r, row in enumerate(grid):
        for c, value in enumerate(row):
            if value == symbol:
                return (r, c)
    raise ValueError(f"{symbol} not found")


def neighbours(grid, state):
    r, c = state

    for dr, dc in MOVES:
        nr, nc = r + dr, c + dc

        if 0 <= nr < len(grid) and 0 <= nc < len(grid[0]):
            if grid[nr][nc] != "#":
                yield (nr, nc)


def reconstruct(parent, goal):
    path = []
    current = goal

    while current is not None:
        path.append(current)
        current = parent[current]

    path.reverse()
    return path


def manhattan(state, goal):
    return abs(state[0] - goal[0]) + abs(state[1] - goal[1])


def euclidean(state, goal):
    return ((state[0] - goal[0]) ** 2 + (state[1] - goal[1]) ** 2) ** 0.5


def astar(grid, heuristic=manhattan, heuristic_scale=1.0):
    start = find(grid, "S")
    goal = find(grid, "G")

    frontier = []
    counter = 0
    heapq.heappush(frontier, (0, counter, start))

    parent = {start: None}
    g_cost = {start: 0}
    expanded = 0

    while frontier:
        _, _, current = heapq.heappop(frontier)

        expanded += 1

        if current == goal:
            return reconstruct(parent, goal), expanded

        for next_state in neighbours(grid, current):
            new_cost = g_cost[current] + 1

            if next_state not in g_cost or new_cost < g_cost[next_state]:
                g_cost[next_state] = new_cost
                h = heuristic_scale * heuristic(next_state, goal)
                f = new_cost + h

                counter += 1
                heapq.heappush(frontier, (f, counter, next_state))
                parent[next_state] = current

    return None, expanded


def bfs(grid):
    start = find(grid, "S")
    goal = find(grid, "G")

    queue = deque([start])
    parent = {start: None}
    expanded = 0

    while queue:
        current = queue.popleft()
        expanded += 1

        if current == goal:
            return reconstruct(parent, goal), expanded

        for next_state in neighbours(grid, current):
            if next_state not in parent:
                parent[next_state] = current
                queue.append(next_state)

    return None, expanded


def print_result(name, result):
    path, expanded = result

    print(f"{name}")
    print("-" * 40)

    if path is None:
        print("Solution found: No")
    else:
        print("Solution found: Yes")
        print("Path length:", len(path) - 1)
        print("Path:", path)

    print("States expanded:", expanded)
    print()


def main():
    print("Warehouse Search: BFS and A*")
    print("=" * 50)

    print_result("BFS", bfs(WAREHOUSE))
    print_result("A* Manhattan", astar(WAREHOUSE, manhattan))
    print_result("A* h(n)=0", astar(WAREHOUSE, manhattan, 0.0))
    print_result("A* Euclidean", astar(WAREHOUSE, euclidean))
    print_result("A* Manhattan x2", astar(WAREHOUSE, manhattan, 2.0))


if __name__ == "__main__":
    main()
