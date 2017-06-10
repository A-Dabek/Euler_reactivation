import resource


def recur_fill(mat, x, y):
    global matrix, max_val
    if x - 1 >= 0:
        if matrix[x - 1][y][1] == 0 or matrix[x - 1][y][1] > matrix[x][y][0] + matrix[x][y][1]:
            matrix[x - 1][y][1] = matrix[x][y][0] + matrix[x][y][1]
            recur_fill(mat, x - 1, y)
    if y - 1 >= 0:
        if matrix[x][y - 1][1] == 0 or matrix[x][y - 1][1] > matrix[x][y][0] + matrix[x][y][1]:
            matrix[x][y - 1][1] = matrix[x][y][0] + matrix[x][y][1]
            recur_fill(mat, x, y - 1)


def solve():
    global matrix, max_val
    matrix = []
    max_val = 80
    file = resource.get_problem_context(81)
    for i in range(max_val):
        values = file[i].replace('\n', '').split(',')
        if len(values) < max_val:
            continue
        matrix.append([])
        matrix[i] = [[int(j), 0] for j in values]

    recur_fill(matrix, max_val - 1, max_val - 1)

    return matrix[0][0][0] + matrix[0][0][1]
