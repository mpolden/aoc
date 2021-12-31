"""Day 10: Syntax Scoring"""

from typing import Dict, List, Optional, Tuple
from util import file_input, text_input

example_input = """
[({(<(())[]>[[{[]{<()<>>
[(()[<>])]({[<{<<[]>>(
{([(<{}[<>[]}>{[]{[(<()>
(((({<>}<{<{<>}{[]{[]{}
[[<[([]))<([[{}[[()]]]
[{[{({}]{}}([{[{{{}}([]
{<[[]]>}<{[{[{[]{()[[[]
[<(<(<(<{}))><([]([]()
<{([([[(<>()){}]>(<<{{
<{([{{}}[<[[[<>{}]]]>[]]
"""

Stack = List[str]
IllegalToken = Optional[str]

TOKENS_OPEN = {
    "(": ")",
    "[": "]",
    "{": "}",
    "<": ">",
}


def parse(line: str) -> Tuple[Stack, IllegalToken]:
    stack = []
    for token in line:
        if token in TOKENS_OPEN:
            stack.append(token)
        elif len(stack) > 0:
            last_opened = stack.pop()
            expected_close = TOKENS_OPEN[last_opened]
            if token != expected_close:
                return stack, token
    return stack, None


def day10_1(lines: List[str]) -> int:
    token_score = {
        ")": 3,
        "]": 57,
        "}": 1197,
        ">": 25137,
    }
    score = 0
    for line in lines:
        _, illegal_token = parse(line)
        if illegal_token is not None:
            score += token_score[illegal_token]
    return score


assert day10_1(text_input(example_input, str)) == 26397
assert day10_1(file_input(10, str)) == 367227


def day10_2(lines: List[str]) -> int:
    token_score = {
        ")": 1,
        "]": 2,
        "}": 3,
        ">": 4,
    }
    scores = []
    for line in lines:
        stack, illegal_token = parse(line)
        if illegal_token is not None:
            continue
        score = 0
        while len(stack) > 0:
            last_opened = stack.pop()
            close_token = TOKENS_OPEN[last_opened]
            score = (5 * score) + token_score[close_token]
        scores.append(score)
    scores.sort()
    return scores[int(len(scores) / 2)]


assert day10_2(text_input(example_input, str)) == 288957
assert day10_2(file_input(10, str)) == 3583341858
