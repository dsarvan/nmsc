#!/usr/bin/env python
# File: program7.py
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
    return np.exp(-x)/np.sqrt(x)


# derivative of the function
def g(x):
    return -2 * x * np.exp(-(x ** 2))


# exact value of the integral
exact = 1.49364826562485405080

# number of grid points
N = [5, 10, 20, 50, 100, 200, 500, 1000]

# number of different set of grids
Ngrids = len(N)

h = np.zeros(Ngrids)

rect = np.zeros(Ngrids)

for k, N in enumerate(N):
    h[k] = (b - a) / (N - 1)
    x = np.linspace(a, b, N)
    y = 0.5*(x[0:N-1] + x[1:N])

    rect[k] = h[k]*np.sum(f(y))


# error calculations
rect_err = abs(np.double(rect - exact))

fig, ax = plt.subplots()
ax.loglog(h, rect_err, 'm.--', label=r'rectangular')
ax.set(xlabel=r"grid size", ylabel=r"error in quadrature")
ax.set_title(r"Quadrature convergence")
ax.grid(True)
ax.legend()
plt.savefig("program7.png")
