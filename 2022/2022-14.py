from aocd import get_data
from aocd import submit
from matplotlib import pyplot

DAY = 14
YEAR = 2022

def part1(s):
    cave = [[0] * 520 for x in range(165)]
    for line in s.splitlines():
        coords = [list(map(int, i)) for i in [x.split(',') for x in line.split(' -> ')]]
        while len(coords) >= 2:
            if coords[0][0] == coords[1][0]:
                small, big = coords[0][1] if coords[0][1] < coords[1][1] else coords[1][1], coords[1][1] if coords[0][1] < coords[1][1] else coords[0][1]
                for i in range(small, big + 1):
                    cave[i][coords[0][0]] = 1
            elif coords[0][1] == coords[1][1]:
                small, big = coords[0][0] if coords[0][0] < coords[1][0] else coords[1][0], coords[1][0] if coords[0][0] < coords[1][0] else coords[0][0]
                for i in range(small, big + 1):
                    cave[coords[0][1]][i] = 1
            coords.pop(0)
    noLeak = True
    result = 0
    while noLeak:
        currentPos = [0, 500]
        moving = True
        while moving:
            if currentPos[0] > 161:
                noLeak = False
                moving = False
            elif cave[currentPos[0] + 1][currentPos[1]] == 0:
                currentPos[0] += 1
            elif cave[currentPos[0] + 1][currentPos[1] - 1] == 0:
                currentPos[1] -= 1
                currentPos[0] += 1
            elif cave[currentPos[0] + 1][currentPos[1] + 1] == 0:
                currentPos[1] += 1
                currentPos[0] += 1
            else:
                cave[currentPos[0]][currentPos[1]] = 2
                moving = False
        result += noLeak

    submit(result, part="a", day=DAY, year=YEAR)


def part2(s):
    cave = [[0] * 800 for x in range(165)]
    for line in s.splitlines():
        coords = [list(map(int, i)) for i in [x.split(',') for x in line.split(' -> ')]]
        while len(coords) >= 2:
            if coords[0][0] == coords[1][0]:
                small, big = coords[0][1] if coords[0][1] < coords[1][1] else coords[1][1], coords[1][1] if coords[0][1] < coords[1][1] else coords[0][1]
                for i in range(small, big + 1):
                    cave[i][coords[0][0]] = 1
            elif coords[0][1] == coords[1][1]:
                small, big = coords[0][0] if coords[0][0] < coords[1][0] else coords[1][0], coords[1][0] if coords[0][0] < coords[1][0] else coords[0][0]
                for i in range(small, big + 1):
                    cave[coords[0][1]][i] = 1
            coords.pop(0)
    for i in range(800):
        cave[163][i] = 1
    notFilled = True
    result = 0
    while notFilled:
        currentPos = [0, 500]
        moving = True
        while moving:
            if cave[currentPos[0] + 1][currentPos[1]] == 0:
                currentPos[0] += 1
            elif cave[currentPos[0] + 1][currentPos[1] - 1] == 0:
                currentPos[1] -= 1
                currentPos[0] += 1
            elif cave[currentPos[0] + 1][currentPos[1] + 1] == 0:
                currentPos[1] += 1
                currentPos[0] += 1
            else:
                cave[currentPos[0]][currentPos[1]] = 2
                moving = False
        if currentPos == [0, 500]:
            notFilled = False
        result += 1

    pyplotCave = [row[337:663] for row in cave]
    pyplot.imshow(pyplotCave)
    pyplot.show()
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
