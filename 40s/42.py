import math


def alpha_value(name):
    suma = 0
    for l in name:
        suma += ord(l) - 64
    return suma


def is_triangle(number):
    number *= 2
    root = math.floor(math.sqrt(number))
    if root * (root+1) == number:
        return True
    return False

file = open('res/42.txt')
words = file.read().replace('\"', '').split(',')
words_v = [alpha_value(i) for i in words]


triangles = 0
for i in words_v:
    if is_triangle(i):
        triangles += 1
print(triangles)


print(words)
print(words_v)
