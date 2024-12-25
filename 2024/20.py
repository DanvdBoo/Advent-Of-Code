from .boilerPlate2024 import puzzle

ds = [(1, 0), (-1, 0), (0, 1), (0, -1)]

def part1(s: str):
    g = [[c for c in line] for line in s.splitlines()]
    st, e = (-1, -1), (-1, -1)
    shortcuts = []
    for x in range(len(g)):
        for y in range(len(g[0])):
            if g[x][y] == 'S':
                st = (x, y)
            elif g[x][y] == 'E':
                e = (x, y)
            elif g[x][y] == '#':
                ps = 0
                for d in ds:
                    if 0 <= x + d[0] < len(g) and 0 <= y + d[1] < len(g[0]):
                        if g[x + d[0]][y + d[1]] != '#':
                            ps += 1
                if ps == 2:
                    shortcuts.append((x, y))
    p = {}
    c, pos = 0, st
    while pos != e:
        p[pos] = c
        c += 1
        for d in ds:
            x, y = pos[0] + d[0], pos[1] + d[1]
            if g[x][y] != '#' and p.get((x, y)) is None:
                pos = (x, y)
                break
    p[pos] = c
    result = 0

    for shortcut in shortcuts:
        n = []
        for d in ds:
            nx, ny = shortcut[0] + d[0], shortcut[1] + d[1]
            if p.get((nx, ny)) is not None:
                n.append(p.get((nx, ny)))
        if max(n) - min(n) - 2 >= 100:
            result += 1
    return result

def part2(s: str):
    g = [[c for c in line] for line in s.splitlines()]
    st, e = (-1, -1), (-1, -1)
    for x in range(len(g)):
        for y in range(len(g[0])):
            if g[x][y] == 'S':
                st = (x, y)
            elif g[x][y] == 'E':
                e = (x, y)
    p = {}
    c, pos = 0, st
    while pos != e:
        p[pos] = c
        c += 1
        for d in ds:
            x, y = pos[0] + d[0], pos[1] + d[1]
            if g[x][y] != '#' and p.get((x, y)) is None:
                pos = (x, y)
                break
    p[pos] = c
    result = 0

    for i, (k, v) in enumerate(p.items()):
        for j, (k1, v1) in enumerate(p.items()):
            if i < j:
                dx = abs(k[0] - k1[0])
                dy = abs(k[1] - k1[1])
                if dx + dy <= 20 and abs(v - v1) - (dx + dy) >= 100:
                    result += 1

    return result

puzzle(20, part1, part2, False, False).run()