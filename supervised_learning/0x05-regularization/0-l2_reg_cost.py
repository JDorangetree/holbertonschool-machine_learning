#!/usr/bin/env python3
"""Script to use L2 regularization in a DNN"""

import numpy as np


def l2_reg_cost(cost, lambtha, weights, L, m):
    """calculates the cost of a neural network with L2 regularization"""
    keys = list(weights.keys())
    normalize = 0
    for i in keys:
        if i[0] == 'W':
            normalize = normalize + (np.linalg.norm(weights[i])**2)
    L2 = cost + (lambtha/(2 * m)) * normalize
    return(L2)
