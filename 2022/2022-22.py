import copy
import re
from aocd import get_data
from aocd import submit

DAY = 22
YEAR = 2022
DIRECTIONS = [(0, 1), (1, 0), (0, -1), (-1, 0)]

def convert(value):
    try:
        return int(value)
    except:
        return value

def part1(s):
    parse = s.split('\n\n')
    unparsedBoard = parse[0].splitlines()
    board = [[-1] * len(unparsedBoard[0]) for x in range(len(unparsedBoard))]
    for i, line in enumerate(unparsedBoard):
        for j, char in enumerate(line):
            if char == '.':
                board[i][j] = 0
            elif char == '#':
                board[i][j] = 1
    parsedPath = [convert(x) for x in filter(None, re.split(r'(\d+)', parse[1].rstrip()))]
    d = 0
    for i, v in enumerate(board[0]):
        if v == 0:
            current = [0, i]
            break
    while parsedPath:
        instruction = parsedPath.pop(0)
        if type(instruction) == int:
            for i in range(instruction):
                nextLocation = copy.deepcopy(current)
                nextValue = -1
                while nextValue == -1:
                    nextLocation[0] += DIRECTIONS[d][0]
                    nextLocation[1] += DIRECTIONS[d][1]
                    try:
                        assert(nextLocation[0] >= 0 and nextLocation[1] >= 0)
                        nextValue = board[nextLocation[0]][nextLocation[1]]
                    except:
                        if nextLocation[0] < 0:
                            nextLocation[0] = len(board) - 1
                        elif nextLocation[0] >= len(board):
                            nextLocation[0] = 0
                        elif nextLocation[1] < 0:
                            nextLocation[1] = len(board[0]) - 1
                        elif nextLocation[1] >= len(board[0]):
                            nextLocation[1] = 0
                        nextValue = board[nextLocation[0]][nextLocation[1]]
                if nextValue == 1:
                    break
                current = copy.deepcopy(nextLocation)
        else:
            if instruction == 'R':
                d = d + 1 if d < 3 else 0
            else:
                d = d - 1 if d > 0 else 3
    result = 1000 * (current[0]+1) + 4 * (current[1]+1) + d
    print(current, d, result)
    submit(result, part="a", day=DAY, year=YEAR)


def part2(s):
    parse = s.split('\n\n')
    unparsedBoard = parse[0].splitlines()
    board = [[-1] * len(unparsedBoard[0]) for x in range(len(unparsedBoard))]
    for i, line in enumerate(unparsedBoard):
        for j, char in enumerate(line):
            if char == '.':
                board[i][j] = 0
            elif char == '#':
                board[i][j] = 1
    parsedPath = [convert(x) for x in filter(None, re.split(r'(\d+)', parse[1].rstrip()))]
    d = 0
    for i, v in enumerate(board[0]):
        if v == 0:
            current = [0, i]
            break
    while parsedPath:
        instruction = parsedPath.pop(0)
        if type(instruction) == int:
            for i in range(instruction):
                nextLocation = copy.deepcopy(current)
                nextLocation[0] += DIRECTIONS[d][0]
                nextLocation[1] += DIRECTIONS[d][1]
                try:
                    assert(nextLocation[0] >= 0 and nextLocation[1] >= 0)
                    nextValue = board[nextLocation[0]][nextLocation[1]]
                except:
                    if nextLocation[0] < 0:
                        nextLocation[0] = len(board) - 1
                    elif nextLocation[0] >= len(board):
                        nextLocation[0] = 0
                    elif nextLocation[1] < 0:
                        nextLocation[1] = len(board[0]) - 1
                    elif nextLocation[1] >= len(board[0]):
                        nextLocation[1] = 0
                    nextValue = board[nextLocation[0]][nextLocation[1]]
                if nextValue == 1:
                    break
                current = copy.deepcopy(nextLocation)
        else:
            if instruction == 'R':
                d = d + 1 if d < 3 else 0
            else:
                d = d - 1 if d > 0 else 3
    result = 1000 * (current[0]+1) + 4 * (current[1]+1) + d
    print(current, d, result)

    return
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
