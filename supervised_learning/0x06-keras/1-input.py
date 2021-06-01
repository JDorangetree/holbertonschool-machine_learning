#!/usr/bin/env python3
"""builds a neural network with the Keras library"""

import tensorflow.keras as K


def build_model(nx, layers, activations, lambtha, keep_prob):
    """Function to create a DNN using keras"""
    L2 = K.regularizers.l2(lambtha)
    inputs = K.Input(shape=(nx,))
    for i in range(len(layers)):
        if i == 0:
            outputs = (K.layers.Dense(layers[i], input_shape=(nx,),
                                      activation=activations[i],
                                      kernel_regularizer=L2))(inputs)
        else:
            dropout = (K.layers.Dropout(1 - keep_prob))(outputs)
            outputs = (K.layers.Dense(layers[i], activation=activations[i],
                                      kernel_regularizer=L2))(dropout)
    model = K.Model(inputs=inputs, outputs=outputs)
    return(model)
