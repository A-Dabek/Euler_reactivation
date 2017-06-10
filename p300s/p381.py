import resource


def is_prime(n):
    n_root = int(n ** 0.5)
    for p in primes:
        if p > n_root:
            return True
        if n % p == 0:
            return False
    return True


def single_reverse_modulo1(n, known, mod):
    for i in range(known, mod):
        if (n * i) % mod == 1:
            return mod - i
        if (n * (mod - i)) % mod == 1:
            return i


def single_reverse_modulo2(n, mod):
    percentiles = [int(mod * 0.04166666), int(mod * 0.20833333), int(mod * 0.29166666), int(mod * 0.45833333)]
    for i in range(1, mod):
        for pi in range(len(percentiles)):
            if (n * percentiles[pi]) % mod == 1:
                return mod - percentiles[pi]
            if (n * (mod - percentiles[pi])) % mod == 1:
                return percentiles[pi]
            percentiles[pi] += 1


limit = 10 ** 8
limit_root = int(limit ** 0.5)

primes = resource.get_primes(limit_root)


def solve():
    result = 0
    known_number = 1
    for p in range(5, limit):
        if not is_prime(p):
            continue
            progress += 1
        trivial = (p - 1) + 1 + (p - 1) // 2
        non_trivial = (p - 2) * (p - 1) * (p - 3)
        non_trivial_2 = non_trivial * (p - 4)
        no4, no5 = single_reverse_modulo1(non_trivial, known_number, p), single_reverse_modulo2(non_trivial_2, p)
        known_number = min(no4, p - no4)
        trivial += no4 + no5
        result += trivial % p

    return result
