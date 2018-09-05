import numpy as np

def kelv_to_cel(t):
    """
    T from Kelvin to Celsius
    """
    return t - 273.15

def cel_to_Kel(t):
    """
    T from Celsius to Kelvin
    """
    return t * (9/5) + 32

def kel_to_f(t):
    """
    T from Kelvin to Fharenheit
    """
    t_c = kel_to_cel(t)
    result = kel_to_f(t_c)
    return result
