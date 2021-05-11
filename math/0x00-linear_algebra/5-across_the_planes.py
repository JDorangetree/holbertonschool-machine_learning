#!/usr/bin/env python3
"""function that adds two matrices element-wise"""


def add_matrices2D(mat1, mat2):
    """return new matrix"""
    if len(mat1) != len(mat2):
        return(None)
    if len(mat1[0]) != len(mat2[0]):
        return(None)
    else:
        element = [[1,1],[1,1]]
        for i in range(0, len(mat1)):
            for j in range(0, len(mat1[0])):
                item = mat1[i][j] + mat2[i][j]
                element[i][j] = item
    return(element)
