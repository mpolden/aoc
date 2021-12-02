#!/usr/bin/env python3

from util import read_input


def day2_part1():
    pair = 0
    tripple = 0
    with read_input(2) as f:
        for line in f:
            symbols = {}
            for c in line:
                symbols[c] = symbols.get(c, 0) + 1
            if 2 in symbols.values():
                pair += 1
            if 3 in symbols.values():
                tripple += 1
    return pair * tripple


assert day2_part1() == 6888


def find_id(a, b):
    unequal = 0
    equal_symbols = ""
    for c1, c2 in zip(a, b):
        if c1 == c2:
            equal_symbols += c1
        else:
            unequal += 1
        if unequal > 1:
            return None
    return equal_symbols


def day2_part2():
    lines = []
    with read_input(2) as f:
        lines = f.readlines()
    for line1 in lines:
        for line2 in lines:
            if line1 == line2:
                continue
            id = find_id(line1.strip(), line2.strip())
            if id is not None:
                return id
    return None


assert day2_part2() == "icxjvbrobtunlelzpdmfkahgs"
