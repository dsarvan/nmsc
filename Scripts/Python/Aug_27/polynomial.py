#!/usr/bin/env python
# File: polynomial.py
# Name: D.Saravanan
# Date: 27/08/2021

""" Script to construct the polynomial interpolation using Lagrange polynomial """

import numpy as np
import matplotlib
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
fnodes = np.sin(np.pi*xnodes)
#fnodes = 1/(1 + 25 * xnodes**2)

x = np.linspace(-1,1,1000)
f = np.sin(np.pi*x)
#f = 1/(1 + 25 * x**2)

fintp = interpolate(fnodes, xnodes, x)

error = max(abs(f - fintp)/abs(f))
print(error)

fig, ax = plt.subplots()
ax.plot(x, f, 'r')
ax.plot(x, fintp, 'g')
ax.plot(xnodes, fnodes, 'b*')
ax.set(xlim=(-1, 1), ylim=(-1.2, 1.2))
ax.set_title(r"Lagrange polynomial interpolation", fontsize=11)
ax.grid(True)
plt.savefig('graph.png')
