import math


def is_prime(number):
    if number % 2 == 0:
        return False
    for i in range(3, int(number**0.5) + 1, 2):
        if number % i == 0:
            return False
    return True


def number_to_digits(number):
    number = str(number)
    digits = [letter for letter in number]
    return digits


def swap_digits(dig_list, vector, to_digit):
    temp = list(dig_list)
    digit_order = 2
    while vector > 0:
        if vector % 2 == 1:
            temp[-digit_order] = to_digit
        vector //= 2
        digit_order += 1
    temp = [str(i) for i in temp]
    return int(''.join(temp))


def solve():
    start = 56001
    current = start
    while True:
        current += 2
        if not is_prime(current):
            continue
        order = int(math.ceil(math.log(current, 10))) - 1
        current_digits = number_to_digits(current)
        for i in range(1, 2 ** order):
            family_members = 0
            family = []
            for digit in range(10):
                sibling = swap_digits(current_digits, i, digit)
                if sibling >= current and is_prime(sibling):
                    family_members += 1
                    family.append(sibling)
            if family_members > 7:
                return min(family)
