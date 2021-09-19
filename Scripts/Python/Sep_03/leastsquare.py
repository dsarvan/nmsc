#!/usr/bin/env python
# File: leastsquare.py
# Name: D.Saravanan
# Date: 03/09/2021

""" Script to compute Least-square """

import numpy as np
import numpy.polynomial.polynomial as poly
from scipy.special import legendre
import matplotlib
matplotlib.rcParams['pgf.texsystem'] = 'pdflatex'
matplotlib.rcParams.update({'font.family': 'serif', 'font.size': 8,
    'axes.labelsize': 10, 'axes.titlesize': 10, 'figure.titlesize': 10})
matplotlib.rcParams['text.usetex'] = True
import matplotlib.pyplot as plt
matplotlib.use('Agg')

M = 10
N = 1000

x = np.linspace(-1, 1, N+1)
f = 1/(1 + 25 * x**2)

X = np.ones((N+1, M+1))

for k in range(1, M+1):
    X[:, k] = x**k

cond_X = np.linalg.cond(X)
cond_XX = np.linalg.cond(X.T @ X)

Q, R = np.linalg.qr(X)

cond_R = np.linalg.cond(R)

print(cond_X, cond_XX, cond_R)

sol = np.linalg.solve(R, Q.T@f)

f_LS = X @ sol

# check that the solution is correct
print(np.allclose(R@sol, Q.T@f))

fig, ax = plt.subplots()
ax.plot(x, f, c='olive', ls='dotted', label=r'$\displaystyle\frac{1}{1+25 x^{2}}$')
ax.plot(x, f_LS, c='teal', label=r'$Least-Squares$')
ax.set(xlabel=r'$x$', ylabel=r'$\displaystyle\frac{1}{1+25 x^{2}}$')
ax.set_title(r'Least-Squares approximation')
ax.grid(True); ax.legend()
plt.savefig('leastsquares.png')
