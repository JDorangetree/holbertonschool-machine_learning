#!/usr/bin/env python3
"""function that performs matrix multiplication"""


def mat_mul(mat1, mat2):
    """return a new matrix"""
    size_mat1 = (len(mat1), len(mat1[0]))
    size_mat2 = (len(mat2), len(mat2[0]))
    if size_mat1[1] == size_mat2[0]:
        new_mat = []
        for i in range(len(mat1)):
            mat_i = []
            for j in range(len(mat2[0])):
                vec = 0
                for k in range(len(mat2)):
                    vec += mat1[i][k] * mat2[k][j]
                mat_i.append(vec)
            new_mat.append(mat_i)
        for x in new_mat:
            return(new_mat)
    else:
        return(None)