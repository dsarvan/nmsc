#!/usr/bin/env python
# File: problem6.py
# Name: D.Saravanan
# Date: 02/12/2021

""" Script to plot the function exp(-x**2) """

import numpy as np
import matplotlib
import matplotlib.pyplot as plt
plt.style.use('classic')

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

x = np.linspace(-1, 1, 1000)
f = lambda x: np.exp(-x**2)

fig, ax = plt.subplots()
ax.plot(x, f(x), label=r"$exp(-x^2)$")
ax.set(xlabel=r"$x$", ylabel=r"$f(x) = exp(-x^2)$")
ax.grid(True); ax.legend()
plt.savefig("problem6.png")
