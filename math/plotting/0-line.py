#!/usr/bin/env python3
"""function that show a line"""

import numpy as np
import matplotlib.pyplot as plt


def line():
    """plt show"""
    y = np.arange(0, 11) ** 3
    plt.figure(figsize=(6.4, 4.8))
    plt.xlim(0, 10)
    plt.plot(y, color='r')
    plt.show()
