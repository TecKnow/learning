from random import random
from statistics import mean


def random_walk(initial_value: int, p_increase: float):
    current_position: int = initial_value
    steps = 0
    while current_position != 0:
        steps += 1
        if random() <= p_increase:
            current_position += 1
        else:
            current_position -= 1
    return steps


if __name__ == "__main__":
    starting_position = 5
    p_right = 1 / 3
    sample_size = 1000000

    elements = tuple(random_walk(starting_position, p_right) for x in range(sample_size))
    print(f"average: {mean(elements)}, max: {max(elements)}")
