# how many ways to write 1000 as a sum of integers

s_value = 5
target = s_value
ways = [0] * (target+1)
ways[0] = 1

for i in range(1, target):
    for j in range(i, target+1):
        ways[j] += ways[j-i]
print(ways[-1])