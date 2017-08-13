import resource


def is_prime(n):
    if n < 2:
        return False
    if n < 4:
        return True
    root = int(n ** 0.5)
    index = 0
    while index < len(primes) and primes[index] <= root:
        if n % primes[index] == 0:
            return False
        index += 1
    if index == len(primes):
        index = primes[-1] + 2
        while index <= root:
            if n % index == 0:
                return False
            index += 2
    return True


limit = 10000
primes = resource.get_primes(limit)
connects = {}


def check_concat_prime(a, b):
    connect_prime = int(str(a) + str(b))
    if not is_prime(connect_prime):
        return True
    connect_prime = int(str(b) + str(a))
    if not is_prime(connect_prime):
        return True
    return False


def solve():
    for p in primes:
        connects[p] = {p}

    for aaa in range(0, len(primes)):
        k1 = primes[aaa]
        for aab in range(aaa + 1, len(primes)):
            k2 = primes[aab]
            if check_concat_prime(k1, k2):
                continue
            for aac in range(aab + 1, len(primes)):
                k3 = primes[aac]
                if check_concat_prime(k2, k3):
                    continue
                if check_concat_prime(k1, k3):
                    continue
                for aad in range(aac + 1, len(primes)):
                    k4 = primes[aad]
                    if check_concat_prime(k4, k1):
                        continue
                    if check_concat_prime(k4, k2):
                        continue
                    if check_concat_prime(k4, k3):
                        continue
                    for aae in range(aad + 1, len(primes)):
                        k5 = primes[aae]
                        if check_concat_prime(k5, k1):
                            continue
                        if check_concat_prime(k5, k2):
                            continue
                        if check_concat_prime(k5, k3):
                            continue
                        if check_concat_prime(k5, k4):
                            continue
                        return k1+k2+k3+k4+k5
