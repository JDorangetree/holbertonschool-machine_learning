#!/usr/bin/env python3
"""that calculates the precision for each class in a confusion matrix"""

import numpy as np


def precision(confusion):
    """Returns: a numpy.ndarray of shape (classes,) precision of each class"""
    sum_row = np.sum(confusion, axis=0)
    diagonal = confusion.diagonal()
    precision = diagonal / sum_row
    return(precision)
