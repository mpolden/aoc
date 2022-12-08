"""Day 8: Treetop Tree House"""

from typing import List, Tuple, Iterable
from util import assert2, text_input, file_input, digits


example_input = """
30373
25512
65332
33549
35390
"""


Grid = List[List[int]]
Point = Tuple[int, int]


def is_edge(tree: Point, trees: Grid) -> bool:
    x, y = tree
    return x == 0 or x == len(trees) - 1 or y == 0 or y == len(trees[x]) - 1


def neighbours(tree: Point, trees: Grid) -> List[Iterable[Point]]:
    x, y = tree
    return [
        ((i, y) for i in range(x - 1, -1, -1)),  # top
        ((i, y) for i in range(x + 1, len(trees))),  # bottom
        ((x, i) for i in range(y - 1, -1, -1)),  # left
        ((x, i) for i in range(y + 1, len(trees[x]))),  # right
    ]


def is_visible(tree: Point, trees: Grid) -> bool:
    if is_edge(tree, trees):
        return True
    for ns in neighbours(tree, trees):
        if max(trees[x][y] for x, y in ns) < trees[tree[0]][tree[1]]:
            return True
    return False


def day8_1(trees: Grid) -> int:
    return sum(
        is_visible((x, y), trees)
        for x in range(len(trees))
        for y in range(len(trees[x]))
    )


assert2(21, day8_1(text_input(example_input, digits)))
assert2(1676, day8_1(file_input(8, digits)))


def scenic_score(tree: Point, trees: Grid) -> int:
    if is_edge(tree, trees):
        return 0
    score = 1
    for ns in neighbours(tree, trees):
        n = 0
        for x, y in ns:
            n += 1
            if trees[x][y] >= trees[tree[0]][tree[1]]:
                break
        score *= n
    return score


def day8_2(trees: Grid) -> int:
    return max(
        scenic_score((x, y), trees)
        for x in range(len(trees))
        for y in range(len(trees[x]))
    )


assert2(8, day8_2(text_input(example_input, digits)))
assert2(313200, day8_2(file_input(8, digits)))
