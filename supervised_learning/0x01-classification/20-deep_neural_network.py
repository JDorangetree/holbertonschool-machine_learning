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
            raise TypeError('layers must be a list of positive integers')
        weights = {}
        for i in range(0, len(layers)):
            if layers[i] < 1:
                raise TypeError('layers must be a list of positive integers')
            if i == 0:
                weights.update({'W' + str(i+1): np.random.randn(layers[i],
                                nx) * np.sqrt(2 / nx)})
            if i >= 1:
                weights.update({'W' + str(i+1): np.random.randn(layers[i],
                                layers[i - 1]) * np.sqrt(2 / layers[i - 1])})
            weights.update({'b' + str(i+1):  np.zeros((layers[i], 1))})
        self.__L = len(layers)
        self.__cache = {}
        self.__weights = weights

    @property
    def weights(self):
        """
        Getter attr
        Args:
            self: Private attribute
            Returns: Weight dictionary
        """
        return self.__weights

    @property
    def L(self):
        """
        Getter attr
        Args:
            self: Private attribute
            Returns: number of hiden layers
        """
        return self.__L

    @property
    def cache(self):
        """
        Getter attr
        Args:
            self: Private attribute
            Returns: hold all intermediary values of the network
        """
        return self.__cache

    def forward_prop(self, X):
        """Calculates the forward propagation of the neural network"""
        self.__cache.update({'A0': X})
        for i in range(1, self.__L + 1):
            key_W = 'W' + str(i)
            key_b = 'b' + str(i)
            key_A = 'A' + str(i - 1)
            if i == 1:
                key_A = 'A0'
            neuron = np.matmul(self.__weights[key_W],
                               self.__cache[key_A]) + self.__weights[key_b]
            activation = 1 / (1 + np.exp(-neuron))
            self.__cache['A' + str(i)] = activation
        return(self.__cache['A' + str(i)], self.__cache)

    def cost(self, Y, A):
        """Calculates the cost of the model using logistic regression"""
        lost_function = np.multiply(Y, np.log(A)) + (
                        np.multiply((1 - Y), np.log(1.0000001 - A)))
        cost_function = -(1 / Y.shape[1]) * np.sum(lost_function)
        return cost_function
    
    def evaluate(self, X, Y):
        """Evaluates the neural network’s predictions"""
        eval1, eval2 = self.forward_prop(X)
        eval2 = np.where(eval2 >= 0.5, 1, 0)
        cost = self.cost(Y, self.__A2)
        return(eval1, cost)

