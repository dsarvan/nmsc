#!/usr/bin/env python
# File: program6.py
# Name: D.Saravanan
# Date: 02/12/2021

""" Script to implement quadrature methods and see how the error behaves """

import matplotlib
import matplotlib.pyplot as plt
import numpy as np

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
def df(x):
    return -2*x*np.exp(-x**2)


# third derivative of the function
def ddf(x):
    return 4*x*(3 - 2*x**2)*np.exp(-x**2)


# exact value of the integral
exact = 1.49364826562485405080

# number of grid points
N = [2, 5, 10, 20, 50, 100]
n = np.array(N)

# number of different set of grids
Ngrids = len(N)

h = np.zeros(Ngrids)     # different grid spacings

trap = np.zeros(Ngrids)  # trapezoidal rule
tend = np.zeros(Ngrids)  # trapezoidal rule using first derivative
tent = np.zeros(Ngrids)  # trapezoidal rule using first and third derivative
gleg = np.zeros(Ngrids)  # gauss-legendre quadrature rule

for k, N in enumerate(N):
    h[k] = (b - a) / (N - 1)
    x = np.linspace(a, b, N)

    # nodes and weights calculation of gauss-legendre
    xnode, wnode = np.polynomial.legendre.leggauss(N)

    trap[k] = h[k] * (np.sum(f(x)) - (f(a) + f(b)) / 2)
    tend[k] = trap[k] - (h[k]**2 / 12) * (df(b) - df(a))
    tent[k] = tend[k] + (h[k]**4 / 720) * (ddf(b) - ddf(a))
    gleg[k] = np.inner(wnode, f(xnode))


# error calculations
trap_err = abs(np.double(trap - exact))
tend_err = abs(np.double(tend - exact))
tent_err = abs(np.double(tent - exact))
gleg_err = abs(np.double(gleg - exact))

fig, ax = plt.subplots()
ax.loglog(n, trap_err, "b.--", label=r"trapezoidal rule")
ax.loglog(n, tend_err, "r.--", label=r"trapezoidal rule using 1st derivative")
ax.loglog(n, tent_err, "m.--", label=r"trapezoidal rule using 1st and 3rd derivative")
ax.loglog(n, gleg_err, "g.--", label=r"gauss-legendre quadrature rule")
ax.set(xlabel=r"grid size", ylabel=r"error in quadrature")
ax.set_title(r"Quadrature convergence")
ax.grid(True); ax.legend()
plt.savefig("program6.png")
