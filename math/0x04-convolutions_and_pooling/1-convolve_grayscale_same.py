#!/usr/bin/env python3
"""Script to perform a same convolution operation"""

import numpy as np


def convolve_grayscale_same(images, kernel):
    """Function to perform a grayscale same convolution"""
    m = images.shape[0]
    h = images.shape[1]
    w = images.shape[2]
    kh = kernel.shape[0]
    kw = kernel.shape[1]

    pad_h = int((kh - 1) / 2)
    pad_w = int((kw - 1) / 2)

    if kh % 2 == 0:
        pad_h = int(kh / 2)
    if kw % 2 == 0:
        pad_w = int(kw / 2)
    image_pad = np.pad(images, pad_width=((0, 0),
                                          (pad_h, pad_h),
                                          (pad_w, pad_w)), mode='constant')
    conv_out = np.zeros((m, h, w))
    image = np.arange(m)
    for i in range(h):
        for j in range(w):
            conv_out[image, i, j] = (np.sum(image_pad[image,
                                            i:kh+i, j:kw+j] * kernel,
                                            axis=(1, 2)))
    return conv_out
