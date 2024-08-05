#!/usr/bin/env python3
"""function that performs element-wise add, sub, mul, and div"""


def np_elementwise(mat1, mat2):
    """return tuple"""
    add = mat1 + mat2
    sub = mat1 - mat2
    mul = mat1 * mat2
    div = mat1 / mat2
    return add, sub, mul, div
