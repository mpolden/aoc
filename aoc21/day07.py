"""Day 7: The Treachery of Whales"""

from collections import defaultdict
from typing import List, Dict
from util import file_input, text_input, ints

example_input = "16,1,2,0,4,2,7,1,2,14"


def optimal_position(initial: List[int], fixed_burn_rate: bool = True) -> int:
    fuel_required: Dict[int, int] = defaultdict(int)
    positions = range(0, max(initial) + 1)
    for from_pos in initial:
        for to_pos in positions:
            fuel_spent = abs(to_pos - from_pos)
            if not fixed_burn_rate:
                fuel_spent = int((fuel_spent ** 2 + fuel_spent) / 2)
            fuel_required[to_pos] += fuel_spent
    return min(fuel_required.values())


def day7_1(nums: List[int]) -> int:
    return optimal_position(nums)


assert day7_1(text_input(example_input, ints)[0]) == 37
assert day7_1(file_input(7, ints)[0]) == 345035


def day7_2(nums: List[int]) -> int:
    return optimal_position(nums, fixed_burn_rate=False)


assert day7_2(text_input(example_input, ints)[0]) == 168
assert day7_2(file_input(7, ints)[0]) == 97038163
