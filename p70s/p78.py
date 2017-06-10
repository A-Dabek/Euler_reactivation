import math


def g(k):
    return k * (3 * k - 1) // 2


def p(n):
    res = 0
    if partition_cache[n] > 0:
        return partition_cache[n]

    root = math.sqrt(24 * n + 1)
    ll = int(- (root + 1) / 6)
    ul = int(((root - 1) / 6) + 1)
    for k in range(ll, ul+1):
        g_k = g(k)
        if 0 < g_k <= n:
            res += (-1)**(k+1) * p(n - g_k)
            res %= 1000000
    partition_cache[n] = int(res)
    if partition_cache[n] == 0:
        print(n)
        exit(0)
    return res


limit = 100000
partition_cache = [0 for _ in range(limit+1)]
partition_cache[0] = 1
print(p(limit))
print(partition_cache)
exit(0)

s_value = 100
target = s_value
ways = [0] * (target + 1)
ways[0] = 1
for i in range(1, target):
    for j in range(i, target + 1):
        ways[j] += ways[j - i]
print(ways)
