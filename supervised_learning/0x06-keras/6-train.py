#!/usr/bin/env python3
"""builds a neural network with the Keras library"""

import tensorflow.keras as K


def train_model(network, data, labels, batch_size, epochs,
                validation_data=None, early_stopping=False,
                patience=0, verbose=True, shuffle=False):
    """train the model using early stopping"""
    if validation_data and early_stopping:
        callback = K.callbacks.EarlyStopping(monitor='val_loss', mode='min',
                                             patience=patience)
    history = network.fit(x=data, y=labels, epochs=epochs,
                          batch_size=batch_size, verbose=verbose,
                          shuffle=shuffle, validation_data=validation_data,
                          callbacks=list(callback))
    return(history)
