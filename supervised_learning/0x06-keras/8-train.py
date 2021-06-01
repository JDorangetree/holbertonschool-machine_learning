#!/usr/bin/env python3
"""Script to train a model using keras"""

import tensorflow.keras as K


def train_model(network, data, labels, batch_size, epochs,
                validation_data=None, early_stopping=False,
                patience=0, learning_rate_decay=False,
                alpha=0.1, decay_rate=1, save_best=False,
                filepath=None, verbose=True, shuffle=False):
    """Function to train a model using keras and LRD"""

    def scheduler(epoch):
        """Function o get the learning reate of each epoch"""
        return alpha / (1 + decay_rate * epoch)

    custom_callbacks = []
    ES = K.callbacks.EarlyStopping(monitor='val_loss', mode='min',
                                   patience=patience)
    LRD = K.callbacks.LearningRateScheduler(scheduler, verbose=1)

    if validation_data and early_stopping:
        custom_callbacks.append(ES)
    if validation_data and learning_rate_decay:
        custom_callbacks.append(LRD)
    if save_best:
        save = K.callbacks.ModelCheckpoint(filepath, save_best_only=True)
        custom_callbacks.append(save)

    history = network.fit(x=data, y=labels, batch_size=batch_size,
                          epochs=epochs, validation_data=validation_data,
                          callbacks=custom_callbacks,
                          verbose=verbose, shuffle=shuffle)
    return history
