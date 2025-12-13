from .boilerPlate2025 import puzzle

def part1(s: str):
    result = 0
    dirs = [(-1, -1), (-1, 1), (1, -1), (1, 1), (-1, 0), (1, 0), (0, -1), (0, 1)]
    g = [[1 if x == '@' else 0 for x in y] for y in s.splitlines()]
    mx, my = len(g), len(g[0])
    for x in range(mx):
        for y in range(my):
            if g[x][y] == 0:
                continue
            s = 0
            for d in dirs:
                if 0 <= x + d[0] < mx and 0 <= y + d[1] < my:
                    s += g[x + d[0]][y + d[1]]
            if s < 4:
                result += 1
    return result

def part2(s: str):
    result = 0
    dirs = [(-1, -1), (-1, 1), (1, -1), (1, 1), (-1, 0), (1, 0), (0, -1), (0, 1)]
    g = [[1 if x == '@' else 0 for x in y] for y in s.splitlines()]
    mx, my = len(g), len(g[0])

    r = 1
    while r > 0:
        r = 0
        for x in range(mx):
            for y in range(my):
                if g[x][y] == 0:
                    continue
                s = 0
                for d in dirs:
                    if 0 <= x + d[0] < mx and 0 <= y + d[1] < my:
                        s += g[x + d[0]][y + d[1]]
                if s < 4:
                    g[x][y] = 0
                    result += 1
                    r += 1
    return result

puzzle(4, part1, part2, False, False).run()
