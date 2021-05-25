#!/usr/bin/env python3
"""that calculates the precision for each class in a confusion matrix"""

import numpy as np

sensitivity = __import__('1-sensitivity').sensitivity
precision = __import__('2-precision').precision


def f1_score(confusion):
    """Returns: a numpy.ndarray of shape (classes,) precision of each class"""
    pr = precision(confusion)
    sen = sensitivity(confusion)
    f1 = 2 * (pr * sen) / (pr + sen)
    return(f1)
