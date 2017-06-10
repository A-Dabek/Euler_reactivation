import time
import resource


def minimal_factorial(divisor, reps):
    start_number = divisor * reps
    fits = reps
    pre_fits = fits
    pre_number = start_number
    while fits >= reps:
        power = divisor
        pre_fits = fits
        fits = 0
        while power <= start_number:
            fits += start_number // power
            power *= divisor
        pre_number = start_number
        start_number -= divisor
    return pre_number + divisor, pre_fits


def is_prime(n):
    root = int(n ** 0.5)
    index = 0
    prime_divisor = primes[index]
    while prime_divisor <= root and index < len(primes) - 1:
        if n % prime_divisor == 0:
            return False
        index += 1
        prime_divisor = primes[index]
    return True


TIMESTAMP = time.time()

limit = 10 ** 8  # 136817 / 10125843 / 793183093
limit_root = int(limit ** 0.5)
primes = resource.get_primes(limit_root + 10)

factorial_sieve = [0] * (limit + 1)
factorial_sieve[0] = 0
factorial_sieve[1] = 0


def solve():
    for i in range(2, limit):
        if not is_prime(i):
            continue
        factorial_sieve[i] = i
        powered = i
        log_of_powered = 1
        value_factorial, how_many_can_fit = minimal_factorial(i, log_of_powered)
        while powered <= limit:
            for j in range(powered, limit + 1, powered):
                if value_factorial > factorial_sieve[j]:
                    factorial_sieve[j] = value_factorial
            powered *= i
            log_of_powered += 1
            if log_of_powered > how_many_can_fit:
                value_factorial, how_many_can_fit = minimal_factorial(i, log_of_powered)

    return sum(factorial_sieve)
