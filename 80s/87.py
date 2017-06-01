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

upper_limit = 50000000
primes = erato_primes(2000000)
squares = []
cubes = []
fourths = []
temp = 0
index = 0
count_s = True
count_c = True
count_f = True
while index < len(primes) and (count_c or count_f or count_s):
    temp = primes[index]
    if count_s:
        temp *= primes[index]
        if temp >= upper_limit:
            count_s = False
        else:
            squares.append(temp)
    if count_c:
        temp *= primes[index]
        if temp >= upper_limit:
            count_c = False
        else:
            cubes.append(temp)
    if count_f:
        temp *= primes[index]
        if temp >= upper_limit:
            count_f = False
        else:
            fourths.append(temp)
    index += 1

how_many = 0
results = set()
for i in squares:
    for j in cubes:
        temp = i + j
        if temp > upper_limit:
            break
        for k in fourths:
            temp = i + j + k
            if temp > upper_limit:
                break
            how_many += 1
            results.add(i+j+k)
print(how_many, len(results))


