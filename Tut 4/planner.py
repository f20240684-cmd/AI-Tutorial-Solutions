from collections import deque


class Action:
    def __init__(self, name, positive_preconditions=None,
                 negative_preconditions=None, positive_effects=None,
                 negative_effects=None):
        self.name = name
        self.positive_preconditions = set(positive_preconditions or [])
        self.negative_preconditions = set(negative_preconditions or [])
        self.positive_effects = set(positive_effects or [])
        self.negative_effects = set(negative_effects or [])

    def is_applicable(self, state):
        return (
            self.positive_preconditions <= state
            and self.negative_preconditions.isdisjoint(state)
        )

    def apply(self, state):
        new_state = set(state)
        new_state -= self.negative_effects
        new_state |= self.positive_effects
        return frozenset(new_state)


def bfs_plan(initial_state, actions, goal):
    initial_state = frozenset(initial_state)
    goal = set(goal)

    if goal <= initial_state:
        return []

    queue = deque([(initial_state, [])])
    visited = {initial_state}

    while queue:
        state, plan = queue.popleft()

        for action in actions:
            if not action.is_applicable(state):
                continue

            next_state = action.apply(state)

            if next_state in visited:
                continue

            new_plan = plan + [action]
            if goal <= next_state:
                return new_plan

            visited.add(next_state)
            queue.append((next_state, new_plan))

    return None


def build_warehouse_actions(include_pickup=True, include_irrelevant=False):
    actions = [
        Action(
            "Move(A, B)",
            positive_preconditions={"At(Robot,A)"},
            positive_effects={"At(Robot,B)"},
            negative_effects={"At(Robot,A)"}
        ),
        Action(
            "Move(B, A)",
            positive_preconditions={"At(Robot,B)"},
            positive_effects={"At(Robot,A)"},
            negative_effects={"At(Robot,B)"}
        ),
        Action(
            "Move(B, C)",
            positive_preconditions={"At(Robot,B)"},
            positive_effects={"At(Robot,C)"},
            negative_effects={"At(Robot,B)"}
        ),
        Action(
            "Move(C, B)",
            positive_preconditions={"At(Robot,C)"},
            positive_effects={"At(Robot,B)"},
            negative_effects={"At(Robot,C)"}
        ),
    ]

    if include_pickup:
        actions.append(
            Action(
                "PickUp(Package, A)",
                positive_preconditions={
                    "At(Robot,A)",
                    "At(Package,A)"
                },
                positive_effects={"Holding(Package)"},
                negative_effects={"At(Package,A)"}
            )
        )

    actions.append(
        Action(
            "PickUp(Package, B)",
            positive_preconditions={
                "At(Robot,B)",
                "At(Package,B)"
            },
            positive_effects={"Holding(Package)"},
            negative_effects={"At(Package,B)"}
        )
    )

    actions.append(
        Action(
            "PickUp(Package, C)",
            positive_preconditions={
                "At(Robot,C)",
                "At(Package,C)"
            },
            positive_effects={"Holding(Package)"},
            negative_effects={"At(Package,C)"}
        )
    )

    actions.extend([
        Action(
            "Drop(Package, A)",
            positive_preconditions={
                "At(Robot,A)",
                "Holding(Package)"
            },
            positive_effects={"At(Package,A)"},
            negative_effects={"Holding(Package)"}
        ),
        Action(
            "Drop(Package, B)",
            positive_preconditions={
                "At(Robot,B)",
                "Holding(Package)"
            },
            positive_effects={"At(Package,B)"},
            negative_effects={"Holding(Package)"}
        ),
        Action(
            "Drop(Package, C)",
            positive_preconditions={
                "At(Robot,C)",
                "Holding(Package)"
            },
            positive_effects={"At(Package,C)"},
            negative_effects={"Holding(Package)"}
        )
    ])

    if include_irrelevant:
        actions.append(
            Action(
                "Wait(A)",
                positive_preconditions={"At(Robot,A)"},
                positive_effects={"At(Robot,A)"}
            )
        )

    return actions


def execute_plan(initial_state, plan):
    state = frozenset(initial_state)
    states = [state]

    for action in plan:
        if not action.is_applicable(state):
            return None

        state = action.apply(state)
        states.append(state)

    return states


def print_plan(initial_state, plan):
    if plan is None:
        print("No plan found.")
        return

    states = execute_plan(initial_state, plan)

    print("Plan:")
    for i, action in enumerate(plan, start=1):
        print(f"{i}. {action.name}")

    print("\nStates:")
    for i, state in enumerate(states):
        print(f"S{i}: {sorted(state)}")

    print("\nGoal achieved:", "At(Package,C)" in states[-1])


def main():
    initial = {
        "At(Robot,A)",
        "At(Package,A)"
    }

    goal = {"At(Package,C)"}
    actions = build_warehouse_actions()

    print("Logical Planning Agent")
    print("=" * 50)
    print_plan(initial, bfs_plan(initial, actions, goal))


if __name__ == "__main__":
    main()
