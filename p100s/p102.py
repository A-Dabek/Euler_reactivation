import math


file = open('res/102.txt')

line = file.readline()
coords = []
while len(line) > 5:
    points = line.replace('\n', '').split(',')
    line = file.readline()
    points = [int(i) for i in points]
    coords.append(points)

print(coords)
how_many = 0
how_many_2 = 0
for c in coords:
    p0x, p0y, p1x, p1y, p2x, p2y = c
    area = -p1y * p2x + p0y * (-p1x + p2x) + p0x * (p1y - p2y) + p1x * p2y
    s = (p0y * p2x - p0x * p2y)
    t = (p0x * p1y - p0y * p1x)
    if area < 0:
        s = -s
        t = -t
        area = -area
    if s > 0 and t > 0 and s + t <= area:
        how_many_2 += 1
print(how_many, how_many_2)
