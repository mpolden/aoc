"""Day 8: Treetop Tree House"""

from typing import List
from itertools import takewhile
from util import assert2, text_input, file_input, digits


example_input = """
30373
25512
65332
33549
35390
"""


def visible(row: int, col: int, trees: List[List[int]]) -> bool:
    # edges are always visible
    if row == 0 or row == len(trees) - 1:
        return True
    if col == 0 or col == len(trees[row]) - 1:
        return True
    # visible from top edge?
    if max(trees[i][col] for i in range(0, row)) < trees[row][col]:
        return True
    # visible from bottom edge?
    if max(trees[i][col] for i in range(row + 1, len(trees))) < trees[row][col]:
        return True
    # visible from left edge?
    if max(trees[row][i] for i in range(0, col)) < trees[row][col]:
        return True
    # visible from right edge?
    if max(trees[row][i] for i in range(col + 1, len(trees[row]))) < trees[row][col]:
        return True
    return False


def day8_1(trees: List[List[int]]) -> int:
    return sum(
        visible(row, col, trees)
        for row in range(len(trees))
        for col in range(len(trees[row]))
    )


assert2(21, day8_1(text_input(example_input, digits)))
assert2(1676, day8_1(file_input(8, digits)))


def scenic_score(row: int, col: int, trees: List[List[int]]) -> int:
    if row == 0 or row == len(trees) - 1:
        return 0
    if col == 0 or col == len(trees[row]) - 1:
        return 0
    top = 0
    for i in range(row - 1, -1, -1):
        top += 1
        if trees[i][col] >= trees[row][col]:
            break
    bottom = 0
    for i in range(row + 1, len(trees)):
        bottom += 1
        if trees[i][col] >= trees[row][col]:
            break
    left = 0
    for i in range(col - 1, -1, -1):
        left += 1
        if trees[row][i] >= trees[row][col]:
            break
    right = 0
    for i in range(col + 1, len(trees[row])):
        right += 1
        if trees[row][i] >= trees[row][col]:
            break
    return top * bottom * left * right


def day8_2(trees: List[List[int]]) -> int:
    return max(
        scenic_score(row, col, trees)
        for row in range(len(trees))
        for col in range(len(trees[row]))
    )


assert2(8, day8_2(text_input(example_input, digits)))
assert2(313200, day8_2(file_input(8, digits)))
