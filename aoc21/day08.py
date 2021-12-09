"""Day 8: Seven Segment Search"""

from typing import Dict, List, Set, Tuple
from util import file_input, text_input


example_input = """
be cfbegad cbdgef fgaecd cgeb fdcge agebfd fecdb fabcd edb | fdgacbe cefdb cefbgd gcbe
edbfga begcd cbg gc gcadebf fbgde acbgfd abcde gfcbed gfec | fcgedb cgb dgebacf gc
fgaebd cg bdaec gdafb agbcfd gdcbef bgcad gfac gcb cdgabef | cg cg fdcagb cbg
fbegcd cbd adcefb dageb afcb bc aefdc ecdab fgdeca fcdbega | efabcd cedba gadfec cb
aecbfdg fbg gf bafeg dbefa fcge gcbea fcaegb dgceab fcbdga | gecf egdcabf bgf bfgea
fgeab ca afcebg bdacfeg cfaedg gcfdb baec bfadeg bafgc acf | gebdcfa ecba ca fadegcb
dbcfg fgd bdegcaf fgec aegbdf ecdfab fbedc dacgb gdcebf gf | cefg dcbef fcge gbcadfe
bdfegc cbegaf gecbf dfcage bdacg ed bedf ced adcbefg gebcd | ed bcgafe cdgba cbgef
egadfb cdbfeg cegd fecab cgb gbdefca cg fgcdab egfdb bfceg | gbdfcae bgc cg cgb
gcafb gcf dcaebfg ecagb gf abcdeg gaef cafbge fdbac fegbdc | fgae cfgab fg bagce
"""

Entry = Tuple[List[str], List[str]]


def parse_entry(line: str) -> Entry:
    signal_patterns, output = line.split(" | ")
    return signal_patterns.split(" "), output.split(" ")


def day8_1(entries: List[Entry]) -> int:
    unique_segments = (2, 4, 3, 7)
    count = 0
    for _, values in entries:
        for value in values:
            if len(value) in unique_segments:
                count += 1
    return count


assert day8_1(text_input(example_input, parse_entry)) == 26
assert day8_1(file_input(8, parse_entry)) == 392


def sort_segment(text: str) -> str:
    return "".join(sorted(list(text)))


def day8_2(entries: List[Entry]) -> int:
    total = 0
    for inputs, outputs in entries:
        inputs = [sort_segment(seg) for seg in inputs]
        segments: Dict[str, int] = {}
        for seg in inputs:
            width = len(seg)
            if width == 2:
                segments[seg] = 1
            elif width == 4:
                segments[seg] = 4
            elif width == 3:
                segments[seg] = 7
            elif width == 7:
                segments[seg] = 8
        # Inverted table of known segments by their value, e.g. 1 => ab
        numbers: Dict[int, Set[str]] = {v: set(k) for k, v in segments.items()}
        for seg in inputs:
            s = set(seg)
            if len(seg) == 5:  # 2, 3 and 5
                if len(s.intersection(numbers[1])) == 2:
                    segments[seg] = 3
                elif len(s.intersection(numbers[4])) == 3:
                    segments[seg] = 5
                else:
                    segments[seg] = 2
            elif len(seg) == 6:  # 0, 6, 9
                if len(s.intersection(numbers[4])) == 4:
                    segments[seg] = 9
                elif len(s.intersection(numbers[1])) == 2:
                    segments[seg] = 0
                else:
                    segments[seg] = 6
        digits = "".join(str(segments[sort_segment(output)]) for output in outputs)
        total += int(digits)
    return total


assert day8_2(text_input(example_input, parse_entry)) == 61229
assert day8_2(file_input(8, parse_entry)) == 1004688
