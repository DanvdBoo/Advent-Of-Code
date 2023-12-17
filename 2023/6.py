import math
from .boilerPlate2023 import puzzle

def part1(s: str):
    lines = s.splitlines()
    times = [int(n) for n in lines[0].split()[1:]]
    distances = [int(n) for n in lines[1].split()[1:]]
    result = 1
    for i in range(len(times)):
        options = 0
        speed = 0
        timeLeft = times[i]
        for _ in range(times[i]):
            if speed * timeLeft > distances[i]:
                options += 1
            speed += 1
            timeLeft -= 1
        result *= options
    return result

def part2(s: str):
    lines = s.splitlines()
    time = int(lines[0].split(':')[1].replace(' ',''))
    distance = int(lines[1].split(':')[1].replace(' ',''))
    minTime = 0
    maxTime = math.ceil(time/2)
    while minTime != maxTime:
        t = math.ceil((minTime + maxTime) / 2)
        if t == minTime or t == maxTime:
            return time - (2*t) + 1
        if t * (time - t) > distance:
            maxTime = t
        elif t * (time - t) < distance:
            minTime = t
        else:
            return time - (2*t) + 1
    return -1

puzzle(6, part1, part2, False, False).run()
