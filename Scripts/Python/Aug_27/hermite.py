#!/usr/bin/env python
# File: hermite.py
# Name: D.Saravanan
# Date: 27/08/2021

""" Script to calculate and plot Hermite polynomials """

import numpy as np
import matplotlib
matplotlib.rcParams['pgf.texsystem'] = 'pdflatex'
matplotlib.rcParams.update({'font.family': 'serif', 'font.size': 8,
    'axes.labelsize': 10, 'axes.titlesize': 10, 'figure.titlesize': 10})
matplotlib.rcParams['text.usetex'] = True
import matplotlib.pyplot as plt
matplotlib.use('Agg')

fig, ax = plt.subplots()

for n in range(4):

    # generate the Hermite basis for the polynomial of degree 'n'
    Hn = np.polynomial.hermite.Hermite.basis(n)

    # interval [-2, 2]
    x = np.linspace(-2, 2, 1000)
    y = Hn(x)

    #x, y = np.polynomial.Hermite.basis(n, [-2,2]).linspace(1000)
    #x, y = np.polynomial.hermite.Hermite.basis(n, [-2,2]).linspace(1000)

    ax.plot(x, y, label=r'$H_{}(x)$'.format(n))

ax.set(xlabel=r'$x$', ylabel=r'$H_{n}(x)$', ylim=(-10,10))
ax.set_title(r'Hermite polynomials')
ax.grid(); ax.legend()
plt.savefig('hermite.pdf')
