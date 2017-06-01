fairy_mem = [0 for _ in range(1000000)]
fairy_mem[0] = 2


def fairy_seq(n):
    if fairy_mem[n - 1] != 0:
        return fairy_mem[n - 1]
    else:
        value = (n + 3) * n // 2
        sum_of_f = 0
        for d in range(2, n + 1):
            sum_of_f += fairy_seq(n // d)
        value -= sum_of_f
        fairy_mem[n - 1] = value
        return value

print(fairy_seq(1000000))
