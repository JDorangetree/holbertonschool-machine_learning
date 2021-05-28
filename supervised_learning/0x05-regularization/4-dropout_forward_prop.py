#!/usr/bin/env python3
"""conducts forward propagation using Dropout"""

import numpy as np


def dropout_forward_prop(X, weights, L, keep_prob):
    """Function that uses dropout in a forward propagation DNN"""
    cache = {}
    cache.update({'A0': X})
    for i in range(0, L):
        W = weights['W' + str(i + 1)]
        A = cache['A' + str(i)]
        bias = weights['b' + str(i + 1)]
        Z = np.matmul(W, A) + bias
        dropout = np.random.binomial(1,
                                     keep_prob,
                                     (W.shape[0] *
                                      A.shape[1])).reshape(W.shape[0],
                                                           A.shape[1])
        if i != L - 1:
            tanh = np.tanh(Z)
            cache["A" + str(i + 1)] = tanh
            cache['D' + str(i + 1)] = dropout
            cache['A' + str(i + 1)] *= dropout
            cache['A' + str(i + 1)] /= keep_prob
        else:
            softmax = np.exp(Z)
            cache['A' + str(i + 1)] = (softmax / np.sum(softmax, axis=0,
                                                        keepdims=True))
        return(cache)
