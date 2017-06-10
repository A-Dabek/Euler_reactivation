import random
import resource


def value_of_order(order):
    global matrix
    total = 0
    for i in range(len(order)):
        total += matrix[i][order[i]]
    return total


def swap(order):
    global max_val, random_order
    temp = value_of_order(order)
    ind1, ind2 = random.randint(0, len(order) - 1), random.randint(0, len(order) - 1)
    order[ind1], order[ind2] = order[ind2], order[ind1]
    if value_of_order(order) < temp:
        order[ind1], order[ind2] = order[ind2], order[ind1]
    else:
        if temp > max_val:
            max_val = temp


def solve():
    global max_val, random_order, matrix
    max_val = 0
    file = resource.get_problem_context(345)
    matrix = []
    for line in file:
        numbers = [int(i) for i in line.replace('\n', ' ').split(' ') if i != '']
        matrix.append(numbers)

    random_order = [list(range(15)) for _ in range(100)]
    for r in random_order:
        random.shuffle(r)
    tries = 10 ** 3
    i = 0
    while i <= tries:
        i += 1
        for r in random_order:
            swap(r)
    return max_val
