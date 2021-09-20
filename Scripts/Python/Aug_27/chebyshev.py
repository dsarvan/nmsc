#!/usr/bin/env python
# File: chebyshev.py
# Name: D.Saravanan
# Date: 27/08/2021

""" Script to calculate and plot Chebyshev polynomials of first kind """

import numpy as np
import matplotlib
matplotlib.rcParams['pgf.texsystem'] = 'pdflatex'
matplotlib.rcParams.update({'font.family': 'serif', 'font.size': 8,
    'axes.labelsize': 10, 'axes.titlesize': 10, 'figure.titlesize': 10})
matplotlib.rcParams['text.usetex'] = True
import matplotlib.pyplot as plt
matplotlib.use('Agg')

fig, ax = plt.subplots()

for n in range(5):

    # generate the Chebyshev basis for the polynomial of degree 'n'
    Tn = np.polynomial.chebyshev.Chebyshev.basis(n)

    # interval [-1, 1]
    x = np.linspace(-1, 1, 1000)
    y = Tn(x)

    #x, y = np.polynomial.Chebyshev.basis(n, [-1, 1]).linspace(1000)
    #x, y = np.polynomial.chebyshev.Chebyshev.basis(n, [-1, 1]).linspace(1000)

    ax.plot(x, y, label=r'$T_{}(x)$'.format(n))

ax.set(xlabel=r'$x$', ylabel=r'$T_{n}(x)$')
ax.set_title(r'Chebyshev polynomials')
ax.grid(); ax.legend()
plt.savefig('chebyshev.pdf')
