#!/usr/bin/env python
# File: gausshermite.py
# Name: D.Saravanan
# Date: 08/03/2022

""" Script to calculate nodes and weights of Gauss-Hermite quadrature """

import numpy as np
from scipy.integrate import quad

# exact value of the integral
f = lambda x: x**4 * np.exp(-x**2)
exact = quad(f, -inf, inf)[0]

# nodes and weights calculations
x, w = np.polynomial.hermite.hermgauss(10)

# integration
integral = np.inner(w, x**4)

# error calculation
error = abs(np.double(integral - exact))

print(exact, integral, error)
