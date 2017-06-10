import resource


def alpha_value(name):
    suma = 0
    for l in name:
        suma += ord(l) - 64
    return suma


def solve():
    data = resource.get_problem_context(22)
    names = ''.join(data).replace('\"', '').split(',')
    names.sort()
    v_names = [alpha_value(i) * (j + 1) for j, i in enumerate(names)]
    return sum(v_names)
