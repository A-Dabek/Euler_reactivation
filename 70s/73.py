from fractions import Fraction


limit = 12000
how_many = 0
naive_many = 0
half = Fraction(1, 2)
third = Fraction(1, 3)
hundreds = 0
fractions = set()

import math
sum = 0
for i in range(1, 12000+1):
    sum += math.floor((i-1) / 2) - math.floor(i / 3)
print(sum)

for n in range(1, limit):
    for d in range(n+1, limit + 1):
        if d >= n*3:
            break
        if d <= n*2:
            continue

        f = Fraction(n, d)
        if third < Fraction(n, d) < half:
            fractions.add((f.numerator, f.denominator))
            if n > hundreds * 100:
                hundreds += 1
                print(n)

print(len(fractions))
