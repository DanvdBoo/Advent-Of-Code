from .boilerPlate2024 import puzzle
from copy import deepcopy

def part1(s: str):
    ns = {}
    for line in s.splitlines():
        n1, n2 = line.split('-')
        if ns.get(n1) is not None:
            ns[n1].append(n2)
        else:
            ns[n1] = [n2]
        if ns.get(n2) is not None:
            ns[n2].append(n1)
        else:
            ns[n2] = [n1]

    triplets = set()

    for k, v in ns.items():
        for i in range(len(v)):
            for j in range(i + 1, len(v)):
                if v[j] in ns[v[i]]:
                    triplets.add((k, v[j], v[i]))
    result = 0
    for t in triplets:
        p = ''
        for n in t:
            p += ' - ' + n
            if n[0] == 't':
                result += 1
                break
    return result // 3

def part2(s: str):
    ns = {}
    for line in s.splitlines():
        n1, n2 = line.split('-')
        if ns.get(n1) is not None:
            ns[n1].append(n2)
        else:
            ns[n1] = [n2]
        if ns.get(n2) is not None:
            ns[n2].append(n1)
        else:
            ns[n2] = [n1]

    def rec(c, vl, i):
        nonlocal ns
        res = deepcopy(c)
        for j in range(i + 1, len(vl)):
            fits = True
            for v in c:
                if v not in ns[vl[j]]:
                    fits = False
            if fits:
                c.append(vl[j])
                nr = rec(c, vl, j)
                c.remove(vl[j])
                if len(nr) > len(res):
                    res = deepcopy(nr)
        return res

    largest = []
    for k, v in ns.items():
        if len(v) <= len(largest):
            continue
        c=[k]
        for i, v1 in enumerate(v):
            c.append(v1)
            nr = rec(c, v, i)
            c.remove(v1)
            if len(nr) > len(largest):
                largest = deepcopy(nr)

    print(largest)
    result = ','.join(sorted(largest))
    return result

puzzle(23, part1, part2, False, False).run()