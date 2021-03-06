#!/usr/bin/env python3
"""L2 regularization in tensorflow"""

import tensorflow as tf


def l2_reg_cost(cost):
    """Function to calculate the L2 regularization in tf"""
    cost_L2 = cost + tf.losses.get_regularization_losses()
    return (cost_L2)
