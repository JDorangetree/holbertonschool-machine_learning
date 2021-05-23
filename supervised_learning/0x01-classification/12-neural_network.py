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

        self.__W1 = np.random.randn(nx, nodes).reshape(nodes, nx)
        self.__b1 = np.zeros(nodes).reshape(nodes, 1)
        self.__A1 = 0
        self.__W2 = np.random.randn(nodes).reshape(1, nodes)
        self.__b2 = 0
        self.__A2 = 0

    @property
    def W1(self):
        """
        Getter attr
        Args:
            self: Private attribute
            Returns: Weight vector 1 hidden layer
        """
        return self.__W1

    @property
    def b1(self):
        """
        Getter attr
        Args:
            self: Private attribute
            Returns: Bias1
        """
        return self.__b1

    @property
    def A1(self):
        """
        Getter attr
        Args:
            self: Private attribute
            Returns: Activated1
        """
        return self.__A1

    @property
    def W2(self):
        """
        Getter attr
        Args:
            self: Private attribute
            Returns: Weight vector 2
        """
        return self.__W2

    @property
    def b2(self):
        """
        Getter attr
        Args:
            self: Private attribute
            Returns: Bias2
        """
        return self.__b2

    @property
    def A2(self):
        """
        Getter attr
        Args:
            self: Private attribute
            Returns: Activated output 2 prediction
        """
        return self.__A2

    def forward_prop(self, X):
        """forward propagation of the neural network"""
        neuron1 = np.matmul(self.__W1, X) + self.__b1
        sigmoid1 = 1 / (1 + np.exp(-neuron1))
        self.__A1 = sigmoid1
        neuron2 = np.matmul(self.__W2, self.__A1) + self.__b2
        sigmoid2 = 1 / (1 + np.exp(-neuron2))
        self.__A2 = sigmoid2
        return(self.__A1, self.__A2)

    def cost(self, Y, A):
        """Calculates the cost of the model using logistic regression"""
        lost_function = np.multiply(Y, np.log(A)) + (
                        np.multiply((1 - Y), np.log(1.0000001 - A)))
        cost_function = -(1 / Y.shape[1]) * np.sum(lost_function)
        return cost_function

    def evaluate(self, X, Y):
        """Evaluates the neural network’s predictions"""
        eval = self.forward_prop(X)
        eval = np.where(eval >= 0.5, 1, 0)
        cost = self.cost(Y, self.__A2)
        return(eval, cost)
