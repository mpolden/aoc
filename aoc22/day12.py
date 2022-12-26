"""Day 12: Hill Climbing Algorithm"""

from typing import List, Tuple, Set, Iterable
from util import text_input, file_input, assert2
import sys

example_input = """
Sabqponm
abcryxxl
accszExk
acctuvwj
abdefghi
"""


Point = Tuple[int, int]
Grid = List[List[str]]


def neighbours(point: Point, grid: Grid) -> Iterable[Point]:
    x, y = point
    if x > 0:
        yield (x - 1, y)  # left
    if x < len(grid[0]) - 1:
        yield (x + 1, y)  # right
    if y > 0:
        yield (x, y - 1)  # up
    if y < len(grid) - 1:
        yield (x, y + 1)  # down


def height(point: Point, grid: Grid) -> int:
    symbol = grid[point[1]][point[0]]
    if symbol == "S":
        return 1
    elif symbol == "E":
        return 26
    return ord(symbol) - 96


def reachable(src: Point, dst: Point, grid: Grid) -> bool:
    return height(dst, grid) - height(src, grid) <= 1


def find_symbol(symbol: str, grid: Grid) -> List[Point]:
    points: List[Point] = []
    for y, line in enumerate(grid):
        for x, c in enumerate(line):
            if c == symbol:
                points.append((x, y))
    return points


def min_steps(s: Point, e: Point, grid: Grid) -> int:
    queue: List[Tuple[Point, int]] = [(s, 0)]
    visited: Set[Point] = set()
    while len(queue) > 0:
        current, steps = queue.pop(0)
        if current == e:
            return steps
        if current not in visited:
            visited.add(current)
            for point in neighbours(current, grid):
                if reachable(current, point, grid):
                    queue.append((point, steps + 1))
    return sys.maxsize


def day12_1(grid: Grid) -> int:
    s = find_symbol("S", grid)[0]
    e = find_symbol("E", grid)[0]
    return min_steps(s, e, grid)


assert2(31, day12_1(text_input(example_input, list)))
assert2(528, day12_1(file_input(12, list)))


def day12_2(grid: Grid) -> int:
    e = find_symbol("E", grid)[0]
    return min(min_steps(s, e, grid) for s in find_symbol("a", grid))


assert2(29, day12_2(text_input(example_input, list)))
assert2(522, day12_2(file_input(12, list)))
