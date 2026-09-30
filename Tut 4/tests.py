from planner import (
    Action,
    bfs_plan,
    build_warehouse_actions,
    execute_plan,
)


def check_plan(initial, goal, actions, expected):
    plan = bfs_plan(initial, actions, goal)

    found = plan is not None
    ok = found == expected

    if found:
        states = execute_plan(initial, plan)
        ok = ok and goal.issubset(states[-1])

    print("PASS" if ok else "FAIL")
    if plan:
        print("  ", [action.name for action in plan])


if __name__ == "__main__":
    initial = {"At(Robot,A)", "At(Package,A)"}
    goal = {"At(Package,C)"}

    print("Test A - original solvable problem")
    check_plan(
        initial,
        goal,
        build_warehouse_actions(),
        True
    )

    print("\nTest B - impossible because PickUp is removed")
    check_plan(
        initial,
        goal,
        build_warehouse_actions(include_pickup=False),
        False
    )

    print("\nTest C - irrelevant action added")
    check_plan(
        initial,
        goal,
        build_warehouse_actions(include_irrelevant=True),
        True
    )
