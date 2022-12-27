import os.path
import re

from functools import reduce
from typing import Callable, List, Optional, Iterable, TypeVar, Any

T = TypeVar("T")
Parser = Callable[[str], T]


def assert2(want: Any, got: Any) -> None:
    """A better assert"""
    if got != want:
        raise AssertionError("got {}, want {}".format(repr(got), repr(want)))


def file_input(day: int, parser: Parser[T], sep: Optional[str] = "\n") -> List[T]:
    "Read input file for given day, split it into lines and apply parser to each line"
    filename = os.path.join("input", "input{:02d}.txt".format(day))
    with open(filename) as f:
        return text_input(f.read(), parser, sep)


def text_input(text: str, parser: Parser[T], sep: Optional[str] = "\n") -> List[T]:
    "Split text into lines and apply parser to each line"
    return [parser(line) for line in text.strip("\n").split(sep)]


def ints(text: str) -> List[int]:
    "Find integers in text"
    return [int(n) for n in re.findall(r"-?[0-9]+", text)]


def digits(text: str) -> List[int]:
    "Split text into individual digits"
    return [int(c) for c in text]


def quantify(iterable: Iterable[T], pred: Callable[[T], bool]) -> int:
    "Count how many times pred is true for items in iterable"
    return sum(1 for item in iterable if pred(item))


def product(iterable: Iterable[int]) -> int:
    "Product of all elements in iterable"
    return reduce(lambda acc, n: acc * n, iterable)


def partition(items: List[T], size: int) -> List[List[T]]:
    "Partition list into sub-lists of given size"
    return [items[i : i + size] for i in range(0, len(items), size)]
