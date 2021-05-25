#!/usr/bin/env python3
"""defines a deep neural network performing binary classification"""


import numpy as np


class DeepNeuralNetwork():
    """class that defines a neural network performing binary classification"""

    def __init__(self, nx, layers):
        """Initialize method"""
        if type(nx) is not int:
            raise TypeError('nx must be an integer')
        elif nx < 1:
            raise ValueError('nx must be a positive integer')
        elif type(layers) != list or len(layers) == 0:
            raise TypeError('nx must be an integer')
        weights = {}
        for i in range(0, len(layers)):
            if layers[i] <= 0:
                raise TypeError('nx must be an integer')
            weights.update({'W' + str(i+1) : np.random.randn(nx, layers[i]).reshape(layers[i], nx)})

        self.L = len(layers)
        self.cache = {}
        self.weights = weights
