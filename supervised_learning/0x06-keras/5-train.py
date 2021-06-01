#!/usr/bin/env python3
"""builds a neural network with the Keras library"""

import tensorflow.keras as K


def train_model(network, data, labels, batch_size, epochs,
                validation_data=None,
                verbose=True, shuffle=False):
    """analyze validaiton data"""
    history = network.fit(data, labels, epochs=epochs,
                          batch_size=batch_size, verbose=verbose,
                          shuffle=shuffle, validation_data=validation_data)
    return(history)
