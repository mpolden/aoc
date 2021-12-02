import os.path


def read_input(day_num, parser=str):
    filename = os.path.join("input", "input{}.txt".format(day_num))
    with open(filename) as f:
        return parse_input(f.read(), parser)


def parse_input(data, parser=str):
    return [parser(line) for line in data.strip().splitlines()]
