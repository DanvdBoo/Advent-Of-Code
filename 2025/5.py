from .boilerPlate2025 import puzzle

def part1(s: str):
    result = 0
    dbs, avas = s.split('\n\n')
    ava = [int(x) for x in avas.splitlines()]
    ava.sort()
    for line in dbs.splitlines():
        mins, maxs = line.split('-')
        a, b = int(mins), int(maxs)
        prev = len(ava)
        ava = list(filter(lambda id: id < a or id > b, ava))
        result += prev - len(ava)
    return result

def part2(s: str):
    result = 0
    dbs, _ = s.split('\n\n')
    dbt = [[int(x) for x in y.split('-')] for y in dbs.splitlines()]
    db0, db1 = [d[0] for d in dbt], [d[1] for d in dbt]
    db0.sort(), db1.sort()
    i = 0
    while i < len(db0):
        og = db0[i]
        while i + 1 < len(db0) and db0[i + 1] <= db1[i]:
            i += 1
        result += db1[i] - og + 1
        i += 1
    return result

puzzle(5, part1, part2, False, False).run()
