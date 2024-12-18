from .boilerPlate2024 import puzzle
import copy

ds = [(1, 0), (-1, 0), (0, 1), (0, -1)]

t1 = False
def part1(s: str):
    b = [(int(l.split(',')[0]), int(l.split(',')[1])) for l in s.splitlines()]
    t = 71 if not t1 else 7
    g = [[0 for _ in range(t)] for _ in range(t)]
    for x, y in b[:1024 if not t1 else 12]:
        g[x][y] = -1
    q = [(0, 0)]
    g[0][0] = 1
    while len(q) > 0:
        x, y = q.pop(0)
        v = g[x][y]
        for dx, dy in ds:
            if not (0 <= x + dx < len(g) and 0 <= y + dy < len(g[0])):
                continue
            if g[x + dx][y + dy] > v + 1 or g[x + dx][y + dy] == 0:
                q.append((x + dx, y + dy))
                g[x + dx][y + dy] = v + 1
    result = g[t - 1][t - 1] - 1
    return result

t2 = False
def part2(s: str):
    b = [(int(l.split(',')[0]), int(l.split(',')[1])) for l in s.splitlines()]
    t = 71 if not t2 else 7
    go = [[0 for _ in range(t)] for _ in range(t)]
    go[0][0] = 1
    bmin, bmax = 1024 if not t2 else 12, len(s.splitlines())
    for x, y in b[:1024 if not t2 else 12]:
        go[x][y] = -1

    def findExit(g):
        nonlocal t
        q = [(0, 0)]
        while len(q) > 0:
            x, y = q.pop(0)
            v = g[x][y]
            for dx, dy in ds:
                if not (0 <= x + dx < len(g) and 0 <= y + dy < len(g[0])):
                    continue
                if g[x + dx][y + dy] > v + 1 or g[x + dx][y + dy] == 0:
                    q.append((x + dx, y + dy))
                    g[x + dx][y + dy] = v + 1
        return g[t - 1][t - 1] != 0
    
    while True:
        bt = (bmax - bmin)//2 + bmin
        g = copy.deepcopy(go)
        for x, y in b[bmin:bt]:
            g[x][y] = - 1
        if findExit(g):
            for x, y in b[bmin:bt]:
                go[x][y] = - 1
            bmin = bt
        else:
            bmax = bt
        if bmax - bmin == 1:
            return ','.join([str(c) for c in b[bmax - 1]])

puzzle(18, part1, part2, t1, t2).run()
