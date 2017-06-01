import time


def sum_of_digits(n):
    sod = 0
    while n > 0:
        sod += n % 10
        n //= 10
    return sod


def is_prime(n):
    if n in [2, 3]:
        return True
    if n % 2 == 0:
        return False
    root = int(n**0.5) + 1
    for i in range(3, root, 2):
        if n % i == 0:
            return False
    return True

TIME_STAMP = time.time()
limit = 13

list_of_start_length = [list() for _ in range(limit)]
list_of_start_length[0] = list(range(1, 10))
for i in range(1, len(list_of_start_length)):
    for j in list_of_start_length[i-1]:
        for d in range(10):
            temp = j*10 + d
            sod = sum_of_digits(temp)
            if temp % sod == 0:
                list_of_start_length[i].append(temp)

# for l in list_of_start_length:
#     print(len(l), l)

solution = []
for i in range(1, len(list_of_start_length)):
    for j in list_of_start_length[i]:
        temp = j / sum_of_digits(j)
        if is_prime(temp):
            for d in [1, 3, 7, 9]:
                temp = j*10 + d
                if is_prime(temp):
                    solution.append(temp)
print(sum(solution), solution)

print(time.time() - TIME_STAMP)
