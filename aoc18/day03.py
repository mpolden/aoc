#!/usr/bin/env python3

import re

from util import read_input


def parse_claim(spec):
    # Example: #1 @ 146,196: 19x14
    parts = re.split(r"[#\s@,:x]", spec)
    if len(parts) != 9:
        raise ValueError("invalid spec '{}'".format(spec))
    return dict(
        id=int(parts[1]),
        x=int(parts[4]),
        y=int(parts[5]),
        x_size=int(parts[7]),
        y_size=int(parts[8]),
    )


assert parse_claim("#1 @ 146,196: 19x14") == {
    "id": 1,
    "x": 146,
    "y": 196,
    "x_size": 19,
    "y_size": 14,
}


def points_from(claim):
    points = []
    for x in range(claim["x"], claim["x"] + claim["x_size"]):
        for y in range(claim["y"], claim["y"] + claim["y_size"]):
            points.append((x, y))
    return points


assert points_from(parse_claim("#1 @ 1,3: 4x4")) == [
    (1, 3),
    (1, 4),
    (1, 5),
    (1, 6),
    (2, 3),
    (2, 4),
    (2, 5),
    (2, 6),
    (3, 3),
    (3, 4),
    (3, 5),
    (3, 6),
    (4, 3),
    (4, 4),
    (4, 5),
    (4, 6),
]


def read_claims():
    claims = []
    with read_input(3) as f:
        for line in f:
            claim = parse_claim(line.strip())
            claims.append(claim)
    return claims


def fabric_from(claims):
    fabric = {}
    for claim in claims:
        points = points_from(claim)
        for point in points:
            fabric[point] = fabric.get(point, 0) + 1
    return fabric


def day3_part1():
    fabric = fabric_from(read_claims())
    collisions = 0
    for visited in fabric.values():
        if visited > 1:
            collisions += 1
    return collisions


def day3_part2():
    claims = read_claims()
    fabric = fabric_from(claims)
    for claim in claims:
        points = points_from(claim)
        if all(fabric[point] == 1 for point in points):
            return claim["id"]
    return None


assert day3_part1() == 106501
assert day3_part2() == 632
