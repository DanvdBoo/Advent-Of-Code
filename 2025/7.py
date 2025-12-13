from .boilerPlate2025 import puzzle

def part1(s: str):
    result = 0
    beams = []
    for line in s.splitlines():
        if len(beams) == 0:
            beams.append(line.find('S'))
            continue
        nbeams = set()
        for b in beams:
            if line[b] == '^':
                nbeams.add(b - 1)
                nbeams.add(b + 1)
                result += 1
            else:
                nbeams.add(b)
        beams = list(nbeams)
    return result

def part2(s: str):
    beams = dict()
    for line in s.splitlines():
        if len(beams) == 0:
            beams[line.find('S')] = 1
            continue
        nbeams = dict()
        for bk, bv in beams.items():
            if line[bk] == '^':
                nbeams[bk - 1] = nbeams.get(bk - 1, 0) + bv
                nbeams[bk + 1] = nbeams.get(bk + 1, 0) + bv
            else:
                nbeams[bk] = nbeams.get(bk, 0) + bv
        beams = nbeams
    return sum(beams.values())

puzzle(7, part1, part2, False, False).run()
