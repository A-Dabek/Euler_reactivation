from resource import get_primes
from math import log10

limit = 10 ** 7
primes = list(filter(lambda x: x > limit, get_primes(2 * limit)))

#   ---  0
# 1 | | 2
#   ---  3
# 4 | | 5
#   ---  6
digits = [
    (0b1110111, 6),  # 0
    (0b0010010, 2),  # 1
    (0b1011101, 5),  # 2
    (0b1011011, 5),  # 3
    (0b0111010, 4),  # 4
    (0b1101011, 5),  # 5
    (0b1101111, 6),  # 6
    (0b1110010, 4),  # 7
    (0b1111111, 7),  # 8
    (0b1111011, 6),  # 9
    (0b0000000, 0)  # empty
]
empty = 10

sam_dict = {}
max_dict = {}


def sum_up(number):
    text = str(number)
    total = 0
    for c in text:
        total += int(c)
    return total


def max_way(prime):
    transitions = 0
    text = str(prime)
    for c in text:
        transitions += digits[int(c)][1]
    while True:
        if prime < 10:
            transitions += digits[prime][1]
            break
        summed_prime = sum_up(prime)
        digits_gone = int(log10(prime)) - int(log10(summed_prime))
        for c in text[:digits_gone]:
            transitions += digits[int(c)][1]
        new_text = str(summed_prime)
        for c, sc in zip(text[digits_gone:], new_text):
            xor = digits[int(c)][0] ^ digits[int(sc)][0]
            xor_text = bin(xor)[-7:]
            ones = 0
            for b in xor_text:
                if b == '1':
                    ones += 1
            transitions += ones
        prime = summed_prime
        text = new_text
    return transitions


def sam_way(prime):
    transitions = 0
    while True:
        text = str(prime)
        for c in text:
            transitions += digits[int(c)][1] * 2
        if prime < 10:
            break
        prime = sum_up(prime)
    return transitions


def solve():
    total = 0
    for p in primes:
        total += sam_way(p) - max_way(p)
    return total
