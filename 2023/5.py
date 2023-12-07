from .boilerPlate2023 import puzzle
import copy

def part1(s: str):
    maps = [g.split(':')[1].split() for g in s.split('\n\n')]
    seeds = [int(seed) for seed in maps[0]]
    for m in maps[1:]:
        m = [int(n) for n in m]
        for index, seed in enumerate(seeds):
            for i in range(0, len(m), 3):
                if m[i + 1] <= seed and m[i + 1] + m[i + 2] > seed:
                    seeds[index] = m[i] + seed - m[i + 1]
    return min(seeds)

def part2(s: str):
    maps = [g.split(':')[1].split() for g in s.split('\n\n')]
    seeds = []
    for index, seed in enumerate(maps[0]):
        if index % 2 == 0:
            seeds.append((int(seed), int(maps[0][index + 1])))

    for m in maps[1:]:  
        m = [int(n) for n in m]
        newSeeds = []
        while seeds:
            pair = seeds.pop()
            adjusted = False
            for i in range(0, len(m), 3):
                if m[i + 1] <= pair[0] < m[i + 1] + m[i + 2]:
                    overlap = min(m[i + 2] - abs(m[i + 1] - pair[0]), pair[1])
                    newSeeds.append((m[i] + pair[0] - m[i + 1], overlap))
                    if overlap == pair[1]:
                        adjusted = True
                        break
                    seeds.append((pair[0] + m[i + 2], pair[1] - overlap))
                    adjusted = True
                    break
                if pair[0] <= m[i + 1] < pair[0] + pair[1]:
                    overlap = min(m[i + 2], pair[1] - abs(pair[0] - m[i + 1]))
                    newSeeds.append((m[i], overlap))
                    seeds.append((pair[0], pair[1] - overlap))
                    adjusted = True
                    break
            if not adjusted:
                newSeeds.append(pair)
        seeds = copy.deepcopy(newSeeds)
    return min(seeds)[0]

puzzle(5, part1, part2, False, False).run()