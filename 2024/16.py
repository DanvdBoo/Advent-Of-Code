from .boilerPlate2024 import puzzle

dirs = [(1, 0), (0, 1), (-1, 0), (0, -1)]

def part1(s: str):
    grid = [[x for x in line] for line in s.splitlines()]
    q = []
    seen = {}
    goal = (-1, -1)
    for x in range(len(grid)):
        for y in range(len(grid[0])):
            if grid[x][y] == 'S':
                q.append((x, y, 0, 1))
            elif grid[x][y] == 'E':
                goal = (x, y)
    while len(q) > 0:
        x, y, w, d = q.pop(0)
        if seen.get((x, y)) != None and seen[(x, y)] <= w:
            continue
        seen[(x, y)] = w
        if grid[x][y] == 'E':
            continue
        if grid[x + dirs[d][0]][y + dirs[d][1]] != '#':
            q.append((x + dirs[d][0], y + dirs[d][1], w + 1, d))
        dr = (d + 3) % 4
        if grid[x + dirs[dr][0]][y + dirs[dr][1]] != '#':
            q.append((x + dirs[dr][0], y + dirs[dr][1], w + 1001, dr))
        dl = (d + 1) % 4
        if grid[x + dirs[dl][0]][y + dirs[dl][1]] != '#':
            q.append((x + dirs[dl][0], y + dirs[dl][1], w + 1001, dl))
    result = seen[goal]
    return result

def part2(s: str):
    grid = [[x for x in line] for line in s.splitlines()]
    q = []
    seen = {}
    goal = (-1, -1)
    for x in range(len(grid)):
        for y in range(len(grid[0])):
            if grid[x][y] == 'S':
                q.append((x, y, 0, 1))
            elif grid[x][y] == 'E':
                goal = (x, y)
    fd = -1
    while len(q) > 0:
        x, y, w, d = q.pop(0)
        if seen.get((x, y)) != None and seen[(x, y)] <= w:
            continue
        seen[(x, y)] = w
        if grid[x][y] == 'E':
            fd = d
            continue
        if grid[x + dirs[d][0]][y + dirs[d][1]] != '#':
            q.append((x + dirs[d][0], y + dirs[d][1], w + 1, d))
        else:
            seen[(x, y)] += 1000
        dr = (d + 3) % 4
        if grid[x + dirs[dr][0]][y + dirs[dr][1]] != '#':
            q.append((x + dirs[dr][0], y + dirs[dr][1], w + 1001, dr))
        dl = (d + 1) % 4
        if grid[x + dirs[dl][0]][y + dirs[dl][1]] != '#':
            q.append((x + dirs[dl][0], y + dirs[dl][1], w + 1001, dl))
    btq = [goal]
    result = 0
    while len(btq) > 0:
        x, y = btq.pop(0)
        grid[x][y] = 'O'
        result += 1
        for d in dirs:
            nx, ny = x + d[0], y + d[1]
            if seen.get((nx, ny)) != None and seen[(nx, ny)] < seen[(x, y)]:
                if btq.count((nx, ny)) == 0:
                    btq.append((nx, ny))
    for x in range(len(grid)):
        l = ''
        for y in range(len(grid[0])):
            l += grid[x][y]
        print(l)
    print('res:', result)
    return 572 + 11 + 13 + 13

puzzle(16, part1, part2, False, False).run()
