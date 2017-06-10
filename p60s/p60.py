import time


def binary_check(n):
    l = 0
    r = len(primes) - 1
    while l < r:
        m = (l + r) // 2
        if primes[m] > n:
            r = m + 1
        elif primes[m] < n:
            l = m - 1
        else:
            return True
    return False


def check_concat(a, b):
    right = int(str(b) + str(a))
    left = int(str(a) + str(b))
    if not binary_check(left) or not binary_check(right):
        return False
    return True

TIMESTAMP = time.time()

limit = 10
primes = []
file_prime = open('../res/primes.txt')
line = int(file_prime.readline())
while line < limit:
    primes.append(line)
    line = int(file_prime.readline())

print(primes)

connects = {}
for pi in range(len(primes)):
    for pj in range(pi+1, len(primes)):
        if check_concat(primes[pi], primes[pj]):
            if connects.get(primes[pi], None) is None:
                connects[primes[pi]] = [primes[pj]]
            else:
                connects[primes[pi]].append(primes[pj])

for k, v in connects.items():
    print(k, v)

print(time.time() - TIMESTAMP)
