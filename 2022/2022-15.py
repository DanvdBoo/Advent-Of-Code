from aocd import get_data
from aocd import submit

DAY = 15
YEAR = 2022

def manhattenDistance(x, y, Bx, By):
    diffX = abs(x - Bx)
    diffY = abs(y - By)
    return diffX + diffY

def part1(s):
    yGiven = 2000000
    xMin, xMax = 0, 0
    sensors = []
    beacons = []
    for line in s.splitlines():
        x, y, Bx, By = 0, 0, 0, 0
        line = line.split(':')
        for part in line[0].split(' '):
            if part[:2] == 'x=':
                x = int(part[2:].replace(',',''))
            elif part[:2] == 'y=':
                y = int(part[2:])
        for part in line[1].split(' '):
            if part[:2] == 'x=':
                Bx = int(part[2:].replace(',',''))
            elif part[:2] == 'y=':
                By = int(part[2:])
        distance = manhattenDistance(x, y, Bx, By)
        sensors.append({'x': x, 'y': y, 'distance': distance})
        if [Bx, By] not in beacons:
            beacons.append([Bx, By])
        if x - distance < xMin:
            xMin = x - distance
        if x + distance > xMax:
            xMax = x + distance

    result = 0
    for x in range(xMin - 1, xMax + 1):
        if [x, yGiven] not in beacons:
            for sensor in sensors:
                if manhattenDistance(x, yGiven, sensor['x'], sensor['y']) <= sensor['distance']:
                    result += 1
                    break
    submit(result, part="a", day=DAY, year=YEAR)


def part2(s):
    yMin, yMax = 0, 4000000
    sensors = []
    beacons = []
    for line in s.splitlines():
        x, y, Bx, By = 0, 0, 0, 0
        line = line.split(':')
        for part in line[0].split(' '):
            if part[:2] == 'x=':
                x = int(part[2:].replace(',',''))
            elif part[:2] == 'y=':
                y = int(part[2:])
        for part in line[1].split(' '):
            if part[:2] == 'x=':
                Bx = int(part[2:].replace(',',''))
            elif part[:2] == 'y=':
                By = int(part[2:])
        distance = manhattenDistance(x, y, Bx, By)
        sensors.append({'x': x, 'y': y, 'distance': distance})
        if [Bx, By] not in beacons:
            beacons.append([Bx, By])

    result = -1
    for y in range(yMin, yMax + 1):
        subSensors = [sensor for sensor in sensors if abs(y - sensor['y']) <= sensor['distance']]
        x = yMin
        while x <= yMax:
            inRange = False
            for sensor in subSensors:
                if manhattenDistance(x, y, sensor['x'], sensor['y']) <= sensor['distance']:
                    inRange = True
                    yDiff = abs(y - sensor['y'])
                    x = sensor['x'] + sensor['distance'] - yDiff + 1
                    break
            if not inRange:
                result = x * 4000000 + y
                break
        if y % 40000 == 0:
            print(y / 40000)

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
