#!/usr/bin/env python
# File: eulermethod.py
# Name: D.Saravanan
# Date: 02/12/2021

""" Script to implement the Euler explicit schme for y' = -10y with y(0) = 1 """

import matplotlib
import numpy as np
import matplotlib.pyplot as plt
plt.style.use('classic')

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

t_ = 10                     # time period
dt = 0.01                   # time step
N = int(t_/dt)              # number of steps
t = np.zeros(N+1)           # time step vector
y = np.zeros(N+1)           # solution vector
t[0] = 0
y[0] = 1

for k in range(0, N):
    t[k+1] = t[k] + dt
    y[k+1] = y[k] + dt * (-10*y[k])

exact = np.exp(-10*t)

figure, ax = plt.subplots()
ax.plot(t, y, 'r+')
ax.plot(t, exact, 'k')
plt.savefig('eulermethod.png')
