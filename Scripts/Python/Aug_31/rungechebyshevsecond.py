#!/usr/bin/env python
# File: rungechebyshevfirst.py
# Name: D.Saravanan
# Date: 31/08/2021

""" Script to construct the polynomial interpolation 
for Runge Function using Chebyshev nodes of Second kind """

import numpy as np
import matplotlib
matplotlib.rcParams['pgf.texsystem'] = 'pdflatex'
matplotlib.rcParams.update({'font.family': 'serif', 'font.size': 8, 
    'axes.labelsize': 10, 'axes.titlesize': 10, 'figure.titlesize': 10})
matplotlib.rcParams['text.usetex'] = True
import matplotlib.pyplot as plt
matplotlib.use('Agg')

def interpolate(fnodes, xnodes, x):

    M, N = len(x), len(xnodes)
    res = np.zeros(M)

    for i in range(0, N):
        res = res + fnodes[i] * lagrange(xnodes, x, i)
    
    return res

def lagrange(xnodes, x, i):

    M, N = len(x), len(xnodes)
    val = np.ones(M)

    for j in range(0, N):

        if i == j:
            continue

        val = val * (x - xnodes[j]) / (xnodes[i] - xnodes[j])

    return val


N = 21

xnodes = np.cos((np.linspace(0,N-1,N) + 1)/(N + 2) * np.pi)
fnodes = 1/(1 + 25 * xnodes**2)

# true function calculated with equi-spaced nodes
x = np.linspace(-1,1,1000)
f = 1/(1 + 25 * x**2)

fintp = interpolate(fnodes, xnodes, x)

error = max(abs(f - fintp)/abs(f))
print(error)

fig, ax = plt.subplots()
ax.plot(x, f, 'r', label=r'$N = {}$'.format(N))
ax.plot(x, fintp, 'g', label=r'$N = {}$'.format(N))
ax.plot(xnodes, fnodes, 'b*')
ax.set(xlim=(-1, 1), ylim=(0, 1.1))
ax.set(xlabel=r'$x$', ylabel=r'$\cos\big(\frac{(x+1) \pi} {N+2}\big)$')
ax.set_title(r'Runge Function with Chebyshev nodes of Second kind')
ax.grid(True); ax.legend()
plt.savefig('rungechebyshevsecond.png')
