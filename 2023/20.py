import math
from .boilerPlate2023 import puzzle
import json

def part1(s: str):
    nodes = {}
    for line in s.splitlines():
        splitted = line.split()
        name, targets = splitted[0], [t.replace(',', '') for t in splitted[2:]]
        if '%' in name:
            nodes[name[1:]] = {"t": targets, "state": False}
        elif '&' in name:
            nodes[name[1:]] = {"t": targets, "hist": []}
        else:
            nodes[name] = {"t": targets}
    for key, node in nodes.items():
        if "hist" in node:
            for k, n in nodes.items():
                if key in n["t"]:
                    node["hist"].append((k, 0))
    history = {}
    history[json.dumps(nodes)] = (0, 0, 0)
    for repeats in range(1000):
        countHigh, countLow = 0, 0
        signals = [("broadcaster", 0, "button")]
        while signals:
            t, sig, sender = signals.pop(0)
            if sig == 1:
                countHigh += 1
            else:
                countLow += 1
            if t in nodes:
                n = nodes[t]
                newSig = 0
                if "state" in n:
                    if sig == 0:
                        n["state"] = not n["state"]
                        newSig = int(n["state"])
                    else:
                        continue
                elif "hist" in n:
                    allHigh = True
                    for i, item in enumerate(n["hist"]):
                        if item[0] == sender:
                            n["hist"][i] = (sender, sig)
                            allHigh = allHigh & sig == 1
                        elif item[1] == 0:
                            allHigh = False
                    newSig = 0 if allHigh else 1
                for target in n["t"]:
                    signals.append((target, newSig, t))
        stringifiedDict = json.dumps(nodes)
        if stringifiedDict in history:
            print(history[stringifiedDict])
            print(repeats)
            return (countHigh * round(1000/(repeats + 1))) * (countLow * round(1000/(repeats + 1)))
        history[stringifiedDict] = (repeats + 1, countLow, countHigh)
    totalCountLow, totalCountHigh = 0, 0
    for _, (_, low, high) in history.items():
        totalCountLow += low
        totalCountHigh += high
    return totalCountLow * totalCountHigh

def part2(s: str):
    nodes = {}
    for line in s.splitlines():
        splitted = line.split()
        name, targets = splitted[0], [t.replace(',', '') for t in splitted[2:]]
        if '%' in name:
            nodes[name[1:]] = {"t": targets, "state": False}
        elif '&' in name:
            nodes[name[1:]] = {"t": targets, "hist": []}
        else:
            nodes[name] = {"t": targets}
    for key, node in nodes.items():
        if "hist" in node:
            for k, n in nodes.items():
                if key in n["t"]:
                    node["hist"].append((k, 0))
    repeats = [0, 0, 0, 0]
    count = 0
    while min(repeats) == 0:
        signals = [("broadcaster", 0, "button")]
        rxSigs = []
        while signals:
            t, sig, sender = signals.pop(0)
            if t in nodes:
                n = nodes[t]
                newSig = 0
                if "state" in n:
                    if sig == 0:
                        n["state"] = not n["state"]
                        newSig = int(n["state"])
                    else:
                        continue
                elif "hist" in n:
                    allHigh = True
                    for i, item in enumerate(n["hist"]):
                        if item[0] == sender:
                            n["hist"][i] = (sender, sig)
                            allHigh = allHigh & sig == 1
                        elif item[1] == 0:
                            allHigh = False
                    newSig = 0 if allHigh else 1
                for target in n["t"]:
                    signals.append((target, newSig, t))
                    if target == "hp" and newSig == 1:
                        if t == "sr":
                            repeats[0] = count + 1
                        elif t == "sn":
                            repeats[1] = count + 1
                        elif t == "rf":
                            repeats[2] = count + 1
                        elif t == "vq":
                            repeats[3] = count + 1
            elif t == "rx":
                rxSigs.append(sig)
        if len(rxSigs) == 1 and rxSigs[0] == 0:
            return repeats
        count += 1
    print(repeats)
    return math.lcm(*repeats)

puzzle(20, part1, part2, False, False).run()
