#!/usr/bin/env python
# File: gausslag.py
# Name: D.Saravanan
# Date: 08/03/2022

""" Script to calculate nodes and weights of Gauss-Laguerre quadrature """

import numpy as np
from scipy.integrate import quad
import matplotlib.pyplot as plt

# exact value of the integral
f = lambda x: np.exp(-x)*np.sin(x**2)
exact = quad(f, 0, np.inf)[0]

# nodes and weights calculations
x, w = np.polynomial.laguerre.laggauss(10)

# integration
integral = np.inner(w, np.exp(-x)*np.sin(x**2))

# error calculation
error = abs(np.double(integral - exact))

print(exact, integral, error)
