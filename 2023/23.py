from collections import deque
from .boilerPlate2023 import puzzle

def part1(s: str):
    grid = [[c for c in line] for line in s.splitlines()]
    V = set()
    for r in range(len(grid)):
        for c in range(len(grid[0])):
            nbr = 0
            for dr, dc in [[1, 0] ,[0, 1] ,[-1, 0] ,[0, -1]]:
                if 0 <= r+dr < len(grid) and 0 <= c+dc < len(grid[0]) and grid[r+dr][c+dc] != '#':
                    nbr += 1
            if nbr > 2 and grid[r][c] != '#':
                V.add((r,c))
    for c in range(len(grid[0])):
        if grid[0][c] == '.':
            V.add((0,c))
            start = (0, c)
        elif grid[len(grid) - 1][c] == '.':
            V.add((len(grid) - 1, c))
            end = (len(grid) - 1, c)
    
    E = {}
    for (rv, cv) in V:
        E[(rv,cv)] = []
        Q = deque([(rv,cv,0)])
        SEEN = set()
        while Q:
            r,c,d = Q.popleft()
            if (r,c) in SEEN:
                continue
            SEEN.add((r,c))
            if (r,c) in V and (r,c) != (rv, cv):
                E[(rv,cv)].append(((r,c),d))
                continue
            for dr, dc in [[1, 0] ,[0, 1] ,[-1, 0] ,[0, -1]]:
                if 0 <= r+dr < len(grid) and 0 <= c+dc < len(grid[0]) and grid[r+dr][c+dc] != '#':
                    if (grid[r][c] == '>' and dc != 1) or (grid[r][c] == 'v' and dr != 1):
                        continue
                    Q.append((r+dr,c+dc,d+1))
    ans = 0
    SEEN = [[False for _ in line] for line in s.splitlines()]
    def dfs(v, d):
        nonlocal ans
        r,c = v
        if SEEN[r][c]:
            return
        SEEN[r][c] = True
        if v == end:
            ans = max(ans, d)
        for (y, yd) in E[v]:
            dfs(y, d+yd)
        SEEN[r][c] = False
    dfs(start, 0)
    return ans

def part2(s: str):
    grid = [[c for c in line] for line in s.splitlines()]
    V = set()
    for r in range(len(grid)):
        for c in range(len(grid[0])):
            nbr = 0
            for dr, dc in [[1, 0] ,[0, 1] ,[-1, 0] ,[0, -1]]:
                if 0 <= r+dr < len(grid) and 0 <= c+dc < len(grid[0]) and grid[r+dr][c+dc] != '#':
                    nbr += 1
            if nbr > 2 and grid[r][c] != '#':
                V.add((r,c))
    for c in range(len(grid[0])):
        if grid[0][c] == '.':
            V.add((0,c))
            start = (0, c)
        elif grid[len(grid) - 1][c] == '.':
            V.add((len(grid) - 1, c))
            end = (len(grid) - 1, c)
    
    E = {}
    for (rv, cv) in V:
        E[(rv,cv)] = []
        Q = deque([(rv,cv,0)])
        SEEN = set()
        while Q:
            r,c,d = Q.popleft()
            if (r,c) in SEEN:
                continue
            SEEN.add((r,c))
            if (r,c) in V and (r,c) != (rv, cv):
                E[(rv,cv)].append(((r,c),d))
                continue
            for dr, dc in [[1, 0] ,[0, 1] ,[-1, 0] ,[0, -1]]:
                if 0 <= r+dr < len(grid) and 0 <= c+dc < len(grid[0]) and grid[r+dr][c+dc] != '#':
                    Q.append((r+dr,c+dc,d+1))
    ans = 0
    SEEN = [[False for _ in line] for line in s.splitlines()]
    def dfs(v, d):
        nonlocal ans
        r,c = v
        if SEEN[r][c]:
            return
        SEEN[r][c] = True
        if v == end:
            ans = max(ans, d)
        for (y, yd) in E[v]:
            dfs(y, d+yd)
        SEEN[r][c] = False
    dfs(start, 0)
    return ans

puzzle(23, part1, part2, False, False).run()
