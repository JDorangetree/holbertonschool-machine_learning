#!/usr/bin/env python3
"""builds a neural network with the Keras library"""

import tensorflow.keras as K


def one_hot(labels, classes=None):
    one_hot = K.utils.to_categorical(labels, num_classes=classes)
    return(one_hot)
