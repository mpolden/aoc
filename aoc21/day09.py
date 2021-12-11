"""Day 9: Smoke Basin"""

from typing import List, Set, Tuple, Dict
from collections import namedtuple
from util import file_input, text_input, ints, product


example_input = """
2199943210
3987894921
9856789892
8767896789
9899965678
"""

Point = Tuple[int, int]


def parse_line(text: str) -> List[int]:
    return [int(c) for c in text]


def neighbours_of(point: Point, height: int, width: int) -> Set[Point]:
    neighbours: Set[Point] = set()
    x, y = point
    if x > 0:
        neighbours.add((x - 1, y))  # left
    if x < width - 1:
        neighbours.add((x + 1, y))  # right
    if y > 0:
        neighbours.add((x, y - 1))  # up
    if y < height - 1:
        neighbours.add((x, y + 1))  # down
    return neighbours


def min_neighbour(point: Point, lines: List[List[int]]) -> int:
    _, y = point
    return min(lines[y][x] for x, y in neighbours_of(point, len(lines), len(lines[y])))


def day9_1(lines: List[List[int]]) -> int:
    risk_level = 0
    for y, line in enumerate(lines):
        for x, n in enumerate(line):
            if n < min_neighbour((x, y), lines):
                risk_level += 1 + n
    return risk_level


assert day9_1(text_input(example_input, parse_line)) == 15
assert day9_1(file_input(9, parse_line)) == 633


def cluster_of(point: Point, lines: List[List[int]], cluster: Set[Point]) -> Set[Point]:
    cluster.add(point)
    _, y = point
    for np in neighbours_of(point, len(lines), len(lines[y])):
        x, y = np
        if np not in cluster and lines[y][x] != 9:
            cluster_of(np, lines, cluster)
    return cluster


def day9_2(lines: List[List[int]]) -> int:
    basin_sizes = []
    for y, line in enumerate(lines):
        for x, n in enumerate(line):
            point = (x, y)
            if n >= min_neighbour(point, lines):
                continue
            basin = cluster_of(point, lines, set())
            basin_sizes.append(len(basin))
    return product(sorted(basin_sizes)[-3:])


assert day9_2(text_input(example_input, parse_line)) == 1134
assert day9_2(file_input(9, parse_line)) == 1050192
