import resource


def alpha_value(name):
    suma = 0
    for l in name:
        suma += ord(l) - 64
    return suma


def is_triangle(number):
    number *= 2
    root = int(number**0.5)
    if root * (root+1) == number:
        return True
    return False


def solve():
    d = resource.get_problem_context(42)
    words = ''.join(d).replace('\"', '').split(',')
    words_v = [alpha_value(i) for i in words]
    triangles = 0
    for i in words_v:
        if is_triangle(i):
            triangles += 1
    return triangles
