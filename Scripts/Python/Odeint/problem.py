#!/usr/bin/env python
# File: problem.py
# Name: D.Saravanan
# Date: 24/03/2022

""" Script to solve the differential equation with odeint """

import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt
plt.style.use('classic')
plt.rcParams.update(
    {
        "font.family": "serif",
        "font.size": 10,
        "axes.labelsize": 12,
        "axes.titlesize": 12,
        "figure.titlesize": 12,
    }
)
plt.rcParams["text.usetex"] = True

# function that returns dy/dt
def f(y, t):
   return -0.5*y


# initial condition
y0 = 1

# time points
t = np.linspace(0, 25)

# solve ODE
y = odeint(f, y0, t)

# exact solution
exact = np.exp(-0.5*t)

# plot results
figure, ax = plt.subplots()
ax.plot(t, y, "r--", label=r"$\displaystyle \frac{dy}{dt} = - 0.5 * y$")
ax.plot(t, exact, "k.", label=r"exact solution")
ax.set(xlabel=r"t", ylabel=r"y(t)")
ax.set_title(r"Solve differential equation with ODEINT")
ax.grid(True); ax.legend()
plt.savefig('problem.png')
