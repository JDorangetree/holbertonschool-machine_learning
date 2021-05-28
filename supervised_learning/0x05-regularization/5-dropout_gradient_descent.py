#!/usr/bin/env python3
"""updates the weights of a neural network with Dropout"""

import numpy as np


def dropout_gradient_descent(Y, weights, cache, alpha, keep_prob, L):
    """Function to use dropout in a gradient descent optimization model"""
    m = Y.shape[1]
    W_copy = weights.copy()

    for i in reversed(range(L)):
        A = cache["A" + str(i + 1)]
        if i == L - 1:
            dZ = A - Y
            dW = (np.matmul(cache["A" + str(i)], dZ.T) / m).T
            db = np.sum(dZ, axis=1, keepdims=True) / m
        else:
            dW2 = np.matmul(W_copy["W" + str(i + 2)].T, dZ2)
            dtanh = 1 - (A * A)
            dZ = dW2 * dtanh
            dZ = dZ * cache["D" + str(i + 1)]
            dZ = dZ / keep_prob
            dW = np.matmul(dZ, cache["A" + str(i)].T) / m
            db = np.sum(dZ, axis=1, keepdims=True) / m
        weights["W" + str(i + 1)] = (W_copy["W" + str(i + 1)] - (alpha * dW))
        weights["b" + str(i + 1)] = W_copy["b" + str(i + 1)] - (alpha * db)
        dZ2 = dZ
