file = open('res/82.txt')


def recur_fill(mat, x, y):
    if x - 1 >= 0:
        if matrix[y][x - 1][1] == 0 or matrix[y][x - 1][1] > matrix[y][x][0] + matrix[y][x][1]:
            matrix[y][x - 1][1] = matrix[y][x][0] + matrix[y][x][1]
            recur_fill(mat, x - 1, y)
    if 0 < x < max_val - 1 and y - 1 >= 0:
        if matrix[y - 1][x][1] == 0 or matrix[y - 1][x][1] > matrix[y][x][0] + matrix[y][x][1]:
            matrix[y - 1][x][1] = matrix[y][x][0] + matrix[y][x][1]
            recur_fill(mat, x, y - 1)
    if 0 < x < max_val - 1 and y + 1 < max_val:
        if matrix[y + 1][x][1] == 0 or matrix[y + 1][x][1] > matrix[y][x][0] + matrix[y][x][1]:
            matrix[y + 1][x][1] = matrix[y][x][0] + matrix[y][x][1]
            recur_fill(mat, x, y + 1)


# matrix = [[131, 673, 234, 103, 18],
#           [201, 96, 342, 965, 150],
#           [630, 803, 746, 422, 111],
#           [537, 699, 497, 121, 956],
#           [805, 732, 524, 37, 331]]
#
# for i in range(len(matrix)):
#     for j in range(len(matrix[i])):
#         matrix[i][j] = [matrix[i][j], 0]
# max_val = 5

matrix = []
max_val = 80
for i in range(max_val):
    values = file.readline().replace('\n', '').split(',')
    if len(values) < max_val:
        continue
    matrix.append([])
    matrix[i] = [[int(j), 0] for j in values]

for i in range(max_val):
    recur_fill(matrix, max_val - 1, i)

minimum = 1000000
for i in range(max_val):
    if matrix[i][0][1] > 0 and matrix[i][0][0] + matrix[i][0][1] < minimum:
        minimum = matrix[i][0][0] + matrix[i][0][1]
print(minimum)
for i in matrix:
    print(i)
