"""Day 2: Rock Paper Scissors"""

from typing import List, Tuple
from util import file_input, text_input

example_input = """
A Y
B X
C Z
"""

shape_scores = {
    "X": 1,
    "Y": 2,
    "Z": 3,
}

scores = {
    "A": {
        "Y": 6,
        "X": 3,
        "Z": 0,
    },
    "B": {
        "Z": 6,
        "Y": 3,
        "X": 0,
    },
    "C": {
        "X": 6,
        "Z": 3,
        "Y": 0,
    },
}


def day2_1(moves: List[List[str]]) -> int:
    return sum(shape_scores[b] + scores[a][b] for a, b in moves)


assert day2_1(text_input(example_input, str.split)) == 15
assert day2_1(file_input(2, str.split)) == 15691


def day2_2(moves: List[List[str]]) -> int:
    score_by_move = {
        "X": 0,
        "Y": 3,
        "Z": 6,
    }
    inverted_scores = {k: {v2: k2 for k2, v2 in v.items()} for k, v in scores.items()}
    score = 0
    for a, b in moves:
        wanted_score = score_by_move[b]
        b = inverted_scores[a][wanted_score]
        score += shape_scores[b] + scores[a][b]
    return score


assert day2_2(text_input(example_input, str.split)) == 12
assert day2_2(file_input(2, str.split)) == 12989
