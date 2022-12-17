from aocd import get_data
from aocd import submit

DAY = 16
YEAR = 2022
currentMax = 0
distances = {}
maxAtTime = [0] * 32
added = {}
addedMax = {}

def distance(currentValve, targetValve, listOfValves):
    if currentValve == targetValve:
        return 0
    if targetValve in listOfValves[currentValve][1]:
        return 1
    minDistance = len(listOfValves) + 1
    for relatedValve in listOfValves[currentValve][1]:
        if relatedValve in listOfValves.keys():
            try:
                dist = distances[relatedValve][targetValve]
            except:
                dist = distance(relatedValve, targetValve, {k: v for k, v in listOfValves.items() if k != currentValve})
            if dist < minDistance:
                minDistance = dist
    return minDistance + 1

def Recursion(timer, currentValve, listOfValves, openValves, value):
    global currentMax, distances
    if timer == 0:
        if value > currentMax:
            print("new max:", value, openValves, timer)
            currentMax = value
        return
    if maxAtTime[timer] + value < currentMax:
        return
    if currentValve not in openValves:
        openValves.append(currentValve)
        for valve in listOfValves:
            if valve != currentValve and valve not in openValves:
                if timer - 1 - distances[currentValve][valve] >= 0:
                    Recursion(timer - 1 - distances[currentValve][valve], valve, {k: v for k, v in listOfValves.items() if k != currentValve}, openValves, value + ((timer - 1) * listOfValves[currentValve]))
        if value + (timer - 1) * listOfValves[currentValve] > currentMax:
            print("new max:", value + (timer - 1) * listOfValves[currentValve], openValves, timer)
            currentMax = value + (timer - 1) * listOfValves[currentValve]
        openValves.remove(currentValve)
    if currentValve == 'AA':
        for valve in listOfValves:
            if valve != currentValve and valve not in openValves:
                if timer - distances[currentValve][valve] >= 0:
                    Recursion(timer - distances[currentValve][valve], valve, listOfValves, openValves, value)
    return

def RecursiveElephant(timer, currentValve, elephantValve, listOfValves, openValves, value, stepsLeft, elephantStepsLeft):
    global currentMax, distances, addedMax, added
    if timer == 0:
        if value > currentMax:
            print("new max:", value, openValves, timer)
            currentMax = value
        return
    if maxAtTime[timer] + value < currentMax:
        return
    if currentValve == elephantValve == 'AA':
        for valve in listOfValves:
            for secondValve in listOfValves:
                if valve != secondValve:
                    dist = distances[currentValve][valve]
                    elephantDist = distances[elephantValve][secondValve]
                    minimum = min(dist, elephantDist)
                    RecursiveElephant(timer - minimum, valve, secondValve, listOfValves, openValves, value, dist - minimum, elephantDist - minimum)

    elif stepsLeft == 0 and elephantStepsLeft != 0:
        if currentValve not in openValves:
            openValves.append(currentValve)
            added[currentValve] = timer - 1
            newValue = value + ((timer - 1) * listOfValves[currentValve])
            for valve in listOfValves:
                if valve != currentValve and valve != elephantValve and valve not in openValves:
                    dist = distances[currentValve][valve] + 1
                    if timer - min(dist, elephantStepsLeft) >= 0:
                        RecursiveElephant(timer - min(dist, elephantStepsLeft), valve, elephantValve, {k: v for k, v in listOfValves.items() if k != currentValve}, openValves, newValue, dist - min(dist, elephantStepsLeft), elephantStepsLeft - min(dist, elephantStepsLeft))
            if len(listOfValves) == 2:
                RecursiveElephant(timer - elephantStepsLeft, currentValve, valve, {k: v for k, v in listOfValves.items() if k != currentValve}, openValves, newValue, 0, 99)
            if newValue > currentMax:
                print("new max:", newValue, openValves, timer - 1)
                currentMax = newValue
            openValves.remove(currentValve)

    elif elephantStepsLeft == 0 and stepsLeft != 0:
        if elephantValve not in openValves:
            openValves.append(elephantValve)
            added[elephantValve] = timer - 1
            newValue = value + ((timer - 1) * listOfValves[elephantValve])
            for valve in listOfValves:
                if valve != elephantValve and valve != currentValve and valve not in openValves:
                    dist = distances[elephantValve][valve] + 1
                    if timer - min(dist, stepsLeft) >= 0:
                        RecursiveElephant(timer - min(dist, stepsLeft), currentValve, valve, {k: v for k, v in listOfValves.items() if k != elephantValve}, openValves, newValue, stepsLeft - min(dist, stepsLeft), dist - min(dist, stepsLeft))
            if len(listOfValves) == 2:
                RecursiveElephant(timer - stepsLeft, currentValve, valve, {k: v for k, v in listOfValves.items() if k != elephantValve}, openValves, newValue, 0, 99)
            if newValue > currentMax:
                print("new max:", newValue, openValves, timer - 1)
                currentMax = newValue
            openValves.remove(elephantValve)

    else:
        if currentValve == elephantValve:
            if currentValve not in openValves:
                openValves.append(currentValve)
                added[currentValve] = timer - 1
                newValue = value + ((timer - 1) * listOfValves[currentValve])
                for valve in listOfValves:
                    for secondValve in listOfValves:
                        if valve != currentValve and valve != secondValve and valve not in openValves and secondValve not in openValves and secondValve != currentValve and valve != elephantValve and secondValve != elephantValve:
                            dist = distances[currentValve][valve] + 1
                            elephantDist = distances[elephantValve][secondValve]
                            minimum = min(dist, elephantDist)
                            if timer - min(dist, elephantStepsLeft) >= 0:
                                RecursiveElephant(timer - minimum, valve, secondValve, {k: v for k, v in listOfValves.items() if k != currentValve}, openValves, newValue, dist - minimum, elephantStepsLeft - minimum)
                if newValue > currentMax:
                    print("new max:", newValue, openValves, timer - 1)
                    currentMax = newValue
                openValves.remove(currentValve)

        elif currentValve not in openValves and elephantValve not in openValves:
            openValves.append(currentValve)
            openValves.append(elephantValve)
            added[currentValve] = timer - 1
            added[elephantValve] = timer - 1
            newValue = value + ((timer - 1) * (listOfValves[currentValve] + listOfValves[elephantValve]))
            if len(listOfValves) == 1:
                for valve in listOfValves:
                    if dist[currentValve][valve] <= dist[elephantValve][valve]:
                        dist = distances[currentValve][valve] + 1
                        if timer - min(dist, elephantStepsLeft) >= 0:
                            RecursiveElephant(timer - min(dist, elephantStepsLeft), valve, elephantValve, {k: v for k, v in listOfValves.items() if k != currentValve and k != elephantValve}, openValves, newValue, dist - min(dist, elephantStepsLeft), elephantStepsLeft - min(dist, elephantStepsLeft))
                    else:
                        dist = distances[elephantValve][valve] + 1
                        if timer - min(dist, stepsLeft) >= 0:
                            RecursiveElephant(timer - min(dist, stepsLeft), currentValve, valve, {k: v for k, v in listOfValves.items() if k != currentValve and k != elephantValve}, openValves, newValue, stepsLeft - min(dist, stepsLeft), dist - min(dist, stepsLeft))
            else:
                for valve in listOfValves:
                    for secondValve in listOfValves:
                        if valve != currentValve and valve != secondValve and valve not in openValves and secondValve not in openValves and secondValve != currentValve and valve != elephantValve and secondValve != elephantValve:
                            dist = distances[currentValve][valve] + 1
                            elephantDist = distances[elephantValve][secondValve] + 1
                            minimum = min(dist, elephantDist)
                            if timer - minimum >= 0:
                                RecursiveElephant(timer - minimum, valve, secondValve, {k: v for k, v in listOfValves.items() if k != currentValve and k != elephantValve}, openValves, newValue, dist - minimum, elephantDist - minimum)
            if newValue > currentMax:
                print("new max:", newValue, openValves, timer - 1,)
                currentMax = newValue
                addedMax = {k: v for k, v in added.items()}
            openValves.remove(currentValve)
            openValves.remove(elephantValve)
    return

def part1(s):
    global distances, maxAtTime
    valves = {}
    for line in s.splitlines():
        line = [substring.replace(',', '').replace(';','') for substring in line.split(' ')]
        valves[line[1]] = [int(line[4][line[4].find('=') + 1:]), [connection for connection in line[9:]]]
        distances[line[1]] = {}
    for valve in valves:
        for secondValve in valves:
            try:
                distances[valve][secondValve]
            except:
                dist = distance(valve, secondValve, valves)
                distances[valve][secondValve] = dist
                distances[secondValve][valve] = dist
        print(valve, valves[valve])
    
    values = sorted([v[0] for k, v in valves.items() if v[0] != 0], reverse=True)
    for minute in range(1,31):
        maxAtTime[minute] = maxAtTime[minute - 1]
        if minute % 2 == 0 and len(values) > 0:
            maxAtTime[minute] += values[0]
            values.pop(0)
    for minute in range(0, 31):
        maxAtTime[minute] = maxAtTime[minute] * (minute - 1)

    print({k: v[0] for k, v in valves.items() if v[0] != 0})
    Recursion(30, 'AA', {k: v[0] for k, v in valves.items() if v[0] != 0}, ['AA'], 0)
    
    print(currentMax)
    submit(currentMax, part="a", day=DAY, year=YEAR)


def part2(s):
    global distances, maxAtTime
    valves = {}
    for line in s.splitlines():
        line = [substring.replace(',', '').replace(';','') for substring in line.split(' ')]
        valves[line[1]] = [int(line[4][line[4].find('=') + 1:]), [connection for connection in line[9:]]]
        distances[line[1]] = {}
    for valve in valves:
        for secondValve in valves:
            try:
                distances[valve][secondValve]
            except:
                dist = distance(valve, secondValve, valves)
                distances[valve][secondValve] = dist
                distances[secondValve][valve] = dist
        print(valve, valves[valve])
    
    values = sorted([v[0] for k, v in valves.items() if v[0] != 0], reverse=True)
    for minute in range(1,27):
        maxAtTime[minute] = maxAtTime[minute - 1]
        if minute % 2 == 0 and len(values) > 0:
            maxAtTime[minute] += values[0]
            values.pop(0)
            if len(values) > 0:
                maxAtTime[minute] += values[0]
                values.pop(0)
    for minute in range(0, 26):
        maxAtTime[minute] = maxAtTime[minute] * (minute - 1)

    print({k: v[0] for k, v in valves.items() if v[0] != 0})
    RecursiveElephant(26, 'AA', 'AA', {k: v[0] for k, v in valves.items() if v[0] != 0}, ['AA'], 0, 0, 0)
    
    print(currentMax)
    return
    submit(result, part="b", day=DAY, year=YEAR)


DATA = get_data(day=DAY, year=YEAR)
TESTDATA = open("testinput.txt", "r").read()
# part1(DATA)
part2(DATA)

# lines = data.splitlines()
#
# # SOLUTION
# for index, line in enumerate(lines):
#     result = index
