import copy
from .boilerPlate2023 import puzzle

def part1(s: str):
    bricks = [[[int(x) for x in coord.split(',')] for coord in line.split('~')] for line in s.splitlines()]
    grid = [[[0 for _ in range(400)] for _ in range(10)] for _ in range(10)]
    maxHeight = 0
    for i, b in enumerate(bricks):
        x1, y1, z1 = b[0]
        x2, y2, z2 = b[1]
        if x1 != x2:
            for off in range(x2-x1 + 1):
                grid[x1 + off][y1][z1] = i + 1
        elif y1 != y2:
            for off in range(y2-y1 + 1):
                grid[x1][y1 + off][z1] = i + 1
        elif z1 != z2:
            for off in range(z2-z1 + 1):
                grid[x1][y1][z1 + off] = i + 1
        else:
            grid[x1][y1][z1] = i + 1
        maxHeight = max(maxHeight, z1, z2)
    downed = {10000: {"on": [], "below": []}}
    for x in range(10):
        for y in range(10):
            grid[x][y][0] = 10000
    for z in range(maxHeight + 1):
        b = []
        for x in range(10):
            for y in range(10):
                if grid[x][y][z] != 0 and grid[x][y][z] != 10000 and grid[x][y][z] not in b:
                    b.append(grid[x][y][z])
        for brick in b:
            if brick in downed:
                continue
            x1, y1, z1 = bricks[brick - 1][0]
            x2, y2, z2 = bricks[brick - 1][1]
            blocking = []
            while True:
                if z1 != z2:
                    if grid[x1][y1][min(z1, z2) - 1] == 0:
                        grid[x1][y1][max(z1, z2)] = 0
                        grid[x1][y1][min(z1, z2) - 1] = brick
                        z1 -= 1
                        z2 -= 1
                    else:
                        if brick not in downed[grid[x1][y1][min(z1, z2) - 1]]["below"]:
                            downed[grid[x1][y1][min(z1, z2) - 1]]["below"].append(brick)
                            blocking.append(grid[x1][y1][min(z1, z2) - 1])
                        break
                elif x1 != x2:
                    below = 0
                    for off in range(x2-x1 + 1):
                        if grid[x1 + off][y1][z1 - 1] != 0:
                            below += 1
                            if brick not in downed[grid[x1 + off][y1][z1 - 1]]["below"]:
                                downed[grid[x1 + off][y1][z1 - 1]]["below"].append(brick)
                                blocking.append(grid[x1 + off][y1][z1 - 1])
                    if below == 0:
                        for off in range(x2-x1 + 1):
                            grid[x1 + off][y1][z1] = 0
                            grid[x1 + off][y1][z1 - 1] = brick
                        z1 -= 1
                        z2 -= 1
                    else:
                        break
                elif y1 != y2:
                    below = 0
                    for off in range(y2-y1 + 1):
                        if grid[x1][y1 + off][z1 - 1] != 0:
                            below += 1
                            if brick not in downed[grid[x1][y1 + off][z1 - 1]]["below"]:
                                downed[grid[x1][y1 + off][z1 - 1]]["below"].append(brick)
                                blocking.append(grid[x1][y1 + off][z1 - 1])
                    if below == 0:
                        for off in range(y2-y1 + 1):
                            grid[x1][y1 + off][z1] = 0
                            grid[x1][y1 + off][z1 - 1] = brick
                        z1 -= 1
                        z2 -= 1
                    else:
                        break
                else:
                    if grid[x1][y1][z1 - 1] == 0:
                        grid[x1][y1][z1] = 0
                        grid[x1][y1][z1 - 1] = brick
                        z1 -= 1
                        z2 -= 1
                    else:
                        if brick not in downed[grid[x1][y1][z1 - 1]]["below"]:
                            downed[grid[x1][y1][z1 - 1]]["below"].append(brick)
                            blocking.append(grid[x1][y1][z1 - 1])
                        break
            downed[brick] = {"on": blocking, "below": []}
    result = 0
    for id, block in downed.items():
        if id == 10000:
            continue
        if len(block["below"]) == 0:
            result += 1
        else:
            for b in block["below"]:
                if len(downed[b]["on"]) == 1:
                    break
            else:
                result += 1
    return result

def part2(s: str):
    bricks = [[[int(x) for x in coord.split(',')] for coord in line.split('~')] for line in s.splitlines()]
    grid = [[[0 for _ in range(400)] for _ in range(10)] for _ in range(10)]
    maxHeight = 0
    for i, b in enumerate(bricks):
        x1, y1, z1 = b[0]
        x2, y2, z2 = b[1]
        if x1 != x2:
            for off in range(x2-x1 + 1):
                grid[x1 + off][y1][z1] = i + 1
        elif y1 != y2:
            for off in range(y2-y1 + 1):
                grid[x1][y1 + off][z1] = i + 1
        elif z1 != z2:
            for off in range(z2-z1 + 1):
                grid[x1][y1][z1 + off] = i + 1
        else:
            grid[x1][y1][z1] = i + 1
        maxHeight = max(maxHeight, z1, z2)
    downed = {10000: {"on": [], "below": []}}
    for x in range(10):
        for y in range(10):
            grid[x][y][0] = 10000
    for z in range(maxHeight + 1):
        b = []
        for x in range(10):
            for y in range(10):
                if grid[x][y][z] != 0 and grid[x][y][z] != 10000 and grid[x][y][z] not in b:
                    b.append(grid[x][y][z])
        for brick in b:
            if brick in downed:
                continue
            x1, y1, z1 = bricks[brick - 1][0]
            x2, y2, z2 = bricks[brick - 1][1]
            blocking = []
            while True:
                if z1 != z2:
                    if grid[x1][y1][min(z1, z2) - 1] == 0:
                        grid[x1][y1][max(z1, z2)] = 0
                        grid[x1][y1][min(z1, z2) - 1] = brick
                        z1 -= 1
                        z2 -= 1
                    else:
                        if brick not in downed[grid[x1][y1][min(z1, z2) - 1]]["below"]:
                            downed[grid[x1][y1][min(z1, z2) - 1]]["below"].append(brick)
                        if grid[x1][y1][min(z1, z2) - 1] not in blocking:
                            blocking.append(grid[x1][y1][min(z1, z2) - 1])
                        break
                elif x1 != x2:
                    below = 0
                    for off in range(x2-x1 + 1):
                        if grid[x1 + off][y1][z1 - 1] != 0:
                            below += 1
                            if brick not in downed[grid[x1 + off][y1][z1 - 1]]["below"]:
                                downed[grid[x1 + off][y1][z1 - 1]]["below"].append(brick)
                            if grid[x1 + off][y1][z1 - 1] not in blocking:
                                blocking.append(grid[x1 + off][y1][z1 - 1])
                    if below == 0:
                        for off in range(x2-x1 + 1):
                            grid[x1 + off][y1][z1] = 0
                            grid[x1 + off][y1][z1 - 1] = brick
                        z1 -= 1
                        z2 -= 1
                    else:
                        break
                elif y1 != y2:
                    below = 0
                    for off in range(y2-y1 + 1):
                        if grid[x1][y1 + off][z1 - 1] != 0:
                            below += 1
                            if brick not in downed[grid[x1][y1 + off][z1 - 1]]["below"]:
                                downed[grid[x1][y1 + off][z1 - 1]]["below"].append(brick)
                            if grid[x1][y1 + off][z1 - 1] not in blocking:
                                blocking.append(grid[x1][y1 + off][z1 - 1])
                    if below == 0:
                        for off in range(y2-y1 + 1):
                            grid[x1][y1 + off][z1] = 0
                            grid[x1][y1 + off][z1 - 1] = brick
                        z1 -= 1
                        z2 -= 1
                    else:
                        break
                else:
                    if grid[x1][y1][z1 - 1] == 0:
                        grid[x1][y1][z1] = 0
                        grid[x1][y1][z1 - 1] = brick
                        z1 -= 1
                        z2 -= 1
                    else:
                        if brick not in downed[grid[x1][y1][z1 - 1]]["below"]:
                            downed[grid[x1][y1][z1 - 1]]["below"].append(brick)
                        if grid[x1][y1][z1 - 1] not in blocking:
                            blocking.append(grid[x1][y1][z1 - 1])
                        break
            downed[brick] = {"on": blocking, "below": []}
    result = 0
    for id, block in downed.items():
        if id == 10000:
            continue
        if len(block["below"]) == 0:
            result += 0
        else:
            removed = [id]
            staying = []
            for b in block["below"]:
                for b2 in downed[b]["on"]:
                    if b2 not in staying and b2 != id:
                        staying.append(b2)
            q = copy.deepcopy(downed[id]["below"])
            while len(q) > 0:
                currentBlock = q.pop(0)
                if currentBlock in removed or currentBlock in staying:
                    continue
                shouldBeRemoved = True
                for dingsBooms in downed[currentBlock]["on"]:
                    if dingsBooms in staying:
                        shouldBeRemoved = False
                    elif dingsBooms not in removed:
                        shouldBeRemoved = False
                if shouldBeRemoved:
                    removed.append(currentBlock)
                    q.extend(copy.deepcopy(downed[currentBlock]["below"]))
                else:
                    staying.append(currentBlock)
            result += (len(removed) - 1) if len(removed) > 1 else 0
    return result

puzzle(22, part1, part2, False, False).run()
