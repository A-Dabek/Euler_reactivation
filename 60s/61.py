# start from 32, end on 99
number_type = [[[] for _ in range(100)] for _ in range(6)]


def search_for_cycle(current, searched, result):
    global number_type
    if len(searched) == 6:
        if result[5][2] == result[0][1]:
            sum_of = 0
            for r in result:
                sum_of += r[1] * 100 + r[2]
            return sum_of
        return 0
    all = {0, 1, 2, 3, 4, 5}
    max_sum = 0
    for i in all.difference(searched):
        for j in number_type[i][current % 100]:
            #result.append((i, current % 100, j))
            #searched.append(i)
            answer = search_for_cycle((current % 100) * 100 + j, searched + [i], result + [(i, current % 100, j)])
            if answer > max_sum:
                max_sum = answer
    return max_sum




curr_number = 0
index = 18
overflow = 0
while overflow < 6:
    overflow = 0
    index += 1

    #print(index)
    curr_number = int(index * (index + 1) / 2)
    #if index == 127:
    #    print(curr_number)
    if not (curr_number >= 10000 or curr_number < 1000 or curr_number % 100 < 10):
        number_type[0][curr_number // 100].append(curr_number % 100)
    elif curr_number >= 10000:
        overflow += 1
    curr_number = index ** 2
    if not (curr_number >= 10000 or curr_number < 1000 or curr_number % 100 < 10):
        number_type[1][curr_number // 100].append(curr_number % 100)
    elif curr_number >= 10000:
        overflow += 1
    curr_number = int(index * (3 * index - 1) / 2)
    if not (curr_number >= 10000 or curr_number < 1000 or curr_number % 100 < 10):
        number_type[2][curr_number // 100].append(curr_number % 100)
    elif curr_number >= 10000:
        overflow += 1
    curr_number = index * (2 * index - 1)
    if not (curr_number >= 10000 or curr_number < 1000 or curr_number % 100 < 10):
        number_type[3][curr_number // 100].append(curr_number % 100)
    elif curr_number >= 10000:
        overflow += 1
    curr_number = int(index * (5 * index - 3) / 2)
    if not (curr_number >= 10000 or curr_number < 1000 or curr_number % 100 < 10):
        number_type[4][curr_number // 100].append(curr_number % 100)
    elif curr_number >= 10000:
        overflow += 1
    curr_number = index * (3 * index - 2)
    if not (curr_number >= 10000 or curr_number < 1000 or curr_number % 100 < 10):
        number_type[5][curr_number // 100].append(curr_number % 100)
    elif curr_number >= 10000:
        overflow += 1

max_sum = 0
for i in range(len(number_type[0])):
    for j in number_type[0][i]:
        t_sum = 0
        res = search_for_cycle(i * 100 + j, [], [])
        if res > 0:
            print(res)
            exit(0)
        # if res is None:
        #     continue
        # for k in res:
        #     print(k)
        #     t_sum += k[1] * 100 + k[2]
        # if t_sum > max_sum:
        #     max_sum = t_sum

