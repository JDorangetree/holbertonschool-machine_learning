#!/usr/bin/env python3
"""function that adds two arrays element-wise"""


def add_arrays(arr1, arr2):
    """return new list"""
    result = []
    if len(arr1) == len(arr2):
        for i in range(0, len(arr1)):
            result.append(arr1[i] + arr2[i])
        return result
    else:
        return None
