import numpy as np

def kelv_to_celsius(temp):
"""COnvert a temperature from Kelvin to Celsius"""
    return t -273.15

def cel_to_fahr(temp):
"""Convert a temp from Celsius to Fahr"""
    return t * (9/5) + 32

def kel_to_fahr(temp):
"""Convert temp from kelvin to fahr"""
    t_c = kel_to_cel(temp)
    result = kel_to_fahr(t_c)
    return result
