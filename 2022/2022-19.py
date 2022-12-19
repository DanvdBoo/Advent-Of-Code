from aocd import get_data
from aocd import submit
import math

DAY = 19
YEAR = 2022
possible = [0]*25

def initializePossible():
    global possible
    temp = [0]*24
    currentGeode = 0
    for i in range(24):
        temp[i] = currentGeode + i
        currentGeode += i
    for i, t in enumerate(temp):
        possible[24 - i] = t
    return

def canAfford(price, resources):
    for i, resource in enumerate(resources):
        if price[i] > resource:
            return False
    return True


def resourceAvailable(price, robots):
    for i, resource in enumerate(price):
        if robots[i] == 0 and resource >= 1:
            return False
    return True


def timeNeededForPurchase(price, robots, resources):
    time = 0
    for i, robot in enumerate(robots):
        if price[i] >= 1:
            if resources[i] >= price[i]:
                continue
            resourceNeeded = price[i] - resources[i]
            timeNeeded = int(math.ceil(resourceNeeded/robot))
            time = timeNeeded if timeNeeded > time else time
    return time


def recursiveCalculations(time, resources, robots, prices, currentMax, maxPrices):
    if time > 24:
        print("whoops")
    if time == 24:
        return resources[3]
    newResources = [r + robots[i] for i, r in enumerate(resources)]

    if possible[time] + newResources[3] + (robots[3] * 24-time) < currentMax:
        return resources[3]

    # don't do anything
    timeLeft = 24-time
    doNothingResources = [r + (timeLeft * robots[i])
                          for i, r in enumerate(newResources)]
    tempMax = doNothingResources[3] if doNothingResources[3] > currentMax else currentMax

    if canAfford(prices[3], resources):
        tmp = [0]*4
        tmp[3] = 1
        current = recursiveCalculations(
                    time+1, [r - prices[3][j] for j, r in enumerate(newResources)], [r + tmp[j] for j, r in enumerate(robots)], prices, tempMax, maxPrices)
        if current > tempMax:
            tempMax = current
    else:
        # foreach robot add one
        for i in reversed(range(4)):
            if resourceAvailable(prices[i], robots):
                if i != 3 and robots[i] + 1 > maxPrices[i]:
                    continue
                tmp = [0]*4
                tmp[i] = 1
                timeTillPurchase = timeNeededForPurchase(
                    prices[i], robots, resources)
                if time + timeTillPurchase + 1 > 24:
                    continue
                simulatedResources = [r + ((timeTillPurchase) * robots[i])
                                    for i, r in enumerate(newResources)]
                current = recursiveCalculations(
                    time+timeTillPurchase+1, [r - prices[i][j] for j, r in enumerate(simulatedResources)], [r + tmp[j] for j, r in enumerate(robots)], prices, tempMax, maxPrices)
                if current > tempMax:
                    tempMax = current
    return tempMax


def part1(s):
    results = []
    initializePossible()
    for line in s.splitlines():
        numbers = [int(i) for i in line.split() if i.isdigit()]
        resources = [0, 0, 0, 0]
        robots = [1, 0, 0, 0]
        prices = [[numbers[0], 0, 0, 0], [numbers[1], 0, 0, 0], [
            numbers[2], numbers[3], 0, 0], [numbers[4], 0, numbers[5], 0]]
        maxPrices = [0] * 4
        for price in prices:
            for i, p in enumerate(price):
                maxPrices[i] = p if p > maxPrices[i] else maxPrices[i]
        currentAnswer = recursiveCalculations(
            1, resources, robots, prices, 0, maxPrices)
        results.append(currentAnswer)
        print(len(results), currentAnswer)
    finalAnswer = 0
    for index, result in enumerate(results):
        finalAnswer += result * (index+1)
    print(finalAnswer)
    return
    submit(result, part="a", day=DAY, year=YEAR)


def part2(s):
    return
    submit(result, part="b", day=DAY, year=YEAR)


DATA = get_data(day=DAY, year=YEAR)
TESTDATA = open("testinput.txt", "r").read()
part1(TESTDATA)
part2(DATA)

# lines = data.splitlines()
#
# # SOLUTION
# for index, line in enumerate(lines):
#     result = index
