#!/usr/bin/env python
# File: program6.py
# Name: D.Saravanan
# Date: 02/12/2021

""" Script to implement the different quadrature """

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
a, b = 0, 1

# function to be integrated
def f(x):
    return np.exp(-(x ** 2))


# derivative of the function
def g(x):
    return -2 * x * np.exp(-(x ** 2))


# exact value of the integral
exact = 0.746824132812427025399

# number of grid points
N = [2, 5, 10, 20, 50, 100]

# number of different set of grids
Ngrids = len(N)

h = np.zeros(Ngrids)

trap = np.zeros(Ngrids)
tend = np.zeros(Ngrids)

for k, N in enumerate(N):
    h[k] = (b - a) / (N - 1)
    x = np.linspace(a, b, N)

    trap[k] = h[k] * (np.sum(f(x)) - (f(a) + f(b)) / 2)
    tend[k] = trap[k] - h[k] ** 2 / 12 * (g(b) - g(a))


# error calculations
trap_err = abs(np.double(trap - exact))
tend_err = abs(np.double(tend - exact))

fig, ax = plt.subplots()
ax.loglog(h, trap_err, "b.--", label=r"trapezoidal")
ax.loglog(h, tend_err, "r.--", label=r"trependpont")
ax.set(xlabel=r"grid size", ylabel=r"error in quadrature")
ax.set_title(r"Quadrature convergence")
ax.grid(True)
ax.legend()
plt.savefig("program6.png")
