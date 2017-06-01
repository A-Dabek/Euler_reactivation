import math


def is_prime(n):
    global primes
    if n > max_prime:
        for i in range(2, int(math.sqrt(n))+1):
            if n % i == 0:
                return False
        return True
    if n in primes:
        return True
    return False


def erato_primes(n):
    divisors = [0 for _ in range(n)]
    divisors[0] = 1
    divisors[1] = 1
    divisors[2] = 1
    primes = set()
    for i in range(2, n):
        for j in range(i * 2, n, i):
            divisors[j] = 1
        if divisors[i] == 0:
            primes.add(i)
    return primes


def check_concat(a, b):
    right = int(str(b) + str(a))
    left = int(str(a) + str(b))
    if not is_prime(left) or not is_prime(right):
        return False
    return True


def check_family_bonds(family, related):
    if len(related) == 5:
        return related
    answer = list(related)
    for mem in family:
        if connects.get(mem, None) is None:
            answer = list(related) + [mem]
            continue
        intersect = set(connects[mem]).intersection(set(family))
        if len(intersect) > 0:
            for sub_mem in intersect:
                answer = check_family_bonds(intersect, related + [mem])
                if len(answer) == 5:
                    return answer
        else:
            return related + [mem]
    return answer


max_prime = 100000
primes = sorted(erato_primes(max_prime))
max_prime = primes[-1]
print('primes generated')
connects = {}
for pi in range(len(primes)):
    for pj in range(pi+1, len(primes)):
        if check_concat(primes[pi], primes[pj]):
            if connects.get(primes[pi], None) is None:
                connects[primes[pi]] = [primes[pj]]
            else:
                connects[primes[pi]].append(primes[pj])
print('connections generated')
for k, v in connects.items():
    print(k, v)

print(check_family_bonds(connects[3], [3]))
