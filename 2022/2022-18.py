from aocd import get_data
from aocd import submit

DAY = 18
YEAR = 2022


def part1(s):
    cubes = []
    for line in s.splitlines():
        numbers = line.split(',')
        x, y, z = int(numbers[0]), int(numbers[1]), int(numbers[2])
        cubes.append([x, y, z])

    surface = 0
    for cube in cubes:
        cubeSurface = 6
        x, y, z = cube
        for x2, y2, z2 in ((x+1, y, z), (x-1, y, z), (x, y+1, z), (x, y-1, z), (x, y, z+1), (x, y, z-1)):
            if [x2, y2, z2] in cubes:
                cubeSurface -= 1
        surface += cubeSurface

    submit(surface, part="a", day=DAY, year=YEAR)


def part2(s):
    minX, maxX, minY, maxY, minZ, maxZ = 0, 0, 0, 0, 0, 0
    cubes = []
    for line in s.splitlines():
        numbers = line.split(',')
        x, y, z = int(numbers[0]), int(numbers[1]), int(numbers[2])
        cubes.append([x, y, z])
        minX = x if x < minX else minX
        minY = y if y < minY else minY
        minZ = z if z < minZ else minZ
        maxX = x if x > maxX else maxX
        maxY = y if y > maxY else maxY
        maxZ = z if z > maxZ else maxZ

    completeGrid = [[[0] * (maxZ + 2) for i in range(maxY + 2)]
                    for j in range(maxX + 2)]
    for cube in cubes:
        completeGrid[cube[0]][cube[1]][cube[2]] = 1
    for i in range(3):
        for x, row in enumerate(completeGrid):
            for y, column in enumerate(row):
                for z, depth in enumerate(column):
                    if completeGrid[x][y][z] != 1 and completeGrid[x][y][z] != 2:
                        for x2, y2, z2 in ((x-1, y, z), (x, y-1, z), (x, y, z-1), (x+1, y, z), (x, y+1, z), (x, y, z+1)):
                            if x2 < 0 or y2 < 0 or z2 < 0:
                                completeGrid[x][y][z] = 2
                                break
                            if x2 > len(completeGrid) - 1 or y2 > len(completeGrid[0]) - 1 or z2 > len(completeGrid[0][0]) - 1:
                                completeGrid[x][y][z] = 2
                                break
                            if completeGrid[x2][y2][z2] == 2:
                                completeGrid[x][y][z] = 2
                                break
    surface = 0
    for cube in cubes:
        cubeSurface = 0
        x, y, z = cube
        for x2, y2, z2 in ((x+1, y, z), (x-1, y, z), (x, y+1, z), (x, y-1, z), (x, y, z+1), (x, y, z-1)):
            if x2 < 0 or y2 < 0 or z2 < 0:
                cubeSurface += 1
            elif x2 > len(completeGrid) - 1 or y2 > len(completeGrid[0]) - 1 or z2 > len(completeGrid[0][0]) - 1:
                cubeSurface += 1
            elif completeGrid[x2][y2][z2] == 2:
                cubeSurface += 1
        surface += cubeSurface
    submit(surface, part="b", day=DAY, year=YEAR)


DATA = get_data(day=DAY, year=YEAR)
TESTDATA = open("testinput.txt", "r").read()
part1(DATA)
part2(DATA)

# lines = data.splitlines()
#
# # SOLUTION
# for index, line in enumerate(lines):
#     result = index
