#!/usr/bin/env python
# File: lagrange.py
# Name: D.Saravanan
# Date: 27/08/2021

""" Script for lagrange function """

import numpy as np

def lagrange(xnodes, xvalues, i):

    """ returns product of lagrange polynomial """

    mval, nval = len(xvalues), len(xnodes)
    val = np.ones(mval)

    for j in range(0, nval):

        if i == j:
            continue

        val = val * (xvalues - xnodes[j]) / (xnodes[i] - xnodes[j])

    return val
