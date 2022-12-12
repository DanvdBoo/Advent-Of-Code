import collections
import copy
from aocd import get_data
from aocd import submit

DAY = 12
YEAR = 2022

def part1(s):
    lines = s.splitlines()
    width, height = len(lines), len(lines[0])
    heightGrid = [[0] * height for i in range(width)]
    startingLocation, targetLocation = (0, 0), (0, 0)
    for lineIndex, line in enumerate(lines):
        for charIndex, char in enumerate(line):
            heightGrid[lineIndex][charIndex] = ord(char) - 96
            if char == 'S':
                startingLocation = (lineIndex, charIndex)
                heightGrid[lineIndex][charIndex] = 1
            elif char == 'E':
                targetLocation = (lineIndex, charIndex)
                heightGrid[lineIndex][charIndex] = 26
    
    queue = collections.deque([[startingLocation]])
    seen = set([startingLocation])
    while queue:
        path = queue.popleft()
        x, y = path[-1]
        if (x, y) == targetLocation:
            queue = []
            result = len(path) - 1
            continue
        for x2, y2 in ((x+1,y), (x-1,y), (x,y+1), (x,y-1)):
            if 0 <= x2 < width and 0 <= y2 < height and heightGrid[x2][y2] - heightGrid[x][y] <= 1 and (x2, y2) not in seen:
                queue.append(path + [(x2, y2)])
                seen.add((x2, y2))
    submit(result, part="a", day=DAY, year=YEAR)


def part2(s):
    lines = s.splitlines()
    width, height = len(lines), len(lines[0])
    heightGrid = [[0] * height for i in range(width)]
    startingLocation, targetLocation = (0, 0), (0, 0)
    for lineIndex, line in enumerate(lines):
        for charIndex, char in enumerate(line):
            heightGrid[lineIndex][charIndex] = ord(char) - 96
            if char == 'S':
                startingLocation = (lineIndex, charIndex)
                heightGrid[lineIndex][charIndex] = 1
            elif char == 'E':
                targetLocation = (lineIndex, charIndex)
                heightGrid[lineIndex][charIndex] = 26
    
    result = width * height
    for startingLocation in ((x, 0) for x in range(width)):
        queue = collections.deque([[startingLocation]])
        seen = set([startingLocation])
        while queue:
            path = queue.popleft()
            x, y = path[-1]
            if (x, y) == targetLocation:
                queue = []
                tempResult = len(path) - 1
                continue
            for x2, y2 in ((x+1,y), (x-1,y), (x,y+1), (x,y-1)):
                if 0 <= x2 < width and 0 <= y2 < height and heightGrid[x2][y2] - heightGrid[x][y] <= 1 and (x2, y2) not in seen:
                    queue.append(path + [(x2, y2)])
                    seen.add((x2, y2))
        if tempResult < result:
            result = tempResult
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
