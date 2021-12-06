"""Day 6: Lanternfish"""

from itertools import repeat
from typing import List
from util import file_input, text_input, ints

example_input = "3,4,3,1,2"


def population(initial: List[int], days: int) -> int:
    timers = list(repeat(0, 9))
    for n in initial:
        timers[n] += 1
    for day in range(days):
        reproduced = timers[0]
        for timer in range(len(timers) - 1):
            timers[timer] = timers[timer + 1]
        timers[6] += reproduced
        timers[8] = reproduced
    return sum(timers)


def day6_1(initial: List[int]) -> int:
    return population(initial, 80)


assert day6_1(text_input(example_input, ints)[0]) == 5934
assert day6_1(file_input(6, ints)[0]) == 389726


def day6_2(initial: List[int]) -> int:
    return population(initial, 256)


assert day6_2(text_input(example_input, ints)[0]) == 26984457539
assert day6_2(file_input(6, ints)[0]) == 1743335992042
