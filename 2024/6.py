from .boilerPlate2024 import puzzle
import copy

def part1(s: str):
    dirs = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    grid = [[c for c in line] for line in s.splitlines()]
    pos = (0, 0)
    for x in range(len(grid)):
        for y in range(len(grid[x])):
            if grid[x][y] == '^':
                pos = (x, y)
                break
    onsite = True
    currentDir = 0
    while onsite:
        grid[pos[0]][pos[1]] = 'X'
        newPos = (pos[0] + dirs[currentDir][0], pos[1] + dirs[currentDir][1])
        if not (0 <= newPos[0] < len(grid)) or not (0 <= newPos[1] < len(grid[0])):
            onsite = False
            break
        if grid[newPos[0]][newPos[1]] == '#':
            currentDir = currentDir + 1 if currentDir < 3 else 0
            newPos = (pos[0] + dirs[currentDir][0], pos[1] + dirs[currentDir][1])
        pos = newPos
    result = 0
    for x in range(len(grid)):
        for y in range(len(grid[x])):
            if grid[x][y] == 'X':
                result += 1
    return result

def part2(s: str):
    dirs = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    grid = [list(st) for st in s.splitlines()]
    startPos = (0, 0)
    skipPoints = []
    for x in range(len(grid)):
        for y in range(len(grid[0])):
            if grid[x][y] == '^':
                startPos = (x, y)
            if grid[x][y] == '.':
                skipPoints.append((x, y))

    def isLoop(startPos, skipX, skipY, grid):
        seen = set()
        curDir = 0
        grid[skipX][skipY] = '#'
        stack = [startPos]

        while stack:
            x, y = stack.pop()
            if (x, y, curDir) in seen:
                grid[skipX][skipY] = '.'
                return True
            seen.add((x, y, curDir))
            newPos = (x + dirs[curDir][0], y + dirs[curDir][1])
            if not (0 <= newPos[0] < len(grid)) or not (0 <= newPos[1] < len(grid[0])):
                grid[skipX][skipY] = '.'
                return False
            if grid[newPos[0]][newPos[1]] != '#':
                stack.append(newPos)
            else:
                while grid[newPos[0]][newPos[1]] == '#':
                    curDir = (curDir + 1) % 4
                    newPos = (x + dirs[curDir][0], y + dirs[curDir][1])
                stack.append(newPos)
        grid[skipX][skipY] = '.'
        return False

    result = 0
    for x, y in skipPoints:
        if isLoop(startPos, x, y, grid):
            result += 1
    return result

puzzle(6, part1, part2, False, False).run()
