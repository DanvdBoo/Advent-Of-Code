from .boilerPlate2025 import puzzle
import math

def part1(s: str):
    g = [[t.strip() for t in l.split()] for l in s.splitlines()]
    r = [[g[j][i] if j == len(g) - 1 else int(g[j][i]) for j in range(len(g))] for i in range(len(g[0]))]
    result = 0
    for su in r:
        if su[-1] == '+':
            result += sum(su[:-1])
        else:
            result += math.prod(su[:-1])
    return result

def part2(s: str):
    lines = s.splitlines()
    l = len(lines[0]) - 1
    nums, t = lines[:-1], lines[-1]
    r = []
    curr = []
    for i in range(len(lines[0])):
        n = ''
        for j in range(len(nums)):
            n += nums[j][l - i]
        if n.strip() == '':
            continue
        curr.append(int(n.strip()))
        if t[l - i] != ' ':
            curr.append(t[l - i])
            r.append(curr)
            curr = []

    result = 0
    for su in r:
        if su[-1] == '+':
            result += sum(su[:-1])
        else:
            result += math.prod(su[:-1])
    return result

puzzle(6, part1, part2, False, False).run()
