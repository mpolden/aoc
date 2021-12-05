import os.path
import re

from typing import Callable, List, Optional, Iterable, TypeVar

T = TypeVar("T")


def file_input(day_num: int, parser=str) -> List:
    "Read input file for day_num, split it into lines and apply parser to each line"
    filename = os.path.join("input", "input{}.txt".format(day_num))
    with open(filename) as f:
        return text_input(f.read(), parser)


def text_input(text: str, parser=str) -> List:
    "Split text into lines and apply parser to each line"
    return [parser(line) for line in text.strip().splitlines()]


def split(text: str, parser=str, sep: Optional[str] = " ") -> List:
    "Split text on sep and apply parser to each part"
    return [parser(t) for t in text.split(sep)]


def ints(text: str) -> List[int]:
    "Find integers in text"
    return [int(n) for n in re.findall(r"-?[0-9]+", text)]


def quantify(iterable: Iterable[T], pred: Callable[[T], bool]) -> int:
    "Count how many times pred is true when applied to elements in iterable"
    return sum(map(pred, iterable))
