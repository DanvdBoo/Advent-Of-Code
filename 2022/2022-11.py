from aocd import get_data
from aocd import submit
import math

DAY = 11
YEAR = 2022

def monkey0(old):
    return old * 5

def monkey1(old):
    return old * old

def monkey2(old):
    return old + 1

def monkey3(old):
    return old + 6

def monkey4(old):
    return old * 17

def monkey5(old):
    return old + 8

def monkey6(old):
    return old + 7

def monkey7(old):
    return old + 5

def monkeyTest(worryLevel, testValue):
    return worryLevel % testValue == 0

def part1(s):
    items = [[50, 70, 89, 75, 66, 66],
            [85],
            [66, 51, 71, 76, 58, 55, 58, 60],
            [79, 52, 55, 51],
            [69, 92],
            [71, 76, 73, 98, 67, 79, 99],
            [82, 76, 69, 69, 57],
            [65, 79, 86]]
    operations = [monkey0, monkey1, monkey2, monkey3, monkey4, monkey5, monkey6, monkey7]
    testValue = [2, 7, 13, 3, 19, 5, 11, 17]
    targetTrue = [2, 3, 1, 6, 7, 0, 7, 5]
    targetFalse = [1, 6, 3, 4, 5, 2, 4, 0]
    inspections = [0] * 8

    for i in range(20):
        for m in range(8):
            while len(items[m]) > 0:
                inspectedItem = items[m].pop(0)
                inspections[m] += 1
                inspectedItem = operations[m](inspectedItem)
                inspectedItem = int(math.floor(inspectedItem / 3))
                if monkeyTest(inspectedItem, testValue[m]):
                    items[targetTrue[m]].append(inspectedItem)
                else:
                    items[targetFalse[m]].append(inspectedItem)

    print(inspections)
    inspections.sort(reverse=True)
    result = inspections[0] * inspections[1]
    submit(result, part="a", day=DAY, year=YEAR)


def part2(s):
    items = [[50, 70, 89, 75, 66, 66],
        [85],
        [66, 51, 71, 76, 58, 55, 58, 60],
        [79, 52, 55, 51],
        [69, 92],
        [71, 76, 73, 98, 67, 79, 99],
        [82, 76, 69, 69, 57],
        [65, 79, 86]]
    operations = [monkey0, monkey1, monkey2, monkey3, monkey4, monkey5, monkey6, monkey7]
    testValue = [2, 7, 13, 3, 19, 5, 11, 17]
    targetTrue = [2, 3, 1, 6, 7, 0, 7, 5]
    targetFalse = [1, 6, 3, 4, 5, 2, 4, 0]
    inspections = [0] * 8

    for i in range(10000):
        for m in range(8):
            while len(items[m]) > 0:
                inspectedItem = items[m].pop(0)
                inspections[m] += 1
                inspectedItem = operations[m](inspectedItem)
                if inspectedItem >= 9699690:
                    inspectedItem = inspectedItem % 9699690
                if monkeyTest(inspectedItem, testValue[m]):
                    items[targetTrue[m]].append(inspectedItem)
                else:
                    items[targetFalse[m]].append(inspectedItem)

    print(inspections)
    inspections.sort(reverse=True)
    result = inspections[0] * inspections[1]
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
