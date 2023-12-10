from .boilerPlate2023 import puzzle

def lookAround(grid, iX, iY):
    pairs = [(-1, -1), (-1, -1)]
    idx = 0
    if iX != 0 and grid[iX - 1][iY] in ('F', '7', '|') and grid[iX][iY] in ('J', 'L', '|', 'S'):
        pairs[idx] = (iX - 1, iY)
        idx += 1
    if iY != 0 and grid[iX][iY - 1] in ('F', 'L', '-') and grid[iX][iY] in ('J', '7', '-', 'S'):
        pairs[idx] = (iX, iY - 1)
        idx += 1
    if iX != len(grid) - 1 and grid[iX + 1][iY] in ('J', 'L', '|') and grid[iX][iY] in ('F', '7', '|', 'S'):
        pairs[idx] = (iX + 1, iY)
        idx += 1
    if iY != len(grid[0]) - 1 and grid[iX][iY + 1] in ('J', '7', '-') and grid[iX][iY] in ('F', 'L', '-', 'S'):
        pairs[idx] = (iX, iY + 1)
        idx += 1
    return pairs

def part1(s: str):
    grid = [[char for char in line] for line in s.splitlines()]
    coords = [(0,0), (0,0)]
    for index, line in enumerate(grid):
        for idx, char in enumerate(line):
            if char == 'S':
                coords = lookAround(grid, index, idx)
                grid[index][idx] = '0'
    steps = 1
    while coords[0] != coords[1]:
        currentCoords = coords[0]
        coords[0] = lookAround(grid, coords[0][0], coords[0][1])[0]
        grid[currentCoords[0]][currentCoords[1]] = '0'
        currentCoords = coords[1]
        coords[1] = lookAround(grid, coords[1][0], coords[1][1])[0]
        grid[currentCoords[0]][currentCoords[1]] = '0'
        steps += 1
    return steps

def part2(s: str):
    grid = [[char for char in line] for line in s.splitlines()]
    coords = [(0,0), (0,0)]
    for index, line in enumerate(grid):
        for idx, char in enumerate(line):
            if char == 'S':
                coords = lookAround(grid, index, idx)
                grid[index][idx] = '0'
    while coords[0] != coords[1]:
        currentCoords = coords[0]
        coords[0] = lookAround(grid, coords[0][0], coords[0][1])[0]
        grid[currentCoords[0]][currentCoords[1]] = '0'
        currentCoords = coords[1]
        coords[1] = lookAround(grid, coords[1][0], coords[1][1])[0]
        grid[currentCoords[0]][currentCoords[1]] = '0'
    grid[coords[0][0]][coords[0][1]] = '0'
    IOcoords = (0, 0)
    for index, line in enumerate(s.splitlines()):
        for idx, char in enumerate(line):
            if grid[index][idx] != '0':
                grid[index][idx] = '.'
            else:
                grid[index][idx] = char
                if ((index == len(grid) - 1 or index == 0) and char == '-') or ((idx == len(grid[0]) - 1 or idx == 0) and char == '|'):
                    IOcoords = (index, idx)
    insideDirection = 'N' if IOcoords[0] == len(grid) - 1 else 'S' if IOcoords[0] == 0 else 'E' if IOcoords[1] == 0 else 'W'
    originalDir = insideDirection
    originalDirIOCoords = IOcoords
    for _ in range(2):
        while IOcoords != (-1, -1):
            if insideDirection == 'N' and grid[IOcoords[0] - 1][IOcoords[1]] == '.':
                grid[IOcoords[0] - 1][IOcoords[1]] = '#'
            elif insideDirection == 'E' and grid[IOcoords[0]][IOcoords[1] + 1] == '.':
                grid[IOcoords[0]][IOcoords[1] + 1] = '#'
            elif insideDirection == 'S' and grid[IOcoords[0] + 1][IOcoords[1]] == '.':
                grid[IOcoords[0] + 1][IOcoords[1]] = '#'
            elif insideDirection == 'W' and grid[IOcoords[0]][IOcoords[1] - 1] == '.':
                grid[IOcoords[0]][IOcoords[1] - 1] = '#'

            if grid[IOcoords[0]][IOcoords[1]] in ('F', 'J'):
                insideDirection = 'N' if insideDirection == 'W' else 'W' if insideDirection == 'N' else 'S' if insideDirection == 'E' else 'E' if insideDirection == 'S' else 'huh'
            elif grid[IOcoords[0]][IOcoords[1]] in ('7', 'L'):
                insideDirection = 'N' if insideDirection == 'E' else 'E' if insideDirection == 'N' else 'S' if insideDirection == 'W' else 'W' if insideDirection == 'S' else 'huh'

            if insideDirection == 'N' and grid[IOcoords[0] - 1][IOcoords[1]] == '.':
                grid[IOcoords[0] - 1][IOcoords[1]] = '#'
            elif insideDirection == 'E' and grid[IOcoords[0]][IOcoords[1] + 1] == '.':
                grid[IOcoords[0]][IOcoords[1] + 1] = '#'
            elif insideDirection == 'S' and grid[IOcoords[0] + 1][IOcoords[1]] == '.':
                grid[IOcoords[0] + 1][IOcoords[1]] = '#'
            elif insideDirection == 'W' and grid[IOcoords[0]][IOcoords[1] - 1] == '.':
                grid[IOcoords[0]][IOcoords[1] - 1] = '#'
            grid[IOcoords[0]][IOcoords[1]] = 'S'
            IOcoords = lookAround(grid, IOcoords[0], IOcoords[1])[0]
        IOcoords = originalDirIOCoords
        insideDirection = originalDir
    while True:
        madeChanges = False
        for index, line in enumerate(grid):
            for idx, char in enumerate(line):
                if char == '#':
                    if index != 0 and grid[index - 1][idx] == '.':
                        grid[index - 1][idx] = '#'
                        madeChanges = True
                    elif idx != 0 and grid[index][idx - 1] == '.':
                        grid[index][idx - 1] = '#'
                        madeChanges = True
                    elif index != len(grid) - 1 and grid[index + 1][idx] == '.':
                        grid[index + 1][idx] = '#'
                        madeChanges = True
                    elif idx != len(grid[0]) and grid[index][idx + 1] == '.':
                        grid[index][idx + 1] = '#'
                        madeChanges = True
        if not madeChanges:
            break
    result = 0
    for line in grid:
        for char in line:
            if char == '#':
                result += 1
    return result

puzzle(10, part1, part2, False, False).run()
