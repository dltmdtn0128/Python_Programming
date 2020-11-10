def matrix_add(*args):
    return[[sum(row) for row in zip(*t)]for t in zip(*args)]

matrix_x = [[2,5],[2,1],[3,5]]
matrix_y = [[3,4],[5,6],[7,8]]

print(matrix_add(matrix_x,matrix_y))
