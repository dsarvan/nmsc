#!/usr/bin/env python
# File: leastsquares.py
# Name: D.Saravanan
# Date: 03/09/2021

""" Script to compute Least-square """

import numpy as np
import matplotlib
matplotlib.rcParams['pgf.texsystem'] = 'pdflatex'
matplotlib.rcParams.update({'font.family': 'serif', 'font.size': 8,
    'axes.labelsize': 10, 'axes.titlesize': 10, 'figure.titlesize': 10})
matplotlib.rcParams['text.usetex'] = True
import matplotlib.pyplot as plt
matplotlib.use('Agg')

# degree of the polynomial
M = 10

# data is given at N+1 points
N = 1000

# true function calculated with equi-spaced nodes
x = np.linspace(-1, 1, N+1)
f = 1/(1 + 25 * x**2)

# desired matrix of size (N+1, M+1)
X = np.ones((N+1, M+1))

for k in range(1, M+1):
    X[:, k] = x**k

# condition number of the matrix X
cond_X = np.linalg.cond(X)

# condition number of transpose of X with X
cond_XX = np.linalg.cond(X.T @ X)

# QR decomposition of the matrix X
Q, R = np.linalg.qr(X)

# condition number of the matrix R (same as the condition number of the matrix X)
cond_R = np.linalg.cond(R)

#print(cond_X, cond_XX, cond_R)

# solution to the equation: R a = Q.T f
a = np.linalg.solve(R, Q.T@f)
# check that the solution is correct (True)
#print(np.allclose(R@a, Q.T@f))

# computing the least-squares 
ls = X @ a

fig, ax = plt.subplots()
ax.plot(x, f, c='olive', ls='dotted', label=r'$\displaystyle\frac{1}{1+25 x^{2}}$')
ax.plot(x, ls, c='teal', label=r'$Least-Squares$')
ax.set(xlim=(-1, 1), ylim=(0, 1.1))
ax.set(xlabel=r'$x$', ylabel=r'$\displaystyle\frac{1}{1+25 x^{2}}$')
ax.set_title(r'Least-Squares approximation')
ax.grid(True); ax.legend()
plt.savefig('leastsquares.pdf')
