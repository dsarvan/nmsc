#!/usr/bin/env python
# File: program8.py
# Name: D.Saravanan
# Date: 02/12/2021

""" Script to compute the angular displacement and angular velocity for a simple
pendulum using Euler's method """

import matplotlib.pyplot as plt
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

t_ = 100  # time period (s)

for n, dt in enumerate([0.01, 0.02, 0.05, 0.1, 0.2, 0.5, 1, 2, 5, 10, 20]):  # time step

    N = int(t_ / dt)  # number of steps
    t = np.zeros(N + 1)  # time vector (s)

    theta1 = np.ones(N + 1)  # angular displacement
    omega1 = np.ones(N + 1)  # angular velocity

    theta1[0] = np.pi / 6  # initial value of angular displacement (rad)
    omega1[0] = 0.0  # initial value of angular velocity (1/s)

    theta2 = np.ones(N + 1)  # angular displacement
    omega2 = np.ones(N + 1)  # angular velocity

    theta2[0] = np.pi / 6  # initial value of angular displacement (rad)
    omega2[0] = 0.0  # initial value of angular velocity (1/s)

    theta3 = np.ones(N + 1)  # angular displacement
    omega3 = np.ones(N + 1)  # angular velocity

    theta3[0] = np.pi / 6  # initial value of angular displacement (rad)
    omega3[0] = 0.0  # initial value of angular velocity (1/s)

    for k in range(0, N):

        t[k + 1] = t[k] + dt

        # forward euler
        theta1[k + 1] = theta1[k] + omega1[k] * dt
        omega1[k + 1] = omega1[k] - np.sin(theta1[k]) * dt

        # backward euler
        theta2[k + 1] = theta2[k] + (omega2[k] - np.sin(theta2[k]) * dt) * dt
        omega2[k + 1] = omega2[k] - np.sin(theta2[k] + omega2[k] * dt) * dt

        # trapezoidal scheme
        theta3[k + 1] = theta3[k] + (dt / 2) * (
            omega3[k] + omega3[k] - np.sin(theta3[k]) * dt
        )
        omega3[k + 1] = omega3[k] - (dt / 2) * (
            np.sin(theta3[k]) + np.sin(theta3[k] + dt * omega3[k])
        )

    figure, ax = plt.subplots()
    ax.plot(t, theta1, "r-", label=r"$euler\ explicit$")
    ax.plot(t, theta2, "b-", label=r"$euler\ implicit$")
    ax.plot(t, theta3, "k-", label=r"$trapezoidal\ scheme$")
    ax.set(xlabel=r"$time\ (s)$", ylabel=r"$\theta\ (rad)$")
    ax.set_title(r"$Simple\ pendulum\ solution\ (time\ step = {}\ (s))$".format(dt))
    ax.grid(True); ax.legend(loc="best")
    plt.savefig("program8{}.pgf".format(n))
