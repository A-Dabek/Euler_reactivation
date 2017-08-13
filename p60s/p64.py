from math import gcd

limit = 10000


def go_deeper(num, sqrt, min, den):
    min = abs(min)
    new_denom = num - min ** 2
    frac_gcd = gcd(den, new_denom)
    den //= frac_gcd
    new_denom //= frac_gcd
    min = den * min
    new_min = 0
    while min >= - sqrt:
        min -= new_denom
        new_min += 1
    return new_min - 1, min + new_denom, new_denom


def solve():
    total = 0
    for i in range(1, limit + 1):
        root = i ** 0.5
        if root % 1 == 0:
            continue
        root = int(root)
        minus, denom = root, 1
        count = 0
        while True:
            sol, minus, denom = go_deeper(i, root, minus, denom)
            count += 1
            if sol >= root * 2:
                if count % 2 == 1:
                    total += 1
                break
    return total
