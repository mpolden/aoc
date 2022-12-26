#!/usr/bin/env python3

import sys


template = """\"\"\"Day {day}: {description}\"\"\"

from typing import List
from util import text_input, file_input, assert2

example_input = \"\"\"
{example_input}
\"\"\"


def day{day}_1(lines: List[str]) -> int:
    return 0


assert2(0, day{day}_1(text_input(example_input, str)))
assert2(0, day{day}_1(file_input({day}, str)))


def day{day}_2(lines: List[str]) -> int:
    return 0


assert2(0, day{day}_2(text_input(example_input, str)))
assert2(0, day{day}_2(file_input({day}, str)))
"""


def fail(msg: str) -> None:
    print(msg, file=sys.stderr)
    sys.exit(1)


def main() -> None:
    if len(sys.argv) < 3:
        fail(sys.argv[0] + ": <day> <description>")
    day = int(sys.argv[1])
    desc = sys.argv[2]
    filepath = "day{0:02d}.py".format(day)
    example_input = sys.stdin.read().strip()
    with open(filepath, "x") as f:
        content = template.format(
            day=day, description=desc, example_input=example_input
        )
        f.write(content)
    print("wrote", filepath, file=sys.stderr)


if __name__ == "__main__":
    main()
