from .boilerPlate2025 import puzzle

def part1(s: str):
    p = [(int(l.split(',')[0].strip()), int(l.split(',')[1].strip())) for l in s.splitlines()]
    result = 0
    for i in range(len(p)):
        for j in range(i + 1, len(p)):
            size = (abs(p[i][0] - p[j][0]) + 1) * (abs(p[i][1] - p[j][1]) + 1)
            if size > result:
                result = size
    return result

def part2(s: str):
    p = [(int(l.split(',')[0].strip()), int(l.split(',')[1].strip())) for l in s.splitlines()]
    m, mm = min([x[0] for x in p]), min([x[1] for x in p])
    p = [(x[0] - m, x[1] - mm) for x in p]
    sizes = []
    for i in range(len(p)):
        for j in range(i + 1, len(p)):
            size = (abs(p[i][0] - p[j][0]) + 1) * (abs(p[i][1] - p[j][1]) + 1)
            sizes.append((size, i, j))
    sizes.sort(key=lambda x: x[0], reverse=True)
    for size in sizes:
        found = False
        for i in range(len(p)):
            if min(p[size[1]][0], p[size[2]][0]) < p[i][0] < max(p[size[1]][0], p[size[2]][0]) and min(p[size[1]][1], p[size[2]][1]) < p[i][1] < max(p[size[1]][1], p[size[2]][1]):
                found = True
                break
            if i != len(p) - 1 and ((p[i][0] == p[i + 1][0] and min(p[size[1]][0], p[size[2]][0]) < p[i][0] < max(p[size[1]][0], p[size[2]][0]) and min(p[i][1], p[i + 1][1]) <= min(p[size[1]][1], p[size[2]][1]) and max(p[size[1]][1], p[size[2]][1]) <= max(p[i][1], p[i + 1][1])) or (p[i][1] == p[i + 1][1] and min(p[size[1]][1], p[size[2]][1]) < p[i][1] < max(p[size[1]][1], p[size[2]][1]) and min(p[i][0], p[i + 1][0]) <= min(p[size[1]][0], p[size[2]][0]) and max(p[size[1]][0], p[size[2]][0]) <= max(p[i][0], p[i + 1][0]))):
                found = True
                break
            if i == len(p) - 1 and ((p[i][0] == p[0][0] and min(p[size[1]][0], p[size[2]][0]) < p[i][0] < max(p[size[1]][0], p[size[2]][0]) and min(p[i][1], p[0][1]) <= min(p[size[1]][1], p[size[2]][1]) and max(p[size[1]][1], p[size[2]][1]) <= max(p[i][1], p[0][1])) or (p[i][1] == p[0][1] and min(p[size[1]][1], p[size[2]][1]) < p[i][1] < max(p[size[1]][1], p[size[2]][1]) and min(p[i][0], p[0][0]) <= min(p[size[1]][0], p[size[2]][0]) and max(p[size[1]][0], p[size[2]][0]) <= max(p[i][0], p[0][0]))):
                found = True
                break
        if not found:
            print(size[0], p[size[1]], p[size[2]])
            return size[0]
    return 0

puzzle(9, part1, part2, False, False).run()
