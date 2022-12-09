from aocd import get_data
from aocd import submit

DAY = 8
YEAR = 2022

def part1(s):
    lines = s.splitlines()
    trees = [ [0] * len(lines[0]) for i in range(len(lines))]
    for lineIndex, line in enumerate(lines):
        for charIndex, char in enumerate(line):
            trees[lineIndex][charIndex] = int(char)

    result = 0

    for i in range(len(lines)):
        for j in range(len(lines[0])):
            if i == 0 or j == 0 or i == (len(lines) - 1) or j == (len(lines[0]) - 1):
                result += 1
            else:
                value = trees[i][j]
                visible = [True, True, True, True]
                for iUp in range(i):
                    if trees[iUp][j] >= value:
                        visible[0] = False
                        break
                for iDown in range(i + 1, len(lines)):
                    if trees[iDown][j] >= value:
                        visible[1] = False
                        break
                for jLeft in range(j):
                    if trees[i][jLeft] >= value:
                        visible[2] = False
                        break
                for jRight in range(j + 1, len(lines[0])):
                    if trees[i][jRight] >= value:
                        visible[3] = False
                        break
                if visible[0] or visible[1] or visible[2] or visible[3]:
                    result += 1

    print(result)
    submit(result, part="a", day=DAY, year=YEAR)


def part2(s):
    lines = s.splitlines()
    trees = [ [0] * len(lines[0]) for i in range(len(lines))]
    for lineIndex, line in enumerate(lines):
        for charIndex, char in enumerate(line):
            trees[lineIndex][charIndex] = int(char)

    result = 0

    for i in range(len(lines)):
        for j in range(len(lines[0])):
            value = trees[i][j]
            directions = [0] * 4
            for iUp in reversed(range(i)):
                directions[0] += 1
                if trees[iUp][j] >= value:
                    break
            for iDown in range(i + 1, len(lines)):
                directions[1] += 1
                if trees[iDown][j] >= value:
                    break
            for jLeft in reversed(range(j)):
                directions[2] += 1
                if trees[i][jLeft] >= value:
                    break
            for jRight in range(j + 1, len(lines[0])):
                directions[3] += 1
                if trees[i][jRight] >= value:
                    break
            beautyscore = directions[0] * directions[1] * directions[2] * directions[3]
            if beautyscore > result:
                result = beautyscore

    submit(result, part="b", day=DAY, year=YEAR)


DATA = get_data(day=DAY, year=YEAR)
part1(DATA)
part2(DATA)

# lines = data.splitlines()
#
# # SOLUTION
# for index, line in enumerate(lines):
#     result = index
