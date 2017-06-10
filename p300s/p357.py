import numpy as np
import resource


limit = 100000000
primes, prime_size = resource.atkin_sieve(limit)


def is_prime(n):
    index = np.searchsorted(primes[:prime_size], n)
    return n == primes[index]


def solve():
    progress = 0
    i = 2
    total_sum = 1
    while i <= limit:
        if i > progress * 100000:
            print(i)
            progress += 1
        match = True
        if is_prime(i + 1) and is_prime(i / 2 + 2):
            root = int(i ** 0.5)
            j = 3
            while j <= root:
                if i % j == 0 and not is_prime(i / j + j):
                    match = False
                    break
                j += 1
            if match:
                total_sum += i
        i += 4
    return total_sum
