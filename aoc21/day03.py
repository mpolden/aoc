"""Day 3: Binary Diagnostic"""

from collections import Counter
from typing import List
from util import file_input, text_input

example_input = """
00100
11110
10110
10111
10101
01111
00111
11100
10000
11001
00010
01010
"""

Binary = List[int]
Report = List[Binary]


def parse_bin(text: str) -> Binary:
    return [int(c) for c in text]


def parse_int(num: Binary) -> int:
    return int("".join(str(bit) for bit in num), 2)


def day3_1(report: Report) -> int:
    width = len(report[0])
    gamma_rate = 0
    epsilon_rate = 0
    for i in range(width):
        most_common = int(Counter((n[i] for n in report)).most_common()[0][0])
        shift_count = width - i - 1
        gamma_rate += most_common << shift_count
        epsilon_rate += (most_common ^ 1) << shift_count
    return gamma_rate * epsilon_rate


assert day3_1(text_input(example_input)) == 198
assert day3_1(file_input(3)) == 4001724


def find_rating(report: Report, max_freq: bool = True) -> int:
    width = len(report[0])
    f = max if max_freq else min
    ratings = report
    for i in range(width):
        if len(ratings) == 1:
            break
        most_common = Counter((n[i] for n in ratings)).most_common()
        target_freq = most_common[0][1] if max_freq else most_common[-1][1]
        wanted_bit = f((bit for bit, freq in most_common if freq == target_freq))
        ratings = [n for n in ratings if n[i] == wanted_bit]
    return parse_int(ratings[0])


def day3_2(report: Report) -> int:
    return find_rating(report, max_freq=True) * find_rating(report, max_freq=False)


assert day3_2(text_input(example_input, parser=parse_bin)) == 230
assert day3_2(file_input(3, parser=parse_bin)) == 587895
