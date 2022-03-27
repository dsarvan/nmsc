#!/usr/bin/env python

import numpy as np
import matplotlib.pyplot as plt

plt.style.use("classic")
plt.rcParams.update(
    {
        "font.family": "serif",
        "font.size": 10,
        "axes.labelsize": 12,
        "axes.titlesize": 12,
        "figure.titlesize": 12,
    }
)


t_ = 40                 # time period
dt = 0.05               # time step
N = int(t_/dt)          # number of steps
t = np.zeros(N+1)       # time vector

theta = np.ones(N+1)    # angular displacement
omega = np.ones(N+1)    # angular velocity

theta[0] = 0.5          # initial value of angular displacement
omega[0] = 0.0          # initial value of angular velocity

for k in range(0, N):
    t[k+1] = t[k] + dt

    theta[k+1] = (theta[k] + dt * omega[k]) / (1 + dt**2)
    omega[k+1] = (omega[k] - dt * theta[k]) / (1 + dt**2) 

figure, ax = plt.subplots()
ax.plot(theta, omega, "r--", label=r"$angular\ displacement$")
ax.set(xlabel=r"$time\ (s)$", ylabel=r"$\theta\ (rad)$")
ax.set_title(r"$Simple\ pendulum\ using\ Euler's\ method$")
ax.grid(True); ax.legend()
plt.savefig("spendulum.png")
