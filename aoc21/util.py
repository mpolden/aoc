import os.path
import re

from typing import List, Optional


def file_input(day_num: int, parser=str) -> List:
    filename = os.path.join("input", "input{}.txt".format(day_num))
    with open(filename) as f:
        return text_input(f.read(), parser)


def text_input(text: str, parser=str) -> List:
    return [parser(line) for line in text.strip().splitlines()]


def split(text: str, parser=str, sep: Optional[str] = " ") -> List:
    return [parser(t) for t in text.split(sep)]


def ints(text: str) -> List[int]:
    return [int(n) for n in re.findall(r"-?[0-9]+", text)]
