import math
import numpy as np
limit = 10**10
size = int(1.26*(limit+1)/math.log(limit+1))
print('array size', size)
primes = np.zeros((size, ), dtype=np.uint64)
file = open('res/primes.txt', mode='r')

line = file.readline().replace('\n', '')
primes_known = 0
while len(line) > 0:
    prime = int(line)
    primes[primes_known] = prime
    primes_known += 1
    line = file.readline().replace('\n', '')

print('max found', primes[primes_known-1])
file.close()

file = open('res/primes.txt', mode='a')


def is_prime(n):
    global primes_known
    root = int(n ** 0.5)
    p_at = 0
    while primes[p_at] <= root:
        if n % primes[p_at] == 0:
            return False
        p_at += 1
    primes[primes_known] = n
    primes_known += 1
    return True


for i in range(primes[primes_known-1] + 1, limit):
    if is_prime(i):
        file.write(str(i) + '\n')
file.close()
