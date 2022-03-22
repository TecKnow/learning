from random import random


def random_walk_destination(initial_value: int, target_value: int, p_increase: float):
    current_position: int = initial_value
    steps = 0
    while current_position != 0:
        steps += 1
        if random() <= p_increase:
            current_position += 1
        else:
            current_position -= 1
        if current_position == target_value:
            return True, steps
    return False, steps


if __name__ == "__main__":
    starting_position = 3
    destination_position = 5
    p_right = 1 / 3
    sample_size = 10000000

    choices = 1/37, 7/31, 1/73, 7/13

    elements = tuple(
        random_walk_destination(starting_position, destination_position, p_right) for x in range(sample_size))
    successes = tuple(e[1] for e in elements if e[0] is True)
    failures = tuple(e[1] for e in elements if e[0] is False)
    print(
        f"P(success): {(p_success := len(successes) / sample_size)}, "
        f"longest success: {max(successes)}, longest failure: {max(failures)}")
    print(choices)
    print(*(x - p_success for x in choices))

