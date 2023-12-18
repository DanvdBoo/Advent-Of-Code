from .boilerPlate2023 import puzzle

def part1(s: str):
    # grid2 = [[1e4, -1e4] for _ in range(1000)]
    grid2 = {0: [1e4, -1e4]}
    r, c = 0, 0
    maxD, maxU = 0 ,0
    for line in s.splitlines():
        d, l, color = line.split()
        color = color.replace('(','').replace(')','')
        if d == 'R':
            c += int(l)
            grid2[r][1] = max(grid2[r][1], c)
        elif d == 'L':
            c -= int(l)
            grid2[r][0] = min(grid2[r][0], c)
        if d == 'D':
            for i in range(1, int(l) + 1):
                if not r+i in grid2:
                    grid2.update([(r+i, [c, c])])
                grid2[r+i][0] = min(grid2[r+i][0], c)
                grid2[r+i][1] = max(grid2[r+i][1], c)
            r += int(l)
        elif d == 'U':
            for i in range(1, int(l) + 1):
                if r-i not in grid2:
                    grid2.update([(r-i, [c, c])])
                grid2[r-i][0] = min(grid2[r-i][0], c)
                grid2[r-i][1] = max(grid2[r-i][1], c)
            r -= int(l)
    result = 0
    for _, [minC, maxC] in grid2.items():
        if minC != 1e4 and maxC != -1e4:
            result += maxC - minC + 1
    return result

def part2(s: str):
    result = s
    return 0

puzzle(18, part1, part2, False, True).run()
