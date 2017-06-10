import time
import numpy as np
import math


def get_problem_info(number):
    file = open('res/info.txt')
    txt = file.read()
    file.close()
    s = txt.find(str.format('Problem {}:', number))
    e = txt.find(str.format('Problem {}:', number + 1))
    d = txt[s:e]
    d = d.rstrip()
    return d
    pass


def get_primes(upper_limit):
    primes = []
    file = open('res/primes.txt')
    p = int(file.readline())
    try:
        while p < upper_limit:
            primes.append(p)
            p = int(file.readline())
    except ValueError:
        print('There is no that many primes')
    finally:
        file.close()
        return primes


def get_problem_context(number):
    file = open(str.format('res/{}.txt', number))
    data = file.readlines()
    file.close()
    return data


def measure_time(method, *args):
    t = time.time()
    r = method(*args)
    return time.time() - t, r


def atkin_sieve(limit):
    P = np.zeros((int(1.26 * limit / (math.log(limit))),))
    P[0] = 2
    P[1] = 3
    p_size = 2
    sieve = np.zeros((limit + 1,), dtype=bool)
    for x in range(1, int(limit ** 0.5) + 1):
        for y in range(1, int(limit ** 0.5) + 1):
            n = 4 * x ** 2 + y ** 2
            if n <= limit and (n % 12 == 1 or n % 12 == 5):
                sieve[n] = not sieve[n]
            n = 3 * x ** 2 + y ** 2
            if n <= limit and n % 12 == 7:
                sieve[n] = not sieve[n]
            n = 3 * x ** 2 - y ** 2
            if x > y and n <= limit and n % 12 == 11:
                sieve[n] = not sieve[n]
    for x in range(5, int(limit ** 0.5)):
        if sieve[x]:
            for y in range(x ** 2, limit + 1, x ** 2):
                sieve[y] = False
    for p in range(5, limit):
        if sieve[p]:
            P[p_size] = p
            p_size += 1
    return P, p_size
