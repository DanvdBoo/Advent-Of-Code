from aocd import get_data
from aocd import submit

DAY = 3
YEAR = 2023

options = [[-1, -1], [-1, 0], [-1, 1], [0, -1], [0, 1], [1, -1], [1, 0], [1, 1]]

def part1(s: str):
    result = 0
    lines = s.splitlines()
    grid = [ [0] * len(lines[0]) for i in range(len(lines))]
    for lineIndex, line in enumerate(lines):
        for charIndex, char in enumerate(line):
            grid[lineIndex][charIndex] = char
    for iX, x in enumerate(grid):
        currNumber = []
        included = False
        for iY, y in enumerate(x):
            if y >= '0' and y <= '9':
                currNumber.append(int(y))
                if not included:
                    for option in options:
                        if iX + option[0] < 0 or iY + option[1] < 0 or iX + option[0] >= len(grid) or iY + option[1] >= len(x):
                            continue
                        if (grid[iX + option[0]][iY + option[1]] < '0' or grid[iX + option[0]][iY + option[1]] > '9') and grid[iX + option[0]][iY + option[1]] != '.':
                            included = True
            if y < '0' or y > '9' or iY == len(x) - 1:
                if included:
                    tempNumber, dec = 0, 1
                    while currNumber:
                        tempNumber += currNumber.pop() * dec
                        dec *= 10
                    result += tempNumber
                included = False
                currNumber = []
    submit(result, part="a", day=DAY, year=YEAR)


def part2(s: str):
    result = 0
    lines = s.splitlines()
    grid = [ [0] * len(lines[0]) for i in range(len(lines))]
    for lineIndex, line in enumerate(lines):
        for charIndex, char in enumerate(line):
            grid[lineIndex][charIndex] = char
    stars = {}
    for iX, x in enumerate(grid):
        currNumber = []
        currentStar = []
        for iY, y in enumerate(x):
            if y >= '0' and y <= '9':
                currNumber.append(int(y))
                for option in options:
                    if iX + option[0] < 0 or iY + option[1] < 0 or iX + option[0] >= len(grid) or iY + option[1] >= len(x):
                        continue
                    if grid[iX + option[0]][iY + option[1]] == '*':
                        currentStar.append((iX + option[0], iY + option[1]))
            if y < '0' or y > '9' or iY == len(x) - 1:
                for star in currentStar:
                    tempNumber, dec = 0, 1
                    while currNumber:
                        tempNumber += currNumber.pop() * dec
                        dec *= 10
                    if tempNumber == 0:
                        continue
                    try:
                        stars[star].append(tempNumber)
                    except:
                        stars.update({star: [tempNumber]})
                currNumber = []
                currentStar = []
    for star in stars:
        starValue = stars[star]
        if len(starValue) == 2:
            result += starValue[0] * starValue[1]
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
