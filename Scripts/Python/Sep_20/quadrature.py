#!/usr/bin/env python
# File: quadrature.py
# Name: D.Saravanan
# Date: 20/09/2021

""" Script to implement the different quadrature and see how the error behaves """

import numpy as np
import matplotlib
matplotlib.rcParams['pgf.texsystem'] = 'pdflatex'
matplotlib.rcParams.update({'font.family': 'serif', 'font.size': 8,
    'axes.labelsize': 10, 'axes.titlesize': 10, 'figure.titlesize': 10})
matplotlib.rcParams['text.usetex'] = True
import matplotlib.pyplot as plt
matplotlib.use('Agg')

# end points of interval
a, b = 0, 1

# function to be integrated
f = lambda x: np.exp(-x**2)

# derivative of the function
g = lambda x: -2*x*np.exp(-x**2)

# exact value of the integral
exact = 0.746824132812427025399

# number of different set of grids
Ngrids = 10

h = np.zeros(Ngrids)       # different grid spacings

rect = np.zeros(Ngrids)    # rectangular rule
trap = np.zeros(Ngrids)    # trapezoidal rule
simp = np.zeros(Ngrids)    # simpson rule
rend = np.zeros(Ngrids)    # rectangular rule with end point correction
tend = np.zeros(Ngrids)    # trapezoidal rule with end point correction

for k in range(0, Ngrids):
    N = 10*2**(k+2)             # number of grid points
    h[k] = (b - a)/(N - 1)      # grid spacing 
    x = np.linspace(a,b,N)      # grid points
    y = 0.5*(x[0:N-1] + x[1:N]) # mid-points of each panel

    rect[k] = h[k]*np.sum(f(y))                     # rectangular rule
    trap[k] = h[k]*(np.sum(f(x)) - (f(a) + f(b))/2) # trapezoidal rule 
    simp[k] = (2*rect[k] + trap[k])/3               # simpson rule
    rend[k] = rect[k] + h[k]**2 / 24*(g(b) - g(a))  # rectangular rule with end-point correction
    tend[k] = trap[k] - h[k]**2 / 12*(g(b) - g(a))  # trapezoidal rule with end-point correction

# error calculations
rect_err = abs(np.double(rect - exact))     # error in rectangular rule
trap_err = abs(np.double(trap - exact))     # error in trapezoidal rule
simp_err = abs(np.double(simp - exact))     # error in simpson rule
rend_err = abs(np.double(rend - exact))     # error in rectangular rule with end-point correction
tend_err = abs(np.double(tend - exact))     # error in trapezoidal rule with end-point correction

fig, ax = plt.subplots()
ax.loglog(h, rect_err, 'r.--', label=r'rectangular')
ax.loglog(h, trap_err, 'b.--', label=r'trapezoidal')
ax.loglog(h, simp_err, 'k.--', label=r'simpsonrule')
ax.loglog(h, rend_err, 'r+--', label=r'rectendpont')
ax.loglog(h, tend_err, 'b+--', label=r'trapendpont')
ax.set(xlabel=r'grid size', ylabel=r'error in quadrature')
ax.set_title(r'Quadrature convergence')
ax.grid(True); ax.legend()
plt.savefig('quadrature.pdf')
