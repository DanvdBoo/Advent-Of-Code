import regex as re
import functools
from .boilerPlate2023 import puzzle

def part1(s: str):
    return part2(s, 1)

_reDot = re.compile(r'[^\.]')
_reHash = re.compile(r'[^\#]')
_reQuest = re.compile(r'[^\?]')

def part2(s: str, x: int = 5):
    @functools.cache
    def search(springs: str, control: str):
        if springs == '':
            return 1 if control == '' else 0
        if control == '':
            return 1 if '#' not in springs else 0

        if springs[0] == '.':
            noDotMatch = _reDot.search(springs[1::])
            if not noDotMatch:
                return 0
            return search(springs[noDotMatch.start() + 1::], control)

        controlNum = int(control.split(',')[0])
        if controlNum > len(springs):
            return 0

        if springs[0] == '#':
            noHashMatch = _reHash.search(springs[1::])
            if not noHashMatch:
                return 1 if len(springs) == controlNum and control.partition(',')[2] == '' else 0
            elif noHashMatch.start() + 1 > controlNum:
                return 0
            elif noHashMatch.start() + 1 == controlNum == springs.find('.'):
                return search(springs[controlNum + 1::], control.partition(',')[2])
            else:
                if '.' in springs[0:controlNum]:
                    return 0
                else:
                    if len(springs) == controlNum:
                        return 1 if control.partition(',')[2] == '' else 0
                    return search(springs[controlNum + 1::], control.partition(',')[2]) if springs[controlNum] != '#' else 0
        
        res = 0
        if springs[0] == '?':
            noQuestMatch = _reQuest.search(springs[1::])
            if not noQuestMatch:
                if sum([int(num) + 1 for num in control.split(',')]) - 1 > len(springs):
                    return 0
                res += search(springs[controlNum + 1::], control.partition(',')[2])
            elif noQuestMatch.start() + 1 > controlNum:
                res += search(springs[controlNum + 1::], control.partition(',')[2])
            elif noQuestMatch.start() + 1 == controlNum:
                if springs[controlNum] != '#':
                    res += search(springs[controlNum + 1::], control.partition(',')[2])
            elif noQuestMatch.start() + 1 < controlNum:
                if '.' in springs[0:controlNum]:
                    part = springs.partition('.')
                    if '#' in part[0]:
                        return 0
                    return search(part[2], control)
                else:
                    if len(springs) == controlNum:
                        res += 1 if control.partition(',')[2] == '' else 0
                    else:
                        res += search(springs[controlNum + 1::], control.partition(',')[2]) if springs[controlNum] != '#' else 0
            res += search(springs[1::], control)
        return res

    result = 0
    for line in s.splitlines():
        springs = ((line.split()[0] + '?') * x)[:-1]
        control = ((line.split()[1] + ',') * x)[:-1]
        tmp = search(springs, control)

        result += tmp
    return result

puzzle(12, part1, part2, False, False).run()
