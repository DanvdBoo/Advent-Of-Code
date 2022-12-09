from aocd import get_data
from aocd import submit
import copy

DAY = 9
YEAR = 2022

def part1(s):
    tail = [0, 0]
    head = [0, 0]
    visited = [[0, 0]]

    for line in s.splitlines():
        direction = (0, 0)
        if line[0] == 'D':
            direction = (0, -1)
        elif line[0] == 'U':
            direction = (0, 1)
        elif line[0] == 'R':
            direction = (1, 0)
        elif line[0] == 'L':
            direction = (-1, 0)
        for i in range(int(line.split(' ')[1])):
            oldHead = copy.deepcopy(head)
            head[0] += direction[0]
            head[1] += direction[1]
            if abs(head[0] - tail[0]) >= 2 or abs(head[1] - tail[1]) >= 2:
                tail = copy.deepcopy(oldHead)
                if tail not in visited:
                    visited.append(tail)
    
    result = len(visited)
    submit(result, part="a", day=DAY, year=YEAR)


def part2(s):
    rope = [[0, 0] for y in range(10)]
    visited = [[0, 0]]

    for line in s.splitlines():
        direction = (0, 0)
        if line[0] == 'D':
            direction = (0, -1)
        elif line[0] == 'U':
            direction = (0, 1)
        elif line[0] == 'R':
            direction = (1, 0)
        elif line[0] == 'L':
            direction = (-1, 0)
        for i in range(int(line.split(' ')[1])):
            prevLocation = copy.deepcopy(rope[0])
            rope[0][0] += direction[0]
            rope[0][1] += direction[1]
            for i in range(9):
                if abs(rope[i][0] - rope[i + 1][0]) == 2 and rope[i][1] == rope[i + 1][1]:
                    rope[i + 1][0] += int((rope[i][0] - rope[i + 1][0])/2)
                elif abs(rope[i][1] - rope[i + 1][1]) == 2 and rope[i][0] == rope[i + 1][0]:
                    rope[i + 1][1] += int((rope[i][1] - rope[i + 1][1])/2)
                elif abs(rope[i][0] - rope[i + 1][0]) == 2 and abs(rope[i][1] - rope[i + 1][1]) == 1:
                    rope[i + 1][0] += int((rope[i][0] - rope[i + 1][0])/2)
                    rope[i + 1][1] += rope[i][1] - rope[i + 1][1]
                elif abs(rope[i][1] - rope[i + 1][1]) == 2 and abs(rope[i][0] - rope[i + 1][0]) == 1:
                    rope[i + 1][1] += int((rope[i][1] - rope[i + 1][1])/2)
                    rope[i + 1][0] += rope[i][0] - rope[i + 1][0]
                elif abs(rope[i][0] - rope[i + 1][0]) == 2 and abs(rope[i][1] - rope[i + 1][1]) == 2:
                    rope[i + 1][0] += int((rope[i][0] - rope[i + 1][0])/2)
                    rope[i + 1][1] += int((rope[i][1] - rope[i + 1][1])/2)
            if rope[9] not in visited:
                visited.append(copy.deepcopy(rope[9]))
    
    result = len(visited)
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
