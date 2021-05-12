#!/usr/bin/env python3
"""function that calculates sum i^2"""


def square(numero):
    """return list"""
    return(pow(numero, 2))


def summation_i_squared(n):
    """return integer"""
    if type(n) == int and n > 0:
        list_numeros = list(range(1, n + 1))
        resultado = sum(list(map(square, list_numeros)))
        return(resultado)
    else:
        return(None)
