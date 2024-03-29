#!/usr/bin/env python
# File: bernsteinlambda.py
# Name: D.Saravanan
# Date: 03/09/2021

""" Script to compute Bernstein polynomial using lambda function """

import numpy as np
import matplotlib
matplotlib.rcParams['pgf.texsystem'] = 'pdflatex'
matplotlib.rcParams.update({'font.family': 'serif', 'font.size': 8,
    'axes.labelsize': 10, 'axes.titlesize': 10, 'figure.titlesize': 10})
matplotlib.rcParams['text.usetex'] = True
import matplotlib.pyplot as plt
matplotlib.use('Agg')

def factorial(n):
    return 1 if n < 2 else n*factorial(n-1)

M = 1001
x = np.linspace(-1,1,M)
f = lambda x: 1/(1 + 25 * x**2)

N = 35

Bern = sum(map(lambda k: factorial(N)/(factorial(N-k)*factorial(k)) \
        * ((x + 1)/2)**k * ((1 - x)/2)**(N-k) * f(2*k/N-1), range(N+1)))

fig, ax = plt.subplots()
ax.plot(x, f(x), c='red', ls='dotted', label=r'$\displaystyle\frac{1}{1+25 x^{2}}$')
ax.plot(x, Bern, c='teal', label=r'$Bernstein$')
ax.set(xlim=(-1, 1), ylim=(0, 1.1))
ax.set(xlabel=r'$x$', ylabel=r'$\displaystyle\frac{1}{1+25 x^{2}}$')
ax.set_title(r'Bernstein polynomial')
ax.grid(True); ax.legend()
plt.savefig('bernsteinlambda.pdf')
