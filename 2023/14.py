from .boilerPlate2023 import puzzle

def part1(s: str):
    result = 0
    grid = [[char for char in line] for line in s.splitlines()]
    for iRow, row in enumerate(grid):
        for iCol, char in enumerate(row):
            if char == 'O':
                i = iRow
                while i != 0:
                    if grid[i - 1][iCol] == '.':
                        i -= 1
                    else:
                        break
                grid[iRow][iCol] = '.'
                grid[i][iCol] = 'O'
                result += len(grid) - i
    return result

def part2(s: str):
    result = 0
    grid = [[char for char in line] for line in s.splitlines()]
    grids = [''.join(char for line in grid for char in line)]
    cycle = 0
    while cycle < 1000000000:
        for _ in range(4):
            for iRow, row in enumerate(grid):
                for iCol, char in enumerate(row):
                    if char == 'O':
                        i = iRow
                        while i != 0:
                            if grid[i - 1][iCol] == '.':
                                i -= 1
                            else:
                                break
                        grid[iRow][iCol] = '.'
                        grid[i][iCol] = 'O'
            grid = [list(elem) for elem in list(zip(*grid[::-1]))]
        stringifyGrid = ''.join(char for line in grid for char in line)
        if stringifyGrid in grids:
            finalGrid = [[char for char in line] for line in list(map(''.join, zip(*[iter(grids[(1000000000 - grids.index(stringifyGrid)) % (len(grids) - grids.index(stringifyGrid)) + grids.index(stringifyGrid)])]*len(grid[0]))))]
            for iRow, row in enumerate(finalGrid):
                for char in row:
                    if char == 'O':
                        result += len(finalGrid) - iRow
            break
        grids.append(stringifyGrid)
        cycle += 1
    return result

puzzle(14, part1, part2, False, False).run()
