#!/usr/bin/env python3
"""builds a neural network with the Keras library"""

import tensorflow.keras as K


def train_model(network, data, labels, batch_size, epochs,
                validation_data=None, early_stopping=False,
                patience=0, learning_rate_decay=False, alpha=0.1,
                decay_rate=1, verbose=True, shuffle=False):

    def decayed_learning_rate(epochs):
        """get the learning reate of each epoch"""
        return alpha / (1 + decay_rate * epochs)

    if validation_data and early_stopping:
        callback = K.callbacks.EarlyStopping(monitor='val_loss', mode='min',
                                             patience=patience)
    if validation_data and learning_rate_decay:
        lrd = K.callbacks.LearningRateScheduler(decayed_learning_rate,
                                                verbose=1)
    else:
        callback = []
        lrd = []
    history = network.fit(data, labels, epochs=epochs,
                          batch_size=batch_size, verbose=verbose,
                          shuffle=shuffle, validation_data=validation_data,
                          callbacks=([callback] + [lrd]))
    return(history)
