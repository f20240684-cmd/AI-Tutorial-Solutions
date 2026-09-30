from warehouse_agent import bfs


def run_test(name, grid, expected_found):
    path, _ = bfs(grid)
    found = path is not None
    print(f"{name}: {'PASS' if found == expected_found else 'FAIL'}")
    if found:
        print("  path length:", len(path))


if __name__ == "__main__":
    original = [
        "#####################",
        "#S....#............G#",
        "#.##....##########..#",
        "#....##.............#",
        "#.######.###.#.###..#",
        "#........#..........#",
        "#####################",
    ]

    trivial = [
        "#####",
        "#SG.#",
        "#####",
    ]

    impossible = [
        "#######",
        "#S....#",
        "###.###",
        "#...#G#",
        "#######",
    ]

    run_test("Original warehouse", original, True)
    run_test("Trivial case", trivial, True)
    run_test("No-solution case", impossible, False)
