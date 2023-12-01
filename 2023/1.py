import regex as re
from aocd import get_data
from aocd import submit

DAY = 1
YEAR = 2023

def part1(s):
    result = 0
    for index, line in enumerate(s.splitlines()):
        numbers = [int(s) for s in re.findall(r'\d', line)]
        if len(numbers) >= 1:
            result += numbers[0] * 10 + numbers[len(numbers) - 1]
    submit(result, part="a", day=DAY, year=YEAR)

def getNumber(s):
    if s == "one":
        return 1
    if s == "two":
        return 2
    if s == "three":
        return 3
    if s == "four":
        return 4
    if s == "five":
        return 5
    if s == "six":
        return 6
    if s == "seven":
        return 7
    if s == "eight":
        return 8
    if s == "nine":
        return 9
    return int(s)

def part2(s):
    result = 0
    for index, line in enumerate(s.splitlines()):
        numbers = [getNumber(s) for s in re.findall(r'\d|one|two|three|four|five|six|seven|eight|nine', line, overlapped=True)]
        if len(numbers) >= 1:
            result += numbers[0] * 10 + numbers[len(numbers) - 1]
    submit(result, part="b", day=DAY, year=YEAR)

DATA = get_data(day=DAY, year=YEAR)
TESTDATA = open("testinput.txt", "r").read()
part1(DATA)
part2(DATA)

# lines = data.splitlines()
#
# # SOLUTION
# for index, line in enumerate(lines):
#     result = index
