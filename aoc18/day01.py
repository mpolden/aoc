#!/usr/bin/env python3

from util import read_input


def day1_part1():
    sum = 0
    with read_input(1) as f:
        for line in f:
            sum += int(line)
    return sum


assert day1_part1() == 420


def day1_part2(sum=0, seen=None):
    if seen is None:
        seen = {}
    with read_input(1) as f:
        for line in f:
            sum += int(line)
            if seen.get(sum):
                return sum
            seen[sum] = True
    return day1_part2(sum, seen)


assert day1_part2() == 227
