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

a, b = 0, 1

# function to be integrated
f = lambda x: np.exp(-x**2)

# derivative of the function
g = lambda x: -2*x*np.exp(-x**2)

# exact value of the integral
exact_integral = 0.746824132812427025399

# number of different set of grids
Ngrids = 10

h = zeros(Ngrids)   # different grid spacings

rect = zeros(Ngrids)    # rectangular rule
trap = zeros(Ngrids)    # trapezoidal rule
simp = zeros(Ngrids)    # simpson rule
rend = zeros(Ngrids)    # rectangular rule with end point correction
tend = zeros(Ngrids)    # trapezoidal rule with end point correction

for k in range(1, Ngrids):
    N = 10*2**(k+1)             # number of grid points
    h[k] = (b - a)/(N - 1)      # grid spacing 
