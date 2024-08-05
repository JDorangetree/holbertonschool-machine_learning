#!/usr/bin/env python3
"""function that returns the transpose of a 2D matrix"""


def matrix_transpose(element):
    """return a new matrix"""
    new_matrix = []
    for i in range(0, len(element[0])):
        count = 0
        row = []
        while count < len(element):
            row.append(element[count][i])
            count += 1
        new_matrix.append(row)
    return new_matrix
