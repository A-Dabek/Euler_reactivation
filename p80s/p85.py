import math


def solve():
    opt = 2000000
    total_opt = 4 * opt
    diff = total_opt
    max_r = []
    for m in range(1, int(total_opt ** 0.5)):
        m_p = m * (m + 1)
        rest = total_opt // m_p
        start = int(rest ** 0.5)
        for n in range(start, start + 2):
            val = m_p * n * (n + 1)
            if math.fabs(val - total_opt) < diff:
                diff = math.fabs(val - total_opt)
                max_r.append(m * n)
    return max(max_r)
