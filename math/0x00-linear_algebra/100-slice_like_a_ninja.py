#!/usr/bin/env python3
"""function that slices a matrix along specific axes"""


def np_slice(matrix, axes={}):
    """return a new numpy.ndarray"""
    slice_mat = [slice(None, None, None)] * matrix.ndim
    for k, v in sorted(axes.items()):
        slice_val = slice(*v)
        slice_mat[k] = slice_val
    matrix = matrix[tuple(slice_mat)]
    return matrix
