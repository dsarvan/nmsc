#!/usr/bin/env python
# File: finitedifference.py
# Name: D.Saravanan
# Date: 13/09/2021

""" Script to compute derivative of sin(x)/x**3 at x = 4 using finite-difference """

import numpy as np
import matplotlib
matplotlib.rcParams['pgf.texsystem'] = 'pdflatex'
matplotlib.rcParams.update({'font.family': 'serif', 'font.size': 8,
    'axes.labelsize': 10, 'axes.titlesize': 10, 'figure.titlesize': 10})
matplotlib.rcParams['text.usetex'] = True
import matplotlib.pyplot as plt
matplotlib.use('Agg')

f = lambda x: np.sin(x)/x**3
g = lambda x: np.cos(x)/x**3 - 3*np.sin(x)/x**4

x = 4

# N different grid spacing
N = 10

# different grid spacing
h = np.zeros(N)

forward = np.zeros(N)   # forward difference
backwrd = np.zeros(N)   # backward difference
central = np.zeros(N)   # central difference
fourthd = np.zeros(N)   # fourth order difference

for k in range(N):
    h[k] = 1/(2**(k+1)) # decrease the grid spacing by a factor of 1/2 every single time
    
    forward[k] = (f(x + h[k]) - f(x))/h[k]
    backwrd[k] = (f(x) - f(x - h[k]))/h[k]
    central[k] = (f(x + h[k]) - f(x - h[k]))/(2*h[k])
    fourthd[k] = (-f(x + 2*h[k]) + 8*f(x + h[k]) - 8*f(x - h[k]) + f(x - 2*h[k]))/(12*h[k])

fig, ax = plt.subplots()
ax.loglog(h, np.abs(forward - g(x)), 'r.--', label=r'forward')
ax.loglog(h, np.abs(backwrd - g(x)), 'r.--', label=r'backwrd')
ax.loglog(h, np.abs(central - g(x)), 'b.--', label=r'central')
ax.loglog(h, np.abs(fourthd - g(x)), 'k.--', label=r'fourthd')
ax.set(xlabel=r'grid size', ylabel=r'error in derivative') 
ax.set_title(r'Finite-difference convergence')
ax.grid(True); ax.legend()
plt.savefig('convergence.pdf')
