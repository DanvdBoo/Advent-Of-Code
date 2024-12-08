from .boilerPlate2024 import puzzle

def part1(s: str):
    d = dict()
    maxX, maxY = 0, 0
    for x, line in enumerate(s.splitlines()):
        maxX = x
        for y, char in enumerate(line):
            maxY = y if y > maxY else maxY
            if char != '.':
                if d.get(char) != None:
                    d[char].append((x, y))
                else:
                    d[char] = [(x, y)]
    antinodes = set()
    for _, freq in d.items():
        pairs = [(freq[i],freq[j]) for i in range(len(freq)) for j in range(i+1, len(freq))]
        for pair in pairs:
            c1, c2 = pair
            x1, y1 = c1
            x2, y2 = c2
            dx, dy = x1 - x2, y1 - y2
            an1, an2 = (x1 + dx, y1 + dy), (x2 + (-1 * dx), y2 + (-1 * dy))
            if 0 <= an1[0] <= maxX and 0 <= an1[1] <= maxY and an1 not in antinodes:
                antinodes.add(an1)
            if 0 <= an2[0] <= maxX and 0 <= an2[1] <= maxY and an2 not in antinodes:
                antinodes.add(an2)
    result = len(antinodes)
    return result

def part2(s: str):
    d = dict()
    maxX, maxY = 0, 0
    for x, line in enumerate(s.splitlines()):
        maxX = x
        for y, char in enumerate(line):
            maxY = y if y > maxY else maxY
            if char != '.':
                if d.get(char) != None:
                    d[char].append((x, y))
                else:
                    d[char] = [(x, y)]
    antinodes = set()
    for _, freq in d.items():
        if len(freq) > 1:
            for loc in freq:
                if loc not in antinodes:
                    antinodes.add(loc)

        pairs = [(freq[i],freq[j]) for i in range(len(freq)) for j in range(i+1, len(freq))]
        for pair in pairs:
            c1, c2 = pair
            x1, y1 = c1
            x2, y2 = c2
            dx, dy = x1 - x2, y1 - y2
            while 0 <= x1 + dx <= maxX and 0 <= y1 + dy <= maxY:
                x1, y1 = x1 + dx, y1 + dy
                an1 = (x1, y1)
                if an1 not in antinodes:
                    antinodes.add(an1)
            while 0 <= x2 + (-1 * dx) <= maxX and 0 <= y2 + (-1 * dy) <= maxY:
                x2, y2 = x2 + (-1 * dx), y2 + (-1 * dy)
                an2 = (x2, y2)
                if an2 not in antinodes:
                    antinodes.add(an2)
    result = len(antinodes)
    return result

puzzle(8, part1, part2, False, False).run()
