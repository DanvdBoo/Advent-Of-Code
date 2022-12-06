from aocd import get_data
from aocd import submit
import re

DAY = 6
YEAR = 2022

def part1(s):
    string = ''
    result = 0
    for char in s:
        result += 1
        string = string[-3:] + char
        unique = True
        for c in string:
            if len(re.findall(c, string)) >= 2:
                unique = False
        if unique and result > 3:
            break

    submit(result, part="a", day=DAY, year=YEAR)


def part2(s):
    string = ''
    result = 0
    for char in s:
        result += 1
        string = string[-13:] + char
        unique = True
        for c in string:
            if len(re.findall(c, string)) >= 2:
                unique = False
        if unique and result > 13:
            break
    submit(result, part="b", day=DAY, year=YEAR)


DATA = get_data(day=DAY, year=YEAR)
part1(DATA)
part2(DATA)

# lines = data.splitlines()
#
# # SOLUTION
# for index, line in enumerate(lines):
#     result = index
