#!/usr/bin/env python3
# File: recurrence.py
# Name: D.Saravanan
# Date: 06/08/2021

""" Script for fibonacci recurrence series """

import numpy as np

def fibonacci(n):
    """ 
    returns fibonacci number:
        fibonacci(3) = 2
    """

    f = np.zeros((n), dtype=int)
    f[0], f[1] = 1, 1

    for i in range(1,n-1):
        f[i+1] = f[i] + f[i-1]

    return f[-1]


N = 20

# exact values
e = np.zeros(N)
e[0] = 2.95
e[1] = 2.95

# values
a = np.zeros(N)
a[0] = 2.95
a[1] = 2.95

# relative error terms
err = np.zeros(N)

for n in range(1,N-1):
    a[n+1] = a[n] + a[n-1]
    e[n+1] = 2.95 * fibonacci(n+2)

for n in range(0,N):
    err[n] = abs((a[n]-e[n])/(e[n]))

# print relative error terms
print(err)
