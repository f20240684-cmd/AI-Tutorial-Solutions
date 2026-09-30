from collections import deque

WAREHOUSE = [
    "#####################",
    "#S....#............G#",
    "#.##....##########..#",
    "#....##.............#",
    "#.######.###.#.###..#",
    "#........#..........#",
    "#####################",
]

MOVES = {
    "Up": (-1, 0),
    "Down": (1, 0),
    "Left": (0, -1),
    "Right": (0, 1),
}


def find_position(grid, symbol):
    for r, row in enumerate(grid):
        for c, value in enumerate(row):
            if value == symbol:
                return (r, c)
    return None


def valid_moves(grid, position):
    r, c = position

    for name, (dr, dc) in MOVES.items():
        nr, nc = r + dr, c + dc
        if 0 <= nr < len(grid) and 0 <= nc < len(grid[0]):
            if grid[nr][nc] != "#":
                yield name, (nr, nc)


def bfs(grid):
    start = find_position(grid, "S")
    goal = find_position(grid, "G")

    queue = deque([start])
    parent = {start: None}
    move_used = {}

    while queue:
        current = queue.popleft()

        if current == goal:
            path = []
            position = current

            while parent[position] is not None:
                path.append(move_used[position])
                position = parent[position]

            path.reverse()
            return path, parent

        for move, next_position in valid_moves(grid, current):
            if next_position not in parent:
                parent[next_position] = current
                move_used[next_position] = move
                queue.append(next_position)

    return None, parent


def print_path(grid, path):
    position = find_position(grid, "S")
    print("\nPath:")
    print(" -> ".join(path))
    print("Path length:", len(path))

    print("\nVisited positions in the final path:")
    print(position, end="")

    for move in path:
        dr, dc = MOVES[move]
        position = (position[0] + dr, position[1] + dc)
        print(" ->", position, end="")
    print()


def main():
    path, visited = bfs(WAREHOUSE)

    print("Warehouse Navigation - Goal Based Agent")
    print("-" * 50)

    if path is None:
        print("No path found.")
        return

    print("Environment: warehouse grid")
    print("Start:", find_position(WAREHOUSE, "S"))
    print("Goal:", find_position(WAREHOUSE, "G"))
    print_path(WAREHOUSE, path)
    print("States discovered:", len(visited))


if __name__ == "__main__":
    main()
