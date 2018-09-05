import numpy as np

def kelv_to_cel(t):
    return t -273.15

def cel_to_Kel(t):
    return t * (9/5) + 32

def kel_to_f(t):
    t_c = kel_to_cel(t)
    result = kel_to_f(t_c)
    return result
