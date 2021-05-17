#!/usr/bin/env python3
"""class that defines a single neuron performing binary classification"""


import numpy as np


class Neuron():
    """class that defines a single neuron performing binary classification"""

    def __init__(self, nx):
        """Initialize method"""
        if type(nx) is not int:
            raise TypeError('nx must be an integer')
        elif nx < 1:
            raise ValueError('nx must be a positive integer')

        self.__W = np.random.randn(nx).reshape((1, nx))
        self.__b = 0
        self.__A = 0

    @property
    def W(self):
        """
        Returns: private instance weight
        """
        return self.__W

    @property
    def b(self):
        """
        Returns: private instance bias
        """
        return self.__b

    @property
    def A(self):
        """
        Returns: private instance output
        """
        return self.__A

    def forward_prop(self, X):
        """Calculates the forward propagation of the neuron"""
        Z = np.matmul(X, self.__W) + self.__b
        sigmoid = 1 / (1 + np.exp(-Z))
        self.__A = sigmoid
        return(self.__A)
