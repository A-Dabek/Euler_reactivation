def solve():
    limit = 30
    bit_lists = [[] for _ in range(limit)]
    bit_lists[0] = [0, 1]
    for i in range(1, limit):
        for j in bit_lists[i-1]:
            bit_lists[i].append(0)
            if j == 0:
                bit_lists[i].append(1)
    return len(bit_lists[-1])
