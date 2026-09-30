from search_agent import astar, bfs, manhattan


def check(name, grid, should_find, expected_length=None):
    path, expanded = astar(grid, manhattan)

    found = path is not None
    ok = found == should_find

    if expected_length is not None and found:
        ok = ok and (len(path) - 1 == expected_length)

    print(f"{name}: {'PASS' if ok else 'FAIL'}")
    if found:
        print("  path length:", len(path) - 1)
        print("  states expanded:", expanded)


if __name__ == "__main__":
    original = [
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

    trivial = [
        "#####",
        "#SG.#",
        "#####",
    ]

    impossible = [
        "#####",
        "#S#G#",
        "#####",
    ]

    check("Original warehouse", original, True)
    check("Trivial case", trivial, True, 1)
    check("No-solution case", impossible, False)
