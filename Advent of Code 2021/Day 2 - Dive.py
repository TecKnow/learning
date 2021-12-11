sample_data = """
forward 5
down 5
forward 8
up 3
down 8
forward 2
"""
sample_data = [line for line in sample_data.splitlines() if line.strip()]


def simple_commands(input_filename: str = "Day 2 Data.txt"):
    position = 0
    depth = 0

    with open(input_filename) as input_file:
        for command_line in input_file:
            cmd_parts = command_line.split()  # type: list[str]
            if len(cmd_parts) != 2:
                raise ValueError("Command line has too many parts")
            if cmd_parts[0] not in set("forward up down".split()):
                raise ValueError(f"Command {cmd_parts[0]} not recognized.")
            cmd_parts[1] = int(cmd_parts[1])
            direction, distance = cmd_parts
            if direction == "up":
                depth -= distance
            elif direction == "down":
                depth += distance
            elif direction == "forward":
                position += distance
            else:
                raise ValueError("Can't be here!")
        print(f"{position=} {depth=}")
        print(position * depth)


def aim_commands(input_filename: str = "Day 2 Data.txt"):
    position = 0
    depth = 0
    aim = 0

    with open(input_filename) as input_file:
        for command_line in input_file:
            if not command_line:
                continue
            command_parts = command_line.split()
            if len(command_parts) != 2:
                raise ValueError(f"Command line {command_line} has too many parts.")
            direction, distance = command_parts
            if direction not in set("up down forward".split()):
                raise ValueError(f"Command {direction} not recognized.")
            distance = int(distance)
            if direction == "down":
                aim += distance
            if direction == "up":
                aim -= distance
            if direction == "forward":
                position += distance
                depth += aim*distance
    print(f"{position=}, {depth=}, {aim=}")
    print(position * depth)


if __name__ == "__main__":
    aim_commands()
