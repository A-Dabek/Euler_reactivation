from fractions import Fraction


def partial(ind):
    if ind % 3 == 2:
        return 2 * (ind//3 + 1)
    return 1


def bottom_to_top(frac, level):
    frac = 1 / frac
    if level == 0:
        return frac
    frac = (partial(level) + frac)
    return bottom_to_top(frac, level-1)


def solve():
    start = Fraction(2, 1)
    index = 100-2

    result = start + bottom_to_top(Fraction(partial(index+1), 1), index)
    sum_digits = 0
    numerator = result.numerator
    while numerator > 0:
        sum_digits += numerator % 10
        numerator //= 10
    return sum_digits
