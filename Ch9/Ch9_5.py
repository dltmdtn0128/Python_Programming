from functools import reduce


def matrix_mul(x, y):
    return [[sum(a * b for a, b in zip(row_a, col_b)) for col_b in zip(*y)] for row_a in x]


matrix_x = [[1, 2, 3], [4, 5, 6]]
matrix_y = [[1, 2], [3, 4], [5, 6]]

print(matrix_mul(matrix_x, matrix_y))


def matrix_mul_1(*args):
    mul = lambda x, y: [[sum(a * b for a, b in zip(row_x, column_y)) for column_y in zip(*y)] for row_x in x]
    print(reduce(mul, args))


print(matrix_mul_1(matrix_x, matrix_y))
