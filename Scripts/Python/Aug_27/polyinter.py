#!/usr/bin/env python
# File: polyinter.py
# Name: D.Saravanan
# Date: 27/08/2021

""" Script to construct the polynomial interpolation 
using Lagrange polynomial """

import numpy as np
import matplotlib
matplotlib.rcParams['pgf.texsystem'] = 'pdflatex'
matplotlib.rcParams.update({'font.family': 'serif', 'font.size': 8,
    'axes.labelsize': 10, 'axes.titlesize': 10, 'figure.titlesize': 10})
matplotlib.rcParams['text.usetex'] = True
import matplotlib.pyplot as plt
matplotlib.use('Agg')

import interpolate as itp

N = 9

xnodes = np.linspace(-1,1,N)
fnodes = np.sin(np.pi*xnodes)

# true function calculated with equi-spaced nodes
x = np.linspace(-1,1,1000)
f = np.sin(np.pi*x)

fintp = itp.interpolate(fnodes, xnodes, x)

error = max(abs(f - fintp)/abs(f))
print(error)

fig, ax = plt.subplots()
ax.plot(x, f, c='olive', ls='dotted', label=r'$\sin(\pi x)$')
ax.plot(x, fintp, c='teal', label=r'$Interpolation$')
ax.plot(xnodes, fnodes, 'm.', label=r'$N = 9$')
ax.set(xlim=(-1, 1), ylim=(-1.1, 1.1))
ax.set(xlabel=r'$x$', ylabel=r'$\sin(\pi x)$')
ax.set_title(r'Lagrange polynomial interpolation')
ax.grid(True); ax.legend()
plt.savefig('polyinter.pdf')
