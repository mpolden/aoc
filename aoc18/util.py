import os.path

def read_input(day):
    filename = os.path.join("input", "input{}.txt".format(day))
    return open(filename)
