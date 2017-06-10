import resource
from random import shuffle


def find_in_list(number, list, start=0, stop=-1):
    if stop < 0:
        stop = len(list)
    for i_el in range(start, stop):
        if list[i_el][0] == number:
            return i_el
    return -1


def solve():
    codes = ''.join(resource.get_problem_context(79)).split('\n')[:-1]
    password = ['7', '3', '1', '6', '2', '8', '9', '0']
    shuffle(password)
    is_right = False
    while not is_right:
        is_right = True
        for c in codes:
            pre = 0
            for d_i in range(len(c)):
                if d_i == 0:
                    pre = password.index(c[d_i])
                else:
                    post = password.index(c[d_i])
                    if post < pre:
                        temp = password[pre]
                        password[pre] = password[post]
                        password[post] = temp
                        is_right = False
                    pre = post
    return int(''.join(password))
