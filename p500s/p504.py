def gcd(a, b):
    while b > 0:
        a, b = b, a % b
    return a


def pre_gcd(limit):
    mem = [[0 for _ in range(limit)] for _ in range(limit)]
    for a in range(limit):
        for b in range(limit):
            mem[a][b] = a * b - gcd(a, b)
    return mem


def solve():
    m = 100  # 862 / 5582 / 19281 / 45655 / 88013
    gcds = pre_gcd(m+1)
    count = 0
    for a in range(1, m + 1):
        for b in range(1, a+1):
            for c in range(1, a+1):
                for d in range(1, b+1):
                    lattice = (gcds[a][b] + gcds[b][c] + gcds[c][d] + gcds[a][d]) / 2 + 1
                    if (lattice ** 0.5) % 1 == 0:
                        add_up = 1
                        if a != b:
                            add_up *= 2
                        if a != c:
                            add_up *= 2
                        if b != d:
                            add_up *= 2
                        count += add_up
    return count
