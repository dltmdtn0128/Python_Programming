from functools import reduce
def matrix_mul(x,y):
    return[[sum(a*b for a,b in zip(row_a,col_b)) for col_b in zip(*y)]for row_a in x]
matrix_x = [[1,2,3],[4,5,6]]
matrix_y = [[1,2],[3,4],[5,6]]

print(matrix_mul(matrix_x,matrix_y))