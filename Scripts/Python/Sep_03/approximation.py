#!/usr/bin/env python
# File: approximation.py
# Name: D.Saravanan
# Date: 03/09/2021

""" Script to compare the convergence """

import numpy as np
import matplotlib
matplotlib.rcParams['pgf.texsystem'] = 'pdflatex'
matplotlib.rcParams.update({'font.family': 'serif', 'font.size': 8,
    'axes.labelsize': 10, 'axes.titlesize': 10, 'figure.titlesize': 10})
matplotlib.rcParams['text.usetex'] = True
import matplotlib.pyplot as plt
matplotlib.use('Agg')

def interpolate(fnodes, xnodes, x):

    m, n = len(x), len(xnodes)
    p = np.zeros(m)

    for i in range(0, n):
        p = p + fnodes[i] * lagrange(xnodes, x, i)
    
    return p

def lagrange(xnodes, x, i):

    m, n = len(x), len(xnodes)
    l = np.ones(m)

    for j in range(0, n):

        if i == j:
            continue

        l = l * (x - xnodes[j]) / (xnodes[i] - xnodes[j])

    return l

def factorial(n):
    return 1 if n < 2 else n*factorial(n-1)

# degree of the polynomial
n = 10

# data is given at N+1 points
N = 1000

# true function calculated with equi-spaced nodes
x = np.linspace(-1, 1, N+1)
f = lambda x: 1/(1 + 25 * x**2)

""" polynomial interpolation using Chebyshev nodes of first kind """
m = n-1  # polynomial of degree m
xnodes = np.cos((2*np.linspace(0,m-1,m) + 1)/(2*m + 2) * np.pi)
fnodes = 1/(1 + 25 * xnodes**2)
fintpt = interpolate(fnodes, xnodes, x)

""" polynomial approximation using Bernstein polynomials """
bern = sum(map(lambda k: factorial(n)/(factorial(n-k)*factorial(k)) \
        * ((x+1)/2)**k * ((1-x)/2)**(n-k) * f(2*k/n-1), range(n+1)))

""" computing Least-Squares approximation """
# desired matrix of size (N+1, n+1)
X = np.ones((N+1, n+1))

for k in range(1, n+1):
    X[:, k] = x**k

# condition number of the matrix X
cond_X = np.linalg.cond(X)

# condition number of transpose of X with X
cond_XX = np.linalg.cond(X.T @ X)

# QR decomposition of the matrix X
Q, R = np.linalg.qr(X)

# condition number of the matrix R (same as the condition number of the matrix X)
cond_R = np.linalg.cond(R)

# solution to the equation: R a = Q.T f
a = np.linalg.solve(R, Q.T@f(x))

# computing the least-squares
ls = X @ a

fig, ax = plt.subplots()
ax.plot(xnodes, fnodes, 'k.', label=r'$n = {}$'.format(n))
ax.plot(x, f(x), c='#005249', ls='dotted', label=r'$\displaystyle\frac{1}{1+25 x^{2}}$')
ax.plot(x, ls, c='#fdb915', ls='dotted', label=r'$Least-Squares$')
ax.plot(x, fintpt, c='#f5054f', ls='dotted', label=r'$Interpolation$')
ax.plot(x, bern, c='#952e8f', ls='dotted', label=r'$Bernstein$')
ax.set(xlim=(-1, 1), ylim=(0, 1.1))
ax.set(xlabel=r'$x$', ylabel=r'$\displaystyle\frac{1}{1+25 x^{2}}$')
ax.set_title(r'Interpolation and Approximation')
ax.grid(True); ax.legend()
plt.savefig('approximation.pdf')
