"""Day 1: Sonar Sweep"""

from util import file_input, text_input

example_input = """
199
200
208
210
200
207
240
269
260
263
"""


def day1_1(reports):
    prev = reports[0]
    inc = 0
    for report in reports[1:]:
        if report > prev:
            inc += 1
        prev = report
    return inc


assert day1_1(text_input(example_input, parser=int)) == 7
assert day1_1(file_input(1, parser=int)) == 1462


def day1_2(reports):
    window_size = 3
    prev = 0
    inc = 0
    for i in range(len(reports)):
        window = []
        for r in reports[i : i + window_size]:
            window.append(r)
        if len(window) < window_size:
            continue
        window_sum = sum(window)
        if i > 0 and window_sum > prev:
            inc += 1
        prev = window_sum
    return inc


assert day1_2(text_input(example_input, parser=int)) == 5
assert day1_2(file_input(1, parser=int)) == 1497
