#!/usr/bin/env python
# File: finite_difference.py
# Name: D.Saravanan
# Date: 13/09/2021

""" Script to compute derivative of a function using finite-difference """

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
N = 30

h = np.zeros(N)

forward = np.zeros(N)
backwrd = np.zeros(N)
central = np.zeros(N)
fourthd = np.zeros(N)

for k in range(N):
    h[k] = 1/(2**k)
    
    forward[k] = (f(x + h[k]) - f(x))/h[k]
    backwrd[k] = (f(x) - f(x - h[k]))/h[k]
    central[k] = (f(x + h[k]) - f(x - h[k]))/(2*h[k])
    fourthd[k] = (-f(x + 2*h[k]) + 8*f(x + h[k]) - 8*f(x - h[k]) + f(x - 2*h[k]))/(12*h[k])


fig, ax = plt.subplots()
ax.loglog(h, np.abs(forward - g(x)), label=r'forward')
#ax.loglog(h, np.abs(backwrd - g(x)), label=r'backwrd')
#ax.loglog(h, np.abs(central - g(x)), label=r'central')
#ax.loglog(h, np.abs(fourthd - g(x)), label=r'fourthd')
ax.grid(True); ax.legend()

plt.savefig('finite.png')
