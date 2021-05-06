#!/usr/bin/env python3
"""function that adds two matrices element-wise"""


def add_matrices2D(mat1, mat2):
    """return new matrix"""
    element = [[1, 2], [1, 2]]
    if len(mat1[0]) == len(mat2[0]):
        for i in range(0, len(mat1)):
            for j in range(0, len(mat1[0])):
                item = mat1[i][j] + mat2[i][j]
                element[i][j] = item
    else:
        return(None)
    return(element)
