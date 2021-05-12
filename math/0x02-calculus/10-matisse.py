#!/usr/bin/env python3
"""function that calculates the derivative of a polynomial"""


def poly_derivative(poly):
    """return a list"""
    if len(poly) == 0:
        return(None)
    new_poly = poly[1:]
    if len(new_poly) == 0:
        return([0])
    poly = []
    for j in new_poly:
        if type(j) != int:
            poly.append(j)
    if len(poly) != 0:
        return(None)
    if sum(new_poly) == 0:
        return([0])
    result = []
    mul = 1
    for i in new_poly:
        valor = i * mul
        mul += 1
        result.append(valor)
    return(result)
