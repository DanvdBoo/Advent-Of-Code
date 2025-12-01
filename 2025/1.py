from .boilerPlate2025 import puzzle
import math

def part1(s: str):
    p = 50
    r = 0
    for l in s.splitlines():
        if l[0] == 'R':
            p += (int(l[1:]) % 100)
            if p > 99:
                p -= 100
        else:
            p -= (int(l[1:]) % 100)
            if p < 0:
                p = 100 + p
        if p == 0:
            r += 1
    return r

def part2(s: str):
    p = 50
    r = 0
    for l in s.splitlines():
        roll = False
        if l[0] == 'R':
            p += int(l[1:])
            if p > 99:
                roll = True
                t = math.floor(p / 100)
                p -= t * 100
                r += t
        else:
            if p == 0:
                r -= 1
            p -= int(l[1:])
            if p < 0:
                t = abs(math.floor(p / 100))
                p = t * 100 + p
                r += t
        if not roll and p == 0:
            r += 1
    return r

puzzle(1, part1, part2, False, False).run()
