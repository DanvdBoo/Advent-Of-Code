from aocd import get_data
from aocd import submit
import re

DAY = 4
YEAR = 2022

def part1(s):
    result = 0
    for line in s.splitlines():
        numbers = re.split(r',|-', line)
        if int(numbers[0]) <= int(numbers[2]) and int(numbers[1]) >= int(numbers[3]):
            result += 1
        elif int(numbers[0]) >= int(numbers[2]) and int(numbers[1]) <= int(numbers[3]):
            result += 1
    submit(result, part="a", day=DAY, year=YEAR)


def part2(s):
    result = 0
    for line in s.splitlines():
        numbers = re.split(r',|-', line)
        if int(numbers[0]) <= int(numbers[3]) and int(numbers[1]) >= int(numbers[2]):
            result += 1
        elif int(numbers[0]) >= int(numbers[3]) and int(numbers[1]) <= int(numbers[2]):
            result += 1
    submit(result, part="b", day=DAY, year=YEAR)


DATA = get_data(day=DAY, year=YEAR)
part1(DATA)
part2(DATA)

# lines = data.splitlines()
#
# # SOLUTION
# for index, line in enumerate(lines):
#     result = index
