"""Day 4: Giant Squid"""

from typing import List, Set, Tuple
from util import file_input, text_input, split

example_input = """
7,4,9,5,11,17,23,2,0,14,21,24,10,16,13,6,15,25,12,22,18,20,8,19,3,26,1

22 13 17 11  0
 8  2 23  4 24
21  9 14 16  7
 6 10  3 18  5
 1 12 20 15 19

 3 15  0  2 22
 9 18 13 17  5
19  8  7 25 23
20 11 10 24  4
14 21 16 12  6

14 21 17 24  4
10 16 15  9 19
18  8 23 26 20
22 11 13  6  5
 2  0 12  3  7
"""

Board = List[List[int]]


def parse_board(lines: List[str]) -> Board:
    return [split(line, parser=int, sep=None) for line in lines]


def parse_boards(lines: List[str], board_height: int = 5) -> List[Board]:
    return [
        parse_board(lines[i : i + board_height])
        for i in range(2, len(lines), board_height + 1)
    ]


def nums_and_boards(lines: List[str]) -> Tuple[List[int], List[Board]]:
    nums = split(lines[0], parser=int, sep=",")
    boards = parse_boards(lines)
    return nums, boards


def is_winner(board: Board, drawn: Set[int]) -> bool:
    for i, row in enumerate(board):
        if set(row) <= drawn:
            return True
        col = (row[i] for row in board)
        if set(col) <= drawn:
            return True
    return False


def score(board: Board, drawn: List[int]) -> int:
    last_drawn = drawn[-1]
    return sum((n for row in board for n in row if n not in drawn)) * last_drawn


def winning_score(boards: List[Board], nums: List[int], last: bool = False) -> int:
    drawn = []
    winners = []
    for n in nums:
        drawn.append(n)
        for i, board in enumerate(boards):
            if not is_winner(board, set(drawn)):
                continue
            if i in winners:
                continue
            winners.append(i)
            if not last or len(winners) == len(boards):
                return score(board, drawn)
    raise ValueError("no winner found")


def day4_1(lines: List[str]) -> int:
    nums, boards = nums_and_boards(lines)
    return winning_score(boards, nums)


assert day4_1(text_input(example_input)) == 4512
assert day4_1(file_input(4)) == 33348


def day4_2(lines: List[str]) -> int:
    nums, boards = nums_and_boards(lines)
    return winning_score(boards, nums, last=True)


assert day4_2(text_input(example_input)) == 1924
assert day4_2(file_input(4)) == 8112
