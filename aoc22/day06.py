"""Day 6: Tuning Trouble"""

from typing import Tuple, Dict
from util import assert2, file_input


example_inputs: Dict[str, Tuple[int, int]] = {
    "mjqjpqmgbljsphdztnvjfqwrcgsmlb": (7, 19),
    "bvwbjplbgvbhsrlpgdmjqwftvncz": (5, 23),
    "nppdvjthqldpwncqszvftbrmjlhg": (6, 23),
    "nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg": (10, 29),
    "zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw": (11, 26),
}


def find_marker(packet: str, size: int) -> int:
    read = ""
    for c in packet:
        read += c
        if len(read) < size:
            continue
        if len(set(read[-size:])) == size:
            break
    return len(read)


def day6_1(packet: str) -> int:
    return find_marker(packet, 4)


for packet, want in example_inputs.items():
    assert2(want[0], day6_1(packet))

assert2(1892, day6_1(file_input(6, str)[0]))


def day6_2(packet: str) -> int:
    return find_marker(packet, 14)


for packet, want in example_inputs.items():
    assert2(want[1], day6_2(packet))

assert2(2313, day6_2(file_input(6, str)[0]))
