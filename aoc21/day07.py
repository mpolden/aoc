"""Day 7: The Treachery of Whales"""

from typing import List, Dict
from util import file_input, text_input, ints

example_input = "16,1,2,0,4,2,7,1,2,14"


def min_consumption(positions: List[int], fixed_burn_rate: bool = True) -> int:
    num_positions = max(positions) + 1
    fuel_required = [0] * num_positions
    for from_pos in positions:
        for to_pos in range(0, num_positions):
            fuel_spent = abs(to_pos - from_pos)
            if not fixed_burn_rate:
                fuel_spent = int((fuel_spent ** 2 + fuel_spent) / 2)
            fuel_required[to_pos] += fuel_spent
    return min(fuel_required)


def day7_1(nums: List[int]) -> int:
    return min_consumption(nums)


assert day7_1(text_input(example_input, ints)[0]) == 37
assert day7_1(file_input(7, ints)[0]) == 345035


def day7_2(nums: List[int]) -> int:
    return min_consumption(nums, fixed_burn_rate=False)


assert day7_2(text_input(example_input, ints)[0]) == 168
assert day7_2(file_input(7, ints)[0]) == 97038163
