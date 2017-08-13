limit = 10 ** 7 + 1
all_factors = [[] for _ in range(limit)]

for i in range(2, limit):
    for j in range(i, limit, i):
        all_factors[j].append(i)


def solve():
    results = [1 for _ in range(limit)]
    results[:2] = [0, 0]
    for s in range(1, limit-1):
        for ff in all_factors[s]:
            results[ff] = max(results[ff], ff - s)
            for sf in all_factors[s+1]:
                results[sf] = max(results[sf], sf - s)
                over = sf * ff
                if over < limit:
                    results[over] = max(results[over], over - s)
    return sum(results)
