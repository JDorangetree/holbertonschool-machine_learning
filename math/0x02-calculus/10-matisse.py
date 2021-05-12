#!/usr/bin/env python3
"""function that calculates the derivative of a polynomial"""


def poly_derivative(poly):
    """return a list"""
    new_poly = poly[1:]
    if len(new_poly) == 0:
        return([0])
    
    result = []
    mul = 1
    for i in new_poly:
        valor = i * mul
        mul += 1
        result.append(valor)
    return(result)
