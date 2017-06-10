import resource


def solve():
    upper_limit = 50000000
    primes = resource.get_primes(upper_limit)  # erato_primes(2000000)
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
                results.add(i + j + k)
    return len(results)
