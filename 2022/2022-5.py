from aocd import get_data
from aocd import submit
import re

DAY = 5
YEAR = 2022

def part1(s):
    parts = s.split("\n\n")
    crane = [[] *1 for i in range(9)]

    for line in reversed(parts[0].splitlines()):
        for index, char in enumerate(line):
            if index == 1 and char >= 'A' and char <= 'Z':
                crane[0].append(char)
            elif index == 5 and char >= 'A' and char <= 'Z':
                crane[1].append(char)
            elif index == 9 and char >= 'A' and char <= 'Z':
                crane[2].append(char)
            elif index == 13 and char >= 'A' and char <= 'Z':
                crane[3].append(char)
            elif index == 17 and char >= 'A' and char <= 'Z':
                crane[4].append(char)
            elif index == 21 and char >= 'A' and char <= 'Z':
                crane[5].append(char)
            elif index == 25 and char >= 'A' and char <= 'Z':
                crane[6].append(char)
            elif index == 29 and char >= 'A' and char <= 'Z':
                crane[7].append(char)
            elif index == 33 and char >= 'A' and char <= 'Z':
                crane[8].append(char)

    for line in parts[1].splitlines():
        nums = [int(s) for s in re.findall(r'\b\d+\b', line)]
        for i in range(nums[0]):
            char = crane[nums[1] - 1].pop()
            crane[nums[2] - 1].append(char)

    result = ''
    for stack in crane:
        result += stack.pop()

    submit(result, part="a", day=DAY, year=YEAR)


def part2(s):
    parts = s.split("\n\n")
    crane = [[] *1 for i in range(9)]

    for line in reversed(parts[0].splitlines()):
        for index, char in enumerate(line):
            if index == 1 and char >= 'A' and char <= 'Z':
                crane[0].append(char)
            elif index == 5 and char >= 'A' and char <= 'Z':
                crane[1].append(char)
            elif index == 9 and char >= 'A' and char <= 'Z':
                crane[2].append(char)
            elif index == 13 and char >= 'A' and char <= 'Z':
                crane[3].append(char)
            elif index == 17 and char >= 'A' and char <= 'Z':
                crane[4].append(char)
            elif index == 21 and char >= 'A' and char <= 'Z':
                crane[5].append(char)
            elif index == 25 and char >= 'A' and char <= 'Z':
                crane[6].append(char)
            elif index == 29 and char >= 'A' and char <= 'Z':
                crane[7].append(char)
            elif index == 33 and char >= 'A' and char <= 'Z':
                crane[8].append(char)

    for line in parts[1].splitlines():
        nums = [int(s) for s in re.findall(r'\b\d+\b', line)]
        chars = []
        for i in range(nums[0]):
            chars.append(crane[nums[1] - 1].pop())
        for i in range(nums[0]):
            crane[nums[2] - 1].append(chars.pop())

    result = ''
    for stack in crane:
        result += stack.pop()

    submit(result, part="b", day=DAY, year=YEAR)


DATA = get_data(day=DAY, year=YEAR)
part1(DATA)
part2(DATA)

# lines = data.splitlines()
#
# # SOLUTION
# for index, line in enumerate(lines):
#     result = index
