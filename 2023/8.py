import math
from .boilerPlate2023 import puzzle

def part1(s: str):
    lines = s.splitlines()
    node = {}
    for line in lines[2::]:
        tmp = line.replace(' ','')
        key = tmp.split('=')[0]
        left = tmp.split('=')[1].split(',')[0].replace('(','')
        right = tmp.split('=')[1].split(',')[1].replace(')','')
        node.update({key: (left, right)})
    currentNode = 'AAA'
    steps = 0
    while currentNode != 'ZZZ':
        for char in lines[0]:
            currentNode = node[currentNode][0 if char == 'L' else 1]
            steps += 1
            if currentNode == 'ZZZ':
                break
    return steps

def part2(s: str):
    lines = s.splitlines()
    node = {}
    currentNodes = []
    for line in lines[2::]:
        tmp = line.replace(' ','').split('=')
        key = tmp[0]
        left = tmp[1].split(',')[0].replace('(','')
        right = tmp[1].split(',')[1].replace(')','')
        node.update({key: (left, right)})
        if key[2] == 'A':
            currentNodes.append(key)
    allSteps = []
    for c in currentNodes:
        steps = 0
        currentNode = c
        while currentNode[2] != 'Z':
            for char in lines[0]:
                currentNode = node[currentNode][0 if char == 'L' else 1]
                steps += 1
                if currentNode[2] == 'Z':
                    break
        allSteps.append(steps)
    return math.lcm(*allSteps)

puzzle(8, part1, part2, False, False).run()
