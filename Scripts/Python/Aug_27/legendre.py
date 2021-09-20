#!/usr/bin/env python
# File: legendre.py
# Name: D.Saravanan
# Date: 27/08/2021

""" Script to calculate and plot Legendre polynomials """

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

    # generate the Legendre basis for the polynomial of degree 'n'
    Pn = np.polynomial.legendre.Legendre.basis(n)

    # interval [-1, 1]
    x = np.linspace(-1, 1, 1000) 
    y = Pn(x)

    #x, y = np.polynomial.Legendre.basis(n, [-1,1]).linspace(1000)
    #x, y = np.polynomial.legendre.Legendre.basis(n, [-1,1]).linspace(1000)

    ax.plot(x, y, label=r'$P_{}(x)$'.format(n))

ax.set(xlabel=r'$x$', ylabel=r'$P_{n}(x)$')
ax.set_title(r'Legendre polynomials')
ax.grid(); ax.legend()
plt.savefig('legendre.pdf')
