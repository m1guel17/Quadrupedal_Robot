import numpy as np
import sympy as sp
from sympy import symbols as syms
dx = sp.symbols("dx"); dy = sp.symbols("dy"); dz = sp.symbols("dz")
x = syms("x"); y = syms("y"); z = syms("z")

# =============================================================================
# Pure Rotation about the x-axis | Rotation about the n-axis | ROLL
def trotx(x):
    if type(x) == sp.Symbol or type(x) == sp.Mul:
        return np.matrix([[1,         0,         0, 0],
                          [0, sp.cos(x),-sp.sin(x), 0],
                          [0, sp.sin(x), sp.cos(x), 0],
                          [0,         0,         0, 1]])
    else:
        return np.matrix([[1,         0,         0, 0],
                          [0, np.cos(x),-np.sin(x), 0],
                          [0, np.sin(x), np.cos(x), 0],
                          [0,         0,         0, 1]])
# =============================================================================
# Pure Rotation about the y-axis | Rotation about the o-axis | PITCH
def troty(y):
    if type(y) == sp.Symbol or type(y) == sp.Mul:
        return np.matrix([[sp.cos(y), 0, sp.sin(y), 0],
                          [0,         1,         0, 0],
                          [-sp.sin(y),0, sp.cos(y), 0],
                          [0,         0,         0, 1]])
    else:
        return np.matrix([[np.cos(y), 0, np.sin(y), 0],
                          [0,         1,         0, 0],
                          [-np.sin(y),0, np.cos(y), 0],
                          [0,         0,         0, 1]])
# =============================================================================

# Pure Rotation about the z-axis | Rotation about the a-axis | YAW
def trotz(z):
    if type(z) == sp.Symbol or type(z) == sp.Mul:
        return np.matrix([[sp.cos(z),-sp.sin(z), 0, 0],
                          [sp.sin(z), sp.cos(z), 0, 0],
                          [0,         0,         1, 0],
                          [0,         0,         0, 1]])
    else:
        return np.matrix([[np.cos(z),-np.sin(z), 0, 0],
                          [np.sin(z), np.cos(z), 0, 0],
                          [0,         0,         1, 0],
                          [0,         0,         0, 1]])
# =============================================================================

# Composed Rotations | trotx(x)@troty(y)@trotz(z)
def trotxyz(x,y,z):
    return trotx(x)*troty(y)*trotz(z)
# =============================================================================

# Pure Translation along the xyz axes | Pure Translation along the noa axes
def transl(x,y,z):
    if type(x) == sp.Symbol or type(y) == sp.Symbol or type(z) == sp.Symbol:
        return np.matrix([[1, 0, 0, x],
                          [0, 1, 0, y],
                          [0, 0, 1, z],
                          [0, 0, 0, 1]])
    else:
        return np.matrix([[1, 0, 0, x],
                          [0, 1, 0, y],
                          [0, 0, 1, z],
                          [0, 0, 0, 1]])
    

"""
θ1 = syms("θ1")
θ2 = syms("θ2")
θ3 = syms("θ3")
π = syms("π")
L1 = syms("L1")
L2 = syms("L2")
L3 = syms("L3")

T01 = trotz(θ1)*transl(0,0,0)*transl(L1,0,0)*trotx(0)
T12 = trotz(-π/2)*transl(0,0,0)*transl(0,0,0)*trotx(-π/2)
T23 = trotz(θ2)*transl(0,0,0)*transl(L2,0,0)*trotx(0)
T34 = trotz(θ3)*transl(0,0,0)*transl(L3,0,0)*trotx(0)
"""