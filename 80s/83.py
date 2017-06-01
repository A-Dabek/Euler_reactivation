file = open('res/83.txt')


def recur_fill(mat, x, y):
    if x - 1 >= 0:
        if matrix[y][x - 1][1] == 0 or matrix[y][x - 1][1] >= matrix[y][x][0] + matrix[y][x][1]:
            matrix[y][x - 1][1] = matrix[y][x][0] + matrix[y][x][1]
            recur_fill(mat, x - 1, y)
    if x + 1 < max_val:
        if matrix[y][x + 1][1] == 0 or matrix[y][x + 1][1] >= matrix[y][x][0] + matrix[y][x][1]:
            matrix[y][x + 1][1] = matrix[y][x][0] + matrix[y][x][1]
            recur_fill(mat, x + 1, y)
    if y - 1 >= 0:
        if matrix[y - 1][x][1] == 0 or matrix[y - 1][x][1] >= matrix[y][x][0] + matrix[y][x][1]:
            matrix[y - 1][x][1] = matrix[y][x][0] + matrix[y][x][1]
            recur_fill(mat, x, y - 1)
    if y + 1 < max_val:
        if matrix[y + 1][x][1] == 0 or matrix[y + 1][x][1] >= matrix[y][x][0] + matrix[y][x][1]:
            matrix[y + 1][x][1] = matrix[y][x][0] + matrix[y][x][1]
            recur_fill(mat, x, y + 1)

# max_val = 5
# matrix = [[131, 673, 234, 103, 18],
#           [201, 96, 342, 965, 150],
#           [630, 803, 746, 422, 111],
#           [537, 699, 497, 121, 956],
#           [805, 732, 524, 37, 331]]

# for i in reversed(range(len(matrix))):
#     for j in reversed(range(len(matrix[i]))):
#         neighs = []
#         if i < max_val-1:
#             if type(matrix[i+1][j]) == list:
#                 temp = sum(matrix[i+1][j])
#             else:
#                 temp = matrix[i+1][j]
#             neighs.append(temp)
#         # if i > 0:
#         #     if type(matrix[i-1][j]) == list:
#         #         temp = sum(matrix[i-1][j])
#         #     else:
#         #         temp = matrix[i-1][j]
#         #     neighs.append(temp)
#         if j < max_val-1:
#             if type(matrix[i][j+1]) == list:
#                 temp = sum(matrix[i][j+1])
#             else:
#                 temp = matrix[i][j+1]
#             neighs.append(temp)
#         # if j > 0:
#         #     if type(matrix[i][j-1]) == list:
#         #         temp = sum(matrix[i][j-1])
#         #     else:
#         #         temp = matrix[i][j-1]
#         #     neighs.append(temp)
#         if len(neighs) == 0:
#             neighs = [0]
#         matrix[i][j] = [matrix[i][j], min(neighs)]

# for i in matrix:
#     print(i)

matrix = []
max_val = 80
for i in range(max_val):
    values = file.readline().replace('\n', '').split(',')
    if len(values) < max_val:
        continue
    matrix.append([])
    matrix[i] = [[int(j), 0] for j in values]

for i in reversed(range(len(matrix))):
    for j in reversed(range(len(matrix[i]))):
        neighs = []
        if i < max_val-1:
            if type(matrix[i+1][j]) == list:
                temp = sum(matrix[i+1][j])
            else:
                temp = matrix[i+1][j]
            neighs.append(temp)
        # if i > 0:
        #     if type(matrix[i-1][j]) == list:
        #         temp = sum(matrix[i-1][j])
        #     else:
        #         temp = matrix[i-1][j]
        #     neighs.append(temp)
        if j < max_val-1:
            if type(matrix[i][j+1]) == list:
                temp = sum(matrix[i][j+1])
            else:
                temp = matrix[i][j+1]
            neighs.append(temp)
        # if j > 0:
        #     if type(matrix[i][j-1]) == list:
        #         temp = sum(matrix[i][j-1])
        #     else:
        #         temp = matrix[i][j-1]
        #     neighs.append(temp)
        if len(neighs) == 0:
            neighs = [0]
        matrix[i][j] = [matrix[i][j][0], min(neighs)]

recur_fill(matrix, max_val - 1, max_val - 1)

print(matrix[0][0][0] + matrix[0][0][1])
