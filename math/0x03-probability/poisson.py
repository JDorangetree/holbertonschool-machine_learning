#!/usr/bin/env python3
"""class Poisson that represents a poisson distribution"""


class Poisson():
    """The class to call method of poisson distribution"""
    
    e = 2.7182818285
    def __init__(self, data=None, lambtha=1.):
        """Initialize method"""
       
        if data == None:
            if lambtha >= 0:
                self.lambtha = float(lambtha)
            else:
               raise ValueError("lambtha must be a positive value")
        else:
            if type(data) != list:
                raise TypeError('data must be a list')
            if len(data) < 2:
                raise ValueError('data must contain multiple values')
            self.lambtha =  (sum(data) / len(data))
