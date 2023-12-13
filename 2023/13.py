from .boilerPlate2023 import puzzle

def part1(s: str):
    def checkMirror(i1, i2, grid):
        while i1 != -1 and i2 != len(grid):
            if grid[i1] != grid[i2]:
                return False
            i1 -= 1
            i2 += 1
        return True
    
    def rotate(grid):
        res = ['' for _ in grid[0]]
        for line in grid:
            for index, char in enumerate(line):
                res[index] += char
        return res

    result = 0
    for grid in s.split('\n\n'):
        gridLines = grid.splitlines()
        prevLine = ''
        prevIndex = -1
        matchFound = False
        for index, line in enumerate(gridLines):
            if prevLine == line:
                if checkMirror(prevIndex, index, gridLines):
                    matchFound = True
                    break
            prevIndex = index
            prevLine = line
        if matchFound and prevIndex != -1:
            result += 100 * (prevIndex + 1)
        elif not matchFound:
            prevLine = ''
            prevIndex = -1
            flippedLines = rotate(gridLines)
            for index, line in enumerate(flippedLines):
                if prevLine == line:
                    if checkMirror(prevIndex, index, flippedLines):
                        matchFound = True
                        break
                prevIndex = index
                prevLine = line
            if matchFound and prevIndex != -1:
                result += prevIndex + 1
            elif not matchFound:
                print(grid, 'beep boop there is an error')
    return result

def part2(s: str):
    def checkMirror(i1, i2, grid):
        smudge = False
        while i1 != -1 and i2 != len(grid):
            if grid[i1] != grid[i2]:
                if sum([grid[i1][i] != grid[i2][i] for i in range(len(grid[0]))]) == 1 and not smudge:
                    smudge = True
                else:
                    return False
            i1 -= 1
            i2 += 1
        return smudge
    
    def rotate(grid):
        res = ['' for _ in grid[0]]
        for line in grid:
            for index, char in enumerate(line):
                res[index] += char
        return res

    result = 0
    for grid in s.split('\n\n'):
        gridLines = grid.splitlines()
        prevLine = ''
        prevIndex = -1
        matchFound = False
        for index, line in enumerate(gridLines):
            if prevLine == line or (prevLine != '' and sum([prevLine[i] != line[i] for i in range(len(line))]) == 1):
                if checkMirror(prevIndex, index, gridLines):
                    matchFound = True
                    break
            prevIndex = index
            prevLine = line
        if matchFound and prevIndex != -1:
            result += 100 * (prevIndex + 1)
        elif not matchFound:
            prevLine = ''
            prevIndex = -1
            flippedLines = rotate(gridLines)
            for index, line in enumerate(flippedLines):
                if prevLine == line or (prevLine != '' and sum([prevLine[i] != line[i] for i in range(len(line))]) == 1):
                    if checkMirror(prevIndex, index, flippedLines):
                        matchFound = True
                        break
                prevIndex = index
                prevLine = line
            if matchFound and prevIndex != -1:
                result += prevIndex + 1
            elif not matchFound:
                print(grid, 'beep boop there is an error')
    return result

puzzle(13, part1, part2, False, False).run()
