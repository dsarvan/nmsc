#!/usr/bin/env python
# File: numerical.py
# Name: D.Saravanan
# Date: 10/03/2022

""" Script to compute the integral f(x) = cos(20*pi*x) exp(-x**2) on the interval [-1, 1] """

import numpy as np
from scipy.integrate import quad
import matplotlib.pyplot as plt
from matplotlib.ticker import ScalarFormatter

# exact value of the integral
f = lambda x: np.cos(20*np.pi*x) * np.exp(-x**2)
exact = quad(f, -1, 1)[0]

x = np.linspace(-1, 1, 1000)

N = range(1, 81)
n = np.array(N)

Ngrids = len(N)

gleg = np.zeros(Ngrids)

for k, N in enumerate(N):

    # nodes and weights calculation of gauss-legendre
    xnode, wnode = np.polynomial.legendre.leggauss(N)

    gleg[k] = np.inner(wnode, f(xnode))

# error calculations
gleg_err = abs(np.double(gleg - exact))

fig, ax = plt.subplots(1, 2, figsize=(10,4))
ax[0].plot(x, f(x))
ax[0].set(xlim=(-1, 1), xticks=np.arange(-1, 1.5, 0.5))
ax[0].set(ylim=(-1, 1), yticks=np.arange(-1, 1.2, 0.2))
ax[0].set(xlabel=r"x", ylabel=r"f(x)")
ax[0].tick_params(direction="in")
ax[1].semilogy(n, gleg_err)
ax[1].set(xlim=(0, 80), xticks=np.arange(0, 90, 10))
ax[1].set(ylim=(10**-17, 10))
ax[1].set(xlabel=r"number of points", ylabel=r"quadrature error")
ax[1].tick_params(direction="in")
fig.tight_layout()
plt.savefig("numerical.png")
