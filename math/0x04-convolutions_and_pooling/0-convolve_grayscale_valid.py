#!/usr/bin/env python3
""" Script that perfoms a valid convolution"""


import numpy as np


def convolve_grayscale_valid(images, kernel):
    """Function to perform a valid grayscale convolution"""
    m = images.shape[0]
    h = images.shape[1]
    w = images.shape[2]
    kh = kernel.shape[0]
    kw = kernel.shape[1]
    output_h = h - kh + 1
    output_w = w - kw + 1

    conv_out = np.zeros((m, output_h, output_w))

    image = np.arange(m)

    for i in range(0, output_h):
        for j in range(output_w):
            conv_out[image, i, j] = (np.sum(images[image, i:kh+i,
                                            j:kw+j] * kernel,
                                            axis=(1, 2)))
    return conv_out
