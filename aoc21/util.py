import os.path
import re

from functools import reduce
from typing import Callable, List, Optional, Iterable, TypeVar

T = TypeVar("T")
Parser = Callable[[str], T]


def file_input(day_num: int, parser: Parser[T]) -> List[T]:
    "Read input file for day_num, split it into lines and apply parser to each line"
    filename = os.path.join("input", "input{}.txt".format(day_num))
    with open(filename) as f:
        return text_input(f.read(), parser)


def text_input(text: str, parser: Parser[T]) -> List[T]:
    "Split text into lines and apply parser to each line"
    return [parser(line) for line in text.strip().splitlines()]


def split(text: str, parser: Parser[T], sep: Optional[str] = " ") -> List[T]:
    "Split text on sep and apply parser to each part"
    return [parser(t) for t in text.split(sep)]


def ints(text: str) -> List[int]:
    "Find integers in text"
    return [int(n) for n in re.findall(r"-?[0-9]+", text)]


def digits(text: str) -> List[int]:
    "Split text into individual digits"
    return [int(c) for c in text]


def quantify(iterable: Iterable[T], pred: Callable[[T], bool]) -> int:
    "Count how many times pred is true when applied to elements in iterable"
    return sum(map(pred, iterable))


def product(iterable: Iterable[int]) -> int:
    "Product of all elements in iterable"
    return reduce(lambda acc, n: acc * n, iterable)
