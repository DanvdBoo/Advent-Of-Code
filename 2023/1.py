import regex as re
from .boilerPlate2023 import puzzle

def part1(d: str):
    return sum([x[0] * 10 + x[-1] for x in [[int(n) for n in re.findall(r'\d', l)] for l in d.splitlines()]])

def part2(d: str):
    a = {'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5, 'six': 6, 'seven': 7, 'eight': 8, 'nine': 9}
    return sum([x[0] * 10 + x[-1] for x in [[a.get(n) or int(n) for n in re.findall(r'\d|one|two|three|four|five|six|seven|eight|nine', l, overlapped=True)] for l in d.splitlines()]])

puzzle(1, part1, part2, False, False).run()