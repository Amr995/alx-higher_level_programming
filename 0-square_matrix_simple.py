#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    response = []
    for row in matrix:
        sub_mat = map(lambda num: num**2, row)
        response.append(list(sub_mat))
    return response
