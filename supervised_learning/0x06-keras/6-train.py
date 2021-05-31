#!/usr/bin/env python3
"""builds a neural network with the Keras library"""

import tensorflow.keras as K
from tensorflow.keras import callbacks
from tensorflow.python.keras.callbacks import EarlyStopping


def train_model(network, data, labels, batch_size, epochs,
                validation_data=None, early_stopping=False,
                patience=0, verbose=True, shuffle=False):

    if validation_data and early_stopping:
        callback = K.callbacks.EarlyStopping(monitor='val_loss', mode='min',
                                             patience=patience)
    history = network.fit(data, labels, epochs=epochs,
                          batch_size=batch_size, verbose=verbose,
                          shuffle=shuffle, validation_data=validation_data,
                          callbacks=[callback])
    return(history)
