from .boilerPlate2023 import puzzle

def part1(s: str):
    def distance(galaxy1, galaxy2):
        return abs(galaxy1[0] - galaxy2[0]) + abs(galaxy1[1] - galaxy2[1])

    grid = []
    for line in s.splitlines():
        grid.append([])
        for char in line:
            grid[-1].append(char)
        if all([c == '.' for c in line]):
            grid.append([])
            for char in line:
                grid[-1].append(char)
    idx = 0
    while True:
        try:
            if all([g[idx] == '.' for g in grid]):
                for g in grid:
                    g.insert(idx, '.')
                idx += 1
        except Exception:
            break
        idx += 1
    coords = []
    for iLine, line in enumerate(grid):
        for iChar, char in enumerate(line):
            if char == '#':
                coords.append((iLine, iChar))
    result = 0
    while coords:
        currentGalaxy = coords.pop()
        for coord in coords:
            result += distance(currentGalaxy, coord)
    return result

def part2(s: str):
    EMPTYSIZE = 1000000
    def distance(galaxy1, galaxy2, grid):
        dist = 0
        for i in range(abs(galaxy1[0] - galaxy2[0])):
            neg = -1 if galaxy2[0] - galaxy1[0] < 0 else 1
            if grid[galaxy1[0] + i*neg][galaxy1[1]] == '-':
                dist += EMPTYSIZE
            else:
                dist += 1
        for i in range(abs(galaxy1[1] - galaxy2[1])):
            neg = -1 if galaxy2[1] - galaxy1[1] < 0 else 1
            if grid[galaxy1[0]][galaxy1[1] + i*neg] == '-':
                dist += EMPTYSIZE
            else:
                dist += 1
        return dist

    grid = []
    for line in s.splitlines():
        grid.append([])
        if all([c == '.' for c in line]):
            for _ in line:
                grid[-1].append('-')
        else:
            for char in line:
                grid[-1].append(char)
    for idx in range(len(grid[0])):
        if all([g[idx] in ('.', '-') for g in grid]):
            for g in grid:
                g[idx] = '-'
    coords = []
    for iLine, line in enumerate(grid):
        for iChar, char in enumerate(line):
            if char == '#':
                coords.append((iLine, iChar))
    result = 0
    while coords:
        currentGalaxy = coords.pop()
        for coord in coords:
            result += distance(currentGalaxy, coord, grid)
    return result

puzzle(11, part1, part2, False, False).run()
