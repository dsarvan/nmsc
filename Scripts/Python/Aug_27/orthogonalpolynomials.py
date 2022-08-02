#!/usr/bin/env python
# File: orthogonalpolynomials.py
# Name: D.Saravanan
# Date: 01/08/2022

""" Script to compute the orthogonal polynomials
with their corresponding recurrence relation """

# Chebyshev polynomials of the first kind
def chebyshev(x, n):
    """ recurrence relation of chebyshev polynomials of the first kind
     T_0 = 1, T_1 = x
     T_(n+1) = 2 x T_(n) - T_(n-1)
    """
    return (
        1
        if n == 0
        else x
        if n == 1
        else 2 * x * chebyshev(x, n - 1) - chebyshev(x, n - 2)
    )


# Hermite polynomials
def hermite(x, n):
    """ recurrence relation of hermite polynomials
     H_0 = 1, H_1 = 2x
     H_(n+1) = 2 x H_(n) - 2 n H_(n-1)
    """
    return (
        1
        if n == 0
        else 2 * x
        if n == 1
        else 2 * x * hermite(x, n - 1) - 2 * (n - 1) * hermite(x, n - 2)
    )


# Laguerre polynomials
def laguerre(x, n):
    """ recurrence relation of laguerre polynomials
     L_0 = 1, L_1 = 1-x
     (n+1) L_(n+1) = (2n + 1 - x) L_(n) - n L_(n-1)
    """
    return (
        1
        if n == 0
        else 1 - x
        if n == 1
        else ((2 * (n - 1) + 1 - x) * laguerre(x, n - 1) - (n - 1) * laguerre(x, n - 2)) / n
    )


# Legendre polynomials
def legendre(x, n):
    """ recurrence relation of legendre polynomials
     P_0 = 1, P_1 = x
     (n+1)  P_(n+1) = (2n+1) x P_(n) - n P_(n-1)
    """
    return (
        1
        if n == 0
        else x
        if n == 1
        else ((2 * (n - 1) + 1) * x * legendre(x, n - 1) - (n - 1) * legendre(x, n - 2)) / n
    )
