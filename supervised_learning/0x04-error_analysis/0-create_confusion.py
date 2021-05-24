#!/usr/bin/env python3
""" function that creates a confusion matrix"""

import numpy as np


def create_confusion_matrix(labels, logits):
    """Returns: a confusion numpy.ndarray of shape (classes, classes)"""
    return(np.matmul(labels.T, logits))
