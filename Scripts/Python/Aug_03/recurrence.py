#!/usr/bin/env python3
# File: recurrence.py
# Name: D.Saravanan
# Date: 03/08/2021

""" Script for solving recurrence relation:
a(n+1) = 10 a(n) - 9 a(n-1), a(0) = 2.95, a(1) = 2.95 """

import numpy as np

N = 20
a = np.zeros(N)
a[0] = 2.95
a[1] = 2.95

for n in range(1,N-1):
    a[n+1] = 10*a[n] - 9*a[n-1]

print(a)
