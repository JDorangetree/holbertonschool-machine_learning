#!/usr/bin/env python3
"""function that adds two matrices"""


def size(element):
    """Return the shape of a matrix"""
    if not isinstance(element[0], list):
        return [len(element)]
    else:
        return [len(element)] + size(element[0])


def rec_matrix(mat1, mat2):
    """return new matrix"""
    new_matrix = []
    if (type(mat1) and type(mat2)) == list:
        for i in range(len(mat1)):
            if isinstance(mat1[i], list):
                new_matrix.append(rec_matrix(mat1[i], mat2[i]))
            else:
                new_matrix.append(mat1[i] + mat2[i])
        return new_matrix


def add_matrices(mat1, mat2):
    """return new matrix"""
    if size(mat1) != size(mat2):
        return None
    else:
        new_mat = rec_matrix(mat1, mat2)
        return new_mat
