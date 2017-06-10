def erato_primes(n):
    divisors = [0 for _ in range(n)]
    divisors[0] = 1
    divisors[1] = 1
    divisors[2] = 0
    primes = []
    for i in range(2, n):
        for j in range(i * 2, n, i):
            divisors[j] = 1
        if divisors[i] == 0:
            primes.append(i)
    return primes

primes = erato_primes(1000)

s_value = 71
target = s_value
ways = [0] * (target+1)
ways[0] = 1

for i in range(0, len(primes)):
    for j in range(primes[i], target+1):
        ways[j] += ways[j-primes[i]]
print(ways[-1])