from aocd import get_data
from aocd import submit
import math

DAY = 17
YEAR = 2022


def part1(s):
    cave = [[0] * 9 for i in range(8000)]
    for index, item in enumerate(cave):
        cave[index][0] = 1
        cave[index][8] = 1
    cave[0] = [1] * 9

    shapes = [[(0, 0), (0, 1), (0, 2), (0, 3)], [(1, 0), (0, 1), (1, 1), (1, 2), (2, 1)], [
        (0, 0), (0, 1), (0, 2), (1, 2), (2, 2)], [(0, 0), (1, 0), (2, 0), (3, 0)], [(0, 0), (1, 0), (0, 1), (1, 1)]]
    currentShape = 0
    shapeLocation = [4, 3]
    currentHeight = 0
    rocksPlaced = 1
    while rocksPlaced <= 2022:
        for char in s:
            oldShapeLocation = [shapeLocation[0], shapeLocation[1]]
            if char == '>':
                shapeLocation = [shapeLocation[0], shapeLocation[1] + 1]
            elif char == '<':
                shapeLocation = [shapeLocation[0], shapeLocation[1] - 1]
            available = True
            for shapeBlock in shapes[currentShape]:
                if cave[shapeLocation[0] + shapeBlock[0]][shapeLocation[1] + shapeBlock[1]] == 1:
                    available = False
                    break
            if not available:
                shapeLocation = [oldShapeLocation[0], oldShapeLocation[1]]
            oldShapeLocation = [shapeLocation[0], shapeLocation[1]]
            shapeLocation = [shapeLocation[0] - 1, shapeLocation[1]]
            available = True
            for shapeBlock in shapes[currentShape]:
                if cave[shapeLocation[0] + shapeBlock[0]][shapeLocation[1] + shapeBlock[1]] == 1:
                    available = False
                    break
            if not available:
                shapeLocation = [oldShapeLocation[0], oldShapeLocation[1]]
                for shapeBlock in shapes[currentShape]:
                    cave[shapeLocation[0] + shapeBlock[0]
                         ][shapeLocation[1] + shapeBlock[1]] = 1
                if shapeLocation[0] + shapes[currentShape][-1][0] > currentHeight:
                    currentHeight = shapeLocation[0] + \
                        shapes[currentShape][-1][0]
                if currentShape == 4:
                    currentShape = 0
                else:
                    currentShape += 1
                shapeLocation = [currentHeight + 4, 3]
                rocksPlaced += 1
                if rocksPlaced > 2022:
                    break
    submit(currentHeight, part="a", day=DAY, year=YEAR)


def part2(s):
    cave = [[0] * 9 for i in range(14000)]
    for index, item in enumerate(cave):
        cave[index][0] = 1
        cave[index][8] = 1
    cave[0] = [1] * 9

    shapes = [[(0, 0), (0, 1), (0, 2), (0, 3)], [(1, 0), (0, 1), (1, 1), (1, 2), (2, 1)], [
        (0, 0), (0, 1), (0, 2), (1, 2), (2, 2)], [(0, 0), (1, 0), (2, 0), (3, 0)], [(0, 0), (1, 0), (0, 1), (1, 1)]]
    currentShape = 0
    shapeLocation = [4, 3]
    currentHeight = 0
    totalHeight, heightAtIterationCalculation = 0, 0
    rocksPlaced = 1
    prevTotalHeight, prevRocksPlaced = totalHeight, rocksPlaced
    while rocksPlaced <= 1000000000000:
        if rocksPlaced - prevRocksPlaced == 1740 and totalHeight - prevTotalHeight == 2724:
            heightAtIterationCalculation = currentHeight
            iterations = math.floor(
                (1000000000000 - rocksPlaced)/(rocksPlaced - prevRocksPlaced))
            rocksPlaced += iterations * (rocksPlaced - prevRocksPlaced)
            totalHeight += iterations * (totalHeight - prevTotalHeight)
        prevTotalHeight, prevRocksPlaced = totalHeight, rocksPlaced
        for char in s:
            oldShapeLocation = [shapeLocation[0], shapeLocation[1]]
            if char == '>':
                shapeLocation = [shapeLocation[0], shapeLocation[1] + 1]
            elif char == '<':
                shapeLocation = [shapeLocation[0], shapeLocation[1] - 1]
            available = True
            for shapeBlock in shapes[currentShape]:
                if cave[shapeLocation[0] + shapeBlock[0]][shapeLocation[1] + shapeBlock[1]] == 1:
                    available = False
                    break
            if not available:
                shapeLocation = [oldShapeLocation[0], oldShapeLocation[1]]
            oldShapeLocation = [shapeLocation[0], shapeLocation[1]]
            shapeLocation = [shapeLocation[0] - 1, shapeLocation[1]]
            available = True
            for shapeBlock in shapes[currentShape]:
                if cave[shapeLocation[0] + shapeBlock[0]][shapeLocation[1] + shapeBlock[1]] == 1:
                    available = False
                    break
            if not available:
                shapeLocation = [oldShapeLocation[0], oldShapeLocation[1]]
                for shapeBlock in shapes[currentShape]:
                    cave[shapeLocation[0] + shapeBlock[0]
                         ][shapeLocation[1] + shapeBlock[1]] = 1
                if shapeLocation[0] + shapes[currentShape][-1][0] > currentHeight:
                    currentHeight = shapeLocation[0] + \
                        shapes[currentShape][-1][0]
                if currentShape == 4:
                    currentShape = 0
                else:
                    currentShape += 1
                shapeLocation = [currentHeight + 4, 3]
                rocksPlaced += 1
                if rocksPlaced > 1000000000000:
                    break
        if totalHeight < 1565517239:
            totalHeight = currentHeight
        else:
            totalHeight += currentHeight
    result = totalHeight - heightAtIterationCalculation
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
