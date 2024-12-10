from .boilerPlate2024 import puzzle

dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]

def part1(s: str):
    grid = [[int(x) for x in l] for l in s.splitlines()]
    starts = []
    for x in range(len(grid)):
        for y in range(len(grid[0])):
            if grid[x][y] == 0:
                starts.append((x, y))
    result = 0
    for sx, sy in starts:
        nines = set()
        queue = [(sx, sy, 0)]
        while len(queue) > 0:
            x, y, v = queue.pop(0)
            if v == 9:
                nines.add((x, y))
                continue

            for dx, dy in dirs:
                nx, ny = x + dx, y + dy
                if not (0 <= nx < len(grid) and 0 <= ny < len(grid[0])):
                    continue
                if grid[nx][ny] == v + 1:
                    queue.append((nx, ny, v + 1))
        result += len(nines)
    return result

def part2(s: str):
    grid = [[int(x) for x in l] for l in s.splitlines()]
    starts = []
    for x in range(len(grid)):
        for y in range(len(grid[0])):
            if grid[x][y] == 0:
                starts.append((x, y))
    result = 0
    for sx, sy in starts:
        nines = []
        queue = [(sx, sy, 0)]
        while len(queue) > 0:
            x, y, v = queue.pop(0)
            if v == 9:
                nines.append((x, y))
                continue

            for dx, dy in dirs:
                nx, ny = x + dx, y + dy
                if not (0 <= nx < len(grid) and 0 <= ny < len(grid[0])):
                    continue
                if grid[nx][ny] == v + 1:
                    queue.append((nx, ny, v + 1))
        result += len(nines)
    return result

puzzle(10, part1, part2, False, False).run()
