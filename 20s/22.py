def alpha_value(name):
    suma = 0
    for l in name:
        print(l, ord(l) - 64)
        suma += ord(l) - 64
    return suma

file = open('res/22.txt')
names = file.read().replace('\"', '').split(',')
names.sort()
v_names = [alpha_value(i) * (j+1) for j, i in enumerate(names)]
print(sum(v_names))
