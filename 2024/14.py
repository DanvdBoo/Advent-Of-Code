from .boilerPlate2024 import puzzle

test = False

def part1(s: str):
    h = 11 if test else 101
    w = 7 if test else 103
    q1, q2, q3, q4 = 0, 0, 0, 0
    for line in s.splitlines():
        locs = [int(x) for x in line.replace('p=', '').replace(' v=', ',').split(',')]
        sx, sy, vx, vy = locs[0], locs[1], locs[2], locs[3]
        ex, ey = sx + vx * 100, sy + vy * 100

        ex, ey = ex % h, ey % w
        if ex < h//2 and ey < w//2:
            q1 += 1
        elif ex < h//2 and ey > w//2:
            q3 += 1
        elif ex > h//2 and ey < w//2:
            q2 += 1
        elif ex > h//2 and ey > w//2:
            q4 += 1

    result = q1 * q2 * q3 * q4
    return result

def part2(s: str):
    h = 11 if test else 101
    w = 7 if test else 103
    robots = []
    for line in s.splitlines():
        locs = [int(x) for x in line.replace('p=', '').replace(' v=', ',').split(',')]
        sx, sy, vx, vy = locs[0], locs[1], locs[2], locs[3]
        robots.append((sx, sy, vx, vy))

    secs = 0
    while (True):
        pos = set()
        secs += 1
        for robot in robots:
            sx, sy, vx, vy = robot
            x, y = (sx + vx * secs) % h, (sy + vy * secs) % w
            pos.add((x, y))
        if len(pos) == len(robots):
            print(secs)
            return secs

puzzle(14, part1, part2, test, test).run()
