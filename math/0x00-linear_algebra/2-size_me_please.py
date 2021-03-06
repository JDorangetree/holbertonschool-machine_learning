#!/usr/bin/env python3
"""Recursion function to check the shape of the matrix"""


def matrix_shape(element):
    """ return the shape of a matrix """
    if type(element[0]) != list:
        return [len(element)]
    else:
        return [len(element)] + matrix_shape(element[0])
