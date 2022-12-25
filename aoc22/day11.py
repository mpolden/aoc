"""Day 11: Monkey in the Middle"""

from operator import add, mul
from typing import List, NamedTuple, Callable, Tuple, Optional, Counter
from util import text_input, file_input, assert2, product


example_input = """Monkey 0:
  Starting items: 79, 98
  Operation: new = old * 19
  Test: divisible by 23
    If true: throw to monkey 2
    If false: throw to monkey 3

Monkey 1:
  Starting items: 54, 65, 75, 74
  Operation: new = old + 6
  Test: divisible by 19
    If true: throw to monkey 2
    If false: throw to monkey 0

Monkey 2:
  Starting items: 79, 60, 97
  Operation: new = old * old
  Test: divisible by 13
    If true: throw to monkey 1
    If false: throw to monkey 3

Monkey 3:
  Starting items: 74
  Operation: new = old + 3
  Test: divisible by 17
    If true: throw to monkey 0
    If false: throw to monkey 1
"""


class Monkey(NamedTuple):
    levels: List[int]
    operator: Callable[[int, int], int]
    operand: Optional[int]
    divisor: int
    targets: Tuple[int, int]


def parse_monkeys(lines: List[str]) -> List[Monkey]:
    monkeys: List[Monkey] = []
    levels: List[int]
    operator: Callable[[int, int], int]
    operand: Optional[int]
    divisor: int
    targets = (-1, -1)
    for line in lines:
        line = line.strip()
        if line.startswith("Starting items:"):
            levels = [int(n) for n in line.split(": ")[1].split(", ")]
        elif line.startswith("Operation:"):
            symbol, n = line.split(" ")[-2:]
            operand = None if n == "old" else int(n)
            operator = mul if symbol == "*" else add
        elif line.startswith("Test:"):
            divisor = int(line.split(" ")[3])
        elif line.startswith("If "):
            parts = line.split(" ")
            t = int(parts[5])
            if parts[1] == "true:":
                targets = (t, targets[1])
            else:
                targets = (targets[0], t)
                monkeys.append(Monkey(levels, operator, operand, divisor, targets))
    return monkeys


def monkey_business(lines: List[str], rounds: int) -> int:
    monkeys = parse_monkeys(lines)
    inspections = [0] * len(monkeys)
    div_sum = product((m.divisor for m in monkeys))
    for _ in range(rounds):
        for i, m in enumerate(monkeys):
            while len(m.levels) > 0:
                a = m.levels.pop(0)
                b = a if m.operand is None else m.operand
                if rounds <= 20:
                    level = int(m.operator(a, b) / 3)
                else:
                    level = m.operator(a, b) % div_sum
                j = m.targets[0] if level % m.divisor == 0 else m.targets[1]
                monkeys[j].levels.append(level)
                inspections[i] += 1
    inspections.sort()
    return product(inspections[-2:])


def day11_1(lines: List[str]) -> int:
    return monkey_business(lines, 20)


assert2(10605, day11_1(text_input(example_input, str)))
assert2(90294, day11_1(file_input(11, str)))


def day11_2(lines: List[str]) -> int:
    return monkey_business(lines, 10_000)


assert2(2713310158, day11_2(text_input(example_input, str)))
assert2(18170818354, day11_2(file_input(11, str)))
