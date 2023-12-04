"""Day 2: Cube Conundrum"""

from typing import List, Dict, Tuple, NamedTuple
from util import text_input, file_input, assert2, product

example_input = """
Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue
Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red
Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red
Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green
"""

CubeSet = Dict[str, int]
Rgb = Tuple[int, int, int]


class Game(NamedTuple):
    id: int
    cubes: List[CubeSet]


def parse_game(line: str) -> Game:
    parts = line.split(": ")
    game_id = int(parts[0][5:])
    cubes = []
    for p in parts[1].split("; "):
        c: CubeSet = {}
        for p in p.split(", "):
            parts = p.split(" ")
            count = int(parts[0])
            color = parts[1]
            c[color] = count
        cubes.append(c)
    return Game(id=game_id, cubes=cubes)


def valid_game(game: Game, rgb: Rgb) -> bool:
    r, g, b = rgb
    return all(
        c.get("red", 0) <= r and c.get("green", 0) <= g and c.get("blue", 0) <= b
        for c in game.cubes
    )


def min_cubes(game: Game) -> Rgb:
    r, g, b = 0, 0, 0
    for c in game.cubes:
        r = max(r, c.get("red", 0))
        g = max(g, c.get("green", 0))
        b = max(b, c.get("blue", 0))
    return (r, g, b)


def day2_1(games: List[Game]) -> int:
    return sum(g.id for g in games if valid_game(g, (12, 13, 14)))


assert2(8, day2_1(text_input(example_input, parse_game)))
assert2(3035, day2_1(file_input(2, parse_game)))


def day2_2(games: List[Game]) -> int:
    return sum(product(min_cubes(g)) for g in games)


assert2(2286, day2_2(text_input(example_input, parse_game)))
assert2(66027, day2_2(file_input(2, parse_game)))
