#!/usr/bin/env python3
"""class that defines a neural network with one hidden layer"""


import numpy as np


class NeuralNetwork():
    """class that defines a single neuron performing binary classification"""

    def __init__(self, nx, nodes):
        """Initialize method"""
        if type(nx) != int:
            raise TypeError('nx must be an integer')
        elif nx < 1:
            raise ValueError('nx must be a positive integer')
        elif type(nodes) != int:
            raise TypeError('nodes must be an integer')
        elif nodes < 1:
            raise ValueError('nodes must be a positive integer')

        self.W1 = np.random.randn(nx).reshape((1, nx))
        self.b1 = 0
        self.A1 = 0
        self.W2 = np.random.randn(nodes).reshape((1, nodes))
        self.b2 = 0
        self.A2 = 0
