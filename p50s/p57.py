from fractions import Fraction
import math


def iter_run(in_frac):
    out_frac = 1 + 1 / (1 + in_frac)
    return out_frac


def solve():
    start = 1 + Fraction(1, 2)
    how_many = 0

    for i in range(1000):
        start = iter_run(start)
        if int(math.log(start.numerator, 10)) > int(math.log(start.denominator, 10)):
            how_many += 1
    return how_many