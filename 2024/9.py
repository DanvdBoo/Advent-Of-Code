from .boilerPlate2024 import puzzle

def part1(s: str):
    files = dict()
    fbool = True
    idx = 0
    for char in s:
        if fbool:
            files[idx] = int(char)
            idx += 1
        fbool = not fbool
    zipped = []
    fbool = True
    idx2 = 0
    idx -= 1
    for char in s:
        if fbool:
            if idx == idx2:
                for _ in range(files[idx]):
                    zipped.append(idx)
                break
            for _ in range(int(char)):
                zipped.append(idx2)
            idx2 += 1
        else:
            gap = int(char)
            while gap > 0:
                zipped.append(idx)
                files[idx] -= 1
                if files[idx] == 0:
                    idx -= 1
                    if idx < idx2:
                        break
                gap -= 1
        if idx < idx2:
            break
        fbool = not fbool
    result = 0
    for i, v in enumerate(zipped):
        result += (i * v)
    return result

def part2(s: str):
    files = dict()
    sizes = dict()
    fbool = True
    idx = 0
    for char in s:
        if fbool:
            files[idx] = int(char)
            if sizes.get(int(char)) is None:
                sizes[int(char)] = [idx]
            else:
                sizes[int(char)].append(idx)
            idx += 1
        fbool = not fbool
    zipped = []
    fbool = True
    idx = 0
    for char in s:
        if fbool:
            for _ in range(int(char)):
                if files.get(idx) is None or files[idx] == 0:
                    zipped.append(0)
                else:
                    zipped.append(idx)
            idx += 1
        else:
            gap = int(char)
            while gap > 0:
                target = -1
                targetsize = -1
                for size, v in sizes.items():
                    if size > gap:
                        continue
                    if max(v) > target:
                        target = max(v)
                        targetsize = size

                if target == -1 or target < idx:
                    for _ in range(gap):
                        zipped.append(0)
                    break

                sizes[targetsize].remove(target)
                if sizes[targetsize] == []:
                    sizes.pop(targetsize)

                for _ in range(files[target]):
                    zipped.append(target)
                gap -= files[target]
                files.pop(target)
        fbool = not fbool
    result = 0
    for i, v in enumerate(zipped):
        result += (i * v)
    print(result)
    return result

puzzle(9, part1, part2, False, False).run()
