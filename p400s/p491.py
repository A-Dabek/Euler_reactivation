def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n-1)


def is_double_pan(number, digs):
    digits = [0 for _ in range(digs)]
    text = str(number)
    for c in text:
        if int(c) >= digs:
            return 0
        digits[int(c)] += 1
        if digits[int(c)] > 2:
            return 0
    return 1


def brute_force(digits):
    start = 10**(2*digits-1)
    while start % 11 != 0:
        start += 1
    total = 0
    while start <= 10**(2*digits):
        total += is_double_pan(start, digits)
        start += 11
    return total


def solve():
    sets = []
    new_sets = []
    up_to = 9
    base = [x // 2 for x in range((up_to + 1) * 2)]
    base.remove(0)
    sets.append([[0], list(base)])
    prev = -1
    while len(sets[-1][0]) < len(sets[-1][1]):
        for s in sets:
            for d in s[1]:
                if d < s[0][-1] or s[0] + [d] == prev:
                    continue
                prev = list(s[0] + [d])
                new_s = s[0] + [d]
                new_base = list(s[1])
                new_base.remove(d)
                if int(''.join([str(c) for c in new_s])) > int(''.join([str(c) for c in new_base])):
                    continue
                new_sets.append([list(new_s), list(new_base)])
        sets = list(new_sets)
        new_sets = list()
    total_f = 0
    total_b = 0
    total = 0
    for s in sets:
        if (sum(s[0]) - sum(s[1])) % 11 != 0:
            continue
        zeros = s[0].count(0)
        dups_f = len(s[0]) - len(set(s[0]))
        dups_b = len(s[1]) - len(set(s[1]))
        if zeros == 2:
            total_f = factorial(len(s[0]) - 2) * (len(s[0])-1) * (len(s[0])-2) / (2**dups_f)
        elif zeros == 1:
            total_f = factorial(len(s[0]) - 1) * (len((s[0])) - 1) / 2**dups_f
        elif zeros == 0:
            total_f = factorial(len(s[0])) / 2**dups_f
        total_b = factorial(len(s[1])) / 2 ** dups_b
        total += total_b * total_f

        if s[0] != s[1]:
            zeros = s[1].count(0)
            if zeros == 2:
                total_f = factorial(len(s[1]) - 2) * (len(s[1])-1) * (len(s[1])-2) / (2 * 2**dups_b)
            elif zeros == 1:
                total_f = factorial(len(s[1]) - 1) * (len((s[1])) - 1) / 2**dups_b
            elif zeros == 0:
                total_f = factorial(len(s[1])) / (2**dups_b)
            total_b = factorial(len(s[0])) / 2**dups_f
            total += total_b * total_f
    print(total)
    return 0
