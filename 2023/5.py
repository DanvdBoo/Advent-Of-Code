from .boilerPlate2023 import puzzle

def part1(s: str):
    maps = [g.split(':')[1].split() for g in s.split('\n\n')]
    seeds = [int(seed) for seed in maps[0]]
    originalSeeds = [int(seed) for seed in maps[0]]
    for m in maps[1:]:
        m = [int(n) for n in m]
        print(seeds)
        for index, seed in enumerate(seeds):
            for i in range(0, len(m), 3):
                if m[i + 1] <= seed and m[i + 1] + m[i + 2] > seed:
                    seeds[index] = m[i] + seed - m[i + 1]
    print(seeds)
    return originalSeeds[seeds.index(min(seeds))]

def part2(s: str):
    return ''

puzzle(5, part1, part2, False, True).run()