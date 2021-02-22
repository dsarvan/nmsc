#!/usr/bin/env python3
# File: recurrence.py
# Name: D.Saravanan
# Date: 19/02/2021
# Script to obtain I_(n) by recurrence relation

import numpy as np

N = 15              # Number of terms in the recurrence
I = np.zeros(N)     # initialize vector of N elements
I[0] = 0.63662      # initial condition I0 = 0.31831

for n in range(1, N):
    I[n] = (-1/np.pi) * 1**(2*n) * np.cos(np.pi) + (2*n)/(np.pi**2) * 1**(2*n - 1) * np.sin(np.pi) - ((2*n)*(2*n - 1))/(np.pi**2) * I[n-1]

print(I)
