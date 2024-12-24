from .boilerPlate2024 import puzzle

def part1(s: str):
    start, gates = s.split('\n\n')
    wires = {}
    for line in start.splitlines():
        w, v = line.split(': ')
        wires[w] = int(v)
    gi, gs = {}, []
    q = []
    for gate in gates.splitlines():
        x = gate.split(' ')
        curi = len(gs)
        if gi.get(x[0]) is None:
            gi[x[0]] = [curi]
        else:
            gi[x[0]].append(curi)
        if gi.get(x[2]) is None:
            gi[x[2]] = [curi]
        else:
            gi[x[2]].append(curi)
        gs.append((x[0], x[2], x[1], x[4]))
        if (x[0].startswith('x') or x[0].startswith('y')) and (x[2].startswith('x') or x[2].startswith('y')):
            q.append(curi)
    while len(q) > 0:
        n = q.pop(0)
        v1, v2, opp, tar = gs[n]
        if opp == 'AND':
            wires[tar] = wires[v1] & wires[v2]
        elif opp == 'OR':
            wires[tar] = wires[v1] | wires[v2]
        elif opp == 'XOR':
            wires[tar] = wires[v1] ^ wires[v2]
        if gi.get(tar) is not None:
            for ng in gi[tar]:
                tmp = gs[ng]
                if (tmp[0] == tar and wires.get(tmp[1]) is not None) or (tmp[1] == tar and wires.get(tmp[0]) is not None):
                    q.append(ng)
    result = 0
    for wire, v in wires.items():
        if wire.startswith('z'):
            bs = int(wire[1:3])
            result += v << bs
    print(bin(result))
    return result

def part2(s: str):
    start, gates = s.split('\n\n')
    wires = {}
    for line in start.splitlines():
        w, v = line.split(': ')
        wires[w] = int(v)
    vx, vy = 0, 0
    for wire, v in wires.items():
        if wire.startswith('x'):
            bs = int(wire[1:3])
            vx += v << bs
        if wire.startswith('y'):
            bs = int(wire[1:3])
            vy += v << bs
    target = vx + vy
    gi, gs = {}, []
    q = []
    for gate in gates.splitlines():
        x = gate.split(' ')
        curi = len(gs)
        if gi.get(x[0]) is None:
            gi[x[0]] = [curi]
        else:
            gi[x[0]].append(curi)
        if gi.get(x[2]) is None:
            gi[x[2]] = [curi]
        else:
            gi[x[2]].append(curi)
        gs.append((x[0], x[2], x[1], x[4]))
        if (x[0].startswith('x') or x[0].startswith('y')) and (x[2].startswith('x') or x[2].startswith('y')):
            q.append(curi)

    def find(x, y, opp):
        for gate in gs:
            if ((gate[0] == x and gate[1] == y) or (gate[1] == x and gate[0] == y)) and gate[2] == opp:
                return gate[3]
        return None


    swapped = []
    c0 = None
    for i in range(45):
        n = str(i).zfill(2)
        m1 = find('x' + n, 'y' + n, 'XOR')
        n1 = find('x' + n, 'y' + n, 'AND')
        c1, z1 = '', ''

        if c0 is not None:
            r1 = find(c0, m1, 'AND')
            if r1 is None:
                n1, m1 = m1, n1
                swapped.append(n1)
                swapped.append(m1)
                r1 = find(c0, m1, 'AND')
            z1 = find(c0, m1, 'XOR')
            if m1 is not None and m1.startswith('z'):
                m1, z1 = z1, m1
                swapped.append(z1)
                swapped.append(m1)
            if n1 is not None and n1.startswith('z'):
                n1, z1 = z1, n1
                swapped.append(z1)
                swapped.append(n1)
            if r1 is not None and r1.startswith('z'):
                r1, z1 = z1, r1
                swapped.append(z1)
                swapped.append(r1)
            c1 = find(r1, n1, 'OR')

        if c1 is not None and c1.startswith('z') and c1 != 'z45':
            c1, z1 = z1, c1
            swapped.append(z1)
            swapped.append(c1)

        if c0 is not None:
            c0 = c1
        else:
            c0 = n1

    return ','.join(sorted(swapped))

puzzle(24, part1, part2, False, False).run()

