"""Day 1: Trebuchet?!"""

import regex as re
from typing import List
from util import assert2, file_input, text_input, ints

example_input = """
1abc2
pqr3stu8vwx
a1b2c3d4e5f
treb7uchet
"""

example_input2 = """
two1nine
eightwothree
abcone2threexyz
xtwone3four
4nineeightseven2
zoneight234
7pqrstsixteen
"""


def find_digits(text: str, parse_words: bool = False) -> List[int]:
    "Find numerical or english digits in text"
    word_to_int = {str(i): i for i in range(1, 10)}
    expr = "[0-9]"
    if parse_words:
        words = [
            "one",
            "two",
            "three",
            "four",
            "five",
            "six",
            "seven",
            "eight",
            "nine",
        ]
        for i, w in enumerate(words):
            word_to_int[w] = i + 1
            expr += "|" + w
    return [word_to_int[n] for n in re.findall(expr, text, overlapped=True)]


def sum_calibration_values(values: List[str], parse_words: bool = False) -> int:
    s = 0
    for n in values:
        ints = find_digits(n, parse_words)
        s += (ints[0] * 10) + ints[-1]
    return s


def day1_1(values: List[str]) -> int:
    return sum_calibration_values(values)


assert2(142, day1_1(text_input(example_input, str)))
assert2(55488, day1_1(file_input(1, str)))


def day1_2(values: List[str]) -> int:
    return sum_calibration_values(values, parse_words=True)


assert2(281, day1_2(text_input(example_input2, str)))
assert2(0, day1_2(file_input(1, str)))
