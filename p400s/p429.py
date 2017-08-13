from resource import get_primes

limit = 100000000
modulo = 1000000009


def solve():
    primes = get_primes(limit + 1)
    occurences = [0 for _ in range(limit + 1)]
    occurences[1] = 1
    for p in primes:
        div = p
        while limit >= div:
            occurences[p] += limit // div
            div *= p
        occurences[p] = p ** occurences[p] % modulo
    total = 1
    for occ in occurences[2:]:
        if occ == 0:
            continue
        total *= (1 + occ**2)
        total %= modulo
    return total
