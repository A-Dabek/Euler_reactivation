# The largest integer ≤ 100 that is only divisible by both the primes 2 and 3 is 96, as 96=32*3=25*3. For two
# distinct primes p and q let M(p,q,N) be the largest positive integer ≤N only divisible by both p and q and M(p,q,
# N)=0 if such a positive integer does not exist.
#
# E.g. M(2,3,100)=96.
# M(3,5,100)=75 and not 90 because 90 is divisible by 2 ,3 and 5.
# Also M(2,73,100)=0 because there does not exist a positive integer ≤ 100 that is divisible by both 2 and 73.
#
# Let S(N) be the sum of all distinct M(p,q,N). S(100)=2262.
#
# Find S(10 000 000).
import time


TIMESTAMP = time.time()
limit = 10**7  # 2262 / 193408 / 16373230 / 1414000891 /
file_prime = open('../res/primes.txt')

primes = []
results = []

line = int(file_prime.readline())
while line < limit//2:
    primes.append(line)
    line = int(file_prime.readline())

total = 0
for p_i in range(len(primes)):
    if primes[p_i]**2 > limit:
        break
    for q_i in range(p_i+1, len(primes)):
        p, q = primes[p_i], primes[q_i]
        power_p = p
        power_q = q
        max_product = 0
        while power_p * power_q <= limit:
            while power_p * power_q <= limit:
                if power_p * power_q > max_product:
                    max_product = power_q * power_p
                power_q *= q
            power_q = q
            power_p *= p
        if max_product > 0:
            total += max_product

print(total)
print(time.time() - TIMESTAMP)