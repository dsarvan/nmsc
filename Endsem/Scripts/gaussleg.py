#!/usr/bin/env python
# File: gaussleg.py
# Name: D.Saravanan
# Date: 02/12/2021

""" Script to implement quadrature methods and see how the error behaves """

import matplotlib
import matplotlib.pyplot as plt
import numpy as np
from scipy.integrate import quad
matplotlib.rcParams["pgf.texsystem"] = "pdflatex"
matplotlib.rcParams.update(
    {
        "font.family": "serif",
        "font.size": 8,
        "axes.labelsize": 10,
        "axes.titlesize": 10,
        "figure.titlesize": 10,
    }
)
matplotlib.rcParams["text.usetex"] = True
matplotlib.use("Agg")

# end points of interval
a, b = -1, 1

# function to be integrated
def f(x):
    return np.exp(-x**2)


# first derivative of the function
def g(x):
    return -2*x*np.exp(-x**2)


# third derivative of the function
def s(x):
    return 4*x*(3 - 2*x**2)*np.exp(-x**2)


# exact value of the integral
exact = 1.49364826562485405080

# exact value and eroor term calculation
eval, errv = quad(f, -1, 1)

# number of grid points
N = [2, 5, 10, 20, 50, 100]

# number of different set of grids
Ngrids = len(N)

h = np.zeros(Ngrids)
n = np.zeros(Ngrids)

trap = np.zeros(Ngrids)  # trapezoidal rule
tend = np.zeros(Ngrids)  # trapezoidal rule using first derivative
tent = np.zeros(Ngrids)  # trapezoidal rule using first and third derivative
gleg = np.zeros(Ngrids)  # gauss-legendre quadrature rule

for k, N in enumerate(N):

    n[k] = N
    h[k] = (b - a) / (N - 1)
    x = np.linspace(a, b, N)

    trap[k] = h[k] * (np.sum(f(x)) - (f(a) + f(b)) / 2)
    tend[k] = trap[k] - (h[k]**2 / 12) * (g(b) - g(a))
    tent[k] = tend[k] + (h[k]**4 / 720) * (s(b) - s(a))

    # nodes and weights calculations of gauss-legendre
    xnode, wnode = np.polynomial.legendre.leggauss(N)

    # integration
    gleg[k] = np.inner(wnode, f(xnode))


# error calculations
trap_err = abs(np.double(trap - exact))
tend_err = abs(np.double(tend - exact))
tent_err = abs(np.double(tent - exact))
gleg_err = abs(np.double(gleg - exact))

fig, ax = plt.subplots()
ax.loglog(h, trap_err, "b.--", label=r"trapezoidal rule")
ax.loglog(h, tend_err, "r.--", label=r"trapezoidal rule using 1st derivative")
ax.loglog(h, tent_err, "m.--", label=r"trapezoidal rule using 1st and 3rd derivative")
ax.loglog(n, gleg_err, 'g.--', label=r"gauss-legendre")
ax.set(xlabel=r"grid size", ylabel=r"error in quadrature")
ax.set_title(r"Quadrature convergence")
ax.grid(True); ax.legend()
plt.savefig("gaussleg.png")
