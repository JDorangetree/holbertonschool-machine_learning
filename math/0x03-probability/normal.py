#!/usr/bin/env python3
"""class Poisson that represents a poisson distribution"""


class Normal():
    """The class to call method of poisson distribution"""
    def __init__(self, data=None, mean=0., stddev=1.):
        """Initialize method"""
        if data is None:
            if stddev > 0:
                self.stddev = float(stddev)
                self.mean = float(mean)
            else:
                raise ValueError("stddev must be a positive value")
        else:
            if type(data) != list:
                raise TypeError('data must be a list')
            if len(data) < 2:
                raise ValueError('data must contain multiple values')
            self.mean = (sum(data) / len(data))
            sumarize = 0
            for i in data:
                value = i - self.mean
                if value < 0:
                    value = value * (-1)
                sumarize = sumarize + pow(value, 2)
            self.stddev = pow((sumarize / len(data)), 0.5)
