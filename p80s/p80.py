from decimal import *


def solve():
    getcontext().prec = 120
    total = 0
    for i in range(1, 101):
        length = str(Decimal(i).sqrt()).replace('.', '')[:100]
        if len(length) >= 100:
            for let in range(100):
                total += int(length[let])
    return total
