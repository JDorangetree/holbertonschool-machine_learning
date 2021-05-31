#!/usr/bin/env python3
"""builds a neural network with the Keras library"""

import tensorflow.keras as K


def train_model(network, data, labels, batch_size, epochs,
                verbose=True, shuffle=False):
    history = network.fit(data, labels, epochs=epochs,
                          batch_size=batch_size, verbose=verbose,
                          shuffle=shuffle)
    return(history)
