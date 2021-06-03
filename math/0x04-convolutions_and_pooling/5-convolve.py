#!/usr/bin/env python3
"""Script to perform a convolution of images with multiple kernels"""

import numpy as np


def convolve(images, kernels, padding='same', stride=(1, 1)):
    """Function to perform a convolution of img with channels"""
    m = images.shape[0]
    h = images.shape[1]
    w = images.shape[2]
    kh = kernels.shape[0]
    kw = kernels.shape[1]
    nc = kernels.shape[3]  # Needs to be the same frequency of c
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
                                          (pad_w, pad_w), (0, 0)),
                       mode='constant')

    output_h = int(((h + 2 * pad_h - kh) / sh) + 1)
    output_w = int(((w + 2 * pad_w - kw) / sw) + 1)

    out = np.zeros((m, output_h, output_w, nc))

    image = np.arange(m)
    for i in range(output_h):
        for j in range(output_w):
            for w in range(nc):
                out[image, i, j, w] = (np.sum(image_pad[image,
                                       i * sh:((i * sh) + kh),
                                                j * sw:((j * sw) + kw)] *
                                       kernels[:, :, :, w],
                                       axis=(1, 2, 3)))
    return out
