import math
import resource


def solve():
    file = resource.get_problem_context(99)
    numbers = []
    max_exp = 0
    max_base = [0, 0]
    for line in file:
        base, exp = line.split(',')
        numbers.append([int(base), int(exp), 0])
        if int(exp) > max_exp:
            max_exp = int(exp)

    for n in range(len(numbers)):
        numbers[n][2] = math.pow(numbers[n][0], numbers[n][1] / max_exp)
        if numbers[n][2] > max_base[1]:
            max_base = n + 1, numbers[n][2]

    return max_base[0]
