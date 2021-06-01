#!/usr/bin/env python3
"""Script to save and load weights a keras model"""


import tensorflow.keras as K


def save_weights(network, filename, save_format="h5"):
    """Function to save the weights model"""
    network.save_weights(filename, save_format=save_format)
    return None


def load_weights(network, filename):
    """Function to load the weights model"""
    network.load_weights(filename)
    return None
