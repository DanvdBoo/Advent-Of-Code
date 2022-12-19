from aocd import get_data
from aocd import submit
from heapq import heapify, heappop, heappush

DAY = 19
YEAR = 2022
possible = [0]*33

def initializePossible():
    global possible
    currentGeode = 0
    for i in range(33):
        possible[i] = currentGeode + i
        currentGeode += i
    return

def solution(resources, robots, prices, maxPrices, end):
    t, ore, clay, obsidian, geode = 0,0,0,0,0
    queue = [(t, ore, clay, obsidian, geode, robots[0], robots[1], robots[2], robots[3])]
    heapify(queue)
    best = set()
    while queue:
        q = heappop(queue)
        t, ore, clay, obsidian, geode, ore_bots, clay_bots, obsidian_bots, geode_bots = q
        if t >= end:
            best.add(geode)
            continue
        if possible[end - (t + 1)] + geode + (end-t) * geode_bots < max(best or [0]):
            continue
        best.add(geode)
        ore_flag, clay_flag, obsidian_flag, geode_flag = False, False, False, False
        for t in range(t, end):
            best.add(geode)
            if not ore_flag and ore >= (o := prices[0][0]) and ore_bots < maxPrices[0]:
                heappush(queue, (t + 1, ore - o + ore_bots, clay + clay_bots, obsidian + obsidian_bots, geode + geode_bots, ore_bots + 1, clay_bots, obsidian_bots, geode_bots))
                ore_flag = True
            if not clay_flag and ore >= (o := prices[1][0]) and clay_bots < maxPrices[1]:
                heappush(queue, (t + 1, ore - o + ore_bots, clay + clay_bots, obsidian + obsidian_bots, geode + geode_bots, ore_bots, clay_bots + 1, obsidian_bots, geode_bots))
                clay_flag = True
            if not obsidian_flag and ore >= (o := prices[2][0]) and clay >= (c := prices[2][1]) and obsidian_bots < maxPrices[2]:
                heappush(queue, (t + 1, ore - o + ore_bots, clay - c + clay_bots, obsidian + obsidian_bots, geode + geode_bots, ore_bots, clay_bots, obsidian_bots + 1, geode_bots))
                obsidian_flag = True
            if not geode_flag and ore >= (o := prices[3][0]) and obsidian >= (ob := prices[3][2]):
                heappush(queue, (t + 1, ore - o + ore_bots, clay + clay_bots, obsidian - ob + obsidian_bots, geode + geode_bots, ore_bots, clay_bots, obsidian_bots, geode_bots + 1))
                geode_flag = True
            ore += ore_bots
            clay+= clay_bots
            obsidian += obsidian_bots
            geode += geode_bots
    return max(best)


def part1(s):
    initializePossible()
    results = []
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
        currentAnswer = solution(resources, robots, prices, maxPrices, 24)
        results.append(currentAnswer)
        print(len(results), currentAnswer)
    finalAnswer = 0
    for index, result in enumerate(results):
        finalAnswer += result * (index+1)

    submit(finalAnswer, part="a", day=DAY, year=YEAR)


def part2(s):
    results = []
    index = 0
    for line in s.splitlines():
        if index == 3:
            break
        numbers = [int(i) for i in line.split() if i.isdigit()]
        resources = [0, 0, 0, 0]
        robots = [1, 0, 0, 0]
        prices = [[numbers[0], 0, 0, 0], [numbers[1], 0, 0, 0], [
            numbers[2], numbers[3], 0, 0], [numbers[4], 0, numbers[5], 0]]
        maxPrices = [0] * 4
        for price in prices:
            for i, p in enumerate(price):
                maxPrices[i] = p if p > maxPrices[i] else maxPrices[i]
        currentAnswer = solution(resources, robots, prices, maxPrices, 32)
        results.append(currentAnswer)
        print(len(results), currentAnswer)
        index += 1
    finalAnswer = 1
    for index, result in enumerate(results):
        finalAnswer *= result

    submit(finalAnswer, part="b", day=DAY, year=YEAR)


DATA = get_data(day=DAY, year=YEAR)
TESTDATA = open("testinput.txt", "r").read()
part1(DATA)
part2(DATA)

# lines = data.splitlines()
#
# # SOLUTION
# for index, line in enumerate(lines):
#     result = index
