#!/usr/bin/env python3
""" function that creates a confusion matrix"""

import numpy as np


def sensitivity(confusion):
    """Returns: a confusion numpy.ndarray of shape (classes, classes)"""
    sum_row = np.sum(confusion, axis=1)
    diagonal = confusion.diagonal()
    sensitivity = diagonal / sum_row
    return(sensitivity)
