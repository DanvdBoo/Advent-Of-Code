from .boilerPlate2024 import puzzle

def part1(s: str):
    c = 0
    for line in s.splitlines():
        c += line.count('XMAS')
        c += line.count('SAMX')
    rows = [[char for char in line] for line in s.splitlines()]
    cols = []
    for i in range(len(rows[0])):
        newstring = ''
        for j in range(len(rows)):
            newstring += rows[j][i]
        cols.append(newstring)
    for line in cols:
        c += line.count('XMAS')
        c += line.count('SAMX')
    diag1 = []
    for i in range(len(rows[0])):
        newstring = ''
        x, y = i, 0
        while x >= 0 and y < len(rows):
            newstring += rows[y][x]
            x -= 1
            y += 1
        diag1.append(newstring)
    for j in range(1, len(rows)):
        newstring = ''
        x, y = len(rows[0]) - 1, j
        while x >= 0 and y < len(rows):
            newstring += rows[y][x]
            x -= 1
            y += 1
        diag1.append(newstring)
    for line in diag1:
        c += line.count('XMAS')
        c += line.count('SAMX')
    diag2 = []
    for i in range(len(rows[0])):
        newstring = ''
        x, y = len(rows[0]) - i - 1, 0
        while x < len(rows[0]) and y < len(rows):
            newstring += rows[y][x]
            x += 1
            y += 1
        diag2.append(newstring)
    for j in range(1, len(rows)):
        newstring = ''
        x, y = 0, j
        while x < len(rows[0]) and y < len(rows):
            newstring += rows[y][x]
            x += 1
            y += 1
        diag2.append(newstring)
    for line in diag2:
        c += line.count('XMAS')
        c += line.count('SAMX')
    return c

def part2(s: str):
    c = 0
    rows = [[char for char in line] for line in s.splitlines()]
    for i in range(1, len(rows) - 1):
        for j in range(1, len(rows[0]) - 1):
            if rows[i][j] == 'A':
                topleft = rows[i-1][j-1]
                topright = rows[i-1][j+1]
                bottomleft = rows[i+1][j-1]
                bottomright = rows[i+1][j+1]
                if ((topleft == 'M' and bottomright == 'S') or (topleft == 'S' and bottomright == 'M')) and ((topright == 'M' and bottomleft == 'S') or (topright == 'S' and bottomleft == 'M')):
                    c += 1
    return c

puzzle(4, part1, part2, False, False).run()
