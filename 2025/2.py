from .boilerPlate2025 import puzzle

def part1(s: str):
    result = 0
    pairs = [[int(x) for x in y.split('-')] for y in s.split(',')]
    for p in pairs:
        l1, l2 = len(str(p[0])), len(str(p[1]))
        if l1 % 2 == 1 and l2 % 2 == 1 and l1 == l2:
            continue
        t = str(p[0])[:l1//2]
        if t == '':
            t = '1'
        while int(t+t) <= p[1]:
            if int(t+t) >= p[0]:
                result += int(t+t)
            t = str(int(t) + 1)
    return result

def part2(s: str):
    r = []
    pairs = [[int(x) for x in y.split('-')] for y in s.split(',')]
    for p in pairs:
        l1, l2 = len(str(p[0])), len(str(p[1]))
        for i in range(1, 6):
            if l1 % i != 0 and l2 % i != 0:
                continue
            for l in range(l1, l2 + 1):
                times = l // i
                if times <= 1:
                    continue
                t = str(p[0])[:l1//times]
                if t == '':
                    t = '1'
                while int(t*times) <= p[1]:
                    if int(t*times) >= p[0]:
                        if int(t*times) not in r:
                            r.append(int(t*times))
                    t = str(int(t) + 1)
    return sum(r)

puzzle(2, part1, part2, False, False).run()
