#!/usr/bin/env python
# File: rungefunction.py
# Name: D.Saravanan
# Date: 27/08/2021

""" Script to construct the polynomial interpolation 
for Runge Function using Lagrange polynomial """

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


N = 9

xnodes = np.linspace(-1,1,N)
fnodes = 1/(1 + 25 * xnodes**2)

# true function calculated with equi-spaced nodes
x = np.linspace(-1,1,1000)
f = 1/(1 + 25 * x**2)

fintp = interpolate(fnodes, xnodes, x)

error = max(abs(f - fintp)/abs(f))
print(error)

fig, ax = plt.subplots()
ax.plot(x, f, c='olive', ls='dotted', label=r'$\displaystyle \frac{1}{1+25x^{2}}$')
ax.plot(x, fintp, c='teal', label=r'$Interpolation$')
ax.plot(xnodes, fnodes, 'm.', label=r'$N = 9$')
ax.set(xlabel=r'$x$', ylabel=r'$\displaystyle \frac{1}{1+25x^{2}}$')
ax.set_title(r'Runge Function')
ax.grid(True); ax.legend()
plt.savefig('rungefunction.pdf')
