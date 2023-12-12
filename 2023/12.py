import math
from .boilerPlate2023 import puzzle

def part1(s: str):
    def isValid(springs, control):
        idx = 0
        count = 0
        for char in springs:
            if char == '#':
                count += 1
            if char == '.':
                if count != 0:
                    if idx < len(control) and control[idx] == count:
                        idx += 1
                    else:
                        return False
                    count = 0
        if count != 0:
            if idx == len(control) - 1 and control[idx] == count:
                return True
            else:
                return False
        if idx == len(control):
            return True
        return False

    def searchOld(springs: str, index: int, control):
        if index == len(springs):
            return 1 if isValid(springs, control) else 0
        if springs[index] != '?':
            return searchOld(springs, index + 1, control)
        newSprings = springs
        result = searchOld(newSprings.replace('?', '.', 1), index + 1, control)
        result += searchOld(springs.replace('?', '#', 1), index + 1, control)
        return result

    def search(springs: str, index: int, control, controlIndex: int, count: int):
        if index == len(springs):
            return 1 if controlIndex == len(control) or (controlIndex == len(control) - 1 and control[controlIndex] == count) else 0
        if controlIndex == len(control):
            return 1 if all([s == '.' or s == '?' for s in springs[index::]]) else 0
        if springs[index] == '.':
            if count > 0:
                return search(springs, index + 1, control, controlIndex + 1, 0) if control[controlIndex] == count else 0
            return search(springs, index + 1, control, controlIndex, 0)
        if springs[index] == '#':
            return search(springs, index + 1, control, controlIndex, count + 1) if control[controlIndex] > count else 0
        
        result = 0
        result += search(springs.replace('?', '#', 1), index + 1, control, controlIndex, count + 1) if control[controlIndex] > count else 0
        if count > 0:
            result += search(springs.replace('?', '.', 1), index + 1, control, controlIndex + 1, 0) if control[controlIndex] == count else 0
        else:
            result += search(springs.replace('?', '.', 1), index + 1, control, controlIndex, 0)
        return result

    result = 0
    for line in s.splitlines():
        springs = line.split()[0]
        control = [int(x) for x in line.split()[1].split(',')]
        result += search(springs, 0, control, 0, 0)
        print(search(springs, 0, control, 0, 0), line)
    return result

def part2(s: str):
    def search(springs: str, index: int, control, controlIndex: int, count: int):
        if index == len(springs):
            return 1 if controlIndex == len(control) or (controlIndex == len(control) - 1 and control[controlIndex] == count) else 0
        if controlIndex == len(control):
            return 1 if all([s == '.' or s == '?' for s in springs[index::]]) else 0
        if len(springs) - index < sum(control[controlIndex::]) - count:
            return 0
        if springs[index] == '.':
            if count > 0:
                return search(springs, index + 1, control, controlIndex + 1, 0) if control[controlIndex] == count else 0
            return search(springs, index + 1, control, controlIndex, 0)
        if springs[index] == '#':
            return search(springs, index + 1, control, controlIndex, count + 1) if control[controlIndex] > count else 0
        
        result = 0
        result += search(springs.replace('?', '#', 1), index + 1, control, controlIndex, count + 1) if control[controlIndex] > count else 0
        if count > 0:
            result += search(springs.replace('?', '.', 1), index + 1, control, controlIndex + 1, 0) if control[controlIndex] == count else 0
        else:
            result += search(springs.replace('?', '.', 1), index + 1, control, controlIndex, 0)
        return result

    result = 0
    for line in s.splitlines():
        springs = ((line.split()[0] + '?'))[:-1]
        control = [int(x) for x in line.split()[1].split(',')]
        tmp1x = search(springs, 0, control, 0, 0)

        springs = ((line.split()[0] + '?') * 2)[:-1]
        control = [int(x) for x in line.split()[1].split(',')] * 2
        tmp2x = search(springs, 0, control, 0, 0)

        springs = ((line.split()[0] + '?') * 3)[:-1]
        control = [int(x) for x in line.split()[1].split(',')] * 3
        tmp3x = search(springs, 0, control, 0, 0)

        springs = ((line.split()[0] + '?') * 4)[:-1]
        control = [int(x) for x in line.split()[1].split(',')] * 4
        tmp4x = search(springs, 0, control, 0, 0)

        springs = ((line.split()[0] + '?') * 5)[:-1]
        control = [int(x) for x in line.split()[1].split(',')] * 5
        tmp5x = search(springs, 0, control, 0, 0)

        print(tmp1x, tmp2x, tmp3x, tmp4x, tmp5x, math.floor(tmp2x/tmp1x), math.ceil(tmp2x/tmp1x))
        if math.floor(tmp2x/tmp1x) != math.ceil(tmp2x/tmp1x):
            print(line, '---', tmp1x, tmp2x, math.floor(tmp2x/tmp1x), math.ceil(tmp2x/tmp1x))
        result += pow(math.ceil(tmp2x/tmp1x), 4) * tmp1x
        break
    return result

puzzle(12, part1, part2, True, True).run()
