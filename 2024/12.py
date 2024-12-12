from .boilerPlate2024 import puzzle

dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]
dirx = [(1, 1), (1, -1), (-1, 1), (-1, -1)]

def part1(s: str):
    grid = [[c for c in line] for line in s.splitlines()]
    sx, sy = len(grid), len(grid[0])
    index = 0
    def calc(c, xi, yi):
        seen = [(xi, yi)]
        size, per = 1, 0
        while len(seen) > 0:
            x, y = seen.pop(0)
            grid[x][y] = index
            for dir in dirs:
                xn, yn = x + dir[0], y + dir[1]
                if 0 <= xn < sx and 0 <= yn < sy:
                    if grid[xn][yn] == c:
                        if (xn, yn) not in seen:
                            seen.append((xn, yn))
                            size += 1
                    elif grid[xn][yn] != index:
                        per += 1
                else:
                    per += 1
        return (size, per)
    result = 0
    for x in range(sx):
        for y in range(sy):
            if isinstance(grid[x][y], str):
                size, per = calc(grid[x][y], x, y)
                result += size * per
                index += 1
    return result

def part2(s: str):
    grid = [[c for c in line] for line in s.splitlines()]
    sx, sy = len(grid), len(grid[0])
    index = 0
    def calc(c, xi, yi):
        seen = [(xi, yi)]
        size, p = 1, 0
        per = set()
        while len(seen) > 0:
            x, y = seen.pop(0)
            grid[x][y] = index
            o, oi = 0, 0
            for i, dir in enumerate(dirs):
                xn, yn = x + dir[0], y + dir[1]
                if 0 <= xn < sx and 0 <= yn < sy:
                    if grid[xn][yn] == c:
                        if (xn, yn) not in seen:
                            seen.append((xn, yn))
                            size += 1
                    elif grid[xn][yn] != index:
                        per.add((xn, yn))
                        o += 1
                        oi += i
                else:
                    per.add((xn, yn))
                    o += 1
                    oi += i
            if o == 2 and not (oi == 1 or oi == 5):
                p += 1
            elif o == 3:
                p += 2
            elif o == 4:
                p += 4
        for e in per:
            o, oi = 0, 0
            for i, dir in enumerate(dirs):
                xn, yn = e[0] + dir[0], e[1] + dir[1]
                if 0 <= xn < sx and 0 <= yn < sy and grid[xn][yn] == index:
                    o += 1
                    oi += i
            if o == 2 and not (oi == 1 or oi == 5):
                p += 1
            if o == 3:
                p += 2
            if o == 4:
                p += 4
            for dir in dirx:
                if 0 <= e[0] < sx and 0 <= e[0] + dir[0] < sx and 0 <= e[1] < sy and 0 <= e[1] + dir[1] < sy:
                    if grid[e[0] + dir[0]][e[1] + dir[1]] != index and grid[e[0]][e[1] + dir[1]] == index and grid[e[0] + dir[0]][e[1]] == index:
                        p -= 1
        print(c, size, p)
        return size * p
    result = 0
    for x in range(sx):
        for y in range(sy):
            if isinstance(grid[x][y], str):
                result += calc(grid[x][y], x, y)
                index += 1
    return result

puzzle(12, part1, part2, False, False).run()
