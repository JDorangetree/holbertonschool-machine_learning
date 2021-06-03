#!/usr/bin/env python3
"""Script to perform a padding convolution"""

import numpy as np


def convolve_grayscale_padding(images, kernel, padding):
    """Function to perform a graysclae convolution"""
    m = images.shape[0]
    h = images.shape[1]
    w = images.shape[2]
    kh = kernel.shape[0]
    kw = kernel.shape[1]
    pad_w = padding[1]
    pad_h = padding[0]
    output_h = h + (2 * pad_h) - kh + 1
    output_w = w + (2 * pad_w) - kw + 1

    image_pad = np.pad(images, pad_width=((0, 0), (pad_h, pad_h),
                                          (pad_w, pad_w)), mode='constant')
    out = np.zeros((m, output_h, output_w))

    image = np.arange(m)
    for i in range(output_h):
        for j in range(output_w):
            out[image, i, j] = (np.sum(image_pad[image,
                                            i:kh+i, j:kw+j] * kernel,
                                            axis=(1, 2)))
    return out
