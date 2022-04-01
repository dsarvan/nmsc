#!/usr/bin/env python
# File: chebyshevnodes.py
# Name: D.Saravanan
# Date: 08/03/2022

""" Script to compute the nodes of the Chebyshev polynomial of the first kind of degree n """

import numpy as np

n = int(input("degree: "))
a = int(input("lower limit: "))
b = int(input("upper limit: "))

x = np.zeros(n+1)

#xn, wn = np.polynomial.chebyshev.chebgauss(n)
#print("nodes computed: {}\n".format(xn))

for k in range(1, n+1):
    x[k] = 0.5*(b - a) * np.cos(((2*k-1)/(2*n))*np.pi) + 0.5*(b + a)
    print("x[{}] = {:.8f}".format(k, x[k]))
