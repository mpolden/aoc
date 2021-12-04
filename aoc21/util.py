import os.path


def file_input(day_num, parser=str):
    filename = os.path.join("input", "input{}.txt".format(day_num))
    with open(filename) as f:
        return text_input(f.read(), parser)


def text_input(text, parser=str):
    return [parser(line) for line in text.strip().splitlines()]


def split(text, parser=str, sep=" "):
    return [parser(t) for t in text.split(sep)]
