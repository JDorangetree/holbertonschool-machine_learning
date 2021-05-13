#!/usr/bin/env python3
"""class Poisson that represents a poisson distribution"""

pi = 3.1415926536
e = 2.7182818285


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

    def z_score(self, x):
        """Calculates the z-score of a given x-value"""
        z = (x - self.mean) / self.stddev
        return(z)

    def x_value(self, z):
        """Calculates the z-score of a given x-value"""
        x = (z * self.stddev) + self.mean
        return(x)

    def pdf(self, x):
        """Calculates the value of the PDF for a given x-value"""
        var = pow(self.stddev, 2)
        exp = pow((x - self.mean), 2) / (2*var)
        factor2 = pow(e, -exp)
        root = pow(2*pi, 0.5)
        factor1 = (1 / self.stddev) * (1 / root)
        pdf = factor1 * factor2
        return(pdf)

    def cdf(self, x):
        """Calculates the value of the CDF for a given x-value"""
        x = (x - self.mean) / (self.stddev * pow(2, 0.5))
        factor_error = (x - (pow(x, 3) / 3) + (pow(x, 5) / 10) -
         (pow(x, 7) / 42) + (pow(x, 9) / 216))
        erf = factor_error * (2 / (pow(pi, 0.5)))
        cdf = 0.5 * (1 + erf)
        return(cdf)
