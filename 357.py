import numpy as np
import math


def sieveOfAtkin(limit):
    P = np.zeros((int(1.26 * limit / (math.log(limit))),))
    P[0] = 2
    P[1] = 3
    p_size = 2
    sieve = np.zeros((limit + 1,), dtype=bool)
    for x in range(1, int(math.sqrt(limit)) + 1):
        for y in range(1, int(math.sqrt(limit)) + 1):
            n = 4 * x ** 2 + y ** 2
            if n <= limit and (n % 12 == 1 or n % 12 == 5):
                sieve[n] = not sieve[n]
            n = 3 * x ** 2 + y ** 2
            if n <= limit and n % 12 == 7:
                sieve[n] = not sieve[n]
            n = 3 * x ** 2 - y ** 2
            if x > y and n <= limit and n % 12 == 11:
                sieve[n] = not sieve[n]
    for x in range(5, int(math.sqrt(limit))):
        if sieve[x]:
            for y in range(x ** 2, limit + 1, x ** 2):
                sieve[y] = False
    for p in range(5, limit):
        if sieve[p]:
            P[p_size] = p
            p_size += 1
    return P, p_size


limit = 1000000
sieve = np.zeros(shape=(limit + 2,))
sieve[1] = 1
sieve[0] = 0
primes, prime_size = sieveOfAtkin(limit)


def is_prime(n):
    index = np.searchsorted(primes[:prime_size], n)
    return n == primes[index]


del sieve

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

print(total_sum)
