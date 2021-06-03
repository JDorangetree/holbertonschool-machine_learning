#!/usr/bin/env python3
"""Script to perform a strided convolution"""

import numpy as np


def convolve_grayscale(images, kernel, padding='same', stride=(1, 1)):
    """Function to perform a grayscale convolution"""
    m = images.shape[0]
    h = images.shape[1]
    w = images.shape[2]
    kh = kernel.shape[0]
    kw = kernel.shape[1]
    # pad_w = padding[1]
    # pad_h = padding[0]
    pad_w = 0
    pad_h = 0
    sh = stride[0]
    sw = stride[1]

    if padding == 'same':
        pad_h = int((((h - 1) * sh + kh - h) / 2) + 1)
        pad_w = int((((w - 1) * sw + kw - w) / 2) + 1)
    if type(padding) == tuple:
        pad_h = padding[0]
        pad_w = padding[1]

    image_pad = np.pad(images, pad_width=((0, 0), (pad_h, pad_h),
                                          (pad_w, pad_w)), mode='constant')

    output_h = int(((h + 2 * pad_h - kh) / sh) + 1)
    output_w = int(((w + 2 * pad_w - kh) / sw) + 1)

    out = np.zeros((m, output_h, output_w))

    image = np.arange(m)
    for i in range(output_h):
        for j in range(output_w):
            out[image, i, j] = (np.sum(image_pad[image,
                                            i * sh:((i * sh) + kh),
                                            j * sw:((j * sw) + kw)] * kernel,
                                            axis=(1, 2)))
    return out
