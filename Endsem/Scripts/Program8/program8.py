#!/usr/bin/env python
# File: program8.py
# Name: D.Saravanan
# Date: 02/12/2021

""" Script to compute the angular displacement and angular velocity for a simple
pendulum using Euler's method """

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

t_ = 100                    # time period

for n, dt in enumerate([0.01, 0.02, 0.05, 0.1, 0.2, 0.5, 1, 2, 5, 10, 20]):   # time step
    
    N = int(t_/dt)          # number of steps
    print(n, dt, t_, N)
    t = np.zeros(N+1)       # time vector

    theta = np.ones(N+1)    # angular displacement
    omega = np.ones(N+1)    # angular velocity

    theta[0] = np.pi/6      # initial value of angular displacement
    omega[0] = 0.0          # initial value of angular velocity

    for k in range(0, N):

        t[k+1] = t[k] + dt

        # forward euler
        theta[k+1] = theta[k] + omega[k] * dt
        omega[k+1] = omega[k] - np.sin(theta[k]) * dt

    figure, ax = plt.subplots()
    ax.plot(t, theta, "r--", label="{}".format(dt))
    ax.set(xlabel=r"$time\ (s)$", ylabel=r"$\theta\ (rad)$")
    ax.set_title(r"$Simple\ pendulum\ using\ Euler's\ methods\ (time\ step = {}\ (s))$".format(dt)) 
    ax.grid(True); ax.legend()
    plt.savefig("program8{}.png".format(n)) 
