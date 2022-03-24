#!/usr/bin/env python
# File: pendulum.py
# Name: D.Saravanan
# Date: 02/12/2021

import numpy as np
import matplotlib.pyplot as plt

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

t_ = 100
dt = 0.01
N = int(t_/dt)
t = np.zeros(N+1)
y1 = np.ones(N+1)
y2 = np.ones(N+1)

th0 = 0.5



for k in range(0, N):
    t[k+1] = t[k] + dt
    y1[k+1] = y1[k]*(1 - 1*dt)
    y2[k+1] = y2[k]*(1 + 1*dt)

exact = np.sin(t) + np.cos(t)

figure, ax = plt.subplots()
#ax.plot(t, y1, "r.", label=r"euler explicit")
ax.plot(t, y2, "b.", label=r"euler implicit")
ax.plot(t, exact, "k-", label=r"exact solution")
ax.grid(True); ax.legend()
plt.savefig("pendulum.png")
