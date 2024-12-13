from .boilerPlate2024 import puzzle
from sympy import *

import re

def part1(s: str):
    result = 0
    for game in s.split('\n\n'):
        n = [int(d) for d in re.findall(r'\d+', game)]
        a, b, p = (n[0], n[1]), (n[2], n[3]), (n[4], n[5])
        for i in range(1, 101):
            bc = (p[1] - i * a[1])/b[1]
            if not bc.is_integer():
                continue
            else:
                bc = int(bc)
            sol = i * a[0] + (bc * b[0])
            if sol == p[0]:
                result += 3 * i + bc
                break
    return result

def part2(s: str):
    result = 0
    for game in s.split('\n\n'):
        n = [int(d) for d in re.findall(r'\d+', game)]
        an, bn, p = (n[0], n[1]), (n[2], n[3]), (10000000000000 + n[4], 10000000000000 + n[5])
        a, b = symbols('a,b')
        eq0 = Eq((a * an[0] + b * bn[0]), p[0])
        eq1 = Eq((a * an[1] + b * bn[1]), p[1])
        sol = solve((eq0, eq1), (a, b), dict=True)
        if len(sol) == 1 and isinstance(sol[0][a], Integer) and isinstance(sol[0][b], Integer):
            result += 3 * int(sol[0][a]) + int(sol[0][b])
    return result

puzzle(13, part1, part2, False, False).run()