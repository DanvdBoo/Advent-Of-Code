from .boilerPlate2023 import puzzle

def indexFromType(typeNum: int, jokers: int = 0):
    if typeNum == 3125: # Five of a Kind
        return 6
    elif typeNum == 256: # Four of a Kind
        return 5 if jokers == 0 else 6
    elif typeNum == 108: # Full house
        return 4
    elif typeNum == 27: # Three of a Kind
        return 3 if jokers == 0 else (5 if jokers == 1 else 6)
    elif typeNum == 16: # Two Pair
        return 2 if jokers == 0 else 4
    elif typeNum == 4: # Pair
        return 1 if jokers == 0 else (3 if jokers == 1 else (5 if jokers == 2 else 6))
    else: # High Card
        return 0 if jokers == 0 else (1 if jokers == 1 else (3 if jokers == 2 else (5 if jokers == 3 else 6)))

def stringValue(input: str, joker: bool = False):
    returnValue = 0
    for i, char in enumerate(input):
        num = 0
        if char == 'A':
            num = 14
        elif char == 'K':
            num = 13
        elif char == 'Q':
            num = 12
        elif char == 'J':
            num = 1 if joker else 11
        elif char == 'T':
            num = 10
        else:
            num = int(char)
        returnValue += num * (100 ** (5 - i))
    return returnValue

def part1(s: str):
    handTypes = [[], [], [], [], [], [], []]
    for line in s.splitlines():
        hand = line.split()
        handType = 1
        for char in hand[0]:
            handType *= hand[0].count(char)
        handTypes[indexFromType(handType)].append((hand[0], hand[1]))
    currentRank = 1
    result = 0
    for handType in handTypes:
        sortedHandType = sorted(handType, key=lambda x: stringValue(x[0]))
        for hand in sortedHandType:
            result += int(hand[1]) * currentRank
            currentRank += 1
    return result

def part2(s: str):
    handTypes = [[], [], [], [], [], [], []]
    for line in s.splitlines():
        hand = line.split()
        handType = 1
        jokers = hand[0].count('J')
        for char in hand[0]:
            if char == 'J':
                continue
            handType *= hand[0].count(char)
        handTypes[indexFromType(handType, jokers)].append((hand[0], hand[1]))
    currentRank = 1
    result = 0
    for handType in handTypes:
        sortedHandType = sorted(handType, key=lambda x: stringValue(x[0], True))
        for hand in sortedHandType:
            result += int(hand[1]) * currentRank
            currentRank += 1
    return result

puzzle(7, part1, part2, False, False).run()
