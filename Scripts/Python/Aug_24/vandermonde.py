#!/usr/bin/env python
# File: vandermonde.py
# Name: D.Saravanan
# Date: 24/08/2021

""" Script to compute the condition number of Vandermonde matrix """

import numpy as np
import matplotlib
import matplotlib.pyplot as plt
plt.style.use('seaborn-white')
matplotlib.use('Agg')

x1, x2 = [], []

for i, N in enumerate(range(5,37,2)):
    x = np.linspace(-1,1,N)
    V = np.vander(x)
    x1.append(i+1)
    x2.append(np.linalg.cond(V))

fig, ax = plt.subplots()
ax.set_yscale('log')
ax.plot(x1, x2)
ax.set(xlim=(0, 20), ylim=(10**1, 10**17))
ax.set(xlabel='', ylabel='cond(V)')
ax.set_title(r"condition number of Vandermonde matrix for N $\in [5,35]$", fontsize=10)
ax.grid(True)
plt.savefig('graph.png')
