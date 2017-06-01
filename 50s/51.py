# find smallest prime that after replacing part of it, has 7 prime siblings
# smallest known to have 6 siblings is 56003
import math


def is_prime(number):
    if number < 4:
        return True
    for i in range(2, int(math.ceil(math.sqrt(number)) + 1)):
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


start = 56001
current = start
while True:
    current += 2
    order = int(math.ceil(math.log(current, 10))) - 1
    current_digits = number_to_digits(current)
    if not is_prime(current):
        continue
    # print(order, current)
    for i in range(1, 2 ** order):
        # print(bin(i))
        family_members = 0
        family = []
        for digit in range(10):
            sibling = swap_digits(current_digits, i, digit)
            # print(sibling, digit)
            if sibling >= current and is_prime(sibling):
                family_members += 1
                family.append(sibling)
                #print('found', family_members)
            #if (10 - i) < (6 - family_members):
            #    break
        if family_members > 6:
            print(current, family_members, family)
