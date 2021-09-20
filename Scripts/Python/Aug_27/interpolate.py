#!/usr/bin/env python
# File: interpolate.py
# Name: D.Saravanan
# Date: 27/08/2021

""" Script for interpolate function """

import numpy as np
import lagrange as lag

def interpolate(fnodes, xnodes, xvalues):

    """ returns polynomial interpolation """

    mval, nval = len(xvalues), len(xnodes)
    res = np.zeros(mval)

    for i in range(0, nval):
        res = res + fnodes[i] * lag.lagrange(xnodes, xvalues, i)

    return res
