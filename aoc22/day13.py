"""Day 13: Distress Signal"""

from typing import List, Any, Tuple, Optional
from util import text_input, file_input, assert2, partition, product
from itertools import zip_longest
from functools import cmp_to_key

example_input = """
[1,1,3,1,1]
[1,1,5,1,1]

[[1],[2,3,4]]
[[1],4]

[9]
[[8,7,6]]

[[4,4],4,4]
[[4,4],4,4,4]

[7,7,7,7]
[7,7,7]

[]
[3]

[[[]]]
[[]]

[1,[2,[3,[4,[5,6,7]]]],8,9]
[1,[2,[3,[4,[5,6,0]]]],8,9]
"""

# this should ideally be List[Union[int, List[Packet]]], but recursive types do not seem
# to be supported yet
Packet = List[Any]


def parse_packet(text: str) -> Packet:
    packet: Packet = []
    current = packet
    stack = [current]
    n = ""
    for i, token in enumerate(text):
        if token.isdigit():
            n += token
            if i < len(text) - 1:
                continue
        if n != "":
            current.append(int(n))
            n = ""
        if token == "[":
            stack.append([])
            current.append(stack[-1])
            current = stack[-1]
        elif token == "]":
            stack.pop()
            current = stack[-1]
    return packet


def parse_packets(lines: List[str]) -> List[Packet]:
    return [parse_packet(line) for line in lines if line != ""]


def cmp(a: Optional[Packet], b: Optional[Packet]) -> int:
    if a is None:
        return -1
    elif b is None:
        return 1
    elif isinstance(a, int) and isinstance(b, int):
        if a < b:
            return -1
        elif a > b:
            return 1
        return 0
    elif isinstance(a, list) and isinstance(b, list):
        for a2, b2 in zip_longest(a, b):
            result = cmp(a2, b2)
            if result != 0:
                return result
    else:
        a2 = [a] if isinstance(a, int) else a
        b2 = [b] if isinstance(b, int) else b
        return cmp(a2, b2)
    return 0


def day13_1(lines: List[str]) -> int:
    packets = partition(parse_packets(lines), 2)
    return sum(i + 1 for i, pair in enumerate(packets) if cmp(pair[0], pair[1]) == -1)


assert2(13, day13_1(text_input(example_input, str)))
assert2(5659, day13_1(file_input(13, str)))


def day13_2(lines: List[str]) -> int:
    dividers = [[2], [6]]
    packets = parse_packets(lines) + dividers
    packets.sort(key=cmp_to_key(cmp))
    return product((packets.index(d) + 1 for d in dividers))


assert2(140, day13_2(text_input(example_input, str)))
assert2(22110, day13_2(file_input(13, str)))
