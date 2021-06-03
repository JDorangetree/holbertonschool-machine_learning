#!/usr/bin/env python3
"""Script to perform a convolution of images with multiple kernels"""

import numpy as np


def pool(images, kernel_shape, stride, mode='max'):
    """Function to perform a convolution of img with channels"""
    m = images.shape[0]
    h = images.shape[1]
    w = images.shape[2]
    c = images.shape[3]
    kh = kernel_shape[0]
    kw = kernel_shape[1]
    sh = stride[0]
    sw = stride[1]

    output_h = int(1 + ((h - kh) / sh))
    output_w = int(1 + ((w - kw) / sw))

    out = np.zeros((m, output_h, output_w, c))

    image = np.arange(m)

    for i in range(output_h):
        for j in range(output_w):
            if mode == 'max':
                out[image, i, j] = (np.max(images[image,
                                    i * sh:((i * sh) + kh),
                                                j * sw:((j * sw) + kw)],
                                    axis=(1, 2)))
            elif mode == 'avg':
                out[image, i, j] = (np.mean(images[image,
                                    i * sh:((i * sh) + kh),
                                                 j * sw:((j * sw) + kw)],
                                    axis=(1, 2)))
    return out
