from util import read_input, parse_input


example_input = parse_input(
    """199
200
208
210
200
207
240
269
260
263""",
    parser=int,
)


def day1_1(reports):
    prev = 0
    inc = 0
    for i, report in enumerate(reports):
        if i > 0 and report > prev:
            inc += 1
        prev = report
    return inc


assert day1_1(example_input) == 7
assert day1_1(read_input(1, parser=int)) == 1462


def day1_2(reports):
    windows = []
    window_size = 3
    for i in range(len(reports)):
        window = []
        for r in reports[i : i + window_size]:
            window.append(r)
        if len(window) == window_size:
            windows.append(window)
    prev = 0
    inc = 0
    for i, window in enumerate(windows):
        window_sum = sum(window)
        if i > 0 and window_sum > prev:
            inc += 1
        prev = window_sum
    return inc


assert day1_2(example_input) == 5
assert day1_2(read_input(1, parser=int)) == 1497
