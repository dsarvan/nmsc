#!/usr/bin/env python
# File: condition.py
# Name: D.Saravanan
# Date: 17/08/2021

""" Script to compute condition number of a matrix """

import numpy as np

N = 20

A = np.eye(N) - 10 * np.diag(np.ones(N-1), -1) + 9 * np.diag(np.ones(N-2), -2)
A[1,0] = 0

cond_A = np.linalg.cond(A)

print("Condition number of matrix A: %e" %cond_A)

B = np.eye(N) - 1 * np.diag(np.ones(N-1), -1) - 1 * np.diag(np.ones(N-2), -2)
B[1,0] = 0

cond_B = np.linalg.cond(B)

print("Condition number of matrix B: %e" %cond_B)
