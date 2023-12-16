from .boilerPlate2023 import puzzle

def part1(s: str):
    def hash(input: str):
        result = 0
        for char in input:
            result += ord(char)
            result *= 17
            result %= 256
        return result
    
    result = 0
    for string in s.replace('\n', '').split(','):
        result += hash(string)
    return result

def part2(s: str):
    def hash(input: str):
        result = 0
        for char in input:
            result += ord(char)
            result *= 17
            result %= 256
        return result
    
    boxes = [[] for _ in range(256)]
    for string in s.replace('\n', '').split(','):
        part = string.partition('=')
        if not part[1]:
            part = string.partition('-')
        boxNum = hash(part[0])
        replaced = False
        for index, box in enumerate(boxes[boxNum]):
            if box[0] == part[0]:
                boxes[boxNum].pop(index)
                if part[1] == '=':
                    replaced = True
                    boxes[boxNum].insert(index, (part[0], int(part[2])))
        if not replaced and part[1] == '=':
            boxes[boxNum].append((part[0], int(part[2])))
    
    result = 0
    for index, box in enumerate(boxes):
        for slotIndex, slot in enumerate(box):
            result += (index + 1) * (slotIndex + 1) * slot[1]
    return result

puzzle(15, part1, part2, False, False).run()
