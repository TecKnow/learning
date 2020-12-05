import math

def count_collisions(terrain: list[str], dx: int, dy: int) -> int:
    x = y = 0
    width = len(terrain[0])
    height = len(terrain)
    print(f"{width=}, {height=}, {dx=}, {dy=}")
    collisions = 0
    while y < height:
        row = data[y]
        collision = row[x] == "#"
        position_character = "O" if not collision else "X"
        visited_row = row[:x] + position_character + row[x + 1:]
        print(visited_row)
        collisions += collision
        x = (x + dx) % width
        y = y + dy
    return collisions


if __name__ == "__main__":
    data = [x.strip() for x in open("Day 3 Data.txt").readlines()]
    slopes = ((1, 1), (3, 1), (5, 1), (7, 1), (1, 2))
    collisions_by_slope = tuple(count_collisions(data, dx, dy) for (dx, dy) in slopes)
    print(math.prod(collisions_by_slope))

