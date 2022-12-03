"""Day 3: Rucksack Reorganization"""

from typing import List, Set
from util import assert2, file_input, text_input

example_input = """
vJrwpWtwJgWrhcsFMMfFFhFp
jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL
PmmdzqPrVvPwwTWBwg
wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn
ttgJtRGJQctTZtZT
CrZsJsPPZsGzwwsLwLmpwMDw
"""


def priority(c: str) -> int:
    offset = 96 if c.islower() else 38
    return ord(c) - offset


def day3_1(rucksacks: List[List[str]]) -> int:
    n = 0
    for r in rucksacks:
        half = len(r) // 2
        a = set(r[:half])
        b = set(r[half:])
        common = a.intersection(b)
        n += priority(next(iter(common)))
    return n


assert2(157, day3_1(text_input(example_input, list)))
assert2(8109, day3_1(file_input(3, list)))


def day3_2(rucksacks: List[Set[str]]) -> int:
    chunk = 3
    groups = [rucksacks[n : n + chunk] for n in range(0, len(rucksacks), chunk)]
    n = 0
    for group in groups:
        common = set.intersection(*group)
        n += priority(next(iter(common)))
    return n


assert2(70, day3_2(text_input(example_input, set)))
assert2(2738, day3_2(file_input(3, set)))
