import heapq
from .boilerPlate2023 import puzzle

def part1(s: str):
    grid = [[int(char) for char in line] for line in s.splitlines()]
    q = [(0, 0, 0, -1, -1)]
    d = {}
    while q:
        dist, r, c, dir_, dirLen = heapq.heappop(q)
        if (r, c, dir_, dirLen) in d:
            continue
        d[(r, c, dir_, dirLen)] = dist
        for i, (dr, dc) in enumerate([(1,0), (0,1), (-1,0), (0,-1)]):
            rr = r + dr
            cc = c + dc
            newDirLen = 1 if i != dir_ else dirLen + 1
            if 0<=rr<len(grid) and 0<=cc<len(grid[0]) and newDirLen <= 3 and ((i+2)%4 != dir_):
                heapq.heappush(q, (dist + grid[rr][cc], rr, cc, i, newDirLen))
    result = []
    for (r, c, _, _), v in d.items():
        if r == len(grid) - 1 and c == len(grid[0]) - 1:
            result.append(v)
    return min(result)

def part2(s: str):
    grid = [[int(char) for char in line] for line in s.splitlines()]
    q = [(0, 0, 0, -1, -1)]
    d = {}
    while q:
        dist, r, c, dir_, dirLen = heapq.heappop(q)
        if (r, c, dir_, dirLen) in d:
            continue
        d[(r, c, dir_, dirLen)] = dist
        for i, (dr, dc) in enumerate([(1,0), (0,1), (-1,0), (0,-1)]):
            rr = r + dr
            cc = c + dc
            newDirLen = 1 if i != dir_ else dirLen + 1
            if 0<=rr<len(grid) and 0<=cc<len(grid[0]) and newDirLen <= 10 and ((i+2)%4 != dir_) and (i == dir_ or dirLen >= 4 or dirLen == -1):
                heapq.heappush(q, (dist + grid[rr][cc], rr, cc, i, newDirLen))
    result = []
    for (r, c, _, _), v in d.items():
        if r == len(grid) - 1 and c == len(grid[0]) - 1:
            result.append(v)
    return min(result)

puzzle(17, part1, part2, False, False).run()
