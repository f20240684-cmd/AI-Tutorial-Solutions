from first_order import DATA, prepare_data, build_model
from second_order import prepare_data as prepare_second
from second_order import build_model as build_second


def check_first_order():
    data = prepare_data(DATA)
    _, probabilities = build_model(data)

    totals = [sum(dist.values()) for dist in probabilities.values()]
    return all(abs(total - 1.0) < 1e-9 for total in totals)


def check_second_order():
    data = prepare_second(DATA)
    _, probabilities = build_second(data)

    totals = [sum(dist.values()) for dist in probabilities.values()]
    return all(abs(total - 1.0) < 1e-9 for total in totals)


if __name__ == "__main__":
    print("First-order normalisation:", "PASS" if check_first_order() else "FAIL")
    print("Second-order normalisation:", "PASS" if check_second_order() else "FAIL")
