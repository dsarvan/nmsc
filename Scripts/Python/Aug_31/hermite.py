#!/usr/bin/env python
# File: hermite.py
# Name: D.Saravanan
# Date: 31/08/2021

""" Script to calculate and plot Hermite polynomials """

import numpy as np
from scipy.special import hermite
import matplotlib
matplotlib.rcParams['pgf.texsystem'] = 'pdflatex'
matplotlib.rcParams.update({'font.family': 'serif', 'font.size': 8,
    'axes.labelsize': 10, 'axes.titlesize': 10, 'figure.titlesize': 10})
matplotlib.rcParams['text.usetex'] = True
import matplotlib.pyplot as plt
matplotlib.use('Agg')

fig, ax = plt.subplots()

for n in range(4):

    Hn = hermite(n)

    x = np.arange(-2, 2, 0.0001)
    y = Hn(x)

    ax.plot(x, y, label=r'$H_{}(x)$'.format(n))

ax.set(xlabel=r'$x$', ylabel=r'$H_{n}(x)$', ylim=(-10,10))
ax.set_title(r'Hermite polynomials')
ax.grid(); ax.legend()
plt.savefig('hermite.pdf')
