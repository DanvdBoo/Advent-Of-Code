from sympy import var, Eq, solve
from .boilerPlate2023 import puzzle

def part1(s: str):
    MIN = 200000000000000
    MAX = 400000000000000

    hail = [[int(num) for num in line.replace(' @', ',').split(', ')] for line in s.splitlines()]
    intersections = 0
    for i in range(len(hail) - 1):
        for j in range(i + 1, len(hail)):
            x1,y1,_,vx1,vy1,_ = hail[i]
            x2,y2,_,vx2,vy2,_ = hail[j]

            m1 = vy1/vx1
            m2 = vy2/vx2
            if m1 == m2:
                continue

            x = (m2 * x2 - (m1 * x1) + y1 - y2)/(m2 - m1)
            if not (MIN <= x <= MAX):
                continue
            t1 = (x - x1)/vx1
            t2 = (x - x2)/vx2
            y = t1 * vy1 + y1
            if not (MIN <= y <= MAX):
                continue
            if t1 < 0 or t2 < 0:
                continue
            intersections += 1
    return intersections

def part2(s):
    particles = []

    sx = var("sx")
    sy = var("sy")
    sz = var("sz")

    vx = var("vx")
    vy = var("vy")
    vz = var("vz")

    eq = []

    for l in s.splitlines():
        p = l.split(" @ ")
        ps = list(map(int, p[0].split(", ")))
        vs = list(map(int, p[1].split(", ")))

        particles.append((ps, vs))

        ts = "t{}".format(len(eq) // 3)
        exec(f'{ts} = var("{ts}")')

        eq.append(Eq(eval(f"sx + vx * {ts}"), eval(f"ps[0] + vs[0] * {ts}")))
        eq.append(Eq(eval(f"sy + vy * {ts}"), eval(f"ps[1] + vs[1] * {ts}")))
        eq.append(Eq(eval(f"sz + vz * {ts}"), eval(f"ps[2] + vs[2] * {ts}")))

        if len(eq) > 9:
            break

    ans = solve(eq)[0]
    return(ans[sx] + ans[sy] + ans[sz])


puzzle(24, part1, part2, False, True).run()
