"""Day 10: Cathode-Ray Tube"""

from util import assert2, text_input, file_input
from typing import List, Tuple, TypeVar, Callable


example_input = """
addx 15
addx -11
addx 6
addx -3
addx 5
addx -1
addx -8
addx 13
addx 4
noop
addx -1
addx 5
addx -1
addx 5
addx -1
addx 5
addx -1
addx 5
addx -1
addx -35
addx 1
addx 24
addx -19
addx 1
addx 16
addx -11
noop
noop
addx 21
addx -15
noop
noop
addx -3
addx 9
addx 1
addx -3
addx 8
addx 1
addx 5
noop
noop
noop
noop
noop
addx -36
noop
addx 1
addx 7
noop
noop
noop
addx 2
addx 6
noop
noop
noop
noop
noop
addx 1
noop
noop
addx 7
addx 1
noop
addx -13
addx 13
addx 7
noop
addx 1
addx -33
noop
noop
noop
addx 2
noop
noop
noop
addx 8
noop
addx -1
addx 2
addx 1
noop
addx 17
addx -9
addx 1
addx 1
addx -3
addx 11
noop
noop
addx 1
noop
addx 1
noop
noop
addx -13
addx -19
addx 1
addx 3
addx 26
addx -30
addx 12
addx -1
addx 3
addx 1
noop
noop
noop
addx -9
addx 18
addx 1
addx 2
noop
noop
addx 9
noop
noop
noop
addx -1
addx 2
addx -37
addx 1
addx 3
noop
addx 15
addx -21
addx 22
addx -6
addx 1
noop
addx 2
addx 1
noop
addx -10
noop
noop
addx 20
addx 1
addx 2
addx 2
addx -6
addx -11
noop
noop
noop
"""


Add = Tuple[int, int]
T = TypeVar("T")


def parse_add(text: str) -> Add:
    opcode, _, value = text.partition(" ")
    if opcode == "addx":
        return int(value), 2
    return 0, 1


def run(instructions: List[Add], callback: Callable[[int, int], T]) -> None:
    x = 1
    cycle = 1
    for inst in instructions:
        incr, cycles = inst
        for _ in range(cycles):
            callback(cycle, x)
            cycle += 1
        x += incr


def day10_1(instructions: List[Add]) -> int:
    signal = 0

    def calc(cycle: int, x: int) -> None:
        nonlocal signal
        if cycle == 20 or cycle % 40 == 20:
            signal += cycle * x

    run(instructions, calc)
    return signal


assert2(13140, day10_1(text_input(example_input, parse_add)))
assert2(13520, day10_1(file_input(10, parse_add)))


def day10_2(instructions: List[Add]) -> str:
    screen = [["."] * 40 for _ in range(6)]

    def draw(cycle: int, x: int) -> None:
        row = int((cycle - 1) / 40)
        col = (cycle - 1) % 40
        if col in (x - 1, x, x + 1):
            screen[row][col] = "#"

    run(instructions, draw)
    return "\n".join(("".join(line) for line in screen))


assert2(
    """##..##..##..##..##..##..##..##..##..##..
###...###...###...###...###...###...###.
####....####....####....####....####....
#####.....#####.....#####.....#####.....
######......######......######......####
#######.......#######.......#######.....""",
    day10_2(text_input(example_input, parse_add)),
)
assert2(
    """###...##..###..#..#.###..####..##..###..
#..#.#..#.#..#.#..#.#..#.#....#..#.#..#.
#..#.#....#..#.####.###..###..#..#.###..
###..#.##.###..#..#.#..#.#....####.#..#.
#....#..#.#....#..#.#..#.#....#..#.#..#.
#.....###.#....#..#.###..####.#..#.###..""",
    day10_2(file_input(10, parse_add)),
)
