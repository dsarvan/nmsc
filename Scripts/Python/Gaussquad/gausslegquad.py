#!/usr/bin/env python
# File: gausslegquad.py
# Name: D.Saravanan
# Date: 08/03/2022

""" Script to evaluate integral exp(-x**2) from -1 to +1 """

import numpy as np
from scipy.integrate import quad
import matplotlib.pyplot as plt

# exact value of the integral
f = lambda x: np.exp(-x**2)
exact = quad(f, -1, 1)[0]

N = [2, 5, 10, 20, 50, 100]

n, error = [], []

for k in N:

    n.append(k)

    # nodes and weights calculations
    x, w = np.polynomial.legendre.leggauss(k)

    # integration
    integral = np.inner(w, np.exp(-x**2))

    # error calculation
    error.append(abs(np.double(integral - exact)))

fig, ax = plt.subplots()
ax.loglog(n, error, 'r.--', label=r'Gauss-Legendre')
ax.set_title(r"Error plot of Gauss-Legendre quadrature")
ax.set(xlabel=r"n", ylabel=r"error in quadrature")
ax.grid(True); ax.legend()
plt.savefig('gausslegquad.png')
