from .boilerPlate2024 import puzzle

magic_n = 16777215

def part1(s: str):
    result = 0
    for line in s.splitlines():
        n = int(line)
        for _ in range(2000):
            n = n ^ ((n << 6) & magic_n)
            n = n ^ (n >> 5)
            n = n ^ ((n << 11) & magic_n)
        result += n
    return result

def part2(s: str):
    prices = {}
    for line in s.splitlines():
        n = int(line)
        d = n % 10
        seq = []
        seen = set()
        for _ in range(2000):
            n = n ^ ((n << 6) & magic_n)
            n = n ^ (n >> 5)
            n = n ^ ((n << 11) & magic_n)
            nd = n % 10
            diff = nd - d
            d = nd
            seq.append(diff)
            if len(seq) == 5:
                seq.pop(0)
            if len(seq) == 4:
                nseq = (seq[0], seq[1], seq[2], seq[3])
                if nseq in seen:
                    continue
                seen.add(nseq)
                if prices.get(nseq) is not None:
                    prices[nseq] += d
                else:
                    prices[nseq] = d
    result = 0
    for v in prices.values():
        if v > result:
            result = v
    return result

puzzle(22, part1, part2, False, False).run()
