"""Day 11: Dumbo Octopus"""

from itertools import count
from typing import List, Optional, Tuple, Set
from util import file_input, text_input, digits, quantify

example_input = """
5483143223
2745854711
5264556173
6141336146
6357385478
4167524645
2176841721
6882881134
4846848554
5283751526
"""


Point = Tuple[int, int]


def neighbours_of(point: Point, height: int, width: int) -> Set[Point]:
    neighbours: Set[Point] = set()
    x, y = point
    if x > 0:
        neighbours.add((x - 1, y))  # left
    if x < width - 1:
        neighbours.add((x + 1, y))  # right
    if y > 0:
        neighbours.add((x, y - 1))  # top
        if x > 0:
            neighbours.add((x - 1, y - 1))  # top-left
        if x < width - 1:
            neighbours.add((x + 1, y - 1))  # top-right
    if y < height - 1:
        neighbours.add((x, y + 1))  # bottom
        if x > 0:
            neighbours.add((x - 1, y + 1))  # bottom-left
        if x < width - 1:
            neighbours.add((x + 1, y + 1))  # bottom-right
    return neighbours


def flash(point: Point, rows: List[List[int]], flashed: Set[Point]) -> None:
    if point in flashed:
        return
    x, y = point
    rows[y][x] += 1
    if rows[y][x] <= 9:
        return
    flashed.add(point)
    for np in neighbours_of(point, len(rows), len(rows[y])):
        flash(np, rows, flashed)


def run_steps(rows: List[List[int]], max_steps: Optional[int] = 100) -> int:
    result = 0
    steps = count() if max_steps is None else range(max_steps)
    for step in steps:
        flashed: Set[Point] = set()
        for y in range(len(rows)):
            for x in range(len(rows[y])):
                flash((x, y), rows, flashed)
        for x, y in flashed:
            rows[y][x] = 0
        if max_steps is None:
            if all((quantify(r, lambda n: n == 0) == len(r) for r in rows)):
                return step + 1
        else:
            result += len(flashed)
    return result


def day11_1(rows: List[List[int]]) -> int:
    return run_steps(rows, 100)


assert day11_1(text_input(example_input, digits)) == 1656
assert day11_1(file_input(11, digits)) == 1647


def day11_2(rows: List[List[int]]) -> int:
    return run_steps(rows, None)


assert day11_2(text_input(example_input, digits)) == 195
assert day11_2(file_input(11, digits)) == 348
