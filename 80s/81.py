file = open('res/81.txt')



def recur_fill(mat, x, y):
    if x - 1 >= 0:
        if matrix[x - 1][y][1] == 0 or matrix[x - 1][y][1] > matrix[x][y][0] + matrix[x][y][1]:
            matrix[x - 1][y][1] = matrix[x][y][0] + matrix[x][y][1]
            recur_fill(mat, x - 1, y)
    if y - 1 >= 0:
        if matrix[x][y - 1][1] == 0 or matrix[x][y - 1][1] > matrix[x][y][0] + matrix[x][y][1]:
            matrix[x][y - 1][1] = matrix[x][y][0] + matrix[x][y][1]
            recur_fill(mat, x, y - 1)


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

recur_fill(matrix, max_val - 1, max_val - 1)

for i in matrix:
    print(i)
print(matrix[0][0][0] + matrix[0][0][1])
