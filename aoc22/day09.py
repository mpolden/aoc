"""Day 9: Rope Bridge"""

from util import assert2, text_input, file_input
from typing import List, Tuple, Set

example_input = """
R 4
U 4
L 3
D 1
R 4
D 1
L 5
R 2
"""

example_input2 = """
R 5
U 8
L 8
D 3
R 17
D 10
L 25
U 20
"""

Point = Tuple[int, int]
Move = Tuple[Point, int]


def to_vector(direction: str) -> Point:
    if direction == "U":
        return (0, 1)
    elif direction == "D":
        return (0, -1)
    elif direction == "R":
        return (1, 0)
    elif direction == "L":
        return (-1, 0)
    raise ValueError("invalid direction " + direction)


def parse_move(text: str) -> Move:
    direction, _, steps = text.partition(" ")
    return to_vector(direction), int(steps)


def tail_positions(moves: List[Move], knots: int = 2) -> int:
    rope = [(0, 0) for _ in range(knots)]
    visited: Set[Point] = set()
    visited.add(rope[-1])
    for move in moves:
        vector, steps = move
        x, y = vector
        for _ in range(steps):
            head = rope[0]
            rope[0] = (head[0] + x, head[1] + y)
            for i in range(1, len(rope)):
                x1, y1 = rope[i - 1]  # head
                x2, y2 = rope[i]  # tail
                dx, dy = x1 - x2, y1 - y2
                if dx > 1:
                    x2 += 1
                    if dy > 0:
                        y2 += 1
                    elif dy < 0:
                        y2 -= 1
                elif dx < -1:
                    x2 -= 1
                    if dy > 0:
                        y2 += 1
                    elif dy < 0:
                        y2 -= 1
                elif dy > 1:
                    y2 += 1
                    if dx > 0:
                        x2 += 1
                    elif dx < 0:
                        x2 -= 1
                elif dy < -1:
                    y2 -= 1
                    if dx > 0:
                        x2 += 1
                    elif dx < 0:
                        x2 -= 1
                rope[i] = (x2, y2)
            visited.add(rope[-1])
    return len(visited)


def day9_1(moves: List[Move]) -> int:
    return tail_positions(moves)


assert2(13, day9_1(text_input(example_input, parse_move)))
assert2(6494, day9_1(file_input(9, parse_move)))


def day9_2(moves: List[Move]) -> int:
    return tail_positions(moves, 10)


assert2(1, day9_2(text_input(example_input, parse_move)))
assert2(36, day9_2(text_input(example_input2, parse_move)))
assert2(2691, day9_2(file_input(9, parse_move)))
