#!/usr/bin/env python
# File: program7.py
# Name: D.Saravanan
# Date: 02/12/2021

""" Script to evaluate an integral using rectangular rule """

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
a, b = 0, 1

# function to be integrated
def f(x):
    return np.exp(-x)/np.sqrt(x)


# function with chnage of variable
def g(t):
    return 2 * np.exp(-t**2)


# exact value of the integral
exact = 1.49364826562485405080

# number of grid points
N = [5, 10, 20, 50, 100, 200, 500, 1000]
n = np.array(N)

# number of different set of grids
Ngrids = len(N)

h = np.zeros(Ngrids)        # different grid spacings

rect = np.zeros(Ngrids)     # rectangular rule
recv = np.zeros(Ngrids)     # rectangular rule with change of variables

for k, N in enumerate(N):
    h[k] = (b - a) / (N - 1)        # grid spacing
    x = np.linspace(a, b, N)        # grid points
    y = 0.5*(x[0:N-1] + x[1:N])

    rect[k] = h[k]*np.sum(f(y))
    recv[k] = h[k]*np.sum(g(y))


# error calculations
rect_err = abs(np.double(rect - exact))
recv_err = abs(np.double(recv - exact))

formatter = ScalarFormatter()
formatter.set_scientific(False)

fig, ax = plt.subplots()
ax.plot(n, rect_err, "m.--", label=r"$rectangular\ rule$")
ax.plot(n, recv_err, "b.--", label=r"$rectangular\ rule\ (x = t^2)$")
ax.set(xlabel=r"$number\ of\ grid\ points$", ylabel=r"$error\ in\ quadrature$")
ax.set_xscale("log", base=2); ax.set_yscale("log", base=10)
ax.xaxis.set_major_formatter(formatter)
ax.set_title(r"$Quadrature\ convergence$")
ax.grid(True); ax.legend(loc="lower left")
plt.savefig("program7.pgf")
