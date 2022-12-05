"""Day 5: Supply Stacks"""

import re

from collections import deque
from typing import List, Tuple, Deque, Iterable
from util import assert2, file_input, text_input, ints

example_input = """
    [D]
[N] [C]
[Z] [M] [P]
 1   2   3

move 1 from 2 to 1
move 3 from 1 to 3
move 2 from 2 to 1
move 1 from 1 to 2
"""


Move = Tuple[int, int, int]


def parse_stacks(lines: List[str]) -> List[Deque[str]]:
    stacks: List[Deque[str]] = []
    for line in lines:
        crates = re.findall(r"\s{4}|[A-Z]", line)
        while len(stacks) < len(crates):
            stacks.append(deque())
        for col, c in enumerate(crates):
            if c[0] != " ":
                stacks[col].append(c[0])
    return stacks


def parse_moves(lines: List[str]) -> Iterable[Move]:
    def parse_move(s: str) -> Move:
        nums = ints(s)
        return (nums[0], nums[1] - 1, nums[2] - 1)

    return (parse_move(line) for line in lines if line.startswith("move "))


def arrange_stacks(lines: List[str], retain_order: bool = False) -> str:
    stacks = parse_stacks(lines)
    for n, src, dst in parse_moves(lines):
        crates = []
        for _ in range(n):
            crates.append(stacks[src].popleft())
        if retain_order:
            crates.reverse()
        stacks[dst].extendleft(crates)
    return "".join(stack[0] for stack in stacks)


def day5_1(lines: List[str]) -> str:
    return arrange_stacks(lines)


assert2("CMZ", day5_1(text_input(example_input, str)))
assert2("CWMTGHBDW", day5_1(file_input(5, str)))


def day5_2(lines: List[str]) -> str:
    return arrange_stacks(lines, retain_order=True)


assert2("MCD", day5_2(text_input(example_input, str)))
assert2("SSCGWJCRB", day5_2(file_input(5, str)))
