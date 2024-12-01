from .boilerPlate2024 import puzzle

left, right = [], []

def part1(s: str):
    for line in s.splitlines():
        a = line.split(' ')
        left.append(int(a[0]))
        right.append(int(a[3]))
    left.sort()
    right.sort()
    result = 0
    for i in range(len(left)):
        result += abs(left[i] - right[i])
    return result

def part2(s: str):
    result = 0
    for i in left:
        result += i * right.count(i)
    return result

puzzle(1, part1, part2, False, False).run()
