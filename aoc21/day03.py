"""Day 3: Binary Diagnostic"""

from collections import Counter
from util import read_input, parse_input

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


def parse_num(s):
    return [int(c) for c in s]


def parse_bits(bits):
    return int("".join(str(b) for b in bits), 2)


def day3_1(report):
    width = len(report[0])
    gamma_rate = 0
    epsilon_rate = 0
    for i in range(width):
        most_common = int(Counter((n[i] for n in report)).most_common()[0][0])
        shift_count = width - i - 1
        gamma_rate += most_common << shift_count
        epsilon_rate += (most_common ^ 1) << shift_count
    return gamma_rate * epsilon_rate


assert day3_1(parse_input(example_input)) == 198
assert day3_1(read_input(3)) == 4001724


def find_rating(report, max_freq=True):
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
    return parse_bits(ratings[0])


def day3_2(report):
    return find_rating(report, max_freq=True) * find_rating(report, max_freq=False)


assert day3_2(parse_input(example_input, parser=parse_num)) == 230
assert day3_2(read_input(3, parser=parse_num)) == 587895
