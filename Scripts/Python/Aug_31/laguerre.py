#!/usr/bin/env python
# File: laguerre.py
# Name: D.Saravanan
# Date: 31/08/2021

""" Script to calculate and plot Laguerre polynomials """

import numpy as np
from scipy.special import laguerre
import matplotlib
matplotlib.rcParams['pgf.texsystem'] = 'pdflatex'
matplotlib.rcParams.update({'font.family': 'serif', 'font.size': 8,
    'axes.labelsize': 10, 'axes.titlesize': 10, 'figure.titlesize': 10})
matplotlib.rcParams['text.usetex'] = True
import matplotlib.pyplot as plt
matplotlib.use('Agg')

fig, ax = plt.subplots()

for n in range(5):

    Ln = laguerre(n)

    x = np.arange(-4, 7, 0.00001)
    y = Ln(x)

    ax.plot(x, y, label=r'$L_{}(x)$'.format(n))

ax.set(xlabel=r'$x$', ylabel=r'$L_{n}(x)$', xlim=(-2,5), ylim=(-4,4))
ax.set_title(r'Laguerre polynomials')
ax.grid(); ax.legend()
plt.savefig('laguerre.pdf')
