#!/usr/bin/env python
# File: laguerre.py
# Name: D.Saravanan
# Date: 27/08/2021

""" Script to calculate and plot Laguerre polynomials """

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

    # generate the Laguerre basis for the polynomial of degree 'n'
    Ln = np.polynomial.laguerre.Laguerre.basis(n)

    # interval [-4, 7]
    x = np.linspace(-4, 7, 1000)
    y = Ln(x)

    #x, y = np.polynomial.Laguerre.basis(n, [-4,7]).linspace(1000)
    #x, y = np.polynomial.laguerre.Laguerre.basis(n, [-4,7]).linspace(1000)

    ax.plot(x, y, label=r'$L_{}(x)$'.format(n))
    
ax.set(xlabel=r'$x$', ylabel=r'$L_{n}(x)$', xlim=(-2,5), ylim=(-4,4))
ax.set_title(r'Laguerre polynomials')
ax.grid(); ax.legend()
plt.savefig('laguerre.pdf')
