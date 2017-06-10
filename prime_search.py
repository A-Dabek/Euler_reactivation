limit = 10**8
primes = []
file = open('res/primes.txt', mode='r')

line = file.readline().replace('\n', '')
primes_known = 0
while len(line) > 0:
    prime = int(line)
    primes.append(prime)
    line = file.readline().replace('\n', '')

print('max found', primes[-1])
file.close()

file = open('res/primes.txt', mode='a')


def is_prime(n):
    root = int(n ** 0.5)
    p_at = 0
    while primes[p_at] <= root:
        if n % primes[p_at] == 0:
            return False
        p_at += 1
    primes.append(n)
    return True


for i in range(int(primes[-1] + 1), limit):
    if is_prime(i):
        file.write(str(i) + '\n')
file.close()
