#!/usr/bin/env python
# File: pendulum1.py
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

t_ = 40                 # time period
dt = 0.05               # time step
N = int(t_/dt)          # number of steps
t = np.zeros(N+1)       # time vector

explicit_theta = np.ones(N+1)    # angular displacement
explicit_omega = np.ones(N+1)    # angular velocity

implicit_theta = np.ones(N+1)    # angular displacement
implicit_omega = np.ones(N+1)    # angular velocity

theta = np.ones(N+1)
omega = np.ones(N+1)

explicit_theta[0] = 0.5          # initial value of angular displacement
explicit_omega[0] = 0.0          # initial value of angular velocity

implicit_theta[0] = 0.5          # initial value of angular displacement
implicit_omega[0] = 0.0          # initial value of angular velocity

theta[0] = 0.5
omega[0] = 0.0


for k in range(0, N):

    t[k+1] = t[k] + dt

    explicit_theta[k+1] = explicit_theta[k] + explicit_omega[k] * dt
    explicit_omega[k+1] = explicit_omega[k] - np.sin(explicit_theta[k]) * dt

    implicit_theta[k+1] = implicit_theta[k] + implicit_omega[k+1] * dt
    implicit_omega[k+1] = implicit_omega[k] - np.sin(implicit_theta[k+1]) * dt

    theta[k+1] = theta[k] + (dt/2) * (theta[k] + theta[k+1])
    omega[k+1] = omega[k] - (dt/2) * (np.sin(theta[k]) + np.sin(theta[k+1]))


figure, ax = plt.subplots()
ax.plot(t, explicit_theta, "r--", label=r"$euler\ explicit$")
#ax.plot(t, implicit_theta, "b--", label=r"$euler\ implicit$")
#ax.plot(t, theta, "k--", label=r"$trapezoidal\ scheme$")
ax.set(xlabel=r"$time\ (s)$", ylabel=r"$\theta\ (rad)$")
ax.set_title(r"$Simple\ pendulum\ using\ Euler's\ method$")
ax.grid(True); ax.legend()
plt.savefig("pendulum1.png")
