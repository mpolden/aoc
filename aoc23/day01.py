"""Day 1: Trebuchet?!"""

from typing import List
from util import assert2, file_input, text_input

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
    words = ("one", "two", "three", "four", "five", "six", "seven", "eight", "nine")
    ints = []
    buf = ""
    for c in text:
        if ord(c) >= 49 and ord(c) <= 57:
            ints.append(int(c))
        elif parse_words:
            buf += c
            for i, w in enumerate(words):
                if len(buf) >= len(w) and buf[len(buf) - len(w) :] == w:
                    ints.append(i + 1)
    return ints


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
assert2(55614, day1_2(file_input(1, str)))
