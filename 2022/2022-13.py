from aocd import get_data
from aocd import submit

DAY = 13
YEAR = 2022

def correctOrder(first, second):
    if len(first) == 0 and len(second) > 0:
        return True
    elif len(second) == 0 and len(first) > 0:
        return False
    for index, element in enumerate(first):
        tempValue = 2
        if index >= len(second):
            return False
        if type(element) == list and type(second[index]) == list:
            tempValue = correctOrder(element, second[index])
        elif type(element) == int and type(second[index]) == list:
            tempValue = correctOrder([element], second[index])
        elif type(element) == list and type(second[index]) == int:
            tempValue = correctOrder(element, [second[index]])
        elif type(element) == int and type(second[index]) == int:
            if element < second[index]:
                return True
            elif element > second[index]:
                return False
        if tempValue != 2:
            return bool(tempValue)
    if len(second) > len(first):
        return True
    return 2


def part1(s):
    pairs = [x.splitlines() for x in s.split('\n\n')]
    result = 0
    for pairIndex, pair in enumerate(pairs):
        correctOrderBool = False
        pair[0] = eval(pair[0])
        pair[1] = eval(pair[1])
        correctOrderBool = correctOrder(pair[0], pair[1])
        if correctOrderBool:
            result += pairIndex + 1
    submit(result, part="a", day=DAY, year=YEAR)


def part2(s):
    pairs = [x.splitlines() for x in s.split('\n\n')]
    sortedArray = [[[2]], [[6]]]
    for pair in pairs:
        for line in pair:
            added = False
            line = eval(line)
            for index, item in enumerate(sortedArray):
                if not correctOrder(item, line):
                    sortedArray.insert(index, line)
                    added = True
                    break
            if not added:
                sortedArray.append(line)
    
    for index, item in enumerate(sortedArray):
        if item == [[2]]:
            result = index + 1
        elif item == [[6]]:
            result = result * (index + 1)
    submit(result, part="b", day=DAY, year=YEAR)


DATA = get_data(day=DAY, year=YEAR)
TESTDATA = open("testinput.txt", "r").read()
part1(DATA)
part2(DATA)

# lines = data.splitlines()
#
# # SOLUTION
# for index, line in enumerate(lines):
#     result = index
