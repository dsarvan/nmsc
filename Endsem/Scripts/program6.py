#!/usr/bin/env python
# File: program6.py
# Name: D.Saravanan
# Date: 02/12/2021

""" Script to implement quadrature methods and see how the error behaves """

import matplotlib.pyplot as plt
from matplotlib.ticker import ScalarFormatter
import numpy as np

plt.style.use("classic")
plt.rcParams["text.usetex"] = True
plt.rcParams["pgf.texsystem"] = "pdflatex"
plt.rcParams.update(
    {
        "font.family": "serif",
        "font.size": 10,
        "axes.labelsize": 12,
        "axes.titlesize": 12,
        "figure.titlesize": 12,
    }
)

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
    h[k] = (b - a) / (N - 1)        # grid spacing
    x = np.linspace(a, b, N)        # grid points

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

formatter = ScalarFormatter()
formatter.set_scientific(False)

fig, ax = plt.subplots()
ax.plot(n, trap_err, "b.--", label=r"$trapezoidal\ rule$")
ax.plot(n, tend_err, "r.--", label=r"$trapezoidal\ rule\ 1st\ derivative$")
ax.plot(n, tent_err, "m.--", label=r"$trapezoidal\ 1st\ \&\ 3rd\ derivative$")
ax.plot(n, gleg_err, "g.--", label=r"$gauss-legendre\ quadrature\ rule$")
ax.set(xlabel=r"$number\ of\ grid\ points$", ylabel=r"$error\ in\ quadrature$")
ax.set_xscale("log", base=2); ax.set_yscale("log", base=10)
ax.xaxis.set_major_formatter(formatter)
ax.set_title(r"$Quadrature\ convergence$")
ax.grid(True); ax.legend(loc="lower left")
plt.savefig("program6.pgf")
