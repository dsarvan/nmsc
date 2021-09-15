#!/usr/bin/env python
# File: legendreroots.py
# Name: D.Saravanan
# Date: 15/09/2021

""" Script to compute the roots of the Legendre polynomials """

# Reference: https://numpy.org/doc/stable/reference/generated/
# numpy.polynomial.polynomial.polyroots.html

import numpy.polynomial.polynomial as poly
from scipy.special import legendre

# degree of the polynomial
n = 2

# returns the polynomial with coefficients
# P_2(x) = legendre(2)
# type of legendre(n): <class 'scipy.special.orthogonal.orthopolyid'>
# output of legendre(n): polyid([ 1.5, 0., -0.5])
# 3/2 x**2 - 1/2 == 3 x**2 - 1 == 1.5 x**2 - 0.5
Pn = list(legendre(n))          

# reverse the coefficients
Pn.reverse()                    

# numpy.polynomial.polynomial.polyroots(c)
# computes the roots of a polynomial
# return the roots/zeros of the polynomial Pn(x)
# parameter c: 1-D array of polynomial coefficients
# returns: array of the roots of the polynomial
# if all the roots are real, then output is also real,
# otherwise it is complex
# poly.polyroots(c0 x**0, c1 x**1, c2 x**2, ..., cn x**n)
roots = poly.polyroots((Pn))    
print(roots)
