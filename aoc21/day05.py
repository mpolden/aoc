"""Day 5: Hydrothermal Venture"""

from collections import namedtuple, defaultdict
from typing import Dict, List, Optional, Tuple
from util import file_input, text_input, ints, split

example_input = """
0,9 -> 5,9
8,0 -> 0,8
9,4 -> 3,4
2,2 -> 2,1
7,0 -> 7,4
6,4 -> 2,0
0,9 -> 2,9
3,4 -> 1,4
0,0 -> 8,8
5,5 -> 8,2
"""

Point = namedtuple("Point", ["x", "y"])
Line = Tuple[Point, Point]


def parse_line(text: str) -> Line:
    start, end = split(text, parser=ints, sep=" -> ")
    return Point(*start), Point(*end)


def points_of(line: Line, diagonal: bool = False) -> List[Point]:
    start, end = line
    if start.x == end.x:
        return [
            Point(start.x, y)
            for y in range(min(start.y, end.y), max(start.y, end.y) + 1)
        ]
    elif start.y == end.y:
        return [
            Point(x, start.y)
            for x in range(min(start.x, end.x), max(start.x, end.x) + 1)
        ]
    elif diagonal:
        x_step = 1 if start.x < end.x else -1
        y_step = 1 if start.y < end.y else -1
        return [
            Point(x, y)
            for x, y in zip(
                range(start.x, end.x + x_step, x_step),
                range(start.y, end.y + y_step, y_step),
            )
        ]
    return []


def overlapping(lines: List[Line], diagonal: bool = False) -> int:
    freq: Dict[Point, int] = defaultdict(int)
    for line in lines:
        for point in points_of(line, diagonal):
            freq[point] += 1
    return sum(1 for count in freq.values() if count > 1)


def day5_1(lines: List[Line]) -> int:
    return overlapping(lines)


assert day5_1(text_input(example_input, parse_line)) == 5
assert day5_1(file_input(5, parse_line)) == 6710


def day5_2(lines: List[Line]) -> int:
    return overlapping(lines, diagonal=True)


assert day5_2(text_input(example_input, parse_line)) == 12
assert day5_2(file_input(5, parse_line)) == 20121
