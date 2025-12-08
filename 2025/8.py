from .boilerPlate2025 import puzzle
import math
from collections import Counter

def dist(p1, p2):
    return (p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2 + (p1[2] - p2[2]) ** 2

def part1(s: str):
    p = [tuple([int(c) for c in ps.split(',')]) for ps in s.splitlines()]
    nn = len(p)
    d = [0] * (nn ** 2)
    for i in range(len(p)):
        for j in range(i + 1, len(p)):
            d[i * nn + j] = dist(p[i], p[j])
    dc = list(filter(lambda x: x != 0, d))
    dc.sort()
    print('distance calculated')
    ni = 0
    dd = dict()
    for dic in dc[:1000]:
        ind = d.index(dic)
        i, j = ind // nn, ind % nn
        d[ind] = 0
        if dd.get(p[i]) == None:
            dd[p[i]] = -1
        if dd.get(p[j]) == None:
            dd[p[j]] = -1

        if dd[p[i]] == -1 and dd[p[j]] == -1:
            dd[p[i]] = ni
            dd[p[j]] = ni
            ni += 1
        elif dd[p[i]] != -1 and dd[p[j]] == -1:
            dd[p[j]] = dd[p[i]]
        elif dd[p[i]] == -1 and dd[p[j]] != -1:
            dd[p[i]] = dd[p[j]]
        elif dd[p[i]] != -1 and dd[p[j]] != -1 and dd[p[i]] != dd[p[j]]:
            fr, to = dd[p[j]], dd[p[i]]
            for k, v in dd.items():
                if v == fr:
                    dd[k] = to

    css = [x for x in dict(Counter(dd.values())).values()]
    css.sort(reverse=True)
    return math.prod(css[:3])

def part2(s: str):
    p = [tuple([int(c) for c in ps.split(',')]) for ps in s.splitlines()]
    nn = len(p)
    d = [0] * (nn ** 2)
    for i in range(len(p)):
        for j in range(i + 1, len(p)):
            d[i * nn + j] = dist(p[i], p[j])
    dc = list(filter(lambda x: x != 0, d))
    dc.sort()
    print('distance calculated')
    ni = 0
    ncs = 0
    dd = dict()
    for dic in dc:
        ind = d.index(dic)
        i, j = ind // nn, ind % nn
        d[ind] = 0
        if dd.get(p[i]) == None:
            dd[p[i]] = -1
        if dd.get(p[j]) == None:
            dd[p[j]] = -1

        if dd[p[i]] == -1 and dd[p[j]] == -1:
            dd[p[i]] = ni
            dd[p[j]] = ni
            ni += 1
            ncs += 1
        elif dd[p[i]] != -1 and dd[p[j]] == -1:
            dd[p[j]] = dd[p[i]]
        elif dd[p[i]] == -1 and dd[p[j]] != -1:
            dd[p[i]] = dd[p[j]]
        elif dd[p[i]] != -1 and dd[p[j]] != -1 and dd[p[i]] != dd[p[j]]:
            fr, to = dd[p[j]], dd[p[i]]
            for k, v in dd.items():
                if v == fr:
                    dd[k] = to
            ncs -= 1
        if ncs == 1 and len(dd) == len(p):
            return p[i][0] * p[j][0]

    return -1

puzzle(8, part1, part2, False, False).run()
