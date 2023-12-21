from .boilerPlate2023 import puzzle
import numpy as np

def part1(s: str):
    REMAINING_STEPS = 64

    grid = [[c for c in line] for line in s.splitlines()]
    q = []
    for iR, r in enumerate(grid):
        for iC, c in enumerate(r):
            if c == "S":
                q.append((iR, iC, 0))
    evenQ, oddQ = [], []
    while len(q) > 0:
        r, c, step = q.pop(0)
        if step > REMAINING_STEPS:
            break
        for dX, dY in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
            if 0 <= r + dX < len(grid) and 0 <= c + dY < len(grid[0]):
                if grid[r + dX][c + dY] == "#":
                    continue
                q.append((r + dX, c + dY, step + 1))
                grid[r + dX][c + dY] = "#"
                stringified = str((r + dX, c + dY))
                if (step + 1) % 2 == 0:
                    if stringified not in evenQ:
                        evenQ.append(stringified)
                else:
                    if stringified not in oddQ:
                        oddQ.append(stringified)
    return len(evenQ) if REMAINING_STEPS % 2 == 0 else len(oddQ)

def part2(s: str):
    REMAINING_STEPS = [65, 196, 327]

    grid = []
    for i in range(7):
        for line in s.splitlines():
            grid.append([char for char in 7 * line])
    q = [(458, 458, 0)]
    evenQ, oddQ = [], []
    fn = [0, 0, 0]
    while len(q) > 0:
        r, c, step = q.pop(0)
        if step == REMAINING_STEPS[0] and fn[0] == 0:
            print(REMAINING_STEPS[0], len(oddQ))
            fn[0] = len(oddQ)
        elif step == REMAINING_STEPS[1] and fn[1] == 0:
            print(REMAINING_STEPS[1], len(evenQ))
            fn[1] = len(evenQ)
        elif step == REMAINING_STEPS[2] and fn[2] == 0:
            print(REMAINING_STEPS[2], len(oddQ))
            fn[2] = len(oddQ)
            break
        for dX, dY in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
            if 0 <= r + dX < len(grid) and 0 <= c + dY < len(grid[0]):
                if grid[r + dX][c + dY] == "#":
                    continue
                q.append((r + dX, c + dY, step + 1))
                grid[r + dX][c + dY] = "#"
                stringified = str((r + dX, c + dY))
                if (step + 1) % 2 == 0:
                    if stringified not in evenQ:
                        evenQ.append(stringified)
                else:
                    if stringified not in oddQ:
                        oddQ.append(stringified)

    vandermonde = np.matrix([[0, 0, 1], [1, 1, 1], [4, 2, 1]])
    b = np.array(fn)
    x = np.linalg.solve(vandermonde, b).astype(np.int64)

    # note that 26501365 = 202300 * 131 + 65 where 131 is the dimension of the grid
    n = 202300
    return x[0] * n * n + x[1] * n + x[2]

puzzle(21, part1, part2, False, False).run()
