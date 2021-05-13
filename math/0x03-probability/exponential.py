#!/usr/bin/env python3
"""class Poisson that represents a Exponential distribution"""


class Exponential():
    """The class to call method of Exponential distribution"""
    def __init__(self, data=None, lambtha=1.):
        """Initialize method"""
        if data is None:
            if lambtha > 0:
                self.lambtha = float(lambtha)
            else:
                raise ValueError("lambtha must be a positive value")
        else:
            if type(data) != list:
                raise TypeError('data must be a list')
            if len(data) < 2:
                raise ValueError('data must contain multiple values')
            self.lambtha = 1 / ((sum(data) / len(data)))

    def pdf(self, x):
        """Calculates the value of the PDF for a given time period"""
        e = 2.7182818285
        if x < 0:
            return(0)
        pdf = self.lambtha * (pow(e, (-self.lambtha * x)))
        return(pdf)
