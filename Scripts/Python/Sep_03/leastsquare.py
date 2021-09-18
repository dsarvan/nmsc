#!/usr/bin/env python
# File: leastsquare.py
# Name: D.Saravanan
# Date: 03/09/2021

""" Script to compute Least-square """

import numpy as np
import numpy.polynomial.polynomial as poly
from scipy.special import legendre
import matplotlib
matplotlib.rcParams['pgf.texsystem'] = 'pdflatex'
matplotlib.rcParams.update({'font.family': 'serif', 'font.size': 8,
    'axes.labelsize': 10, 'axes.titlesize': 10, 'figure.titlesize': 10})
matplotlib.rcParams['text.usetex'] = True
import matplotlib.pyplot as plt
matplotlib.use('Agg')

M = 10
N = 1000

x = np.linspace(-1, 1, N+1)

X = np.ones((N+1, M+1))

for k in range(1, M+1):
    X[:, k] = x**k

print(np.linalg.cond(X))
print(np.linalg.cond(np.dot(X.T,X)))

Q, R = np.linalg.qr(X)
print(np.linalg.cond(R))

f = 1/(1 + 25 * x**2)


