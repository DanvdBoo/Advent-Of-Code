from .boilerPlate2023 import puzzle

def part1(s: str):
    result = 0
    for line in s.splitlines():
        diff = [[int(s) for s in line.split()]]
        index = 0
        while not all([v == 0 for v in diff[index]]):
            diff.append([])
            for i in range(len(diff[index]) - 1):
                diff[index + 1].append(diff[index][i+1] - diff[index][i])
            index += 1
        sumToNext = 0
        while index != -1:
            diff[index].append(diff[index][-1] + sumToNext)
            sumToNext = diff[index][-1]
            index -= 1
        result += diff[0][-1]
    return result

def part2(s: str):
    result = 0
    for line in s.splitlines():
        diff = [[int(s) for s in line.split()]]
        index = 0
        while not all([v == 0 for v in diff[index]]):
            diff.append([])
            for i in range(len(diff[index]) - 1):
                diff[index + 1].append(diff[index][i+1] - diff[index][i])
            index += 1
        sumToNext = 0
        while index != -1:
            diff[index].insert(0, diff[index][0] - sumToNext)
            sumToNext = diff[index][0]
            index -= 1
        result += diff[0][0]
    return result

puzzle(9, part1, part2, False, False).run()
