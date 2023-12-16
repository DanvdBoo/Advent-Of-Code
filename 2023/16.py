import functools
from .boilerPlate2023 import puzzle

def part1(s: str):
    def getDir(dir: str):
        return (-1 if dir == 'N' else 1 if dir == 'S' else 0, 1 if dir == 'E' else -1 if dir == 'W' else 0)

    grid = [[char for char in line] for line in s.splitlines()]
    visitedLocations = []
    visitedSplitters = []
    currentLocations = [((0, 3), 'S')]
    while len(currentLocations) > 0:
        poppedItem = currentLocations.pop(0)
        direction = poppedItem[1]
        loc = poppedItem[0]
        if loc[0] < 0 or loc[1] < 0 or loc[0] == len(grid) or loc[1] == len(grid[0]):
            continue
        if loc not in visitedLocations:
            visitedLocations.append(loc)
        field = grid[loc[0]][loc[1]]
        if field == '/':
            direction = 'N' if direction == 'E' else 'E' if direction == 'N' else 'S' if direction == 'W' else 'W'
        elif field == '\\':
            direction = 'N' if direction == 'W' else 'W' if direction == 'N' else 'S' if direction == 'E' else 'E'
        elif field == '|':
            if direction == 'E' or direction == 'W':
                if loc in visitedSplitters:
                    continue
                visitedSplitters.append(loc)
                directionTup = getDir('N')
                currentLocations.append(((loc[0] + directionTup[0], loc[1] + directionTup[1]), 'N'))
                direction = 'S'
        elif field == '-':
            if direction == 'N' or direction == 'S':
                if loc in visitedSplitters:
                    continue
                visitedSplitters.append(loc)
                directionTup = getDir('E')
                currentLocations.append(((loc[0] + directionTup[0], loc[1] + directionTup[1]), 'E'))
                direction = 'W'
        directionTup = getDir(direction)
        currentLocations.append(((loc[0] + directionTup[0], loc[1] + directionTup[1]), direction))
    print(len(visitedLocations))
    return len(visitedLocations)

def part2(s: str):
    @functools.cache
    def getDir(dir: str):
        return (-1 if dir == 'N' else 1 if dir == 'S' else 0, 1 if dir == 'E' else -1 if dir == 'W' else 0)

    grid = [[char for char in line] for line in s.splitlines()]
    maximum = 0
    startingPositions = []
    for i in range(len(grid)):
        startingPositions.append(((0, i), 'S'))
        startingPositions.append(((len(grid[0]) - 1, i), 'N'))
    for i in range(len(grid[0])):
        startingPositions.append(((i, 0), 'E'))
        startingPositions.append(((i, len(grid) - 1), 'W'))
    for startingPos in startingPositions:
        visitedLocations = []
        visitedSplitters = []
        currentLocations = [startingPos]
        while len(currentLocations) > 0:
            poppedItem = currentLocations.pop(0)
            direction = poppedItem[1]
            loc = poppedItem[0]
            if loc[0] < 0 or loc[1] < 0 or loc[0] == len(grid) or loc[1] == len(grid[0]):
                continue
            if loc not in visitedLocations:
                visitedLocations.append(loc)
            field = grid[loc[0]][loc[1]]
            if field == '/':
                direction = 'N' if direction == 'E' else 'E' if direction == 'N' else 'S' if direction == 'W' else 'W'
            elif field == '\\':
                direction = 'N' if direction == 'W' else 'W' if direction == 'N' else 'S' if direction == 'E' else 'E'
            elif field == '|':
                if direction == 'E' or direction == 'W':
                    if loc in visitedSplitters:
                        continue
                    visitedSplitters.append(loc)
                    directionTup = getDir('N')
                    currentLocations.append(((loc[0] + directionTup[0], loc[1] + directionTup[1]), 'N'))
                    direction = 'S'
            elif field == '-':
                if direction == 'N' or direction == 'S':
                    if loc in visitedSplitters:
                        continue
                    visitedSplitters.append(loc)
                    directionTup = getDir('E')
                    currentLocations.append(((loc[0] + directionTup[0], loc[1] + directionTup[1]), 'E'))
                    direction = 'W'
            directionTup = getDir(direction)
            currentLocations.append(((loc[0] + directionTup[0], loc[1] + directionTup[1]), direction))
        maximum = max(len(visitedLocations), maximum)
        print(startingPos, len(visitedLocations))
    return maximum

puzzle(16, part1, part2, False, False).run()
