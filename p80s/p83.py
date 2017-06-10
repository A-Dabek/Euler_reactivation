import resource

matrix = []
max_val = 0


def recur_fill(mat, x, y):
    global matrix, max_val
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


def solve():
    global matrix, max_val
    max_val = 80
    file = resource.get_problem_context(83)
    for i in range(max_val):
        values = file[i].replace('\n', '').split(',')
        if len(values) < max_val:
            continue
        matrix.append([])
        matrix[i] = [[int(j), 0] for j in values]

    for i in reversed(range(len(matrix))):
        for j in reversed(range(len(matrix[i]))):
            neighs = []
            if i < max_val - 1:
                if type(matrix[i + 1][j]) == list:
                    temp = sum(matrix[i + 1][j])
                else:
                    temp = matrix[i + 1][j]
                neighs.append(temp)
            if j < max_val - 1:
                if type(matrix[i][j + 1]) == list:
                    temp = sum(matrix[i][j + 1])
                else:
                    temp = matrix[i][j + 1]
                neighs.append(temp)
            if len(neighs) == 0:
                neighs = [0]
            matrix[i][j] = [matrix[i][j][0], min(neighs)]

    recur_fill(matrix, max_val - 1, max_val - 1)
    return matrix[0][0][0] + matrix[0][0][1]
