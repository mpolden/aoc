import os.path


def read_input(day_num):
    filename = os.path.join("input", "input{}.txt".format(day_num))
    with open(filename) as f:
        return parse_input(f.read())


def parse_input(data):
    return data.strip().splitlines()
