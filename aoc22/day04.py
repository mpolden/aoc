"""Day 4: Camp Cleanup"""

from typing import List, Tuple
from util import assert2, file_input, text_input

example_input = """
2-4,6-8
2-3,4-5
5-7,7-9
2-8,3-7
6-6,4-6
2-6,4-8
"""

Range = Tuple[int, int]


def parse_range(s: str) -> Range:
    start, _, end = s.partition("-")
    return int(start), int(end)


def parse_assignment(s: str) -> Tuple[Range, Range]:
    a, _, b = s.partition(",")
    return parse_range(a), parse_range(b)


def overlap(a: Range, b: Range, partial: bool = False) -> bool:
    return (a[0] >= b[0] and a[1] <= b[1]) or (
        partial and a[1] >= b[0] and a[1] <= b[1]
    )


def count_overlaps(assignments: List[Tuple[Range, Range]], partial: bool) -> int:
    return sum(overlap(a, b, partial) or overlap(b, a, partial) for a, b in assignments)


def day4_1(assignments: List[Tuple[Range, Range]]) -> int:
    return count_overlaps(assignments, False)


assert2(2, day4_1(text_input(example_input, parse_assignment)))
assert2(560, day4_1(file_input(4, parse_assignment)))


def day4_2(assignments: List[Tuple[Range, Range]]) -> int:
    return count_overlaps(assignments, True)


assert2(4, day4_2(text_input(example_input, parse_assignment)))
assert2(839, day4_2(file_input(4, parse_assignment)))
