"""Day 3: Rucksack Reorganization"""

from typing import List, Set, Iterable
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


def common_priority(*args: Set[str]) -> int:
    common = set.intersection(*args)
    return priority(next(iter(common)))


def sum_priority(sacks: Iterable[Iterable[Set[str]]]) -> int:
    return sum(common_priority(*sack) for sack in sacks)


def day3_1(rucksacks: List[List[str]]) -> int:
    def split_rucksack(r: List[str]) -> Iterable[Set[str]]:
        half = len(r) // 2
        return set(r[:half]), set(r[half:])

    return sum_priority((split_rucksack(r) for r in rucksacks))


assert2(157, day3_1(text_input(example_input, list)))
assert2(8109, day3_1(file_input(3, list)))


def day3_2(rucksacks: List[Set[str]]) -> int:
    chunk = 3
    sacks = (rucksacks[n : n + chunk] for n in range(0, len(rucksacks), chunk))
    return sum_priority(sacks)


assert2(70, day3_2(text_input(example_input, set)))
assert2(2738, day3_2(file_input(3, set)))
