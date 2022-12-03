"""Day 1: Calorie Counting"""

from typing import List
from util import file_input, text_input, ints

example_input = """
1000
2000
3000

4000

5000
6000

7000
8000
9000

10000
"""


def day1_1(calory_groups: List[List[int]]) -> int:
    return max(sum(group) for group in calory_groups)


assert day1_1(text_input(example_input, ints, "\n\n")) == 24000
assert day1_1(file_input(1, ints, "\n\n")) == 71780


def day1_2(calory_groups: List[List[int]]) -> int:
    top_three = sorted(calory_groups, key=sum)[-3:]
    return sum(sum(group) for group in top_three)


assert day1_2(text_input(example_input, ints, "\n\n")) == 45000
assert day1_2(file_input(1, ints, "\n\n")) == 212489
