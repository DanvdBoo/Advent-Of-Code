from .boilerPlate2023 import puzzle

def calcArea(points):
    res = 0
    for i in range(len(points) - 1):
        x1, y1 = points[i]
        x2, y2 = points[i + 1]
        res += x1 * y2 - x2 * y1
    return abs(res) // 2


def part1(s: str):
    DIRECTION = {"U": (0, -1), "D": (0, 1), "L": (-1, 0), "R": (1, 0)}
    omtrek = 0
    points = [(0, 0)]

    for line in s.splitlines():
        d, l, c = line.split()
        l, c = int(l), c[2:-1]

        omtrek += l

        points.append((points[-1][0] + l * DIRECTION[d][0], points[-1][1] + l * DIRECTION[d][1]))
    
    return calcArea(points) + omtrek // 2 + 1

def part2(s: str):
    DIRECTION = {'3': (0, -1), '1': (0, 1), '2': (-1, 0), '0': (1, 0)}
    omtrek = 0
    points = [(0, 0)]

    for line in s.splitlines():
        _, _, c = line.split()
        l, d = int(c[2:-2], 16), c[-2]

        omtrek += l

        points.append((points[-1][0] + l * DIRECTION[d][0], points[-1][1] + l * DIRECTION[d][1]))
    
    return calcArea(points) + omtrek // 2 + 1

puzzle(18, part1, part2, False, False).run()
