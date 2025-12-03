from .boilerPlate2025 import puzzle

def part1(s: str):
    result = 0
    for line in s.splitlines():
        arr = [int(d) for d in line]
        d1 = max(arr[:-1])
        d2 = max(arr[arr.index(d1) + 1:])
        result += int(str(d1) + str(d2))
    return result

def rec(arr, si: int, ei: int):
    if ei == 0:
        return str(max(arr[si:]))
    d1 = max(arr[si:-ei])
    return str(d1) + rec(arr, arr.index(d1, si) + 1, ei - 1)

def part2(s: str):
    result = 0
    for line in s.splitlines():
        arr = [int(d) for d in line]
        result += int(rec(arr, 0, 11))
    return result

puzzle(3, part1, part2, False, False).run()
