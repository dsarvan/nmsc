#!/usr/bin/env python
# File: linreg.py
# Name: D.Saravanan
# Date: 16/11/2020

""" Script to implement linear regression """

import numpy as np
import matplotlib.pyplot as plt

plt.rcParams["pgf.texsystem"] = "pdflatex"
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


def slope(x: np.ndarray, y: np.ndarray, n: int) -> float:
    """Compute the slope

    Args:
        x: independet variable
        y: dependent variable
        n: number of variables
    """
    return sum((x - np.mean(x)) * (y - np.mean(y))) / sum((x - np.mean(x)) ** 2)


def intercept(x: np.ndarray, y: np.ndarray, m: float) -> float:
    """Compute the intercept

    Args:
        x: independent variable
        y: dependent variable
        m: gradient value
    """
    return np.mean(y) - m * np.mean(x)


height = np.array([151, 174, 138, 186, 128, 136, 179, 163, 152, 131])
weight = np.array([63, 81, 56, 91, 47, 57, 76, 72, 62, 48])

n = len(height)
m = slope(height, weight, n)
c = intercept(height, weight, m)

# predicted weight with values m and c
predicted_y = np.array([m * x + c for x in height])
residuals = [x1 - x2 for (x1, x2) in zip(predicted_y, weight)]
print(sum(residuals))


def rmse(p: np.ndarray, y: np.ndarray, n: int) -> float:
    """Error estimation (Root Mean Squared Error)

    Args:
        p: predicted dependent variable
        y: dependent variable
        n: number of variables
    """
    return np.sqrt(sum((p - y) ** 2) / n)


err = rmse(predicted_y, weight, n)
print(err)

fig, ax = plt.subplots()
ax.plot(height, weight, "b.", label="data points")
ax.plot(height, predicted_y, "r-", label="predicted data")
ax.set(xlabel="height", ylabel="weight")
ax.set_title("Linear regression")
ax.grid(True)
ax.legend()
plt.savefig("linreg.png")
