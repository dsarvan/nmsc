#!/usr/bin/env python
# File: gaussleg.py
# Name: D.Saravanan
# Date: 08/03/2022

""" Script to calculate nodes and weights of Gauss-Legendre quadrature """

import numpy as np
from scipy.integrate import quad

# exact value of the integral
f = lambda x: np.sin(x**2)
exact = quad(f, -1, 1)[0]

# nodes and weights calculations
x, w = np.polynomial.legendre.leggauss(10)

# integration
integral = np.inner(w, np.sin(x**2))

# error calculation
error = abs(np.double(integral - exact))

print(exact, integral, error)
