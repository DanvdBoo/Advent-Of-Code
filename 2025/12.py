from .boilerPlate2025 import puzzle

def part1(s: str):
    result = 0
    ps = []
    for p in s.split('\n\n')[:-1]:
        ps.append(sum([y.count('#') for y in p.splitlines()[1:]]))
    print(ps)
    for line in s.split('\n\n')[-1].splitlines():
        size = [int(x) for x in line.split(':')[0].split('x')]
        pn = [int(p) * ps[i] for i, p in enumerate(line.split(': ')[1].split())]
        if size[0] * size[1] >= sum(pn):
            result += 1
    return result

def part2(s: str):
    result = 0
    return result

puzzle(12, part1, part2, False, True).run()
