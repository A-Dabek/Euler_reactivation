import math

global dict_chain


def sum_of_factorials(number):
    str_number = str(number)
    sum = 0
    for letter in str_number:
        sum += dict_chain[int(letter)]
    return sum


dict_chain = [0] * 10

for i in range(10):
    dict_chain[i] = math.factorial(i)

chain_len = 0
chain_memory = [0] * 2000000
looped = False
results = []
how_many = 0
for i in range(1, 1000000):
    curr_memory = [i]
    #print('\n')
    temp = i
    while not looped:
        temp = sum_of_factorials(temp)
        #print(temp)
        if temp in curr_memory:
            chain_memory[temp] = len(curr_memory) - curr_memory.index(temp)
            curr_value = chain_memory[temp]
            for jj in range(len(curr_memory)-1):
                if chain_memory[curr_memory[jj]] == 0:
                    chain_memory[curr_memory[jj]] = len(curr_memory) - jj
                else:
                    break
            #print('local', i, curr_memory)
            if len(curr_memory) == 60:
                how_many += 1
                print(how_many)
            #results.append((i, len(curr_memory)))
            break
        curr_memory.append(temp)
        if chain_memory[temp] != 0:
            #print('global', i, curr_memory)
            if len(curr_memory) - 1 + chain_memory[temp] == 60:
                how_many += 1
                print(how_many)
            #results.append((i, len(curr_memory) - 1 + chain_memory[temp]))
            break
    pass
#print(chain_memory)
#print(results)
# how_many = 0
# for r in results:
#     if r[1] == 60:
#         how_many += 1
print(how_many)
