import math


def solve():
    limit = 10**12
    repunit_len_limit = int(math.log(limit, 2))
    set_per_repunit = {1}

    for i in range(3, repunit_len_limit + 1):
        base = 2
        while True:
            total = 0
            power = 1
            for _ in range(i):
                total += power
                power *= base
            if total > limit:
                break
            set_per_repunit.add(total)
            base += 1
    return sum(set_per_repunit)
