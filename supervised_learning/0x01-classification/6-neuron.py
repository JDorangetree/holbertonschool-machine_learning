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
        neuron = np.matmul(self.__W, X) + self.__b
        sigmoid = 1 / (1 + np.exp(-neuron))
        self.__A = sigmoid
        return(self.__A)

    def cost(self, Y, A):
        """Calculates the cost of the model using logistic regression"""

        lost_function = np.multiply(Y, np.log(A)) + (
                        np.multiply((1 - Y), np.log(1.0000001 - A)))
        cost_function = -(1 / Y.shape[1]) * np.sum(lost_function)
        return cost_function

    def evaluate(self, X, Y):
        """Evaluates the neuron’s predictions"""
        eval = self.forward_prop(X)
        eval = np.where(eval >= 0.5, 1, 0)
        cost = self.cost(Y, self.__A)
        return(eval, cost)

    def gradient_descent(self, X, Y, A, alpha=0.05):
        """Calculates one pass of gradient descent on the neuron"""
        dW = np.matmul(X, (A - Y).T) / Y.shape[1]
        db = np.sum(A - Y) / Y.shape[1]
        self.__W -= (alpha * dW).T
        self.__b -= alpha * db

    def train(self, X, Y, iterations=5000, alpha=0.05):
        """Trains the neuron"""
        if type(iterations) is not int:
            raise TypeError("iterations must be an integer")
        if iterations < 0:
            raise ValueError("iterations must be a positive integer")
        if type(alpha) is not float:
            raise TypeError("alpha must be a float")
        if alpha < 0:
            raise ValueError("alpha must be positive")

        for i in range(iterations):
            self.forward_prop(X)
            self.gradient_descent(X, Y, self.__A, alpha)
        return self.evaluate(X, Y)
