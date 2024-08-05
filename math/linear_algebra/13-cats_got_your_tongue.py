#!/usr/bin/env python3
"""function that concatenates two matrices along a specific axis"""


import numpy as np


def np_cat(mat1, mat2, axis=0):
    """return numpy array"""
    mat_1 = np.array(mat1)
    mat_2 = np.array(mat2)
    concat = np.concatenate((mat_1, mat_2), axis=axis)
    return concat
