#!/usr/bin/env python3
"""class Poisson that represents a poisson distribution"""


class Poisson():
    """The class to call method of poisson distribution"""
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
            self.lambtha = (sum(data) / len(data))

    def pmf(self, k):
        """Calculates the value of the PMF for a given number of successes"""
        e = 2.7182818285
        if type(k) != int:
            k = int(k)
        if k < 0:
            return(0)
        factorial = 1
        for i in range(1, k + 1):
            factorial = factorial * i
        
        pmf = pow(e, -(self.lambtha)) * pow(self.lambtha, k) / factorial
        return(pmf)
