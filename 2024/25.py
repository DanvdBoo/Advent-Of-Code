from .boilerPlate2024 import puzzle

def part1(s: str):
    kols = s.split('\n\n')
    keys, locks = [], []
    for kol in kols:
        lines = kol.splitlines()
        islock = lines[0][0] == '#'
        arr = [0, 0, 0, 0, 0]
        for i in range(1, 6):
            for j in range(5):
                if lines[i][j] == '#':
                    if islock:
                        arr[j] += 1
                    else:
                        arr[j] = max(6 - i, arr[j])
        if islock:
            locks.append(arr)
        else:
            keys.append(arr)
    result = 0
    for lock in locks:
        for key in keys:
            if max([x + y for x, y in zip(lock, key)]) <= 5:
                result += 1
    return result

def part2(s: str):
    # No Part Two Today
    result = 0
    return result

puzzle(25, part1, part2, False, True).run()
