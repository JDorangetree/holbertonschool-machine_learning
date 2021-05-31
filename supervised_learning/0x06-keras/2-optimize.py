#!/usr/bin/env python3
"""sets up Adam optimization for a keras model"""

import tensorflow.keras as K
from tensorflow.keras import optimizers


def optimize_model(network, alpha, beta1, beta2):
    """categorical crossentropy loss and accuracy metrics"""
    opt = K.optimizers.Adam(learning_rate=alpha, beta_1=beta1, beta_2=beta2)
    network.compile(loss='categorical_crossentropy',
                    optimizer=opt, metrics=['accuracy'])
    return(None)
