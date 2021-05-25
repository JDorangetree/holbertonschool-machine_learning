#!/usr/bin/env python3
"""that calculates the precision for each class in a confusion matrix"""

import numpy as np


def specificity(confusion):
    """Returns: a numpy.ndarray of shape (classes,) precision of each class"""
    diagonal = confusion.diagonal()
    FP = np.sum(confusion, axis=1) - diagonal
    FN = np.sum(confusion, axis=1) - diagonal
    TN = np.sum(confusion) - (diagonal + FN + FP)
    especificity = TN / (TN + FP)
    return(especificity)
