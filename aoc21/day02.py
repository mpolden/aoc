from util import read_input, parse_input


def parse_cmd(data):
    direction, value = data.split(" ")
    value = int(value)
    return direction, value


example_input = parse_input(
    """
forward 5
down 5
forward 8
up 3
down 8
forward 2
""",
    parser=parse_cmd,
)


def day2_1(cmds):
    hpos = 0
    depth = 0
    for cmd in cmds:
        direction, value = cmd
        if direction == "forward":
            hpos += value
        elif direction == "down":
            depth += value
        elif direction == "up":
            depth -= value
    return hpos * depth


assert day2_1(example_input) == 150
assert day2_1(read_input(2, parser=parse_cmd)) == 2039912


def day2_2(cmds):
    hpos = 0
    depth = 0
    aim = 0
    for cmd in cmds:
        direction, value = cmd
        if direction == "forward":
            hpos += value
            depth += aim * value
        elif direction == "down":
            aim += value
        elif direction == "up":
            aim -= value
    return hpos * depth


assert day2_2(example_input) == 900
assert day2_2(read_input(2, parser=parse_cmd)) == 1942068080
