#!/usr/bin/env python
# File: linreg.py
# Name: D.Saravanan
# Date: 16/11/2020

""" Script to implement linear regression """

import numpy as np
import matplotlib.pyplot as plt
plt.rcParams['pgf.texsystem'] = 'pdflatex'
plt.rcParams.update({'font.family': 'serif', 'font.size': 8,
    'axes.labelsize': 10, 'axes.titlesize': 10, 'figure.titlesize': 10})
plt.rcParams['text.usetex'] = True

def slope(x, y, n):
    """ estimating the slope """
    return sum((x - np.mean(x)) * (y - np.mean(y)))/sum((x - np.mean(x))**2)

def intercept(x, y, m):
    """ estimating the intercept """
    return np.mean(y) - m * np.mean(x)

height = np.array([151, 174, 138, 186, 128, 136, 179, 163, 152, 131])
weight = np.array([63, 81, 56, 91, 47, 57, 76, 72, 62, 48])

n = len(height)
m = slope(height, weight, n)
c = intercept(height, weight, m)

# predicted weight with values m and c
predicted_y = [m*x + c for x in height]
residuals = [x1 - x2 for (x1, x2) in zip(predicted_y, weight)]
print(sum(residuals))

def rmse(p, y, n):
    """ error estimation (Root Mean Squared Error) """
    return np.sqrt(sum((p - y)**2)/n)

err = rmse(predicted_y, weight, n)
print(err)

fig, ax = plt.subplots()
ax.plot(height, weight, 'b.', label='data points')
ax.plot(height, predicted_y, 'r-', label='predicted data')
ax.set(xlabel='height', ylabel='weight')
ax.set_title('Linear regression')
ax.grid(True); ax.legend()
plt.savefig('linreg.png')
