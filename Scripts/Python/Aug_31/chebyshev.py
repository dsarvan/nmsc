#!/usr/bin/env python
# File: chebyshev.py
# Name: D.Saravanan
# Date: 31/08/2021

""" Script to calculate and plot Chebyshev polynomials of first kind """

import numpy as np
from scipy.special import chebyt
import matplotlib
matplotlib.rcParams['pgf.texsystem'] = 'pdflatex'
matplotlib.rcParams.update({'font.family': 'serif', 'font.size': 8,
    'axes.labelsize': 10, 'axes.titlesize': 10, 'figure.titlesize': 10})
matplotlib.rcParams['text.usetex'] = True
import matplotlib.pyplot as plt
matplotlib.use('Agg')

fig, ax = plt.subplots()

for n in range(5):

    Tn = chebyt(n)

    x = np.arange(-1, 1, 0.0001)
    y = Tn(x)

    ax.plot(x, y, label=r'$T_{}(x)$'.format(n))

ax.set(xlabel=r'$x$', ylabel=r'$T_{n}(x)$')
ax.set_title(r'Chebyshev polynomials')
ax.grid(); ax.legend()
plt.savefig('chebyshev.pdf')
