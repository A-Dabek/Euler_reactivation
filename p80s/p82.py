import resource


def recur_fill(mat, x, y):
    global matrix, max_val
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


def solve():
    global matrix, max_val
    matrix = []
    max_val = 80
    file = resource.get_problem_context(82)
    for i in range(max_val):
        values = file[i].replace('\n', '').split(',')
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
    return minimum
