#!/usr/bin/env python3

import numpy as np
"""function that concatenates two matrices along a specific axis"""


def np_cat(mat1, mat2, axis=0):
    """return numpy array"""
    concat = np.concatenate((mat1, mat2), axis=axis)
    return(concat)