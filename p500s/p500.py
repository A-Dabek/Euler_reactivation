# The number of divisors of 120 is 16.
# In fact 120 is the smallest number having 16 divisors.
#
# Find the smallest number with 2**500500 divisors.
# Give your answer modulo 500500507.
import resource
import math

primes = resource.get_primes(10000000)
logs = [math.log(p, 2) for p in primes]


def solve():
    print('loaded')
    limit = 500500
    number = [[0, 1]]
    answer = 1
    progress = 0
    for div in range(limit):
        if div > progress * limit // 100:
            print(progress)
            progress += 1
        number[0][1] *= 2
        minimum = 0
        minimum_val = -1
        for pi in range(1, len(number)):
            temp = (number[0][1] // 2) - (number[pi][1] * logs[number[pi][0]])
            if temp > minimum:
                minimum = temp
                minimum_val = pi
            elif number[pi][1] == 2:
                break
        new_prime = primes[number[-1][0] + 1]
        temp = (number[0][1] // 2) - logs[number[-1][0] + 1]
        if temp > minimum:
            answer *= new_prime
            answer %= 500500507
            number.append([number[-1][0] + 1, 2])
            number[0][1] //= 2
        else:
            if minimum_val > 0:
                for _ in range(number[minimum_val][1]):
                    answer *= primes[number[minimum_val][0]]
                    answer %= 500500507
                number[minimum_val][1] *= 2
                number[0][1] //= 2
    for _ in range(number[0][1] - 1):
        answer *= 2
        answer %= 500500507
    print(answer)
    return 1
