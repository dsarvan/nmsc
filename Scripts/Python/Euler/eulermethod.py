#!/usr/bin/env python
# File: eulermethod.py
# Name: D.Saravanan
# Date: 02/12/2021

""" Script to implement the Euler explicit & implicit scheme for y' = -0.5*y with y(0) = 1 """

import numpy as np
import matplotlib.pyplot as plt
plt.style.use('classic')
plt.rcParams.update(
    {
        "font.family": "serif",
        "font.size": 8,
        "axes.labelsize": 10,
        "axes.titlesize": 10,
        "figure.titlesize": 10,
    }
)
plt.rcParams["text.usetex"] = True

t_ = 25                     # time period
dt = 0.5                    # time step
N = int(t_/dt)              # number of steps
t = np.zeros(N+1)           # time vector
y1 = np.ones(N+1)           # solution vector of euler explicit
y2 = np.ones(N+1)           # solution vector of euler implicit

for k in range(0, N):
    t[k+1] = t[k] + dt
    y1[k+1] = y1[k]*(1 - 0.5*dt)
    y2[k+1] = y2[k]/(1 + 0.5*dt)

exact = np.exp(-0.5*t)      # exact solution

figure, ax = plt.subplots()
ax.plot(t, y1, "r.", label=r"euler explicit")
ax.plot(t, y2, "b.", label=r"euler implicit")
ax.plot(t, exact, "k-", label=r"exact solution")
ax.set(xlabel=r"t", ylabel=r"y(t)")
ax.set_title(r"Euler explicit \& implicit scheme")
ax.grid(True); ax.legend()
plt.savefig("eulermethod.png")
