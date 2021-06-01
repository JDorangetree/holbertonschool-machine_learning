#!/usr/bin/env python3
"""Script to test a DNN using keras"""

import tensorflow.keras as K


def test_model(network, data, labels, verbose=True):
    """Function to test a model using keras"""
    evaluation = network.evaluate(data, labels, verbose=verbose)
    return evaluation
