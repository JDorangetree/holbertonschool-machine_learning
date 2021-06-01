#!/usr/bin/env python3
"""Script to predict a DNN using keras"""

import tensorflow.keras as K


def predict(network, data, verbose=False):
    """Function that makes a prediction using keras"""
    prediction = network.predict(data, verbose=verbose)
    return prediction
