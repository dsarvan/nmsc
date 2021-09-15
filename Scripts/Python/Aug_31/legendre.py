#!/usr/bin/env python
# File: legendre.py
# Name: D.Saravanan
# Date: 31/08/2021

""" Script to calculate and plot Legendre polynomials """

import numpy as np
from scipy.special import legendre
import matplotlib
matplotlib.rcParams['pgf.texsystem'] = 'pdflatex'
matplotlib.rcParams.update({'font.family': 'serif', 'font.size': 8,
    'axes.labelsize': 10, 'axes.titlesize': 10, 'figure.titlesize': 10})
matplotlib.rcParams['text.usetex'] = True
import matplotlib.pyplot as plt
matplotlib.use('Agg')

fig, ax = plt.subplots()

for n in range(5): 

    Pn = legendre(n)

    x = np.arange(-1, 1, 0.0001)
    y = Pn(x)

    ax.plot(x, y, label=r'$P_{}$'.format(n))

ax.set(xlabel=r'$x$', ylabel=r'$P_{n}(x)$')
ax.set_title(r'Legendre polynomials')
ax.grid(); ax.legend()
plt.savefig('legendre.pdf')
