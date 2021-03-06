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

        self.W = np.random.randn(nx).reshape((1, nx))
        self.b = 0
        self.A = 0
